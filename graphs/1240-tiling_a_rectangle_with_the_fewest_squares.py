#1240. Tiling a Rectangle with the Fewest Squares
#Hard
#
#Given a rectangle of size n x m, return the minimum number of integer-sided
#squares that tile the rectangle.
#
#Example 1:
#Input: n = 2, m = 3
#Output: 3
#Explanation: 3 squares are necessary to cover the rectangle.
#2 (squares of 1x1)
#1 (square of 2x2)
#
#Example 2:
#Input: n = 5, m = 8
#Output: 5
#
#Example 3:
#Input: n = 11, m = 13
#Output: 6
#
#Constraints:
#    1 <= n, m <= 13

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        """
        Backtracking with pruning.
        Track the "skyline" of filled heights for each column.
        """
        if n > m:
            n, m = m, n

        self.result = n * m  # Worst case: all 1x1

        # Heights of each column (skyline)
        heights = [0] * m

        def backtrack(count):
            if count >= self.result:
                return

            # Find the lowest point in skyline
            min_height = min(heights)
            if min_height == n:
                self.result = min(self.result, count)
                return

            # Find leftmost column with minimum height
            left = heights.index(min_height)

            # Find how far right we can extend at this height
            right = left
            while right < m and heights[right] == min_height:
                right += 1

            # Try placing squares of different sizes
            max_size = min(right - left, n - min_height)

            for size in range(max_size, 0, -1):
                # Place square of given size
                for i in range(left, left + size):
                    heights[i] += size

                backtrack(count + 1)

                # Remove square
                for i in range(left, left + size):
                    heights[i] -= size

        backtrack(0)
        return self.result


class SolutionDP:
    def tilingRectangle(self, n: int, m: int) -> int:
        """
        DP approach for some cases, but backtracking is needed for hard cases.
        """
        # Special cases that DP alone can't handle optimally
        # Use backtracking solution for all

        if n > m:
            n, m = m, n

        # Try the backtracking approach
        best = [n * m]
        heights = [0] * m

        def dfs(count):
            if count >= best[0]:
                return

            min_h = min(heights)
            if min_h == n:
                best[0] = count
                return

            idx = heights.index(min_h)
            right = idx
            while right < m and heights[right] == min_h:
                right += 1

            for size in range(min(right - idx, n - min_h), 0, -1):
                for i in range(idx, idx + size):
                    heights[i] += size
                dfs(count + 1)
                for i in range(idx, idx + size):
                    heights[i] -= size

        dfs(0)
        return best[0]
