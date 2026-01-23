#1353. Maximum Number of Events That Can Be Attended
#Medium
#
#You are given an array of events where events[i] = [startDayi, endDayi]. Every
#event i starts at startDayi and ends at endDayi.
#
#You can attend an event i at any day d where startTimei <= d <= endTimei. You
#can only attend one event at any time d.
#
#Return the maximum number of events you can attend.
#
#Example 1:
#Input: events = [[1,2],[2,3],[3,4]]
#Output: 3
#Explanation: You can attend all the three events.
#One way is as shown.
#Attend the first event on day 1.
#Attend the second event on day 2.
#Attend the third event on day 3.
#
#Example 2:
#Input: events = [[1,2],[2,3],[3,4],[1,2]]
#Output: 4
#
#Constraints:
#    1 <= events.length <= 10^5
#    events[i].length == 2
#    1 <= startDayi <= endDayi <= 10^5

from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Greedy with min heap.
        For each day, add all events starting that day to heap (by end day).
        Attend the event ending soonest.
        """
        events.sort()  # Sort by start day
        n = len(events)

        min_heap = []  # Heap of end days
        event_idx = 0
        attended = 0

        # Process each day
        day = 1
        max_day = max(e[1] for e in events)

        while day <= max_day:
            # Add all events starting on this day
            while event_idx < n and events[event_idx][0] == day:
                heapq.heappush(min_heap, events[event_idx][1])
                event_idx += 1

            # Remove events that have already ended
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Attend the event ending soonest
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1

            day += 1

        return attended


class SolutionOptimized:
    def maxEvents(self, events: List[List[int]]) -> int:
        """Optimized: skip empty days"""
        events.sort()
        n = len(events)

        min_heap = []
        event_idx = 0
        attended = 0
        day = 0

        while event_idx < n or min_heap:
            # If heap is empty, jump to next event's start day
            if not min_heap:
                day = events[event_idx][0]

            # Add all events starting on or before this day
            while event_idx < n and events[event_idx][0] <= day:
                heapq.heappush(min_heap, events[event_idx][1])
                event_idx += 1

            # Remove expired events
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Attend event ending soonest
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1

            day += 1

        return attended
