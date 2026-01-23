#1799. Maximize Score After N Operations
#Hard
#
#You are given nums, an array of positive integers of size 2 * n. You must
#perform n operations on this array.
#
#In the ith operation (1-indexed), you will:
#- Choose two elements, x and y.
#- Receive a score of i * gcd(x, y).
#- Remove x and y from nums.
#
#Return the maximum score you can receive after performing n operations.
#
#The function gcd(x, y) is the greatest common divisor of x and y.
#
#Example 1:
#Input: nums = [1,2]
#Output: 1
#
#Example 2:
#Input: nums = [3,4,6,8]
#Output: 11
#
#Example 3:
#Input: nums = [1,2,3,4,5,6]
#Output: 14
#
#Constraints:
#    1 <= n <= 7
#    nums.length == 2 * n
#    1 <= nums[i] <= 10^6

from typing import List
from functools import lru_cache
from math import gcd

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        """
        Bitmask DP - track which elements have been used.
        """
        n = len(nums)

        # Precompute GCDs
        gcds = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                gcds[i][j] = gcd(nums[i], nums[j])

        @lru_cache(maxsize=None)
        def dp(mask: int, op: int) -> int:
            if op > n // 2:
                return 0

            max_score = 0

            # Try all pairs of unused elements
            for i in range(n):
                if mask & (1 << i):
                    continue
                for j in range(i + 1, n):
                    if mask & (1 << j):
                        continue

                    new_mask = mask | (1 << i) | (1 << j)
                    score = op * gcds[i][j] + dp(new_mask, op + 1)
                    max_score = max(max_score, score)

            return max_score

        return dp(0, 1)


class SolutionIterative:
    def maxScore(self, nums: List[int]) -> int:
        """
        Bottom-up DP with bitmask.
        """
        n = len(nums)
        total_masks = 1 << n

        # Precompute GCDs
        gcds = {}
        for i in range(n):
            for j in range(i + 1, n):
                gcds[(i, j)] = gcd(nums[i], nums[j])

        # dp[mask] = max score using elements in mask
        dp = [0] * total_masks

        for mask in range(total_masks):
            bits = bin(mask).count('1')
            if bits % 2 != 0:
                continue

            op = bits // 2 + 1

            # Try adding a pair
            for i in range(n):
                if mask & (1 << i):
                    continue
                for j in range(i + 1, n):
                    if mask & (1 << j):
                        continue

                    new_mask = mask | (1 << i) | (1 << j)
                    score = dp[mask] + op * gcds[(i, j)]
                    dp[new_mask] = max(dp[new_mask], score)

        return dp[total_masks - 1]


class SolutionBacktrack:
    def maxScore(self, nums: List[int]) -> int:
        """
        Backtracking approach.
        """
        n = len(nums)
        self.max_score = 0

        def backtrack(remaining: list, op: int, current_score: int):
            if not remaining:
                self.max_score = max(self.max_score, current_score)
                return

            # Pruning: upper bound check
            m = len(remaining)
            max_possible = current_score
            for k in range(op, op + m // 2):
                max_possible += k * max(remaining)
            if max_possible <= self.max_score:
                return

            # Try all pairs
            for i in range(len(remaining)):
                for j in range(i + 1, len(remaining)):
                    new_remaining = [remaining[k] for k in range(len(remaining))
                                    if k != i and k != j]
                    score = op * gcd(remaining[i], remaining[j])
                    backtrack(new_remaining, op + 1, current_score + score)

        backtrack(nums, 1, 0)
        return self.max_score
