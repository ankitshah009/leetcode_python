#1246. Palindrome Removal
#Hard
#
#You are given an integer array arr.
#
#In one move, you can select a palindromic subarray arr[i], arr[i + 1], ...,
#arr[j] where i <= j, and remove that subarray from the given array. Note that
#after removing a subarray, the elements on the left and on the right of that
#subarray move to fill the gap left by the removal.
#
#Return the minimum number of moves needed to remove all numbers from the array.
#
#Example 1:
#Input: arr = [1,2]
#Output: 2
#
#Example 2:
#Input: arr = [1,3,4,1,5]
#Output: 3
#Explanation: Remove [4] then remove [1,3,1] then remove [5].
#
#Constraints:
#    1 <= arr.length <= 100
#    1 <= arr[i] <= 20

from typing import List
from functools import lru_cache

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        """
        Interval DP.
        dp[i][j] = minimum moves to remove arr[i..j]

        Base case: dp[i][i] = 1

        Transitions:
        1. dp[i][j] = 1 + dp[i+1][j]  (remove arr[i] alone)
        2. If arr[i] == arr[k] for some k in [i+1, j]:
           dp[i][j] = dp[i+1][k-1] + dp[k][j]
           (arr[i] and arr[k] can be removed together with palindrome containing them)
        """
        n = len(arr)

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1

            # Option 1: Remove arr[i] alone
            result = 1 + dp(i + 1, j)

            # Option 2: Pair arr[i] with some arr[k] where arr[i] == arr[k]
            for k in range(i + 1, j + 1):
                if arr[i] == arr[k]:
                    # Remove arr[i] and arr[k] together
                    # dp(i+1, k-1) handles elements between i and k
                    # dp(k+1, j) handles elements after k
                    # But arr[i] and arr[k] are part of same palindrome
                    # so it's dp(i+1, k-1) + dp(k, j) - 1 adjustment needed
                    # Actually: dp(i, k) + dp(k+1, j) but dp(i, k) benefits from pairing

                    # Better formulation:
                    # If arr[i] == arr[k], we can extend a palindrome
                    middle = dp(i + 1, k - 1) if i + 1 <= k - 1 else 0
                    right = dp(k + 1, j)
                    # The key insight: arr[i..k] takes same moves as arr[i+1..k-1]
                    # because we can wrap the middle palindrome with arr[i] and arr[k]
                    result = min(result, max(1, middle) + right)

            return result

        return dp(0, n - 1)


class Solution2D:
    def minimumMoves(self, arr: List[int]) -> int:
        """Bottom-up DP"""
        n = len(arr)

        # dp[i][j] = min moves to remove arr[i..j]
        dp = [[0] * n for _ in range(n)]

        # Base case: single elements
        for i in range(n):
            dp[i][i] = 1

        # Fill for increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Option 1: Remove arr[i] alone
                dp[i][j] = 1 + dp[i + 1][j]

                # Option 2: Pair arr[i] with arr[k] where arr[i] == arr[k]
                for k in range(i + 1, j + 1):
                    if arr[i] == arr[k]:
                        middle = dp[i + 1][k - 1] if i + 1 <= k - 1 else 0
                        right = dp[k + 1][j] if k + 1 <= j else 0
                        dp[i][j] = min(dp[i][j], max(1, middle) + right)

        return dp[0][n - 1]
