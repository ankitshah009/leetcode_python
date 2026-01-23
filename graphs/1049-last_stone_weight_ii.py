#1049. Last Stone Weight II
#Medium
#
#You are given an array of integers stones where stones[i] is the weight
#of the ith stone.
#
#We are playing a game with the stones. On each turn, we choose any two
#stones and smash them together. Suppose the stones have weights x and y
#with x <= y. The result of this smash is:
#    If x == y, both stones are destroyed, and
#    If x != y, the stone of weight x is destroyed, and the stone of weight
#    y has new weight y - x.
#
#At the end of the game, there is at most one stone left.
#
#Return the smallest possible weight of the left stone. If there are no
#stones left, return 0.
#
#Example 1:
#Input: stones = [2,7,4,1,8,1]
#Output: 1
#Explanation: We can combine stones as follows:
#(2,4) -> 2, array is [2,7,1,8,1]
#(7,8) -> 1, array is [2,1,1,1]
#(2,1) -> 1, array is [1,1,1]
#(1,1) -> 0, array is [1]
#
#Example 2:
#Input: stones = [31,26,33,21,40]
#Output: 5
#
#Constraints:
#    1 <= stones.length <= 30
#    1 <= stones[i] <= 100

from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        This is equivalent to partitioning stones into two groups
        and minimizing |sum1 - sum2|.

        Similar to 0/1 knapsack: find subset with sum closest to total/2.
        """
        total = sum(stones)
        target = total // 2

        # dp[i] = True if sum i is achievable
        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            # Iterate backwards to avoid using same stone twice
            for j in range(target, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]

        # Find largest achievable sum <= target
        for i in range(target, -1, -1):
            if dp[i]:
                return total - 2 * i

        return total


class SolutionSet:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """Using set to track all achievable sums"""
        achievable = {0}

        for stone in stones:
            achievable = {s + stone for s in achievable} | {s for s in achievable}

        total = sum(stones)
        return min(abs(total - 2 * s) for s in achievable)


class SolutionMemo:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """Memoized recursion"""
        from functools import lru_cache

        total = sum(stones)

        @lru_cache(maxsize=None)
        def dp(idx, current_sum):
            if idx == len(stones):
                return abs(total - 2 * current_sum)

            # Include in group 1 or not
            return min(
                dp(idx + 1, current_sum + stones[idx]),
                dp(idx + 1, current_sum)
            )

        return dp(0, 0)
