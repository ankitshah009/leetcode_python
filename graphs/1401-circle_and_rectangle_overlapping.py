#1401. Circle and Rectangle Overlapping
#Medium
#
#You are given a circle represented as (radius, xCenter, yCenter) and an
#axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the
#coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the
#top-right corner of the rectangle.
#
#Return true if the circle and rectangle are overlapped otherwise return false.
#In other words, check if there is any point (xi, yi) that belongs to the circle
#and the rectangle at the same time.
#
#Example 1:
#Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
#Output: true
#Explanation: Circle and rectangle share the point (1,0).
#
#Example 2:
#Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
#Output: false
#
#Example 3:
#Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
#Output: true
#
#Constraints:
#    1 <= radius <= 2000
#    -10^4 <= xCenter, yCenter <= 10^4
#    -10^4 <= x1 < x2 <= 10^4
#    -10^4 <= y1 < y2 <= 10^4

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        Find the closest point on the rectangle to the circle center.
        If distance from center to this point <= radius, they overlap.

        Closest point = clamp(center, rect_min, rect_max) for each axis.
        """
        # Find closest point on rectangle to circle center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        # Calculate distance from center to closest point
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        # Check if distance <= radius
        return dx * dx + dy * dy <= radius * radius


class SolutionExplicit:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:
        """More explicit version"""
        # Clamp x coordinate
        if xCenter < x1:
            closest_x = x1
        elif xCenter > x2:
            closest_x = x2
        else:
            closest_x = xCenter

        # Clamp y coordinate
        if yCenter < y1:
            closest_y = y1
        elif yCenter > y2:
            closest_y = y2
        else:
            closest_y = yCenter

        # Distance squared
        dist_squared = (xCenter - closest_x) ** 2 + (yCenter - closest_y) ** 2

        return dist_squared <= radius ** 2


class SolutionRegions:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        Check overlap based on which region the center is in.
        9 regions: inside, 4 edges, 4 corners.
        """
        # Inside rectangle
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True

        # Check edges (horizontal and vertical distances)
        # Left edge
        if xCenter < x1 and y1 <= yCenter <= y2:
            return x1 - xCenter <= radius
        # Right edge
        if xCenter > x2 and y1 <= yCenter <= y2:
            return xCenter - x2 <= radius
        # Bottom edge
        if yCenter < y1 and x1 <= xCenter <= x2:
            return y1 - yCenter <= radius
        # Top edge
        if yCenter > y2 and x1 <= xCenter <= x2:
            return yCenter - y2 <= radius

        # Check corners
        corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        for cx, cy in corners:
            if (xCenter - cx) ** 2 + (yCenter - cy) ** 2 <= radius ** 2:
                return True

        return False
