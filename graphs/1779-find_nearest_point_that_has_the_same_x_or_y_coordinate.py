#1779. Find Nearest Point That Has the Same X or Y Coordinate
#Easy
#
#You are given two integers, x and y, which represent your current location on
#a Cartesian grid: (x, y). You are also given an array points where each
#points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is
#valid if it shares the same x-coordinate or the same y-coordinate as your
#location.
#
#Return the index (0-indexed) of the valid point with the smallest Manhattan
#distance from your current location. If there are multiple, return the valid
#point with the smallest index. If there are no valid points, return -1.
#
#The Manhattan distance between two points (x1, y1) and (x2, y2) is
#abs(x1 - x2) + abs(y1 - y2).
#
#Example 1:
#Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
#Output: 2
#
#Example 2:
#Input: x = 3, y = 4, points = [[3,4]]
#Output: 0
#
#Example 3:
#Input: x = 3, y = 4, points = [[2,3]]
#Output: -1
#
#Constraints:
#    1 <= points.length <= 10^4
#    points[i].length == 2
#    1 <= x, y, ai, bi <= 10^4

from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """
        Find valid point with minimum Manhattan distance.
        """
        min_dist = float('inf')
        result = -1

        for i, (px, py) in enumerate(points):
            if px == x or py == y:  # Valid point
                dist = abs(px - x) + abs(py - y)
                if dist < min_dist:
                    min_dist = dist
                    result = i

        return result


class SolutionFiltered:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """
        Filter valid points first.
        """
        valid = [(i, abs(px - x) + abs(py - y))
                 for i, (px, py) in enumerate(points)
                 if px == x or py == y]

        if not valid:
            return -1

        return min(valid, key=lambda p: (p[1], p[0]))[0]


class SolutionOneLiner:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """
        Compact one-liner approach.
        """
        valid = [(abs(px - x) + abs(py - y), i)
                 for i, (px, py) in enumerate(points)
                 if px == x or py == y]
        return min(valid)[1] if valid else -1
