#1473. Paint House III
#Hard
#
#There is a row of m houses in a small city, each house must be painted with
#one of the n colors (labeled from 1 to n), some houses that have been painted
#last summer should not be painted again.
#
#A neighborhood is a maximal group of continuous houses that are painted with
#the same color.
#
#For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods
#[{1}, {2,2}, {3,3}, {2}, {1,1}].
#
#Given an array houses, an m x n matrix cost and an integer target where:
#    houses[i]: is the color of the house i, and 0 if the house is not painted yet.
#    cost[i][j]: is the cost of paint the house i with the color j + 1.
#
#Return the minimum cost of painting all the remaining houses in such a way
#that there are exactly target neighborhoods. If it is not possible, return -1.
#
#Example 1:
#Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
#Output: 9
#Explanation: Paint houses of this way [1,2,2,1,1]
#This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
#Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
#
#Example 2:
#Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
#Output: 11
#Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
#This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
#Cost of paint the first and last house (10 + 1) = 11.
#
#Example 3:
#Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
#Output: -1
#Explanation: Houses are already painted with a total of 4 neighborhoods.
#
#Constraints:
#    m == houses.length == cost.length
#    n == cost[i].length
#    1 <= m <= 100
#    1 <= n <= 20
#    1 <= target <= m
#    0 <= houses[i] <= n
#    1 <= cost[i][j] <= 10^4

from typing import List
from functools import lru_cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """
        3D DP: dp[i][j][k] = min cost to paint houses 0..i
        where house i has color j and there are k neighborhoods.
        """
        INF = float('inf')

        @lru_cache(maxsize=None)
        def dp(idx: int, prev_color: int, neighborhoods: int) -> int:
            # Base case
            if idx == m:
                return 0 if neighborhoods == target else INF

            # Too many neighborhoods already
            if neighborhoods > target:
                return INF

            # House already painted
            if houses[idx] != 0:
                color = houses[idx]
                new_neighborhoods = neighborhoods + (1 if color != prev_color else 0)
                return dp(idx + 1, color, new_neighborhoods)

            # Try all colors
            min_cost = INF
            for color in range(1, n + 1):
                new_neighborhoods = neighborhoods + (1 if color != prev_color else 0)
                paint_cost = cost[idx][color - 1]
                min_cost = min(min_cost, paint_cost + dp(idx + 1, color, new_neighborhoods))

            return min_cost

        result = dp(0, 0, 0)  # prev_color = 0 means no previous
        return result if result != INF else -1


class SolutionIterative:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """
        Bottom-up DP.
        dp[i][c][t] = min cost for first i houses, house i-1 has color c, t neighborhoods
        """
        INF = float('inf')

        # dp[color][neighborhoods]
        prev = [[INF] * (target + 1) for _ in range(n + 1)]

        # Initialize first house
        if houses[0] != 0:
            prev[houses[0]][1] = 0
        else:
            for c in range(1, n + 1):
                prev[c][1] = cost[0][c - 1]

        # Process remaining houses
        for i in range(1, m):
            curr = [[INF] * (target + 1) for _ in range(n + 1)]

            if houses[i] != 0:
                # House already painted
                color = houses[i]
                for t in range(1, target + 1):
                    # Same color as previous (no new neighborhood)
                    curr[color][t] = min(curr[color][t], prev[color][t])

                    # Different color (new neighborhood)
                    for prev_c in range(1, n + 1):
                        if prev_c != color and t >= 1:
                            curr[color][t] = min(curr[color][t], prev[prev_c][t - 1])
            else:
                # Try all colors
                for color in range(1, n + 1):
                    paint_cost = cost[i][color - 1]

                    for t in range(1, target + 1):
                        # Same color
                        curr[color][t] = min(curr[color][t], prev[color][t] + paint_cost)

                        # Different color
                        for prev_c in range(1, n + 1):
                            if prev_c != color and t >= 1:
                                curr[color][t] = min(curr[color][t], prev[prev_c][t - 1] + paint_cost)

            prev = curr

        # Find minimum cost with exactly target neighborhoods
        result = min(prev[c][target] for c in range(1, n + 1))
        return result if result != INF else -1


class SolutionOptimized:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """
        Optimized: track minimum and second minimum for each neighborhood count.
        """
        INF = float('inf')

        @lru_cache(maxsize=None)
        def dp(idx: int, prev_color: int, neighborhoods: int) -> int:
            if neighborhoods > target:
                return INF
            if idx == m:
                return 0 if neighborhoods == target else INF

            if houses[idx] != 0:
                color = houses[idx]
                new_n = neighborhoods + (1 if color != prev_color else 0)
                return dp(idx + 1, color, new_n)

            min_cost = INF
            for color in range(1, n + 1):
                new_n = neighborhoods + (1 if color != prev_color else 0)
                min_cost = min(min_cost, cost[idx][color - 1] + dp(idx + 1, color, new_n))

            return min_cost

        result = dp(0, 0, 0)
        dp.cache_clear()
        return result if result != INF else -1
