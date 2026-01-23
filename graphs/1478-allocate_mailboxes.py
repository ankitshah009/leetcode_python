#1478. Allocate Mailboxes
#Hard
#
#Given the array houses where houses[i] is the location of the ith house along
#a street and an integer k, allocate k mailboxes in the street.
#
#Return the minimum total distance between each house and its nearest mailbox.
#
#The test cases are generated so that the answer fits in a 32-bit integer.
#
#Example 1:
#Input: houses = [1,4,8,10,20], k = 3
#Output: 5
#Explanation: Allocate mailboxes in position 3, 9 and 20.
#Minimum total distance from each houses to nearest mailboxes is
#|3-1| + |4-3| + |9-8| + |9-10| + |20-20| = 5
#
#Example 2:
#Input: houses = [2,3,5,12,18], k = 2
#Output: 9
#Explanation: Allocate mailboxes in position 3 and 15.
#Minimum total distance from each houses to nearest mailboxes is
#|2-3| + |3-3| + |5-3| + |12-15| + |18-15| = 9.
#
#Constraints:
#    1 <= k <= houses.length <= 100
#    1 <= houses[i] <= 10^4
#    All the integers of houses are unique.

from typing import List
from functools import lru_cache

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        """
        DP: divide houses into k groups, place one mailbox per group.
        For one mailbox serving houses[i:j+1], optimal position is median.
        """
        houses.sort()
        n = len(houses)

        # Precompute cost to serve houses[i:j+1] with one mailbox
        # Optimal position is median, cost is sum of distances to median
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                median = houses[(i + j) // 2]
                cost[i][j] = sum(abs(houses[x] - median) for x in range(i, j + 1))

        @lru_cache(maxsize=None)
        def dp(idx: int, remaining: int) -> int:
            """Min cost to serve houses[idx:] with 'remaining' mailboxes"""
            if idx == n:
                return 0 if remaining == 0 else float('inf')
            if remaining == 0:
                return float('inf')

            # Try all possible first groups
            min_cost = float('inf')
            for j in range(idx, n):
                group_cost = cost[idx][j]
                min_cost = min(min_cost, group_cost + dp(j + 1, remaining - 1))

            return min_cost

        return dp(0, k)


class SolutionIterative:
    def minDistance(self, houses: List[int], k: int) -> int:
        """
        Bottom-up DP.
        dp[i][j] = min cost to serve first i houses with j mailboxes
        """
        houses.sort()
        n = len(houses)

        # Precompute costs
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                median = houses[(i + j) // 2]
                cost[i][j] = sum(abs(houses[x] - median) for x in range(i, j + 1))

        # DP
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                # Try all possible last groups
                for m in range(j - 1, i):
                    # Houses m to i-1 are served by one mailbox
                    dp[i][j] = min(dp[i][j], dp[m][j - 1] + cost[m][i - 1])

        return dp[n][k]


class SolutionOptimizedCost:
    def minDistance(self, houses: List[int], k: int) -> int:
        """
        Optimized cost calculation using prefix sum.
        """
        houses.sort()
        n = len(houses)

        # Prefix sum for efficient cost calculation
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + houses[i]

        def get_cost(i: int, j: int) -> int:
            """Cost to serve houses[i:j+1] with one mailbox at median"""
            mid = (i + j) // 2
            # Sum of (houses[mid] - houses[x]) for x in [i, mid]
            # + Sum of (houses[x] - houses[mid]) for x in [mid, j]
            left_count = mid - i + 1
            right_count = j - mid

            left_sum = houses[mid] * left_count - (prefix[mid + 1] - prefix[i])
            right_sum = (prefix[j + 1] - prefix[mid + 1]) - houses[mid] * right_count

            return left_sum + right_sum

        @lru_cache(maxsize=None)
        def dp(idx: int, remaining: int) -> int:
            if idx == n:
                return 0 if remaining == 0 else float('inf')
            if remaining == 0:
                return float('inf')

            min_cost = float('inf')
            for j in range(idx, n):
                min_cost = min(min_cost, get_cost(idx, j) + dp(j + 1, remaining - 1))

            return min_cost

        result = dp(0, k)
        dp.cache_clear()
        return result
