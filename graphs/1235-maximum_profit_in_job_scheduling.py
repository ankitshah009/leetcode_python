#1235. Maximum Profit in Job Scheduling
#Hard
#
#We have n jobs, where every job is scheduled to be done from startTime[i] to
#endTime[i], obtaining a profit of profit[i].
#
#You're given the startTime, endTime and profit arrays, return the maximum
#profit you can take such that there are no two jobs in the subset with
#overlapping time range.
#
#If you choose a job that ends at time X you will be able to start another job
#that starts at time X.
#
#Example 1:
#Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
#Output: 120
#Explanation: The subset chosen is the first and fourth job.
#Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
#
#Example 2:
#Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
#Output: 150
#Explanation: The subset chosen is the first, fourth and fifth job.
#We get profit of 150 = 20 + 70 + 60.
#
#Example 3:
#Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
#Output: 6
#
#Constraints:
#    1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
#    1 <= startTime[i] < endTime[i] <= 10^9
#    1 <= profit[i] <= 10^4

from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Sort jobs by end time.
        DP: dp[i] = max profit considering first i jobs.

        For each job, either skip it or take it.
        If take, find latest non-overlapping job using binary search.
        """
        n = len(startTime)

        # Create and sort jobs by end time
        jobs = sorted(zip(endTime, startTime, profit))

        # dp[i] = max profit considering first i jobs (1-indexed)
        dp = [0] * (n + 1)
        end_times = [job[0] for job in jobs]

        for i in range(1, n + 1):
            end, start, p = jobs[i - 1]

            # Option 1: Don't take this job
            dp[i] = dp[i - 1]

            # Option 2: Take this job
            # Find latest job that ends <= start (using end_times which is sorted)
            j = bisect.bisect_right(end_times, start, 0, i - 1)
            dp[i] = max(dp[i], dp[j] + p)

        return dp[n]


class SolutionMemo:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """Top-down DP with memoization"""
        n = len(startTime)

        # Sort by start time
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [job[0] for job in jobs]

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i):
            if i >= n:
                return 0

            start, end, p = jobs[i]

            # Option 1: Skip this job
            skip = dp(i + 1)

            # Option 2: Take this job, find next non-overlapping
            next_job = bisect.bisect_left(starts, end, i + 1)
            take = p + dp(next_job)

            return max(skip, take)

        return dp(0)


class SolutionAlt:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """Alternative implementation with direct mapping"""
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        # dp[i] = (end_time, max_profit up to and including job ending at end_time)
        dp = [(0, 0)]

        for start, end, p in jobs:
            # Binary search for latest job ending <= start
            i = bisect.bisect_right(dp, (start, float('inf'))) - 1

            # Max profit if we take this job
            take_profit = dp[i][1] + p

            # Only update if taking gives better profit
            if take_profit > dp[-1][1]:
                dp.append((end, take_profit))

        return dp[-1][1]
