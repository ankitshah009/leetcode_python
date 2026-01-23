#1798. Maximum Number of Consecutive Values You Can Make
#Medium
#
#You are given an integer array coins of length n which represents the n coins
#that you own. The value of the ith coin is coins[i]. You can make some value x
#if you can choose some of your n coins such that their values sum up to x.
#
#Return the maximum number of consecutive integer values that you can make with
#your coins starting from and including 0.
#
#Note that you may have multiple coins of the same value.
#
#Example 1:
#Input: coins = [1,3]
#Output: 2
#
#Example 2:
#Input: coins = [1,1,1,4]
#Output: 8
#
#Example 3:
#Input: coins = [1,4,10,3,1]
#Output: 20
#
#Constraints:
#    coins.length == n
#    1 <= n <= 4 * 10^4
#    1 <= coins[i] <= 4 * 10^4

from typing import List

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        """
        Greedy: sort coins, track max reachable value.
        If we can make [0, reach], adding coin c extends to [0, reach + c]
        only if c <= reach + 1.
        """
        coins.sort()
        reach = 0  # Can make values [0, reach]

        for coin in coins:
            if coin > reach + 1:
                break
            reach += coin

        return reach + 1  # Number of values [0, reach]


class SolutionExplained:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        """
        Same approach with detailed explanation.

        Key insight: If we can make all values from 0 to X,
        and we have a coin of value C where C <= X + 1,
        then we can make all values from 0 to X + C.

        Why? Because:
        - We already can make 0 to X
        - Adding C gives us C to X + C
        - If C <= X + 1, these ranges overlap, giving us 0 to X + C
        """
        coins.sort()
        max_reachable = 0

        for coin in coins:
            # Can we extend our range with this coin?
            if coin <= max_reachable + 1:
                max_reachable += coin
            else:
                # Gap - can't reach (max_reachable + 1)
                break

        return max_reachable + 1


class SolutionDP:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        """
        DP approach (less efficient but clearer).
        """
        total = sum(coins)
        # dp[i] = True if we can make sum i
        dp = [False] * (total + 1)
        dp[0] = True

        for coin in coins:
            # Process in reverse to avoid using same coin twice
            for i in range(total, coin - 1, -1):
                if dp[i - coin]:
                    dp[i] = True

        # Find first value we can't make
        for i in range(total + 1):
            if not dp[i]:
                return i

        return total + 1
