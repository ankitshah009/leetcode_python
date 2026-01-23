#1697. Checking Existence of Edge Length Limited Paths
#Hard
#
#An undirected graph of n nodes is defined by edgeList, where
#edgeList[i] = [u_i, v_i, dis_i] denotes an edge between nodes u_i and v_i
#with distance dis_i. Note that there may be multiple edges between two nodes.
#
#Given an array queries, where queries[j] = [p_j, q_j, limit_j], your task is
#to determine for each queries[j] whether there is a path between p_j and q_j
#such that each edge on the path has a distance strictly less than limit_j.
#
#Return a boolean array answer, where answer.length == queries.length and
#answer[j] is true if there is a path for queries[j], and false otherwise.
#
#Example 1:
#Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
#Output: [false,true]
#
#Example 2:
#Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
#Output: [true,false]
#
#Constraints:
#    2 <= n <= 10^5
#    1 <= edgeList.length, queries.length <= 10^5
#    edgeList[i].length == 3
#    queries[j].length == 3
#    0 <= u_i, v_i, p_j, q_j <= n - 1
#    u_i != v_i
#    p_j != q_j
#    1 <= dis_i, limit_j <= 10^9
#    There may be multiple edges between two nodes.

from typing import List

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]],
                                   queries: List[List[int]]) -> List[bool]:
        """
        Offline processing with Union-Find.
        Sort queries by limit, add edges in order of distance.
        """
        # Union-Find
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        # Sort edges by distance
        edgeList.sort(key=lambda e: e[2])

        # Process queries offline (sort by limit)
        query_indices = sorted(range(len(queries)), key=lambda i: queries[i][2])

        result = [False] * len(queries)
        edge_idx = 0

        for qi in query_indices:
            p, q, limit = queries[qi]

            # Add all edges with distance < limit
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                u, v, _ = edgeList[edge_idx]
                union(u, v)
                edge_idx += 1

            # Check if p and q are connected
            result[qi] = (find(p) == find(q))

        return result


class SolutionOnline:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]],
                                   queries: List[List[int]]) -> List[bool]:
        """
        Online approach using persistent Union-Find (conceptual, less efficient).
        For each query, use BFS/DFS with edge weight constraint.
        """
        from collections import defaultdict

        # Build adjacency list
        graph = defaultdict(list)
        for u, v, d in edgeList:
            graph[u].append((v, d))
            graph[v].append((u, d))

        def can_reach(start: int, end: int, limit: int) -> bool:
            from collections import deque
            visited = set([start])
            queue = deque([start])

            while queue:
                node = queue.popleft()
                if node == end:
                    return True

                for neighbor, dist in graph[node]:
                    if neighbor not in visited and dist < limit:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return False

        return [can_reach(p, q, limit) for p, q, limit in queries]


class SolutionUnionFind:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]],
                                   queries: List[List[int]]) -> List[bool]:
        """
        Clean Union-Find implementation.
        """
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return
                if self.rank[px] < self.rank[py]:
                    px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1

            def connected(self, x, y):
                return self.find(x) == self.find(y)

        uf = UnionFind(n)
        edgeList.sort(key=lambda x: x[2])

        # Add query index
        indexed_queries = [(limit, p, q, i) for i, (p, q, limit) in enumerate(queries)]
        indexed_queries.sort()

        result = [False] * len(queries)
        edge_i = 0

        for limit, p, q, idx in indexed_queries:
            while edge_i < len(edgeList) and edgeList[edge_i][2] < limit:
                uf.union(edgeList[edge_i][0], edgeList[edge_i][1])
                edge_i += 1

            result[idx] = uf.connected(p, q)

        return result
