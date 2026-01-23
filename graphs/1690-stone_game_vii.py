#1690. Stone Game VII
#Medium
#
#Alice and Bob take turns playing a game, with Alice starting first.
#
#There are n stones arranged in a row. On each player's turn, they can remove
#either the leftmost stone or the rightmost stone from the row and receive
#points equal to the sum of the remaining stones' values in the row.
#
#The winner is the one with the higher score when there are no stones left.
#
#Alice wants to maximize the difference in the scores, and Bob wants to minimize
#the difference. Return the difference in Alice and Bob's scores if they both
#play optimally.
#
#Example 1:
#Input: stones = [5,3,1,4,2]
#Output: 6
#Explanation:
#- Alice removes 2, sum = 5+3+1+4 = 13. Alice 13, Bob 0.
#- Bob removes 5, sum = 3+1+4 = 8. Alice 13, Bob 8.
#- Alice removes 4, sum = 3+1 = 4. Alice 17, Bob 8.
#- Bob removes 1, sum = 3. Alice 17, Bob 11.
#- Alice removes 3, sum = 0. Alice 17, Bob 11.
#Difference = 6.
#
#Example 2:
#Input: stones = [7,90,5,1,100,10,10,2]
#Output: 122
#
#Constraints:
#    n == stones.length
#    2 <= n <= 1000
#    1 <= stones[i] <= 1000

from typing import List
from functools import lru_cache

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        """
        DP: dp[i][j] = max score difference for current player on stones[i:j+1].
        """
        n = len(stones)

        # Prefix sums for range sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        def range_sum(i: int, j: int) -> int:
            return prefix[j + 1] - prefix[i]

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i == j:
                return 0

            # Remove left: gain range_sum(i+1, j), opponent plays on [i+1, j]
            remove_left = range_sum(i + 1, j) - dp(i + 1, j)

            # Remove right: gain range_sum(i, j-1), opponent plays on [i, j-1]
            remove_right = range_sum(i, j - 1) - dp(i, j - 1)

            return max(remove_left, remove_right)

        return dp(0, n - 1)


class SolutionIterative:
    def stoneGameVII(self, stones: List[int]) -> int:
        """
        Iterative DP with table.
        """
        n = len(stones)

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # dp[i][j] = max difference for current player on [i, j]
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Sum of [i+1, j]
                sum_left = prefix[j + 1] - prefix[i + 1]
                # Sum of [i, j-1]
                sum_right = prefix[j] - prefix[i]

                dp[i][j] = max(sum_left - dp[i + 1][j],
                              sum_right - dp[i][j - 1])

        return dp[0][n - 1]


class SolutionSpaceOptimized:
    def stoneGameVII(self, stones: List[int]) -> int:
        """
        Space optimized DP using 1D array.
        """
        n = len(stones)

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # dp[j] represents dp[i][j] for current i
        dp = [0] * n

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                sum_left = prefix[j + 1] - prefix[i + 1]
                sum_right = prefix[j] - prefix[i]

                dp[j] = max(sum_left - dp[j], sum_right - dp[j - 1])

        return dp[n - 1]


class SolutionMemo:
    def stoneGameVII(self, stones: List[int]) -> int:
        """
        Memoization with total tracking.
        """
        n = len(stones)
        total = sum(stones)
        memo = {}

        def helper(left: int, right: int, curr_sum: int) -> int:
            if left == right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            # Remove left stone
            new_sum_left = curr_sum - stones[left]
            opt1 = new_sum_left - helper(left + 1, right, new_sum_left)

            # Remove right stone
            new_sum_right = curr_sum - stones[right]
            opt2 = new_sum_right - helper(left, right - 1, new_sum_right)

            memo[(left, right)] = max(opt1, opt2)
            return memo[(left, right)]

        return helper(0, n - 1, total)
