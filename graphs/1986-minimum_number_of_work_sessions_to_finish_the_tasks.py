#1986. Minimum Number of Work Sessions to Finish the Tasks
#Medium
#
#There are n tasks assigned to you. The task times are represented as an integer
#array tasks of length n, where the ith task takes tasks[i] hours to finish. A
#work session is when you work for at most sessionTime consecutive hours and
#then take a break.
#
#You should finish the given tasks in a way that satisfies the following
#conditions:
#- If you start a task in a work session, you must complete it in the same work
#  session.
#- You can start a new task immediately after finishing the previous one.
#- You may complete the tasks in any order.
#
#Given tasks and sessionTime, return the minimum number of work sessions needed
#to finish all the tasks.
#
#Example 1:
#Input: tasks = [1,2,3], sessionTime = 3
#Output: 2
#Explanation: [1,2] in one session, [3] in another.
#
#Example 2:
#Input: tasks = [3,1,3,1,1], sessionTime = 8
#Output: 2
#
#Example 3:
#Input: tasks = [1,2,3,4,5], sessionTime = 15
#Output: 1
#
#Constraints:
#    n == tasks.length
#    1 <= n <= 14
#    1 <= tasks[i] <= 10
#    max(tasks[i]) <= sessionTime <= 15

from typing import List
from functools import lru_cache

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        """
        Bitmask DP: dp[mask] = (sessions, remaining_time_in_current)
        """
        n = len(tasks)

        @lru_cache(maxsize=None)
        def dp(mask: int) -> tuple:
            """Returns (min_sessions, max_remaining_time)"""
            if mask == 0:
                return (0, 0)

            best = (float('inf'), 0)

            for i in range(n):
                if mask & (1 << i):
                    prev_sessions, prev_remaining = dp(mask ^ (1 << i))

                    if prev_remaining >= tasks[i]:
                        # Fit in current session
                        curr = (prev_sessions, prev_remaining - tasks[i])
                    else:
                        # Need new session
                        curr = (prev_sessions + 1, sessionTime - tasks[i])

                    # Better = fewer sessions, or same sessions with more remaining
                    if curr[0] < best[0] or (curr[0] == best[0] and curr[1] > best[1]):
                        best = curr

            return best

        return dp((1 << n) - 1)[0]


class SolutionPrecompute:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        """
        Precompute valid subsets that fit in one session.
        """
        n = len(tasks)

        # Precompute sum of each subset
        subset_sum = [0] * (1 << n)
        for mask in range(1 << n):
            for i in range(n):
                if mask & (1 << i):
                    subset_sum[mask] = subset_sum[mask ^ (1 << i)] + tasks[i]
                    break

        # valid[mask] = True if subset fits in one session
        valid = [subset_sum[mask] <= sessionTime for mask in range(1 << n)]

        # dp[mask] = min sessions to complete tasks in mask
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            # Try all subsets of remaining tasks
            submask = mask
            while submask:
                if valid[submask]:
                    prev_mask = mask ^ submask
                    dp[mask] = min(dp[mask], dp[prev_mask] + 1)
                submask = (submask - 1) & mask

        return dp[(1 << n) - 1]


class SolutionBacktrack:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        """
        Backtracking with pruning.
        """
        n = len(tasks)
        tasks.sort(reverse=True)  # Largest first for better pruning

        sessions = []
        min_sessions = [n]  # Worst case: each task in own session

        def backtrack(idx: int):
            if idx == n:
                min_sessions[0] = min(min_sessions[0], len(sessions))
                return

            if len(sessions) >= min_sessions[0]:
                return  # Pruning

            # Try adding to existing session
            for i in range(len(sessions)):
                if sessions[i] + tasks[idx] <= sessionTime:
                    sessions[i] += tasks[idx]
                    backtrack(idx + 1)
                    sessions[i] -= tasks[idx]

            # Start new session
            sessions.append(tasks[idx])
            backtrack(idx + 1)
            sessions.pop()

        backtrack(0)
        return min_sessions[0]
