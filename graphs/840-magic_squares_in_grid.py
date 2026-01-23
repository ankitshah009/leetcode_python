#840. Magic Squares In Grid
#Medium
#
#A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
#such that each row, column, and both diagonals all have the same sum.
#
#Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids are
#there? (Note: while a magic square can only contain numbers from 1 to 9, grid
#may contain numbers up to 15.)
#
#Example 1:
#Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
#Output: 1
#
#Example 2:
#Input: grid = [[8]]
#Output: 0
#
#Constraints:
#    row == grid.length
#    col == grid[i].length
#    1 <= row, col <= 10
#    0 <= grid[i][j] <= 15

class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        """
        Check all 3x3 subgrids for magic square property.
        """
        def is_magic(r, c):
            """Check if 3x3 subgrid starting at (r, c) is magic"""
            # Extract values
            vals = []
            for i in range(3):
                for j in range(3):
                    vals.append(grid[r + i][c + j])

            # Check distinct 1-9
            if sorted(vals) != list(range(1, 10)):
                return False

            # Check sums (magic constant is 15)
            s = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            if s != 15:
                return False

            # Rows
            for i in range(3):
                if sum(grid[r+i][c:c+3]) != 15:
                    return False

            # Columns
            for j in range(3):
                if grid[r][c+j] + grid[r+1][c+j] + grid[r+2][c+j] != 15:
                    return False

            # Diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                return False

            return True

        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    count += 1

        return count


class SolutionOptimized:
    """Optimized with early termination"""

    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        def is_magic(r, c):
            # Center must be 5 in a 3x3 magic square
            if grid[r+1][c+1] != 5:
                return False

            # Check distinct 1-9
            seen = set()
            for i in range(3):
                for j in range(3):
                    v = grid[r+i][c+j]
                    if v < 1 or v > 9 or v in seen:
                        return False
                    seen.add(v)

            # Check sums
            # Rows
            for i in range(3):
                if grid[r+i][c] + grid[r+i][c+1] + grid[r+i][c+2] != 15:
                    return False

            # Columns
            for j in range(3):
                if grid[r][c+j] + grid[r+1][c+j] + grid[r+2][c+j] != 15:
                    return False

            # Diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                return False

            return True

        rows, cols = len(grid), len(grid[0])
        return sum(
            is_magic(r, c)
            for r in range(rows - 2)
            for c in range(cols - 2)
        )
