#1288. Remove Covered Intervals
#Medium
#
#Given an array intervals where intervals[i] = [li, ri] represent the interval
#[li, ri), remove all intervals that are covered by another interval in the list.
#
#The interval [a, b) is covered by the interval [c, d) if and only if c <= a
#and b <= d.
#
#Return the number of remaining intervals.
#
#Example 1:
#Input: intervals = [[1,4],[3,6],[2,8]]
#Output: 2
#Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
#
#Example 2:
#Input: intervals = [[1,4],[2,3]]
#Output: 1
#
#Constraints:
#    1 <= intervals.length <= 1000
#    intervals[i].length == 2
#    0 <= li < ri <= 10^5
#    All the given intervals are unique.

from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        Sort by start ascending, then by end descending.
        Count intervals not covered by previous ones.
        """
        # Sort by start asc, end desc
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_end = 0

        for start, end in intervals:
            # If current end is greater than max_end, it's not covered
            if end > max_end:
                count += 1
                max_end = end

        return count


class SolutionBruteForce:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """O(n^2) check each pair"""
        n = len(intervals)
        covered = [False] * n

        for i in range(n):
            for j in range(n):
                if i != j and not covered[i]:
                    # Check if intervals[i] is covered by intervals[j]
                    if intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                        covered[i] = True
                        break

        return sum(1 for c in covered if not c)
