#1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
#Hard
#
#Given a weighted undirected connected graph with n vertices numbered from 0 to
#n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a
#bidirectional and weighted edge between nodes ai and bi. A minimum spanning
#tree (MST) is a subset of the graph's edges that connects all vertices without
#cycles and with the minimum possible total edge weight.
#
#Find all the critical and pseudo-critical edges in the given graph's minimum
#spanning tree (MST). An MST edge whose deletion from the graph would cause the
#MST weight to increase is called a critical edge. On the other hand, a
#pseudo-critical edge is that which can appear in some MSTs but not all.
#
#Note that you can return the indices of the edges in any order.
#
#Example 1:
#Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
#Output: [[0,1],[2,3,4,5]]
#Explanation: The figure above describes the graph.
#The following figure shows all the possible MSTs:
#Notice that the two edges 0 and 1 appear in all MSTs, therefore they are
#critical edges, so we return them in the first list of the output.
#The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are
#considered pseudo-critical edges. We add them to the second list of the output.
#
#Example 2:
#Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
#Output: [[],[0,1,2,3]]
#Explanation: We can observe that since all 4 edges have equal weight, choosing
#any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are
#pseudo-critical.
#
#Constraints:
#    2 <= n <= 100
#    1 <= edges.length <= min(200, n * (n - 1) / 2)
#    edges[i].length == 3
#    0 <= ai < bi < n
#    1 <= weighti <= 1000
#    All pairs (ai, bi) are distinct.

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        1. Find MST weight
        2. For each edge:
           - Critical: removing it increases MST weight (or disconnects graph)
           - Pseudo-critical: forcing it doesn't increase MST weight, but not critical
        """
        # Add original indices
        indexed_edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]

        # Sort by weight
        indexed_edges.sort(key=lambda x: x[2])

        def kruskal(n: int, edges: List, skip: int = -1, force: int = -1) -> int:
            """
            Run Kruskal's algorithm.
            skip: edge index to exclude
            force: edge index to force include first
            Returns MST weight or inf if not possible.
            """
            uf = UnionFind(n)
            weight = 0
            edges_used = 0

            # Force include edge if specified
            if force != -1:
                for u, v, w, idx in edges:
                    if idx == force:
                        uf.union(u, v)
                        weight += w
                        edges_used += 1
                        break

            # Add remaining edges
            for u, v, w, idx in edges:
                if idx == skip or idx == force:
                    continue
                if uf.union(u, v):
                    weight += w
                    edges_used += 1

            # Check if MST is complete
            if edges_used != n - 1:
                return float('inf')

            return weight

        # Find original MST weight
        mst_weight = kruskal(n, indexed_edges)

        critical = []
        pseudo_critical = []

        for u, v, w, idx in indexed_edges:
            # Check if critical: removing increases weight
            if kruskal(n, indexed_edges, skip=idx) > mst_weight:
                critical.append(idx)
            # Check if pseudo-critical: forcing doesn't increase weight
            elif kruskal(n, indexed_edges, force=idx) == mst_weight:
                pseudo_critical.append(idx)

        return [critical, pseudo_critical]


class SolutionOptimized:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        Optimized with early termination and better edge tracking.
        """
        m = len(edges)
        indexed_edges = sorted(range(m), key=lambda i: edges[i][2])

        def find_mst_weight(skip: int = -1, force: int = -1) -> int:
            uf = UnionFind(n)
            weight = 0
            count = 0

            if force != -1:
                u, v, w = edges[force]
                if uf.union(u, v):
                    weight += w
                    count += 1

            for i in indexed_edges:
                if i == skip or i == force:
                    continue
                u, v, w = edges[i]
                if uf.union(u, v):
                    weight += w
                    count += 1
                    if count == n - 1:
                        break

            return weight if count == n - 1 else float('inf')

        mst_weight = find_mst_weight()

        critical = []
        pseudo_critical = []

        for i in range(m):
            # Is it critical?
            if find_mst_weight(skip=i) > mst_weight:
                critical.append(i)
            # Is it pseudo-critical?
            elif find_mst_weight(force=i) == mst_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]
