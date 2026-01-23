#1563. Stone Game V
#Hard
#
#There are several stones arranged in a row, and each stone has an associated
#value which is an integer given in the array stoneValue.
#
#In each round of the game, Alice divides the row into two non-empty rows (i.e.
#left row and right row), then Bob calculates the value of each row which is the
#sum of the values of all the stones in this row. Bob throws away the row which
#has the maximum value, and Alice's score increases by the value of the remaining
#row. If the value of the two rows are equal, Bob lets Alice decide which row
#will be thrown away. The game ends when there is only one stone remaining.
#
#Alice's goal is to maximize her score, and Bob will play optimally. Determine
#the maximum score Alice can obtain.
#
#Example 1:
#Input: stoneValue = [6,2,3,4,5,5]
#Output: 18
#Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5].
#The left row has sum 11 and the right row has sum 14. Bob throws away the right
#row and Alice's score is now 11.
#In the second round Alice divides the row to [6], [2,3]. This time Bob throws
#away the left row and Alice's score becomes 16 (11 + 5).
#The last round Alice has only one choice to divide the row which is [2], [3].
#Bob throws away the right row and Alice's score is now 18 (16 + 2).
#The game ends because only one stone is remaining in the row.
#
#Example 2:
#Input: stoneValue = [7,7,7,7,7,7,7]
#Output: 28
#
#Example 3:
#Input: stoneValue = [4]
#Output: 0
#
#Constraints:
#    1 <= stoneValue.length <= 500
#    1 <= stoneValue[i] <= 10^6

from typing import List
from functools import lru_cache

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        """
        Interval DP with memoization.

        dp[i][j] = max score Alice can get from stones[i:j+1]

        For each split point k:
        - left_sum = sum of stones[i:k+1]
        - right_sum = sum of stones[k+1:j+1]
        - If left_sum < right_sum: keep left, score = left_sum + dp[i][k]
        - If left_sum > right_sum: keep right, score = right_sum + dp[k+1][j]
        - If equal: Alice chooses the better option
        """
        n = len(stoneValue)

        # Prefix sums for O(1) range sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def range_sum(i, j):
            return prefix[j + 1] - prefix[i]

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i >= j:
                return 0

            max_score = 0

            for k in range(i, j):
                left_sum = range_sum(i, k)
                right_sum = range_sum(k + 1, j)

                if left_sum < right_sum:
                    score = left_sum + dp(i, k)
                elif left_sum > right_sum:
                    score = right_sum + dp(k + 1, j)
                else:
                    score = left_sum + max(dp(i, k), dp(k + 1, j))

                max_score = max(max_score, score)

            return max_score

        return dp(0, n - 1)


class SolutionIterative:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        """
        Bottom-up DP with tabulation.
        """
        n = len(stoneValue)
        if n == 1:
            return 0

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def range_sum(i, j):
            return prefix[j + 1] - prefix[i]

        # dp[i][j] = max score for interval [i, j]
        dp = [[0] * n for _ in range(n)]

        # Fill by increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                for k in range(i, j):
                    left = range_sum(i, k)
                    right = range_sum(k + 1, j)

                    if left < right:
                        score = left + dp[i][k]
                    elif left > right:
                        score = right + dp[k + 1][j]
                    else:
                        score = left + max(dp[i][k], dp[k + 1][j])

                    dp[i][j] = max(dp[i][j], score)

        return dp[0][n - 1]


class SolutionOptimized:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        """
        Optimized with precomputed max arrays.

        For each interval [i, j], precompute:
        - maxLeft[i][j] = max(left_sum + dp[i][k]) for splits where left < right
        - maxRight[i][j] = max(right_sum + dp[k+1][j]) for splits where right < left
        """
        n = len(stoneValue)
        if n == 1:
            return 0

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i >= j:
                return 0

            result = 0
            for k in range(i, j):
                left = prefix[k + 1] - prefix[i]
                right = prefix[j + 1] - prefix[k + 1]

                if left < right:
                    result = max(result, left + dp(i, k))
                elif left > right:
                    result = max(result, right + dp(k + 1, j))
                else:
                    result = max(result, left + max(dp(i, k), dp(k + 1, j)))

            return result

        return dp(0, n - 1)
