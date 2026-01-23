#947. Most Stones Removed with Same Row or Column
#Medium
#
#On a 2D plane, we place n stones at some integer coordinate points. Each
#coordinate point may have at most one stone.
#
#A stone can be removed if it shares either the same row or the same column as
#another stone that has not been removed.
#
#Given an array stones where stones[i] = [xi, yi] represents the location of
#the i-th stone, return the largest possible number of stones that can be removed.
#
#Example 1:
#Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
#Output: 5
#
#Example 2:
#Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
#Output: 3
#
#Example 3:
#Input: stones = [[0,0]]
#Output: 0
#
#Constraints:
#    1 <= stones.length <= 1000
#    0 <= xi, yi <= 10^4
#    No two stones are at the same coordinate point.

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        """
        Union-Find: stones in same row/column form a component.
        Can remove all but one stone per component.
        """
        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in stones:
            # Use ~y to distinguish row x from column y
            union(x, ~y)

        # Count unique components
        components = len({find(x) for x, y in stones})

        return len(stones) - components


class SolutionDFS:
    """DFS to find connected components"""

    def removeStones(self, stones: list[list[int]]) -> int:
        from collections import defaultdict

        n = len(stones)

        # Build adjacency: stones sharing row or column
        row_map = defaultdict(list)
        col_map = defaultdict(list)

        for i, (x, y) in enumerate(stones):
            row_map[x].append(i)
            col_map[y].append(i)

        visited = [False] * n
        components = 0

        def dfs(i):
            visited[i] = True
            x, y = stones[i]

            for j in row_map[x]:
                if not visited[j]:
                    dfs(j)

            for j in col_map[y]:
                if not visited[j]:
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1

        return n - components


class SolutionUnionFindExplicit:
    """Union-Find with explicit structure"""

    def removeStones(self, stones: list[list[int]]) -> int:
        n = len(stones)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        from collections import defaultdict
        row_map = defaultdict(list)
        col_map = defaultdict(list)

        for i, (x, y) in enumerate(stones):
            row_map[x].append(i)
            col_map[y].append(i)

        # Union stones in same row
        for indices in row_map.values():
            for i in range(1, len(indices)):
                union(indices[0], indices[i])

        # Union stones in same column
        for indices in col_map.values():
            for i in range(1, len(indices)):
                union(indices[0], indices[i])

        components = len(set(find(i) for i in range(n)))
        return n - components
