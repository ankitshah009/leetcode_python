#812. Largest Triangle Area
#Easy
#
#Given an array of points on the X-Y plane points where points[i] = [xi, yi],
#return the area of the largest triangle that can be formed by any three
#different points. Answers within 10^-5 of the actual answer will be accepted.
#
#Example 1:
#Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
#Output: 2.00000
#Explanation: The five points are (0,0), (0,1), (1,0), (0,2), (2,0).
#The largest triangle is formed by (0,0), (0,2), and (2,0) with area 2.
#
#Example 2:
#Input: points = [[1,0],[0,0],[0,1]]
#Output: 0.50000
#
#Constraints:
#    3 <= points.length <= 50
#    -50 <= xi, yi <= 50
#    All the given points are unique.

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        """
        Use Shoelace formula for triangle area.
        Area = 0.5 * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
        """
        def triangle_area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        max_area = 0
        n = len(points)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    area = triangle_area(points[i], points[j], points[k])
                    max_area = max(max_area, area)

        return max_area


class SolutionCombinations:
    """Using itertools.combinations"""

    def largestTriangleArea(self, points: list[list[int]]) -> float:
        from itertools import combinations

        def area(p1, p2, p3):
            return 0.5 * abs(
                (p2[0] - p1[0]) * (p3[1] - p1[1]) -
                (p3[0] - p1[0]) * (p2[1] - p1[1])
            )

        return max(area(*tri) for tri in combinations(points, 3))


class SolutionCrossProduct:
    """Using cross product formula"""

    def largestTriangleArea(self, points: list[list[int]]) -> float:
        from itertools import combinations

        def area(A, B, C):
            # Vectors AB and AC
            # Area = 0.5 * |AB x AC|
            return 0.5 * abs(
                (B[0] - A[0]) * (C[1] - A[1]) -
                (B[1] - A[1]) * (C[0] - A[0])
            )

        return max(area(a, b, c) for a, b, c in combinations(points, 3))
