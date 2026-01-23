#1637. Widest Vertical Area Between Two Points Containing No Points
#Medium
#
#Given n points on a 2D plane where points[i] = [xi, yi], Return the widest
#vertical area between two points such that no points are inside the area.
#
#A vertical area is an area of fixed-width extending infinitely along the y-axis
#(i.e., infinite height). The widest vertical area is the one with the maximum width.
#
#Note that points on the edge of a vertical area are not considered included in
#the area.
#
#Example 1:
#Input: points = [[8,7],[9,9],[7,4],[9,7]]
#Output: 1
#Explanation: Both the red and the blue area are optimal.
#
#Example 2:
#Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
#Output: 3
#
#Constraints:
#    n == points.length
#    2 <= n <= 10^5
#    points[i].length == 2
#    0 <= xi, yi <= 10^9

from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        """
        Sort by x-coordinate, find maximum gap between consecutive x values.
        """
        # Extract and sort x coordinates
        x_coords = sorted(p[0] for p in points)

        # Find maximum gap
        max_gap = 0
        for i in range(1, len(x_coords)):
            max_gap = max(max_gap, x_coords[i] - x_coords[i - 1])

        return max_gap


class SolutionUnique:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        """
        Using unique x coordinates.
        """
        x_vals = sorted(set(p[0] for p in points))

        if len(x_vals) < 2:
            return 0

        return max(x_vals[i] - x_vals[i - 1] for i in range(1, len(x_vals)))


class SolutionZip:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        """
        Using zip for consecutive pairs.
        """
        x = sorted(p[0] for p in points)
        return max(b - a for a, b in zip(x, x[1:]))


class SolutionOneLiner:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        """
        One-liner solution.
        """
        x = sorted(p[0] for p in points)
        return max(x[i] - x[i-1] for i in range(1, len(x)))
