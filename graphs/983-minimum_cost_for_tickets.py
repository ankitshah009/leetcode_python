#983. Minimum Cost For Tickets
#Medium
#
#You have planned some train traveling one year in advance. The days of the year
#in which you will travel are given as an integer array days. Each day is an
#integer from 1 to 365.
#
#Train tickets are sold in three different ways:
#- a 1-day pass is sold for costs[0] dollars,
#- a 7-day pass is sold for costs[1] dollars, and
#- a 30-day pass is sold for costs[2] dollars.
#
#The passes allow unlimited travels on those days.
#
#Return the minimum number of dollars you need to travel every day in days.
#
#Example 1:
#Input: days = [1,4,6,7,8,20], costs = [2,7,15]
#Output: 11
#Explanation: Buy 1-day pass on day 1, 7-day pass on day 4, 1-day pass on day 20.
#
#Example 2:
#Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
#Output: 17
#
#Constraints:
#    1 <= days.length <= 365
#    1 <= days[i] <= 365
#    days is in strictly increasing order.
#    costs.length == 3
#    1 <= costs[i] <= 1000

class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """
        DP: dp[i] = min cost to cover days[i:]
        """
        from functools import lru_cache

        days_set = set(days)
        last_day = days[-1]

        @lru_cache(maxsize=None)
        def dp(day: int) -> int:
            if day > last_day:
                return 0

            if day not in days_set:
                return dp(day + 1)

            return min(
                costs[0] + dp(day + 1),
                costs[1] + dp(day + 7),
                costs[2] + dp(day + 30)
            )

        return dp(1)


class SolutionIterative:
    """Bottom-up DP"""

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        days_set = set(days)
        last_day = days[-1]

        dp = [0] * (last_day + 1)

        for day in range(1, last_day + 1):
            if day not in days_set:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(
                    dp[max(0, day - 1)] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2]
                )

        return dp[last_day]


class SolutionByDay:
    """DP indexed by day index"""

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        import bisect
        from functools import lru_cache

        n = len(days)

        @lru_cache(maxsize=None)
        def dp(idx: int) -> int:
            if idx >= n:
                return 0

            # 1-day pass
            res = costs[0] + dp(idx + 1)

            # 7-day pass: find first day after days[idx] + 7
            j = bisect.bisect_left(days, days[idx] + 7)
            res = min(res, costs[1] + dp(j))

            # 30-day pass
            j = bisect.bisect_left(days, days[idx] + 30)
            res = min(res, costs[2] + dp(j))

            return res

        return dp(0)
