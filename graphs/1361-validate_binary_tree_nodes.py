#1361. Validate Binary Tree Nodes
#Medium
#
#You have n binary tree nodes numbered from 0 to n - 1 where node i has two
#children leftChild[i] and rightChild[i], return true if and only if all the
#given nodes form exactly one valid binary tree.
#
#If node i has no left child then leftChild[i] will equal -1, similarly for
#the right child.
#
#Note that the nodes have no values and that we only use the node numbers in
#this problem.
#
#Example 1:
#Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
#Output: true
#
#Example 2:
#Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
#Output: false
#
#Example 3:
#Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
#Output: false
#
#Constraints:
#    n == leftChild.length == rightChild.length
#    1 <= n <= 10^4
#    -1 <= leftChild[i], rightChild[i] <= n - 1

from typing import List
from collections import deque

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        """
        Valid binary tree requirements:
        1. Exactly one root (node with no parent)
        2. Each non-root node has exactly one parent
        3. All nodes are reachable from root (connected)
        """
        # Count parents for each node
        parent_count = [0] * n

        for left, right in zip(leftChild, rightChild):
            if left != -1:
                parent_count[left] += 1
            if right != -1:
                parent_count[right] += 1

        # Find root (node with 0 parents)
        roots = [i for i in range(n) if parent_count[i] == 0]

        if len(roots) != 1:
            return False

        root = roots[0]

        # Check all parent counts <= 1
        if any(c > 1 for c in parent_count):
            return False

        # BFS to check connectivity
        visited = set()
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            visited.add(node)

            if leftChild[node] != -1:
                queue.append(leftChild[node])
            if rightChild[node] != -1:
                queue.append(rightChild[node])

        return len(visited) == n


class SolutionUnionFind:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        """Union-Find approach"""
        parent = list(range(n))
        has_parent = [False] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(p, c):
            # p is parent of c
            root_p = find(p)
            root_c = find(c)

            if root_p == root_c:
                return False  # Cycle

            parent[root_c] = root_p
            return True

        for node in range(n):
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if has_parent[child]:
                        return False  # Multiple parents
                    has_parent[child] = True

                    if not union(node, child):
                        return False

        # Check exactly one component
        return len(set(find(i) for i in range(n))) == 1
