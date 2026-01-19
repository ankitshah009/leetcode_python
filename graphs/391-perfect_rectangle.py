#391. Perfect Rectangle
#Hard
#
#Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an
#axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and
#the top-right point of it is (ai, bi).
#
#Return true if all the rectangles together form an exact cover of a
#rectangular region.
#
#Example 1:
#Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
#Output: true
#Explanation: All 5 rectangles together form an exact cover of a rectangular
#region.
#
#Example 2:
#Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
#Output: false
#Explanation: Because there is a gap between the two rectangular regions.
#
#Example 3:
#Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
#Output: false
#Explanation: Because two of the rectangles overlap with each other.
#
#Constraints:
#    1 <= rectangles.length <= 2 * 10^4
#    rectangles[i].length == 4
#    -10^5 <= xi, yi, ai, bi <= 10^5

from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        Key insight:
        1. Total area must equal bounding rectangle area
        2. Each corner should appear odd times except the 4 corners of the
           bounding rectangle (which appear once)
        """
        corners = set()
        area = 0

        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')

        for x1, y1, x2, y2 in rectangles:
            # Update bounding rectangle
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            # Add area
            area += (x2 - x1) * (y2 - y1)

            # Toggle corners (XOR with set)
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

        # Check if remaining corners are exactly the 4 corners of bounding rect
        expected_corners = {(min_x, min_y), (min_x, max_y),
                          (max_x, min_y), (max_x, max_y)}

        if corners != expected_corners:
            return False

        # Check area
        expected_area = (max_x - min_x) * (max_y - min_y)
        return area == expected_area


class SolutionSweepLine:
    """Sweep line approach (more complex but handles edge cases)"""

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        from sortedcontainers import SortedList

        # Events: (x, type, y1, y2)
        # type: 0 = start, 1 = end
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 0, y1, y2))  # Rectangle starts
            events.append((x2, 1, y1, y2))  # Rectangle ends

        events.sort()

        # Active intervals
        active = SortedList()

        i = 0
        while i < len(events):
            x = events[i][0]

            # Process all events at this x coordinate
            while i < len(events) and events[i][0] == x:
                _, event_type, y1, y2 = events[i]
                if event_type == 0:
                    # Check for overlap
                    idx = active.bisect_left((y1, y2))
                    if idx > 0 and active[idx - 1][1] > y1:
                        return False
                    if idx < len(active) and active[idx][0] < y2:
                        return False
                    active.add((y1, y2))
                else:
                    active.remove((y1, y2))
                i += 1

        return True
