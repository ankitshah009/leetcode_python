#310. Minimum Height Trees
#Medium
#
#A tree is an undirected graph in which any two vertices are connected by exactly one path.
#In other words, any connected graph without simple cycles is a tree.
#
#Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where
#edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi
#in the tree, you can choose any node of the tree as the root. When you select a node x as the
#root, the result tree has height h. Among all possible rooted trees, those with minimum height
#(i.e. min(h)) are called minimum height trees (MHTs).
#
#Return a list of all MHTs' root labels. You can return the answer in any order.
#
#Example 1:
#Input: n = 4, edges = [[1,0],[1,2],[1,3]]
#Output: [1]
#
#Example 2:
#Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
#Output: [3,4]
#
#Constraints:
#    1 <= n <= 2 * 10^4
#    edges.length == n - 1
#    0 <= ai, bi < n
#    ai != bi
#    All the pairs (ai, bi) are distinct.
#    The given input is guaranteed to be a tree and there will be no repeated edges.

from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # Build adjacency list
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        # Find initial leaves (nodes with degree 1)
        leaves = deque([node for node in range(n) if len(graph[node]) == 1])

        remaining = n

        # Trim leaves layer by layer until 1 or 2 nodes remain
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = deque()

            while leaves:
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return list(leaves)
