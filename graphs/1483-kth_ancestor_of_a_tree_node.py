#1483. Kth Ancestor of a Tree Node
#Hard
#
#You are given a tree with n nodes numbered from 0 to n - 1 in the form of a
#parent array parent where parent[i] is the parent of ith node. The root of
#the tree is node 0. Find the kth ancestor of a given node.
#
#The kth ancestor of a tree node is the kth node in the path from that node to
#the root node.
#
#Implement the TreeAncestor class:
#    TreeAncestor(int n, int[] parent) Initializes the object with the number
#    of nodes in the tree and the parent array.
#
#    int getKthAncestor(int node, int k) return the kth ancestor of the given
#    node node. If there is no such ancestor, return -1.
#
#Example 1:
#Input
#["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
#[[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
#Output
#[null, 1, 0, -1]
#Explanation
#TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
#treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
#treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
#treeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such ancestor
#
#Constraints:
#    1 <= k <= n <= 5 * 10^4
#    parent.length == n
#    parent[0] == -1
#    0 <= parent[i] < n for all 0 < i < n
#    0 <= node < n
#    There will be at most 5 * 10^4 queries.

from typing import List
import math

class TreeAncestor:
    """
    Binary lifting technique.
    Precompute 2^j-th ancestor for each node.
    Then use binary representation of k to find k-th ancestor.
    """

    def __init__(self, n: int, parent: List[int]):
        self.LOG = int(math.log2(n)) + 1  # Max power of 2 needed

        # ancestor[i][j] = 2^j-th ancestor of node i
        self.ancestor = [[-1] * self.LOG for _ in range(n)]

        # Base case: 2^0 = 1st ancestor is parent
        for i in range(n):
            self.ancestor[i][0] = parent[i]

        # Fill table using DP
        # 2^j-th ancestor = 2^(j-1)-th ancestor of 2^(j-1)-th ancestor
        for j in range(1, self.LOG):
            for i in range(n):
                if self.ancestor[i][j - 1] != -1:
                    self.ancestor[i][j] = self.ancestor[self.ancestor[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        # Use binary representation of k
        for j in range(self.LOG):
            if k & (1 << j):  # If j-th bit is set
                node = self.ancestor[node][j]
                if node == -1:
                    return -1
        return node


class TreeAncestorNaive:
    """
    Naive solution: follow parent pointers k times.
    O(k) per query - too slow for large k.
    """

    def __init__(self, n: int, parent: List[int]):
        self.parent = parent

    def getKthAncestor(self, node: int, k: int) -> int:
        for _ in range(k):
            if node == -1:
                return -1
            node = self.parent[node]
        return node


class TreeAncestorDepth:
    """
    Alternative: precompute depth and path to root for each node.
    Good when tree is not too deep.
    """

    def __init__(self, n: int, parent: List[int]):
        self.parent = parent

        # Compute depth of each node
        self.depth = [-1] * n
        self.depth[0] = 0

        # Also store path to root for each node
        self.path_to_root = [[] for _ in range(n)]

        for i in range(n):
            self._compute_depth(i)

    def _compute_depth(self, node: int) -> int:
        if self.depth[node] != -1:
            return self.depth[node]

        if self.parent[node] == -1:
            self.depth[node] = 0
            self.path_to_root[node] = [node]
        else:
            parent_depth = self._compute_depth(self.parent[node])
            self.depth[node] = parent_depth + 1
            self.path_to_root[node] = self.path_to_root[self.parent[node]] + [node]

        return self.depth[node]

    def getKthAncestor(self, node: int, k: int) -> int:
        if k > self.depth[node]:
            return -1

        target_depth = self.depth[node] - k
        return self.path_to_root[node][target_depth]


class TreeAncestorOptimized:
    """
    Space-optimized binary lifting.
    """

    def __init__(self, n: int, parent: List[int]):
        self.LOG = max(1, n.bit_length())

        # Use list of lists for better cache performance
        self.up = []

        # First level is direct parent
        self.up.append(parent[:])

        # Build higher levels
        for j in range(1, self.LOG):
            prev = self.up[j - 1]
            curr = [-1] * n
            for i in range(n):
                if prev[i] != -1:
                    curr[i] = prev[prev[i]]
            self.up.append(curr)

    def getKthAncestor(self, node: int, k: int) -> int:
        j = 0
        while k > 0 and node != -1:
            if k & 1:
                node = self.up[j][node]
            k >>= 1
            j += 1
        return node
