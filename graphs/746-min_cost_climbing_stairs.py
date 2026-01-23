#746. Min Cost Climbing Stairs
#Easy
#
#You are given an integer array cost where cost[i] is the cost of ith step on
#a staircase. Once you pay the cost, you can either climb one or two steps.
#
#You can either start from the step with index 0, or the step with index 1.
#
#Return the minimum cost to reach the top of the floor.
#
#Example 1:
#Input: cost = [10,15,20]
#Output: 15
#Explanation: You will start at index 1.
#- Pay 15 and climb two steps to reach the top.
#The total cost is 15.
#
#Example 2:
#Input: cost = [1,100,1,1,1,100,1,1,100,1]
#Output: 6
#Explanation: You will start at index 0.
#- Pay 1 and climb two steps to reach index 2.
#- Pay 1 and climb two steps to reach index 4.
#- Pay 1 and climb two steps to reach index 6.
#- Pay 1 and climb one step to reach index 7.
#- Pay 1 and climb two steps to reach index 9.
#- Pay 1 and climb one step to reach the top.
#The total cost is 6.
#
#Constraints:
#    2 <= cost.length <= 1000
#    0 <= cost[i] <= 999

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        DP: min cost to reach step i is min(dp[i-1], dp[i-2]) + cost[i].
        O(1) space by keeping only last two values.
        """
        prev2, prev1 = 0, 0

        for c in cost:
            curr = min(prev1, prev2) + c
            prev2, prev1 = prev1, curr

        return min(prev1, prev2)


class SolutionDP:
    """Explicit DP array"""

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]


class SolutionInPlace:
    """Modify cost array in place"""

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[-1], cost[-2])


class SolutionRecursive:
    """Recursive with memoization"""

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i):
            if i < 2:
                return 0
            return min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])

        return dp(len(cost))
