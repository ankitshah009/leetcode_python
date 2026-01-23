#764. Largest Plus Sign
#Medium
#
#You are given an integer n. You have an n x n binary grid grid with all values
#initially 1's except for some indices given in the array mines. The ith element
#of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.
#
#Return the order of the largest axis-aligned plus sign of 1's contained in
#grid. If there is none, return 0.
#
#An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1
#along with four arms of length k - 1 going up, down, left, and right, and made
#of 1's.
#
#Example 1:
#Input: n = 5, mines = [[4,2]]
#Output: 2
#Explanation: In the grid, the largest plus sign has order 2. One of them is
#marked in bold.
#
#Example 2:
#Input: n = 1, mines = []
#Output: 1
#Explanation: There is no plus sign of order 2, but there is of order 1.
#
#Constraints:
#    1 <= n <= 500
#    1 <= mines.length <= 5000
#    0 <= xi, yi < n
#    All the pairs (xi, yi) are unique.

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        """
        DP: compute consecutive 1s in each direction for each cell.
        """
        banned = {(r, c) for r, c in mines}

        # dp[i][j] = min arm length in all 4 directions
        dp = [[n] * n for _ in range(n)]

        # Process each row (left and right)
        for i in range(n):
            # Left to right
            count = 0
            for j in range(n):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)

            # Right to left
            count = 0
            for j in range(n - 1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)

        # Process each column (up and down)
        for j in range(n):
            # Top to bottom
            count = 0
            for i in range(n):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)

            # Bottom to top
            count = 0
            for i in range(n - 1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)

        return max(max(row) for row in dp)


class SolutionSeparateArrays:
    """Using separate arrays for each direction"""

    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        banned = {(r, c) for r, c in mines}

        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        # Compute consecutive 1s from left
        for i in range(n):
            for j in range(n):
                if (i, j) not in banned:
                    left[i][j] = (left[i][j - 1] if j > 0 else 0) + 1

        # Compute consecutive 1s from right
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if (i, j) not in banned:
                    right[i][j] = (right[i][j + 1] if j < n - 1 else 0) + 1

        # Compute consecutive 1s from up
        for j in range(n):
            for i in range(n):
                if (i, j) not in banned:
                    up[i][j] = (up[i - 1][j] if i > 0 else 0) + 1

        # Compute consecutive 1s from down
        for j in range(n):
            for i in range(n - 1, -1, -1):
                if (i, j) not in banned:
                    down[i][j] = (down[i + 1][j] if i < n - 1 else 0) + 1

        result = 0
        for i in range(n):
            for j in range(n):
                result = max(result, min(left[i][j], right[i][j], up[i][j], down[i][j]))

        return result
