#1595. Minimum Cost to Connect Two Groups of Points
#Hard
#
#You are given two groups of points where the first group has size1 points,
#the second group has size2 points, and size1 >= size2.
#
#The cost of the connection between any two points are given in an size1 x size2
#matrix where cost[i][j] is the cost of connecting point i of the first group
#and point j of the second group. The groups are connected if each point in
#both groups is connected to one or more points in the opposite group. In other
#words, each point in the first group must be connected to at least one point
#in the second group, and each point in the second group must be connected to
#at least one point in the first group.
#
#Return the minimum cost it takes to connect the two groups.
#
#Example 1:
#Input: cost = [[15, 96], [36, 2]]
#Output: 17
#Explanation: The optimal assignment is:
#1--A, 2--B. The cost is 15 + 2 = 17.
#
#Example 2:
#Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
#Output: 4
#Explanation: The optimal assignment is:
#1--A, 2--B, 2--C, 3--A. The cost is 1 + 1 + 1 + 1 = 4.
#
#Example 3:
#Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
#Output: 10
#
#Constraints:
#    size1 == cost.length
#    size2 == cost[i].length
#    1 <= size1, size2 <= 12
#    size1 >= size2
#    0 <= cost[i][j] <= 100

from typing import List
from functools import lru_cache

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        """
        DP with bitmask for group2 connections.

        For each point in group1, we must connect it to at least one point in group2.
        After processing all group1 points, any unconnected group2 points must be
        connected to the minimum cost group1 point.

        State: dp(i, mask) = min cost to process group1 points 0..i-1
               where mask represents which group2 points are connected.
        """
        m, n = len(cost), len(cost[0])

        # Precompute minimum cost to connect each group2 point
        min_cost_g2 = [min(cost[i][j] for i in range(m)) for j in range(n)]

        @lru_cache(maxsize=None)
        def dp(i: int, mask: int) -> int:
            if i == m:
                # Connect any unconnected group2 points with min cost
                total = 0
                for j in range(n):
                    if not (mask & (1 << j)):
                        total += min_cost_g2[j]
                return total

            result = float('inf')

            # Try connecting point i to each subset of group2 points
            # But must connect to at least one
            for j in range(n):
                # Connect point i to point j
                new_mask = mask | (1 << j)
                result = min(result, cost[i][j] + dp(i + 1, new_mask))

            return result

        return dp(0, 0)


class SolutionDP:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        """
        Bottom-up DP with bitmask.
        """
        m, n = len(cost), len(cost[0])

        # Precompute minimum cost to connect each group2 point
        min_cost = [min(cost[i][j] for i in range(m)) for j in range(n)]

        # dp[mask] = min cost to have group2 connections as mask
        # After processing all group1 points
        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0

        for i in range(m):
            new_dp = [INF] * (1 << n)

            for mask in range(1 << n):
                if dp[mask] == INF:
                    continue

                # Point i must connect to at least one group2 point
                for j in range(n):
                    new_mask = mask | (1 << j)
                    new_dp[new_mask] = min(new_dp[new_mask], dp[mask] + cost[i][j])

            dp = new_dp

        # Handle unconnected group2 points
        result = INF
        for mask in range(1 << n):
            if dp[mask] == INF:
                continue

            total = dp[mask]
            for j in range(n):
                if not (mask & (1 << j)):
                    total += min_cost[j]

            result = min(result, total)

        return result


class SolutionOptimized:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        """
        Optimized DP: include unconnected cost incrementally.
        """
        m, n = len(cost), len(cost[0])

        # Min cost to connect each group2 point
        min_g2 = [min(cost[i][j] for i in range(m)) for j in range(n)]

        # dp[i][mask] = min cost with first i group1 points processed
        # and mask showing connected group2 points
        INF = float('inf')

        # Start: no group1 processed, each unconnected group2 has min_cost
        dp = [[INF] * (1 << n) for _ in range(m + 1)]

        # Base case: cost of unconnected group2 points
        for mask in range(1 << n):
            cost_unconnected = sum(min_g2[j] for j in range(n) if not (mask & (1 << j)))
            dp[m][mask] = cost_unconnected

        # Fill from bottom up
        for i in range(m - 1, -1, -1):
            for mask in range(1 << n):
                for j in range(n):
                    new_mask = mask | (1 << j)
                    dp[i][mask] = min(dp[i][mask], cost[i][j] + dp[i + 1][new_mask])

        return dp[0][0]
