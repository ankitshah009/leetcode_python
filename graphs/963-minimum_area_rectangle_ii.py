#963. Minimum Area Rectangle II
#Medium
#
#You are given an array of points in the X-Y plane points where points[i] =
#[xi, yi].
#
#Return the minimum area of any rectangle formed from these points, with sides
#not necessarily parallel to the X and Y axes. If there is not any such
#rectangle, return 0.
#
#Answers within 10^-5 of the actual answer will be accepted.
#
#Example 1:
#Input: points = [[1,2],[2,1],[1,0],[0,1]]
#Output: 2.00000
#
#Example 2:
#Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
#Output: 1.00000
#
#Example 3:
#Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
#Output: 0
#
#Constraints:
#    1 <= points.length <= 50
#    points[i].length == 2
#    0 <= xi, yi <= 4 * 10^4
#    All the given points are unique.

from collections import defaultdict
import math

class Solution:
    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        """
        Group point pairs by their center and distance.
        Two pairs with same center and distance form a rectangle.
        """
        n = len(points)
        point_set = set(map(tuple, points))

        # Group by (center, distance^2)
        groups = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                # Center (use 2x to avoid float)
                cx = x1 + x2
                cy = y1 + y2

                # Distance squared
                dist_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2

                groups[(cx, cy, dist_sq)].append((i, j))

        min_area = float('inf')

        for pairs in groups.values():
            if len(pairs) < 2:
                continue

            for k in range(len(pairs)):
                for m in range(k + 1, len(pairs)):
                    i1, j1 = pairs[k]
                    i2, j2 = pairs[m]

                    # Points form a rectangle
                    p1 = points[i1]
                    p2 = points[j1]
                    p3 = points[i2]

                    # Calculate area using two adjacent sides
                    side1 = math.sqrt((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2)
                    side2 = math.sqrt((p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2)

                    area = side1 * side2
                    min_area = min(min_area, area)

        return min_area if min_area != float('inf') else 0


class SolutionDirect:
    """Check all 4-point combinations"""

    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        n = len(points)
        point_set = {tuple(p) for p in points}
        min_area = float('inf')

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(j + 1, n):
                    if k == i:
                        continue

                    # Check if points[i], points[j], points[k] form right angle at i
                    p1, p2, p3 = points[i], points[j], points[k]

                    # Vectors from p1
                    v1 = (p2[0] - p1[0], p2[1] - p1[1])
                    v2 = (p3[0] - p1[0], p3[1] - p1[1])

                    # Check perpendicular (dot product = 0)
                    if v1[0] * v2[0] + v1[1] * v2[1] != 0:
                        continue

                    # Fourth point
                    p4 = (p2[0] + v2[0], p2[1] + v2[1])

                    if p4 in point_set:
                        side1 = math.sqrt(v1[0]**2 + v1[1]**2)
                        side2 = math.sqrt(v2[0]**2 + v2[1]**2)
                        min_area = min(min_area, side1 * side2)

        return min_area if min_area != float('inf') else 0
