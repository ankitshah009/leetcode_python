#305. Number of Islands II
#Hard
#
#You are given an empty 2D binary grid grid of size m x n. The grid represents
#a map where 0's represent water and 1's represent land. Initially, all the
#cells of grid are water cells (i.e., all the cells are 0's).
#
#We may perform an add land operation which turns the water at position into a
#land. You are given an array positions where positions[i] = [ri, ci] is the
#position (ri, ci) at which we should operate the ith operation.
#
#Return an array of integers answer where answer[i] is the number of islands
#after turning the cell (ri, ci) into a land.
#
#An island is surrounded by water and is formed by connecting adjacent lands
#horizontally or vertically. You may assume all four edges of the grid are all
#surrounded by water.
#
#Example 1:
#Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
#Output: [1,1,2,3]
#
#Example 2:
#Input: m = 1, n = 1, positions = [[0,0]]
#Output: [1]
#
#Constraints:
#    1 <= m, n, positions.length <= 10^4
#    1 <= m * n <= 10^4
#    positions[i].length == 2
#    0 <= ri < m
#    0 <= ci < n
#
#Follow up: Could you solve it in time complexity O(k log(mn)), where k is the
#length of positions?

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}
        count = 0
        result = []

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            count -= 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r, c in positions:
            pos = r * n + c

            # Check if already land
            if pos in parent:
                result.append(count)
                continue

            # Add new land
            parent[pos] = pos
            rank[pos] = 0
            count += 1

            # Check neighbors and union
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                neighbor = nr * n + nc
                if 0 <= nr < m and 0 <= nc < n and neighbor in parent:
                    union(pos, neighbor)

            result.append(count)

        return result
