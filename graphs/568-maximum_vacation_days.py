#568. Maximum Vacation Days
#Hard
#
#LeetCode wants to give one of its best employees the option to travel among n
#cities to collect algorithm problems. But all work and no play makes Jack a dull
#boy, you could take vacations in some particular cities and weeks. Your job is
#to schedule the traveling to maximize the number of vacation days you could take,
#but there are certain rules and restrictions you need to follow.
#
#Rules and restrictions:
#1. You can only travel among n cities, represented by indexes from 0 to n-1.
#2. You start in the city indexed 0 on Monday.
#3. flights[i][j] == 1 means there is a flight from city i to city j; Otherwise,
#   flights[i][j] == 0 means no such flight.
#4. days[i][j] represents the maximum vacation days in city i in week j.
#5. You can stay in a city beyond the number of vacation days, but you should work
#   on the extra days, which won't be counted as vacation days.
#6. If you fly from city A to city B and take the vacation on that day, the
#   deduction will be counted towards the vacation days of city B in that week.
#7. We don't consider the impact of flight hours on the calculation of vacation days.
#
#Constraints:
#    n == flights.length == flights[i].length == days.length
#    k == days[i].length
#    1 <= n, k <= 100
#    flights[i][j] is 0 or 1
#    0 <= days[i][j] <= 7

from typing import List

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        """
        DP: dp[w][c] = max vacation days at end of week w in city c
        """
        n = len(flights)
        k = len(days[0])

        # dp[city] = max vacation days ending at this city
        dp = [float('-inf')] * n
        dp[0] = 0  # Start in city 0

        for week in range(k):
            new_dp = [float('-inf')] * n

            for curr in range(n):
                if dp[curr] == float('-inf'):
                    continue

                # Stay in current city
                new_dp[curr] = max(new_dp[curr], dp[curr] + days[curr][week])

                # Fly to another city
                for dest in range(n):
                    if flights[curr][dest] == 1:
                        new_dp[dest] = max(new_dp[dest], dp[curr] + days[dest][week])

            dp = new_dp

        return max(dp)


class SolutionMemo:
    """Top-down with memoization"""

    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        from functools import lru_cache

        n = len(flights)
        k = len(days[0])

        @lru_cache(maxsize=None)
        def dp(city, week):
            if week == k:
                return 0

            max_days = 0

            # Stay in current city
            max_days = max(max_days, days[city][week] + dp(city, week + 1))

            # Fly to another city
            for dest in range(n):
                if flights[city][dest] == 1:
                    max_days = max(max_days, days[dest][week] + dp(dest, week + 1))

            return max_days

        return dp(0, 0)
