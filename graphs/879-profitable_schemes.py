#879. Profitable Schemes
#Hard
#
#There is a group of n members, and a list of various crimes they could commit.
#The ith crime generates a profit[i] and requires group[i] members to participate.
#
#If a member participates in one crime, that member can't participate in another crime.
#
#Let's call a profitable scheme any subset of these crimes that generates at
#least minProfit profit, and the total number of members participating in that
#subset of crimes is at most n.
#
#Return the number of schemes that can be chosen. Since the answer may be very
#large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: n = 5, minProfit = 3, profit = [2,2], group = [2,2]
#Output: 2
#Explanation: To make at least 3 profit, the group could commit crimes 0 and 1.
#
#Example 2:
#Input: n = 10, minProfit = 5, profit = [2,3,5], group = [2,3,5]
#Output: 7
#
#Constraints:
#    1 <= n <= 100
#    0 <= minProfit <= 100
#    1 <= group.length <= 100
#    1 <= group[i] <= 100
#    profit.length == group.length
#    0 <= profit[i] <= 100

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, profit: list[int], group: list[int]) -> int:
        """
        3D DP: dp[i][j][k] = schemes using first i crimes, j members, k profit
        Optimize to 2D since we process crimes sequentially.
        """
        MOD = 10**9 + 7
        num_crimes = len(group)

        # dp[j][k] = number of schemes using j members with profit k
        # Cap profit at minProfit (anything >= minProfit is equivalent)
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for c in range(num_crimes):
            g, p = group[c], profit[c]

            # Process in reverse to avoid using same crime twice
            for j in range(n, g - 1, -1):
                for k in range(minProfit, -1, -1):
                    # New profit, capped at minProfit
                    new_profit = min(minProfit, k + p)
                    dp[j][new_profit] = (dp[j][new_profit] + dp[j - g][k]) % MOD

        # Sum all schemes with profit >= minProfit
        return sum(dp[j][minProfit] for j in range(n + 1)) % MOD


class SolutionMemo:
    """Memoized recursion"""

    def profitableSchemes(self, n: int, minProfit: int, profit: list[int], group: list[int]) -> int:
        MOD = 10**9 + 7
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, members, curr_profit):
            """Count schemes starting from crime i with members left and curr_profit"""
            if i == len(group):
                return 1 if curr_profit >= minProfit else 0

            # Don't take crime i
            result = dp(i + 1, members, curr_profit)

            # Take crime i
            if members >= group[i]:
                new_profit = min(curr_profit + profit[i], minProfit)
                result = (result + dp(i + 1, members - group[i], new_profit)) % MOD

            return result

        return dp(0, n, 0)
