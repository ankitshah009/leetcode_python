#1388. Pizza With 3n Slices
#Hard
#
#There is a pizza with 3n slices of varying size, you and your friends will take
#slices of pizza as follows:
#    You will pick any pizza slice.
#    Your friend Alice will pick the next slice in the anti-clockwise direction
#    of your pick.
#    Your friend Bob will pick the next slice in the clockwise direction of your pick.
#    Repeat until there are no more slices of pizzas.
#
#Given an integer array slices that represent the sizes of the pizza slices in
#a clockwise direction, return the maximum possible sum of slice sizes that you
#can pick.
#
#Example 1:
#Input: slices = [1,2,3,4,5,6]
#Output: 10
#Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with
#size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob
#will pick slice of size 2 and 1 respectively. Total = 4 + 6.
#
#Example 2:
#Input: slices = [8,9,8,6,1,1]
#Output: 16
#Explanation: Pick pizza slice of size 8 in each turn. If you pick slice with
#size 9 your partners will pick slices of size 8.
#
#Example 3:
#Input: slices = [4,1,2,5,8,3,1,9,7]
#Output: 21
#
#Example 4:
#Input: slices = [3,1,2]
#Output: 3
#
#Constraints:
#    3n == slices.length
#    1 <= slices.length <= 500
#    1 <= slices[i] <= 1000

from typing import List
from functools import lru_cache

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        """
        This is equivalent to: pick n non-adjacent elements from circular array
        to maximize sum.

        For circular array: solve for [0, n-2] and [1, n-1] separately.
        For linear array: dp[i][j] = max sum picking j non-adjacent from first i.
        """
        def max_sum_non_adjacent(arr: List[int], picks: int) -> int:
            n = len(arr)
            # dp[i][j] = max sum picking j elements from first i elements
            # where no two adjacent are picked
            dp = [[-float('inf')] * (picks + 1) for _ in range(n + 1)]

            for i in range(n + 1):
                dp[i][0] = 0

            for i in range(1, n + 1):
                for j in range(1, min(i // 2 + 1, picks + 1)):
                    # Don't pick arr[i-1]
                    dp[i][j] = dp[i - 1][j]
                    # Pick arr[i-1] (can't pick arr[i-2])
                    if i >= 2:
                        dp[i][j] = max(dp[i][j], dp[i - 2][j - 1] + arr[i - 1])
                    else:
                        dp[i][j] = max(dp[i][j], arr[i - 1] if j == 1 else -float('inf'))

            return dp[n][picks]

        n = len(slices)
        picks = n // 3

        # Can't pick both first and last (circular)
        # Case 1: exclude last element
        result1 = max_sum_non_adjacent(slices[:-1], picks)
        # Case 2: exclude first element
        result2 = max_sum_non_adjacent(slices[1:], picks)

        return max(result1, result2)


class SolutionMemo:
    def maxSizeSlices(self, slices: List[int]) -> int:
        """Memoization approach"""
        def solve(arr: List[int], picks: int) -> int:
            n = len(arr)

            @lru_cache(maxsize=None)
            def dp(idx: int, remaining: int) -> int:
                if remaining == 0:
                    return 0
                if idx >= n:
                    return -float('inf')
                if n - idx < remaining:  # Not enough elements left
                    return -float('inf')

                # Pick current or skip
                pick = arr[idx] + dp(idx + 2, remaining - 1)
                skip = dp(idx + 1, remaining)
                return max(pick, skip)

            return dp(0, picks)

        n = len(slices)
        picks = n // 3

        return max(solve(slices[:-1], picks), solve(slices[1:], picks))


class SolutionOptimized:
    def maxSizeSlices(self, slices: List[int]) -> int:
        """Space-optimized DP"""
        def solve(arr: List[int], picks: int) -> int:
            n = len(arr)
            # dp[j] = max sum picking j elements ending at or before current
            # prev_dp[j] = same but skipping one before current

            prev2 = [0] * (picks + 1)  # dp[i-2]
            prev1 = [0] * (picks + 1)  # dp[i-1]

            for i in range(n):
                curr = [0] * (picks + 1)
                for j in range(1, picks + 1):
                    # Don't pick
                    curr[j] = prev1[j]
                    # Pick (need to use i-2 state)
                    pick_val = prev2[j - 1] + arr[i]
                    curr[j] = max(curr[j], pick_val)

                prev2 = prev1
                prev1 = curr

            return prev1[picks]

        n = len(slices)
        picks = n // 3

        return max(solve(slices[:-1], picks), solve(slices[1:], picks))
