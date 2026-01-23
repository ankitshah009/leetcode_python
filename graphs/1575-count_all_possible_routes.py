#1575. Count All Possible Routes
#Hard
#
#You are given an array of distinct positive integers locations where locations[i]
#represents the position of city i. You are also given integers start, finish
#and fuel representing the starting city, ending city, and the initial amount
#of fuel you have, respectively.
#
#At each step, if you are at city i, you can pick any city j such that j != i
#and 0 <= j < locations.length and move to city j. Moving from city i to city j
#reduces the amount of fuel you have by |locations[i] - locations[j]|. Please
#notice that |x| denotes the absolute value of x.
#
#Notice that fuel cannot become negative at any point in time, and that you are
#allowed to visit any city more than once (including start and finish).
#
#Return the count of all possible routes from start to finish. Since the answer
#may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
#Output: 4
#Explanation: The following are all possible routes, each uses 5 units of fuel:
#1 -> 3, 1 -> 2 -> 3, 1 -> 4 -> 3, 1 -> 4 -> 2 -> 3
#
#Example 2:
#Input: locations = [4,3,1], start = 1, finish = 0, fuel = 6
#Output: 5
#
#Example 3:
#Input: locations = [5,2,1], start = 0, finish = 2, fuel = 3
#Output: 0
#Explanation: It is impossible to get from 0 to 2 using only 3 units of fuel.
#
#Constraints:
#    2 <= locations.length <= 100
#    1 <= locations[i] <= 10^9
#    All integers in locations are distinct.
#    0 <= start, finish < locations.length
#    1 <= fuel <= 200

from typing import List
from functools import lru_cache

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        """
        DP with memoization.
        dp[city][fuel] = number of ways to reach finish from city with fuel remaining.
        """
        MOD = 10**9 + 7
        n = len(locations)

        @lru_cache(maxsize=None)
        def dp(city: int, remaining_fuel: int) -> int:
            # Base case: no fuel left
            if remaining_fuel < 0:
                return 0

            # Count routes starting from this state
            count = 1 if city == finish else 0

            # Try moving to each other city
            for next_city in range(n):
                if next_city != city:
                    cost = abs(locations[city] - locations[next_city])
                    if cost <= remaining_fuel:
                        count = (count + dp(next_city, remaining_fuel - cost)) % MOD

            return count

        return dp(start, fuel)


class SolutionIterative:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        """
        Bottom-up DP.
        dp[f][c] = number of ways to reach finish from city c with f fuel.
        """
        MOD = 10**9 + 7
        n = len(locations)

        # dp[f][c] = ways to reach finish from city c with fuel f
        dp = [[0] * n for _ in range(fuel + 1)]

        # Base case: at finish with any amount of fuel
        for f in range(fuel + 1):
            dp[f][finish] = 1

        # Fill table: iterate fuel from 0 to fuel
        for f in range(fuel + 1):
            for c in range(n):
                for next_c in range(n):
                    if next_c != c:
                        cost = abs(locations[c] - locations[next_c])
                        if f >= cost:
                            dp[f][c] = (dp[f][c] + dp[f - cost][next_c]) % MOD

        return dp[fuel][start]


class SolutionOptimized:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        """
        Optimized DP with pruning.
        """
        MOD = 10**9 + 7
        n = len(locations)

        # Precompute distances
        dist = [[abs(locations[i] - locations[j]) for j in range(n)] for i in range(n)]

        # Minimum fuel needed to reach finish from each city
        min_to_finish = [dist[i][finish] for i in range(n)]

        @lru_cache(maxsize=None)
        def dp(city: int, remaining: int) -> int:
            # Pruning: can't reach finish
            if remaining < min_to_finish[city]:
                return 0

            count = 1 if city == finish else 0

            for next_city in range(n):
                if next_city != city:
                    cost = dist[city][next_city]
                    if cost <= remaining:
                        count = (count + dp(next_city, remaining - cost)) % MOD

            return count

        return dp(start, fuel)
