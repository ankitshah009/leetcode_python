#57. Insert Interval
#Medium
#
#You are given an array of non-overlapping intervals intervals where
#intervals[i] = [starti, endi] represent the start and the end of the ith
#interval and intervals is sorted in ascending order by starti. You are also
#given an interval newInterval = [start, end] that represents the start and end
#of another interval.
#
#Insert newInterval into intervals such that intervals is still sorted in
#ascending order by starti and intervals still does not have any overlapping
#intervals (merge overlapping intervals if necessary).
#
#Return intervals after the insertion.
#
#Example 1:
#Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#Output: [[1,5],[6,9]]
#
#Example 2:
#Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#Output: [[1,2],[3,10],[12,16]]
#
#Constraints:
#    0 <= intervals.length <= 10^4
#    intervals[i].length == 2
#    0 <= starti <= endi <= 10^5
#    intervals is sorted by starti in ascending order.
#    newInterval.length == 2
#    0 <= start <= end <= 10^5

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Three-phase approach: left non-overlapping, merge, right non-overlapping.
        """
        result = []
        i = 0
        n = len(intervals)
        start, end = newInterval

        # Add all intervals that end before newInterval starts
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


class SolutionSimple:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Simple iteration approach.
        """
        result = []

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                # newInterval ends before current starts
                return result + [newInterval] + intervals[i:]
            elif newInterval[0] > interval[1]:
                # newInterval starts after current ends
                result.append(interval)
            else:
                # Overlapping - merge
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1])
                ]

        result.append(newInterval)
        return result


class SolutionBinarySearch:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Binary search to find insertion point.
        """
        import bisect

        if not intervals:
            return [newInterval]

        # Find where newInterval would be inserted based on start
        starts = [i[0] for i in intervals]
        left = bisect.bisect_left(starts, newInterval[0])

        # Insert and merge
        intervals.insert(left, newInterval)

        # Merge overlapping
        result = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])

        return result
