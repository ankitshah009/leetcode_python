#1037. Valid Boomerang
#Easy
#
#Given an array points where points[i] = [xi, yi] represents a point on the
#X-Y plane, return true if these points are a boomerang.
#
#A boomerang is a set of three points that are all distinct and not in a
#straight line.
#
#Example 1:
#Input: points = [[1,1],[2,3],[3,2]]
#Output: true
#
#Example 2:
#Input: points = [[1,1],[2,2],[3,3]]
#Output: false
#
#Constraints:
#    points.length == 3
#    points[i].length == 2
#    0 <= xi, yi <= 100

from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        """
        Check if three points are collinear using cross product.
        If cross product of vectors AB and AC is zero, points are collinear.
        """
        (x1, y1), (x2, y2), (x3, y3) = points

        # Cross product: (B-A) x (C-A)
        # = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
        cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

        return cross != 0


class SolutionSlope:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        """
        Check using slope comparison.
        To avoid division, compare cross-multiplied.
        """
        (x1, y1), (x2, y2), (x3, y3) = points

        # Slope AB: (y2-y1)/(x2-x1)
        # Slope AC: (y3-y1)/(x3-x1)
        # Equal if (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1)

        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)


class SolutionArea:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        """
        Three points form a boomerang iff triangle area > 0.
        Area = 0.5 * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
        """
        (x1, y1), (x2, y2), (x3, y3) = points

        area_doubled = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        return area_doubled > 0
