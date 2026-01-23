#861. Score After Flipping Matrix
#Medium
#
#You are given an m x n binary matrix grid.
#
#A move consists of choosing any row or column and toggling each value in that
#row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
#
#Every row of the matrix is interpreted as a binary number, and the score of
#the matrix is the sum of these numbers.
#
#Return the highest possible score after making any number of moves (including
#zero moves).
#
#Example 1:
#Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
#Output: 39
#Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
#
#Example 2:
#Input: grid = [[0]]
#Output: 1
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 20
#    grid[i][j] is either 0 or 1.

class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        """
        Greedy:
        1. Make all first columns 1 (flip rows if needed)
        2. For each other column, maximize 1s (flip if more 0s than 1s)
        """
        m, n = len(grid), len(grid[0])

        # Step 1: Ensure first column is all 1s
        for i in range(m):
            if grid[i][0] == 0:
                # Flip row
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]

        # Step 2: For each column, maximize 1s
        for j in range(1, n):
            ones = sum(grid[i][j] for i in range(m))
            if ones < m - ones:
                # More 0s than 1s, flip column
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]

        # Calculate score
        score = 0
        for row in grid:
            score += int(''.join(map(str, row)), 2)

        return score


class SolutionNoModify:
    """Calculate without modifying grid"""

    def matrixScore(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # First column contributes m * 2^(n-1)
        score = m * (1 << (n - 1))

        for j in range(1, n):
            # Count 1s in column j after row flips
            # If grid[i][0] == 0, row i was flipped
            ones = sum(grid[i][j] ^ (1 - grid[i][0]) for i in range(m))
            # Take max(ones, m-ones) and multiply by column value
            score += max(ones, m - ones) * (1 << (n - 1 - j))

        return score


class SolutionBit:
    """Bit manipulation approach"""

    def matrixScore(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Convert rows to integers (after ensuring MSB is 1)
        rows = []
        for row in grid:
            val = int(''.join(map(str, row)), 2)
            # If MSB is 0, flip row
            if row[0] == 0:
                val = ((1 << n) - 1) ^ val
            rows.append(val)

        # For each bit position (except MSB), maximize 1s
        for bit in range(n - 1):
            ones = sum((r >> bit) & 1 for r in rows)
            if ones < m - ones:
                # Flip this bit in all numbers
                mask = 1 << bit
                rows = [r ^ mask for r in rows]

        return sum(rows)
