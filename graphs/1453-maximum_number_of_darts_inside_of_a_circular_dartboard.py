#1453. Maximum Number of Darts Inside of a Circular Dartboard
#Hard
#
#Alice is throwing n darts on a very large wall. You are given an array darts
#where darts[i] = [xi, yi] is the position of the ith dart that Alice threw on
#the wall.
#
#Bob knows the positions of the n darts on the wall. He wants to place a
#dartboard of radius r on the wall so that the maximum number of darts that
#Alice throws lie on the dartboard.
#
#Given the integer r, return the maximum number of darts that can lie on the
#dartboard.
#
#Example 1:
#Input: darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
#Output: 4
#Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all points.
#
#Example 2:
#Input: darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
#Output: 5
#Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all
#points except the point (7,8).
#
#Constraints:
#    1 <= darts.length <= 100
#    darts[i].length == 2
#    -10^4 <= xi, yi <= 10^4
#    All the darts are unique
#    1 <= r <= 5000

from typing import List
import math

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        """
        Key insight: optimal circle passes through at least 2 dart points.
        For each pair of points, find circle center(s) with radius r
        that pass through both points, then count darts inside.
        """
        n = len(darts)
        if n == 1:
            return 1

        def distance(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        def get_centers(p1, p2, r):
            """Get center(s) of circle with radius r passing through p1 and p2"""
            d = distance(p1, p2)
            if d > 2 * r:
                return []
            if d == 0:
                return [(p1[0], p1[1])]

            # Midpoint
            mx = (p1[0] + p2[0]) / 2
            my = (p1[1] + p2[1]) / 2

            # Distance from midpoint to center
            h = math.sqrt(r * r - (d / 2) ** 2)

            # Perpendicular direction
            dx = (p2[1] - p1[1]) / d
            dy = -(p2[0] - p1[0]) / d

            return [
                (mx + h * dx, my + h * dy),
                (mx - h * dx, my - h * dy)
            ]

        def count_inside(cx, cy, r):
            count = 0
            for x, y in darts:
                if (x - cx)**2 + (y - cy)**2 <= r * r + 1e-6:
                    count += 1
            return count

        max_darts = 1

        for i in range(n):
            for j in range(i + 1, n):
                centers = get_centers(darts[i], darts[j], r)
                for cx, cy in centers:
                    max_darts = max(max_darts, count_inside(cx, cy, r))

        return max_darts


class SolutionAngularSweep:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        """
        Angular sweep: for each dart as potential boundary point,
        sweep around to count maximum darts inside.
        O(n^2 log n)
        """
        n = len(darts)
        max_count = 1

        for i in range(n):
            # Collect angles where other points enter/exit
            events = []

            for j in range(n):
                if i == j:
                    continue

                dx = darts[j][0] - darts[i][0]
                dy = darts[j][1] - darts[i][1]
                d = math.sqrt(dx * dx + dy * dy)

                if d > 2 * r:
                    continue

                # Angle to point j from i
                angle = math.atan2(dy, dx)
                # Half angle subtended
                delta = math.acos(d / (2 * r))

                # Entry and exit angles
                enter = angle - delta
                exit_angle = angle + delta

                events.append((enter, 0))  # 0 = enter
                events.append((exit_angle, 1))  # 1 = exit

            # Sort by angle, enters before exits at same angle
            events.sort(key=lambda x: (x[0], x[1]))

            count = 1  # Current point i is always inside
            for angle, event_type in events:
                if event_type == 0:
                    count += 1
                else:
                    count -= 1
                max_count = max(max_count, count)

        return max_count
