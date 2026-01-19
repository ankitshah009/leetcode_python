#435. Non-overlapping Intervals
#Medium
#
#Given an array of intervals intervals where intervals[i] = [starti, endi],
#return the minimum number of intervals you need to remove to make the rest of
#the intervals non-overlapping.
#
#Example 1:
#Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
#Output: 1
#Explanation: [1,3] can be removed and the rest of the intervals are
#non-overlapping.
#
#Example 2:
#Input: intervals = [[1,2],[1,2],[1,2]]
#Output: 2
#Explanation: You need to remove two [1,2] to make the rest of the intervals
#non-overlapping.
#
#Example 3:
#Input: intervals = [[1,2],[2,3]]
#Output: 0
#Explanation: You don't need to remove any of the intervals since they're
#already non-overlapping.
#
#Constraints:
#    1 <= intervals.length <= 10^5
#    intervals[i].length == 2
#    -5 * 10^4 <= starti < endi <= 5 * 10^4

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Greedy: Keep as many non-overlapping intervals as possible.
        Sort by end time, always pick interval that ends earliest.
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        count = 1  # Count of non-overlapping intervals
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]

        return len(intervals) - count


class SolutionRemoveCount:
    """Direct counting of removals"""

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start < prev_end:
                # Overlap - remove current (keep previous as it ends earlier)
                removals += 1
            else:
                prev_end = end

        return removals


class SolutionSortByStart:
    """Sort by start time"""

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        removals = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start < prev_end:
                # Overlap - remove the one that ends later
                removals += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end

        return removals
