#1335. Minimum Difficulty of a Job Schedule
#Hard
#
#You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work
#on the ith job, you have to finish all the jobs j where 0 <= j < i).
#
#You have to finish at least one task every day. The difficulty of a job
#schedule is the sum of difficulties of each day of the d days. The difficulty
#of a day is the maximum difficulty of a job done on that day.
#
#You are given an integer array jobDifficulty and an integer d. The difficulty
#of the ith job is jobDifficulty[i].
#
#Return the minimum difficulty of a job schedule. If you cannot find a schedule
#for the jobs return -1.
#
#Example 1:
#Input: jobDifficulty = [6,5,4,3,2,1], d = 2
#Output: 7
#Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
#Second day you can finish the last job, total difficulty = 1.
#The difficulty of the schedule = 6 + 1 = 7
#
#Example 2:
#Input: jobDifficulty = [9,9,9], d = 4
#Output: -1
#Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
#
#Example 3:
#Input: jobDifficulty = [1,1,1], d = 3
#Output: 3
#Explanation: The schedule is one job per day. total difficulty will be 3.
#
#Constraints:
#    1 <= jobDifficulty.length <= 300
#    0 <= jobDifficulty[i] <= 1000
#    1 <= d <= 10

from typing import List
from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        DP: dp[i][day] = min difficulty to complete jobs[i:] in 'day' days.
        """
        n = len(jobDifficulty)

        if n < d:
            return -1

        @lru_cache(maxsize=None)
        def dp(i, days_left):
            # Need at least days_left jobs remaining
            if n - i < days_left:
                return float('inf')

            # Last day: do all remaining jobs
            if days_left == 1:
                return max(jobDifficulty[i:])

            # Try each cut point
            min_cost = float('inf')
            max_diff = 0

            # Jobs today: from i to j (inclusive), at least one job remaining for other days
            for j in range(i, n - days_left + 1):
                max_diff = max(max_diff, jobDifficulty[j])
                cost = max_diff + dp(j + 1, days_left - 1)
                min_cost = min(min_cost, cost)

            return min_cost

        return dp(0, d)


class SolutionBottomUp:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """Bottom-up DP"""
        n = len(jobDifficulty)

        if n < d:
            return -1

        INF = float('inf')
        # dp[day][i] = min difficulty to schedule jobs[0:i] in 'day' days
        dp = [[INF] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0

        for day in range(1, d + 1):
            for i in range(day, n + 1):
                # Jobs[0:i] scheduled in 'day' days
                # Last day does jobs[j:i] for some j
                max_diff = 0
                for j in range(i - 1, day - 2, -1):
                    max_diff = max(max_diff, jobDifficulty[j])
                    if dp[day - 1][j] != INF:
                        dp[day][i] = min(dp[day][i], dp[day - 1][j] + max_diff)

        return dp[d][n]


class SolutionOptimized:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """Space optimized O(n) DP"""
        n = len(jobDifficulty)

        if n < d:
            return -1

        INF = float('inf')
        prev = [INF] * n

        # Day 1: must do jobs[0:i+1]
        max_val = 0
        for i in range(n):
            max_val = max(max_val, jobDifficulty[i])
            prev[i] = max_val

        for day in range(2, d + 1):
            curr = [INF] * n

            for i in range(day - 1, n):
                max_diff = 0
                # Last day jobs: j+1 to i
                for j in range(i, day - 2, -1):
                    max_diff = max(max_diff, jobDifficulty[j])
                    if j > 0 and prev[j - 1] != INF:
                        curr[i] = min(curr[i], prev[j - 1] + max_diff)

            prev = curr

        return prev[n - 1]
