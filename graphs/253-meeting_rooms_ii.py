#253. Meeting Rooms II
#Medium
#
#Given an array of meeting time intervals intervals where intervals[i] =
#[starti, endi], return the minimum number of conference rooms required.
#
#Example 1:
#Input: intervals = [[0,30],[5,10],[15,20]]
#Output: 2
#
#Example 2:
#Input: intervals = [[7,10],[2,4]]
#Output: 1
#
#Constraints:
#    1 <= intervals.length <= 10^4
#    0 <= starti < endi <= 10^6

import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Min heap approach.
        Sort by start time, use heap to track end times.
        Heap size = number of rooms needed.
        """
        if not intervals:
            return 0

        # Sort by start time
        intervals.sort(key=lambda x: x[0])

        # Min heap of end times
        heap = []
        heapq.heappush(heap, intervals[0][1])

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # If earliest ending meeting ends before this starts, reuse room
            if heap[0] <= start:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap)


class SolutionChronological:
    """Chronological ordering / sweep line"""

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Create events: +1 for start, -1 for end
        events = []
        for start, end in intervals:
            events.append((start, 1))   # Meeting starts
            events.append((end, -1))    # Meeting ends

        # Sort by time; if same time, process ends before starts
        events.sort(key=lambda x: (x[0], x[1]))

        rooms_needed = 0
        current_rooms = 0

        for _, delta in events:
            current_rooms += delta
            rooms_needed = max(rooms_needed, current_rooms)

        return rooms_needed


class SolutionTwoArrays:
    """Separate start and end arrays"""

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        rooms = 0
        end_ptr = 0

        for start in starts:
            if start >= ends[end_ptr]:
                # A meeting ended, reuse room
                end_ptr += 1
            else:
                # Need new room
                rooms += 1

        return rooms
