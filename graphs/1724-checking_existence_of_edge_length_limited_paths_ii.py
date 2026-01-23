#1724. Checking Existence of Edge Length Limited Paths II
#Hard
#
#An undirected graph of n nodes is defined by edgeList, where edgeList[i] =
#[ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note
#that there may be multiple edges between two nodes, and the graph may not be
#connected.
#
#Implement the DistanceLimitedPathsExist class:
#- DistanceLimitedPathsExist(int n, int[][] edgeList) Initializes the class with
#  an undirected graph.
#- boolean query(int p, int q, int limit) Returns true if there exists a path
#  from p to q such that each edge on the path has a distance strictly less than
#  limit, and otherwise false.
#
#Example 1:
#Input:
#["DistanceLimitedPathsExist", "query", "query", "query", "query"]
#[[6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]], [2, 3, 2], [1, 3, 3], [2, 0, 3], [0, 5, 6]]
#Output: [null, true, false, true, false]
#
#Constraints:
#    2 <= n <= 10^4
#    0 <= edgeList.length <= 10^4
#    edgeList[i].length == 3
#    0 <= ui, vi, p, q <= n - 1
#    ui != vi
#    p != q
#    1 <= disi, limit <= 10^9
#    At most 10^4 calls will be made to query.

from typing import List

class DistanceLimitedPathsExist:
    """
    Persistent Union-Find with edge weight thresholds.
    Sort edges by weight, build forest of union-find snapshots.
    """

    def __init__(self, n: int, edgeList: List[List[int]]):
        # Sort edges by distance
        edges = sorted(edgeList, key=lambda x: x[2])

        # Build MST-like structure with parent pointers and weights
        self.parent = list(range(n))
        self.rank = [0] * n
        self.weight = [0] * n  # weight[i] = max edge weight to reach parent

        # For each node, store (threshold, parent, weight) snapshots
        self.snapshots = [[(0, i, 0)] for i in range(n)]

        for u, v, d in edges:
            pu, pv = self._find(u), self._find(v)
            if pu != pv:
                # Union by rank
                if self.rank[pu] < self.rank[pv]:
                    pu, pv = pv, pu

                # pv becomes child of pu
                self.parent[pv] = pu
                self.weight[pv] = d

                # Record snapshot for pv
                self.snapshots[pv].append((d, pu, d))

                if self.rank[pu] == self.rank[pv]:
                    self.rank[pu] += 1

    def _find(self, x: int) -> int:
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def _find_with_limit(self, x: int, limit: int) -> int:
        """Find root using only edges with weight < limit."""
        while True:
            # Binary search for latest snapshot < limit
            snaps = self.snapshots[x]
            lo, hi = 0, len(snaps) - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if snaps[mid][0] < limit:
                    lo = mid
                else:
                    hi = mid - 1

            threshold, parent, _ = snaps[lo]
            if parent == x:
                return x
            x = parent

    def query(self, p: int, q: int, limit: int) -> bool:
        return self._find_with_limit(p, limit) == self._find_with_limit(q, limit)


class DistanceLimitedPathsExistSimple:
    """
    Simpler but slower approach using sorted edges and union-find rebuild.
    """

    def __init__(self, n: int, edgeList: List[List[int]]):
        self.n = n
        self.edges = sorted(edgeList, key=lambda x: x[2])

    def query(self, p: int, q: int, limit: int) -> bool:
        parent = list(range(self.n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v, d in self.edges:
            if d >= limit:
                break
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv

        return find(p) == find(q)
