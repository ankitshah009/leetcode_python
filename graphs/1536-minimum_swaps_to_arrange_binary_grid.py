#1536. Minimum Swaps to Arrange a Binary Grid
#Medium
#
#Given an n x n binary grid, in one step you can choose two adjacent rows of
#the grid and swap them.
#
#A grid is said to be valid if all the cells above the main diagonal are zeros.
#
#Return the minimum number of steps needed to make the grid valid, or -1 if the
#grid cannot be valid.
#
#The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends
#at cell (n, n).
#
#Example 1:
#Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
#Output: 3
#
#Example 2:
#Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
#Output: -1
#Explanation: All rows are similar, we cannot make the grid valid.
#
#Example 3:
#Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
#Output: 0
#
#Constraints:
#    n == grid.length == grid[i].length
#    1 <= n <= 200
#    grid[i][j] is either 0 or 1

from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        For row i, we need at least (n-1-i) trailing zeros.

        Strategy:
        1. Calculate trailing zeros for each row
        2. Greedily find the first row that satisfies requirement for each position
        3. Bubble it up (swap with adjacent rows)
        """
        n = len(grid)

        # Count trailing zeros for each row
        def trailing_zeros(row):
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            return count

        zeros = [trailing_zeros(row) for row in grid]

        swaps = 0

        for i in range(n):
            required = n - 1 - i

            # Find first row with enough trailing zeros
            found = -1
            for j in range(i, n):
                if zeros[j] >= required:
                    found = j
                    break

            if found == -1:
                return -1

            # Bubble the row up from position found to position i
            while found > i:
                zeros[found], zeros[found - 1] = zeros[found - 1], zeros[found]
                found -= 1
                swaps += 1

        return swaps


class SolutionInPlace:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        Actually swap the grid rows (for verification).
        """
        n = len(grid)

        def trailing_zeros(row):
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            return count

        swaps = 0

        for i in range(n):
            required = n - 1 - i

            # Find valid row
            found = -1
            for j in range(i, n):
                if trailing_zeros(grid[j]) >= required:
                    found = j
                    break

            if found == -1:
                return -1

            # Swap up
            while found > i:
                grid[found], grid[found - 1] = grid[found - 1], grid[found]
                found -= 1
                swaps += 1

        return swaps


class SolutionPrecompute:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        Precompute all trailing zeros.
        """
        n = len(grid)

        # Find position of rightmost 1 in each row (or -1 if all zeros)
        rightmost = []
        for row in grid:
            pos = -1
            for j in range(n):
                if row[j] == 1:
                    pos = j
            rightmost.append(pos)

        swaps = 0

        for i in range(n):
            # Row i needs rightmost 1 at position <= i (to have n-1-i trailing zeros)
            max_pos = i

            # Find first row that satisfies this
            found = -1
            for j in range(i, n):
                if rightmost[j] <= max_pos:
                    found = j
                    break

            if found == -1:
                return -1

            # Bubble up
            while found > i:
                rightmost[found], rightmost[found - 1] = rightmost[found - 1], rightmost[found]
                found -= 1
                swaps += 1

        return swaps


class SolutionCounting:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        Count-based approach using required zeros.
        """
        n = len(grid)

        # Calculate trailing zeros for each row
        trailing = []
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing.append(count)

        result = 0

        for i in range(n):
            need = n - 1 - i

            # Find row with enough trailing zeros
            j = i
            while j < n and trailing[j] < need:
                j += 1

            if j == n:
                return -1

            # Move row j to position i
            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                j -= 1
                result += 1

        return result
