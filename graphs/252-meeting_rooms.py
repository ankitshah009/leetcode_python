#252. Meeting Rooms
#Easy
#
#Given an array of meeting time intervals where intervals[i] = [starti, endi],
#determine if a person could attend all meetings.
#
#Example 1:
#Input: intervals = [[0,30],[5,10],[15,20]]
#Output: false
#
#Example 2:
#Input: intervals = [[7,10],[2,4]]
#Output: true
#
#Constraints:
#    0 <= intervals.length <= 10^4
#    intervals[i].length == 2
#    0 <= starti < endi <= 10^6

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """Sort by start time and check for overlaps"""
        if not intervals:
            return True

        # Sort by start time
        intervals.sort(key=lambda x: x[0])

        # Check if any meeting starts before the previous one ends
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False

        return True


class SolutionAlternative:
    """Using zip to compare consecutive intervals"""

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        return all(
            end <= next_start
            for (_, end), (next_start, _) in zip(intervals, intervals[1:])
        )


class SolutionBruteForce:
    """O(n^2) - check all pairs"""

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)

        for i in range(n):
            for j in range(i + 1, n):
                # Check if intervals overlap
                if self.overlaps(intervals[i], intervals[j]):
                    return False

        return True

    def overlaps(self, a, b):
        # Two intervals overlap if one doesn't end before the other starts
        return not (a[1] <= b[0] or b[1] <= a[0])
