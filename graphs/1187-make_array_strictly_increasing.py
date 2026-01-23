#1187. Make Array Strictly Increasing
#Hard
#
#Given two integer arrays arr1 and arr2, return the minimum number of operations
#(possibly zero) needed to make arr1 strictly increasing.
#
#In one operation, you can choose two indices 0 <= i < arr1.length and
#0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].
#
#If there is no way to make arr1 strictly increasing, return -1.
#
#Example 1:
#Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
#Output: 1
#Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
#
#Example 2:
#Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
#Output: 2
#Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
#
#Example 3:
#Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
#Output: -1
#Explanation: You can't make arr1 strictly increasing.
#
#Constraints:
#    1 <= arr1.length, arr2.length <= 2000
#    0 <= arr1[i], arr2[i] <= 10^9

from typing import List
import bisect
from functools import lru_cache

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """
        DP: dp[i][j] = min operations to make arr1[0:i+1] strictly increasing
                       with arr1[i] = j (where j is actual value, not index)

        Since values can be large, use dictionary or track by value.

        State: For each position, track minimum operations for each possible
        ending value.
        """
        arr2 = sorted(set(arr2))  # Remove duplicates and sort

        # dp[val] = minimum operations to achieve this value at current position
        dp = {-1: 0}  # Before arr1[0], previous value is -1 (anything works)

        for num in arr1:
            new_dp = {}

            for prev_val, ops in dp.items():
                # Option 1: Keep current number if valid
                if num > prev_val:
                    if num not in new_dp or new_dp[num] > ops:
                        new_dp[num] = ops

                # Option 2: Replace with smallest number from arr2 > prev_val
                idx = bisect.bisect_right(arr2, prev_val)
                if idx < len(arr2):
                    replace_val = arr2[idx]
                    if replace_val not in new_dp or new_dp[replace_val] > ops + 1:
                        new_dp[replace_val] = ops + 1

            if not new_dp:
                return -1

            dp = new_dp

        return min(dp.values())


class SolutionMemo:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """Top-down DP with memoization"""
        arr2 = sorted(set(arr2))

        @lru_cache(maxsize=None)
        def dp(i, prev):
            """Min operations to process arr1[i:] with previous value = prev"""
            if i == len(arr1):
                return 0

            result = float('inf')

            # Option 1: Keep arr1[i] if valid
            if arr1[i] > prev:
                result = dp(i + 1, arr1[i])

            # Option 2: Replace with smallest valid from arr2
            idx = bisect.bisect_right(arr2, prev)
            if idx < len(arr2):
                result = min(result, 1 + dp(i + 1, arr2[idx]))

            return result

        ans = dp(0, -1)
        return ans if ans != float('inf') else -1
