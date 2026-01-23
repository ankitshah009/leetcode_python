#1326. Minimum Number of Taps to Open to Water a Garden
#Hard
#
#There is a one-dimensional garden on the x-axis. The garden starts at the point
#0 and ends at the point n. (i.e., the length of the garden is n).
#
#There are n + 1 taps located at points [0, 1, ..., n] in the garden.
#
#Given an integer n and an integer array ranges of length n + 1 where ranges[i]
#(0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]]
#if it was open.
#
#Return the minimum number of taps that should be open to water the whole garden,
#If the garden cannot be watered return -1.
#
#Example 1:
#Input: n = 5, ranges = [3,4,1,1,0,0]
#Output: 1
#Explanation: The tap at point 0 can cover the interval [-3,3]
#The tap at point 1 can cover the interval [-3,5]
#The tap at point 2 can cover the interval [1,3]
#The tap at point 3 can cover the interval [2,4]
#The tap at point 4 can cover the interval [4,4]
#The tap at point 5 can cover the interval [5,5]
#Opening only the second tap will water the whole garden [0,5]
#
#Example 2:
#Input: n = 3, ranges = [0,0,0,0]
#Output: -1
#Explanation: Even if you activate all the four taps you cannot water the whole garden.
#
#Constraints:
#    1 <= n <= 10^4
#    ranges.length == n + 1
#    0 <= ranges[i] <= 100

from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
        Greedy interval covering problem.
        Convert to intervals and use jump game approach.
        """
        # max_reach[i] = furthest right we can reach starting from position i
        max_reach = [0] * (n + 1)

        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            max_reach[left] = max(max_reach[left], right)

        # Greedy: similar to Jump Game II
        taps = 0
        current_end = 0
        next_end = 0

        for i in range(n + 1):
            if i > next_end:
                return -1  # Can't reach position i

            next_end = max(next_end, max_reach[i])

            if i == current_end and i < n:
                taps += 1
                current_end = next_end

        return taps


class SolutionIntervals:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """Convert to interval covering problem"""
        # Create intervals
        intervals = []
        for i, r in enumerate(ranges):
            if r > 0:
                left = max(0, i - r)
                right = min(n, i + r)
                intervals.append((left, right))

        # Sort by start, then by end (descending for same start)
        intervals.sort(key=lambda x: (x[0], -x[1]))

        taps = 0
        covered = 0
        i = 0
        m = len(intervals)

        while covered < n:
            max_right = covered

            # Find the interval that starts before covered and extends furthest
            while i < m and intervals[i][0] <= covered:
                max_right = max(max_right, intervals[i][1])
                i += 1

            if max_right == covered:
                return -1  # Can't extend further

            taps += 1
            covered = max_right

        return taps


class SolutionDP:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """DP approach: dp[i] = min taps to water [0, i]"""
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)

            for j in range(left, right + 1):
                if dp[left] != INF:
                    dp[j] = min(dp[j], dp[left] + 1)

        return dp[n] if dp[n] != INF else -1
