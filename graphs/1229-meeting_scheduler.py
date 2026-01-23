#1229. Meeting Scheduler
#Medium
#
#Given the availability time slots arrays slots1 and slots2 of two people and
#a meeting duration duration, return the earliest time slot that works for
#both of them and is of duration duration.
#
#If there is no common time slot that satisfies the requirements, return an empty array.
#
#The format of a time slot is an array of two elements [start, end] representing
#an inclusive time range from start to end.
#
#It is guaranteed that no two availability slots of the same person intersect
#with each other. That is, for any two time slots [start1, end1] and [start2, end2]
#of the same person, either start1 > end2 or start2 > end1.
#
#Example 1:
#Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
#Output: [60,68]
#
#Example 2:
#Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
#Output: []
#
#Constraints:
#    1 <= slots1.length, slots2.length <= 10^4
#    slots1[i].length, slots2[i].length == 2
#    slots1[i][0] < slots1[i][1]
#    slots2[i][0] < slots2[i][1]
#    0 <= slots1[i][j], slots2[i][j] <= 10^9
#    1 <= duration <= 10^6

from typing import List
import heapq

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        """
        Sort both lists, use two pointers to find intersection.
        """
        slots1.sort()
        slots2.sort()

        i = j = 0

        while i < len(slots1) and j < len(slots2):
            # Find intersection
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])

            if end - start >= duration:
                return [start, start + duration]

            # Move pointer with earlier end time
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1

        return []


class SolutionHeap:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        """
        Use min-heap to process slots in order of start time.
        """
        # Filter out slots that are too short
        slots = [[s, e] for s, e in slots1 if e - s >= duration]
        slots += [[s, e] for s, e in slots2 if e - s >= duration]

        heapq.heapify(slots)

        while len(slots) > 1:
            s1, e1 = heapq.heappop(slots)
            s2, e2 = slots[0]  # Peek at next

            # Check if intersection is long enough
            if e1 >= s2 + duration:
                return [s2, s2 + duration]

        return []
