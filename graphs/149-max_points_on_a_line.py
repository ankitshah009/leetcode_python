#149. Max Points on a Line
#Hard
#
#Given an array of points where points[i] = [xi, yi] represents a point on the
#X-Y plane, return the maximum number of points that lie on the same straight line.
#
#Example 1:
#Input: points = [[1,1],[2,2],[3,3]]
#Output: 3
#
#Example 2:
#Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
#Output: 4

from collections import defaultdict
from math import gcd
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def get_slope(p1, p2):
            """Get slope as a normalized tuple (dy, dx) to avoid float precision issues"""
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            if dx == 0:
                return (1, 0)  # Vertical line
            if dy == 0:
                return (0, 1)  # Horizontal line

            # Normalize the slope
            g = gcd(abs(dx), abs(dy))
            dx, dy = dx // g, dy // g

            # Ensure consistent sign
            if dx < 0:
                dx, dy = -dx, -dy

            return (dy, dx)

        max_points = 1

        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicates = 1

            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    duplicates += 1
                else:
                    slope = get_slope(points[i], points[j])
                    slopes[slope] += 1

            if slopes:
                max_points = max(max_points, max(slopes.values()) + duplicates)
            else:
                max_points = max(max_points, duplicates)

        return max_points


class SolutionBruteForce:
    """Check all pairs of points and count collinear points"""

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        def collinear(p1, p2, p3):
            """Check if three points are collinear using cross product"""
            return (p2[1] - p1[1]) * (p3[0] - p2[0]) == (p3[1] - p2[1]) * (p2[0] - p1[0])

        max_points = 2

        for i in range(n):
            for j in range(i + 1, n):
                count = 2
                for k in range(n):
                    if k != i and k != j:
                        if collinear(points[i], points[j], points[k]):
                            count += 1
                max_points = max(max_points, count)

        return max_points
