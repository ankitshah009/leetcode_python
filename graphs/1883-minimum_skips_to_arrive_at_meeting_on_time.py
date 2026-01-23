#1883. Minimum Skips to Arrive at Meeting On Time
#Hard
#
#You are given an integer hoursBefore, the number of hours you have to travel
#to reach the meeting. To arrive at the meeting, you have to travel through n
#roads. The road lengths are given as an integer array dist of length n, where
#dist[i] describes the length of the ith road in kilometers. In addition, you
#are given an integer speed, which is the speed (in km/h) you will travel at.
#
#After you travel road i, you must rest and wait for the next integer hour
#before you can begin traveling on the next road. Note that you do not have to
#rest after traveling the last road because you are already at the meeting.
#
#However, you are allowed to skip some rests to be able to arrive on time,
#meaning you do not need to wait for the next integer hour. Note that this
#means you may finish traveling future roads at different hours compared to if
#you had not skipped any rests.
#
#Return the minimum number of skips required to arrive at the meeting on time,
#or -1 if it is impossible.
#
#Example 1:
#Input: dist = [1,3,2], speed = 4, hoursBefore = 2
#Output: 1
#
#Example 2:
#Input: dist = [7,3,5,5], speed = 2, hoursBefore = 10
#Output: 2
#
#Example 3:
#Input: dist = [7,3,5,5], speed = 1, hoursBefore = 10
#Output: -1
#
#Constraints:
#    n == dist.length
#    1 <= n <= 1000
#    1 <= dist[i] <= 10^5
#    1 <= speed <= 10^6
#    1 <= hoursBefore <= 10^7

from typing import List
import math

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        """
        DP: dp[i][j] = min time to travel first i roads with j skips.

        Use integer arithmetic to avoid floating point errors.
        Multiply everything by speed.
        """
        n = len(dist)
        INF = float('inf')

        # dp[j] = min time * speed to complete roads with j skips
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            new_dp = [INF] * (n + 1)

            for j in range(i + 1):
                # Option 1: Don't skip (except for last road)
                if i < n - 1:
                    # Round up to next hour: ceil((dp[j] + dist[i]) / speed) * speed
                    time_no_skip = ((dp[j] + dist[i] + speed - 1) // speed) * speed
                    new_dp[j] = min(new_dp[j], time_no_skip)
                else:
                    # Last road: no need to round
                    new_dp[j] = min(new_dp[j], dp[j] + dist[i])

                # Option 2: Skip rest (use one more skip)
                time_skip = dp[j] + dist[i]
                new_dp[j + 1] = min(new_dp[j + 1], time_skip)

            dp = new_dp

        # Find minimum skips where time <= hoursBefore * speed
        max_time = hoursBefore * speed

        for skips in range(n + 1):
            if dp[skips] <= max_time:
                return skips

        return -1


class SolutionMemo:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        """
        Top-down DP with memoization.
        """
        from functools import lru_cache

        n = len(dist)
        max_time = hoursBefore * speed

        @lru_cache(maxsize=None)
        def dp(i: int, skips: int) -> int:
            """Min time*speed to complete first i roads with 'skips' skips."""
            if i == 0:
                return 0

            prev = dp(i - 1, skips)

            # No skip: round up (except last road)
            if i < n:
                no_skip = ((prev + dist[i - 1] + speed - 1) // speed) * speed
            else:
                no_skip = prev + dist[i - 1]

            # Skip: need at least one skip remaining
            if skips > 0:
                skip = dp(i - 1, skips - 1) + dist[i - 1]
                return min(no_skip, skip)

            return no_skip

        for skips in range(n + 1):
            if dp(n, skips) <= max_time:
                return skips

        return -1
