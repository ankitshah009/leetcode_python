#218. The Skyline Problem
#Hard
#
#A city's skyline is the outer contour of the silhouette formed by all the
#buildings in that city when viewed from a distance. Given the locations and
#heights of all the buildings, return the skyline formed by these buildings
#collectively.
#
#The geometric information of each building is given in the array buildings where
#buildings[i] = [lefti, righti, heighti]:
#    lefti is the x coordinate of the left edge of the ith building.
#    righti is the x coordinate of the right edge of the ith building.
#    heighti is the height of the ith building.
#
#You may assume all buildings are perfect rectangles grounded on an absolutely
#flat surface at height 0.
#
#The skyline should be represented as a list of "key points" sorted by their
#x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left
#endpoint of some horizontal segment in the skyline except the last point in the
#list, which always has a y-coordinate 0 and is used to mark the skyline's
#termination where the rightmost building ends.
#
#Example 1:
#Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
#Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
#
#Constraints:
#    1 <= buildings.length <= 10^4
#    0 <= lefti < righti <= 2^31 - 1
#    1 <= heighti <= 2^31 - 1
#    buildings is sorted by lefti in non-decreasing order.

import heapq
from sortedcontainers import SortedList

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create events: (x, type, height)
        # type: 0 for building start (negative height for max heap)
        # type: 1 for building end
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))  # Start event
            events.append((right, 0, 0))            # End event

        # Sort events by x, then by height (starts before ends at same x)
        events.sort()

        result = [[0, 0]]  # Dummy point
        # Max heap: (-height, end_x)
        heap = [(0, float('inf'))]  # Ground level

        for x, neg_height, end_x in events:
            # Remove expired buildings
            while heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_height:  # Building start
                heapq.heappush(heap, (neg_height, end_x))

            # Get current max height
            max_height = -heap[0][0]

            # If height changed, add to result
            if result[-1][1] != max_height:
                result.append([x, max_height])

        return result[1:]  # Remove dummy point

    # Using SortedList for cleaner solution
    def getSkylineSorted(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height))   # Start (negative for sorting)
            events.append((right, height))   # End

        events.sort()
        result = []
        heights = SortedList([0])  # Track active heights

        for x, h in events:
            if h < 0:  # Building start
                heights.add(-h)
            else:      # Building end
                heights.remove(h)

            max_height = heights[-1]

            if not result or result[-1][1] != max_height:
                result.append([x, max_height])

        return result
