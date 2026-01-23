#1954. Minimum Garden Perimeter to Collect Enough Apples
#Medium
#
#In a garden represented as an infinite 2D grid, there is an apple tree planted
#at every integer coordinate. The apple tree planted at an integer coordinate
#(i, j) has |i| + |j| apples growing on it.
#
#You will buy an axis-aligned square plot of land that is centered at (0, 0).
#
#Given an integer neededApples, return the minimum perimeter of a plot such
#that at least neededApples apples are inside or on the perimeter of that plot.
#
#Example 1:
#Input: neededApples = 1
#Output: 8
#Explanation: A square plot of side 2 has perimeter 8 and has at least 1 apple.
#
#Example 2:
#Input: neededApples = 13
#Output: 16
#
#Example 3:
#Input: neededApples = 1000000000
#Output: 5040
#
#Constraints:
#    1 <= neededApples <= 10^15

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        """
        Binary search on half-side length n.
        Total apples in square of half-side n = 2 * n * (n + 1) * (2n + 1)
        """
        def total_apples(n):
            # Formula derived from summing |i| + |j| for all points
            return 2 * n * (n + 1) * (2 * n + 1)

        lo, hi = 1, 100000  # Upper bound from constraints

        while lo < hi:
            mid = (lo + hi) // 2
            if total_apples(mid) >= neededApples:
                hi = mid
            else:
                lo = mid + 1

        return 8 * lo  # Perimeter = 4 * (2n) = 8n


class SolutionLinear:
    def minimumPerimeter(self, neededApples: int) -> int:
        """
        Linear search with formula.
        """
        n = 1

        while True:
            total = 2 * n * (n + 1) * (2 * n + 1)
            if total >= neededApples:
                return 8 * n
            n += 1


class SolutionDerived:
    def minimumPerimeter(self, neededApples: int) -> int:
        """
        Formula derivation:
        For a square from -n to n on both axes:
        - Side contribution: 4 * sum from i=1 to n of (2 * sum from j=0 to n of (i + j))
        - Corner adjustments
        - Simplifies to: 2 * n * (n + 1) * (2n + 1)
        """
        lo, hi = 1, 10**6

        while lo < hi:
            mid = (lo + hi) // 2
            apples = 2 * mid * (mid + 1) * (2 * mid + 1)

            if apples >= neededApples:
                hi = mid
            else:
                lo = mid + 1

        return 8 * lo
