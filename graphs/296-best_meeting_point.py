#296. Best Meeting Point
#Hard
#
#Given an m x n binary grid grid where each 1 marks the home of one friend, return
#the minimal total travel distance.
#
#The total travel distance is the sum of the distances between the houses of the
#friends and the meeting point.
#
#The distance is calculated using Manhattan Distance, where distance(p1, p2) =
#|p2.x - p1.x| + |p2.y - p1.y|.
#
#Example 1:
#Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#Output: 6
#Explanation: Given three friends living at (0,0), (0,4), and (2,2).
#The point (0,2) is an ideal meeting point, as the total travel distance of
#2 + 2 + 2 = 6 is minimal.
#
#Example 2:
#Input: grid = [[1,1]]
#Output: 1
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 200
#    grid[i][j] is either 0 or 1.
#    There will be at least two friends in the grid.

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # Optimal meeting point is at median of all coordinates
        # Because Manhattan distance is separable: x and y dimensions are independent

        rows = []
        cols = []

        m, n = len(grid), len(grid[0])

        # Collect row indices (already sorted)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)

        # Collect column indices (already sorted since we iterate row by row)
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    cols.append(j)

        # Find median and calculate total distance
        def min_distance(points):
            median = points[len(points) // 2]
            return sum(abs(p - median) for p in points)

        return min_distance(rows) + min_distance(cols)

    # Alternative: explicit sorting
    def minTotalDistanceSort(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = []
        cols = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        cols.sort()

        def min_distance(points):
            i, j = 0, len(points) - 1
            total = 0
            while i < j:
                total += points[j] - points[i]
                i += 1
                j -= 1
            return total

        return min_distance(rows) + min_distance(cols)
