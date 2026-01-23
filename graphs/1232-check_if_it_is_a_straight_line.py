#1232. Check If It Is a Straight Line
#Easy
#
#You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
#represents the coordinate of a point. Check if these points make a straight
#line in the XY plane.
#
#Example 1:
#Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
#Output: true
#
#Example 2:
#Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
#Output: false
#
#Constraints:
#    2 <= coordinates.length <= 1000
#    coordinates[i].length == 2
#    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
#    coordinates contains no duplicate point.

from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        Check if all points have the same slope relative to first point.
        Use cross product to avoid division (handles vertical lines).

        For points (x0, y0), (x1, y1), (x2, y2):
        They're collinear if (y1-y0)/(x1-x0) == (y2-y0)/(x2-x0)
        Which is (y1-y0)*(x2-x0) == (y2-y0)*(x1-x0)
        """
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        dx = x1 - x0
        dy = y1 - y0

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            # Cross product check
            if dy * (x - x0) != dx * (y - y0):
                return False

        return True


class SolutionSlope:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """Using slope (need to handle vertical lines)"""
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            # Check (y - y0) * (x1 - x0) == (y1 - y0) * (x - x0)
            if (y - y0) * (x1 - x0) != (y1 - y0) * (x - x0):
                return False

        return True
