#1610. Maximum Number of Visible Points
#Hard
#
#You are given an array points, an integer angle, and your location, where
#location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates
#on the X-Y plane.
#
#Initially, you are facing directly east from your position. You cannot move
#from your position, but you can rotate. In other words, posx and posy cannot
#be changed. Your field of view in degrees is represented by angle, determining
#how wide you can see from any given view direction. Let d be the amount in
#degrees that you rotate counterclockwise. Then, your field of view is the
#inclusive range of angles [d - angle/2, d + angle/2].
#
#You can see some set of points if, for each point, the angle formed by the
#point, your position, and the initial direction from your position is in your
#field of view.
#
#There can be multiple points at one coordinate. There may be points at your
#location, and you can always see these points regardless of your rotation.
#Points do not obstruct your vision to other points.
#
#Return the maximum number of points you can see.
#
#Example 1:
#Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
#Output: 3
#Explanation: All points can be made visible in your field of view.
#
#Example 2:
#Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
#Output: 4
#Explanation: All points can be made visible in your field of view, including
#the one at your location.
#
#Example 3:
#Input: points = [[1,0],[2,1]], angle = 13, location = [1,1]
#Output: 1
#
#Constraints:
#    1 <= points.length <= 10^5
#    points[i].length == 2
#    location.length == 2
#    0 <= angle < 360
#    0 <= posx, posy, xi, yi <= 100

from typing import List
import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        """
        1. Convert each point to angle relative to location
        2. Sort angles
        3. Use sliding window to find max points within angle range
        4. Handle wrap-around by duplicating angles + 360
        """
        x0, y0 = location
        same_location = 0
        angles = []

        for x, y in points:
            if x == x0 and y == y0:
                same_location += 1
            else:
                # Calculate angle in degrees
                rad = math.atan2(y - y0, x - x0)
                deg = math.degrees(rad)
                angles.append(deg)

        if not angles:
            return same_location

        angles.sort()

        # Duplicate angles for wrap-around
        angles = angles + [a + 360 for a in angles]

        # Sliding window
        max_visible = 0
        left = 0

        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)

        return max_visible + same_location


class SolutionBinarySearch:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        """
        Binary search approach for finding range.
        """
        from bisect import bisect_right

        px, py = location
        at_origin = 0
        angles = []

        for x, y in points:
            if x == px and y == py:
                at_origin += 1
            else:
                ang = math.degrees(math.atan2(y - py, x - px))
                angles.append(ang)

        if not angles:
            return at_origin

        angles.sort()
        n = len(angles)

        # Extend for circular
        extended = angles + [a + 360 for a in angles]

        max_count = 0
        for i in range(n):
            target = angles[i] + angle
            count = bisect_right(extended, target, i, i + n) - i
            max_count = max(max_count, count)

        return max_count + at_origin


class SolutionDetailed:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        """
        Detailed solution with comments.
        """
        ox, oy = location

        # Points at the same location are always visible
        same = 0
        degrees = []

        for x, y in points:
            if x == ox and y == oy:
                same += 1
            else:
                # atan2 gives angle in radians from -π to π
                rad = math.atan2(y - oy, x - ox)
                # Convert to degrees (range: -180 to 180)
                deg = math.degrees(rad)
                degrees.append(deg)

        if not degrees:
            return same

        # Sort the angles
        degrees.sort()
        n = len(degrees)

        # Handle wrap-around: add 360 to all angles and append
        degrees += [d + 360 for d in degrees]

        # Sliding window to find max points within 'angle' degrees
        best = 0
        left = 0

        for right in range(2 * n):
            # Shrink window if span exceeds allowed angle
            while degrees[right] - degrees[left] > angle:
                left += 1

            best = max(best, right - left + 1)

        return best + same
