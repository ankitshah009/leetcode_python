#312. Burst Balloons
#Hard
#
#You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with
#a number on it represented by an array nums. You are asked to burst all the
#balloons.
#
#If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1]
#coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if
#there is a balloon with a 1 painted on it.
#
#Return the maximum coins you can collect by bursting the balloons wisely.
#
#Example 1:
#Input: nums = [3,1,5,8]
#Output: 167
#Explanation:
#nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
#coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
#Example 2:
#Input: nums = [1,5]
#Output: 10
#
#Constraints:
#    n == nums.length
#    1 <= n <= 300
#    0 <= nums[i] <= 100

from typing import List
from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        DP with interval approach.
        Key insight: instead of thinking about which balloon to burst first,
        think about which balloon to burst LAST in a subarray.
        """
        # Add virtual balloons with value 1 at boundaries
        nums = [1] + nums + [1]
        n = len(nums)

        # dp[i][j] = max coins from bursting balloons in (i, j) exclusive
        dp = [[0] * n for _ in range(n)]

        # Iterate by interval length
        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                # Try each balloon as the last one to burst
                for k in range(left + 1, right):
                    coins = nums[left] * nums[k] * nums[right]
                    total = dp[left][k] + coins + dp[k][right]
                    dp[left][right] = max(dp[left][right], total)

        return dp[0][n - 1]


class SolutionMemo:
    """Memoization approach"""

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @lru_cache(maxsize=None)
        def dp(left, right):
            if left + 1 >= right:
                return 0

            max_coins = 0
            for k in range(left + 1, right):
                coins = nums[left] * nums[k] * nums[right]
                total = dp(left, k) + coins + dp(k, right)
                max_coins = max(max_coins, total)

            return max_coins

        return dp(0, len(nums) - 1)


class SolutionBottomUp:
    """Alternative bottom-up with explicit indexing"""

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        # dp[i][j] = max coins for bursting balloons i+1 to j-1
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(1, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1

                for k in range(i, j + 1):
                    coins = nums[i - 1] * nums[k] * nums[j + 1]
                    left_coins = dp[i][k - 1] if k > i else 0
                    right_coins = dp[k + 1][j] if k < j else 0
                    dp[i][j] = max(dp[i][j], left_coins + coins + right_coins)

        return dp[1][n]
