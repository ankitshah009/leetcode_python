#1519. Number of Nodes in the Sub-Tree With the Same Label
#Medium
#
#You are given a tree (i.e. a connected, undirected graph that has no cycles)
#consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The
#root of the tree is the node 0, and each node of the tree has a label which
#is a lower-case character given in the string labels (i.e. The node with the
#number i has the label labels[i]).
#
#The edges array is given on the form edges[i] = [ai, bi], which means there
#is an edge between nodes ai and bi in the tree.
#
#Return an array of size n where ans[i] is the number of nodes in the subtree
#of the ith node which have the same label as node i.
#
#A subtree of a tree T is the tree consisting of a node in T and all of its
#descendant nodes.
#
#Example 1:
#Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
#Output: [2,1,1,1,1,1,1]
#Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as
#well, thus the answer is 2. Notice that any node is part of its sub-tree.
#Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes
#4 and 5 have different labels than node 1, the answer is just 1 (the node itself).
#
#Example 2:
#Input: n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
#Output: [4,2,1,1]
#Explanation: The sub-tree of node 2 contains only node 2, so the answer is 1.
#The sub-tree of node 3 contains only node 3, so the answer is 1.
#The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the
#answer is 2.
#The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus
#the answer is 4.
#
#Example 3:
#Input: n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
#Output: [3,2,1,1,1]
#
#Constraints:
#    1 <= n <= 10^5
#    edges.length == n - 1
#    edges[i].length == 2
#    0 <= ai, bi < n
#    ai != bi
#    labels.length == n
#    labels is consisting of only of lowercase English letters.

from typing import List
from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        """
        DFS from root, return count of each label in subtree.
        Use array of size 26 for counting.
        """
        # Build adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        result = [0] * n

        def dfs(node: int, parent: int) -> List[int]:
            # Count array for 26 letters
            count = [0] * 26

            # Recurse on children
            for child in graph[node]:
                if child != parent:
                    child_count = dfs(child, node)
                    for i in range(26):
                        count[i] += child_count[i]

            # Add current node's label
            label_idx = ord(labels[node]) - ord('a')
            count[label_idx] += 1

            # Answer for current node
            result[node] = count[label_idx]

            return count

        dfs(0, -1)
        return result


class SolutionIterative:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        """
        Iterative DFS using stack.
        Post-order processing with state tracking.
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        result = [0] * n
        counts = [[0] * 26 for _ in range(n)]
        visited = [False] * n

        # Stack stores (node, parent, processed)
        stack = [(0, -1, False)]

        while stack:
            node, parent, processed = stack.pop()

            if processed:
                # All children processed, compute result
                label_idx = ord(labels[node]) - ord('a')
                counts[node][label_idx] += 1
                result[node] = counts[node][label_idx]

                # Propagate to parent
                if parent != -1:
                    for i in range(26):
                        counts[parent][i] += counts[node][i]
            else:
                visited[node] = True
                stack.append((node, parent, True))  # Process after children

                for child in graph[node]:
                    if not visited[child]:
                        stack.append((child, node, False))

        return result


class SolutionBFS:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        """
        BFS-based approach: compute depths, process from leaves up.
        """
        from collections import deque

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Find parent relationships and order nodes by depth
        parent = [-1] * n
        depth = [-1] * n
        depth[0] = 0

        queue = deque([0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for child in graph[node]:
                if depth[child] == -1:
                    depth[child] = depth[node] + 1
                    parent[child] = node
                    queue.append(child)

        # Process in reverse order (deepest first)
        counts = [[0] * 26 for _ in range(n)]
        result = [0] * n

        for node in reversed(order):
            label_idx = ord(labels[node]) - ord('a')
            counts[node][label_idx] += 1
            result[node] = counts[node][label_idx]

            # Propagate to parent
            if parent[node] != -1:
                for i in range(26):
                    counts[parent[node]][i] += counts[node][i]

        return result
