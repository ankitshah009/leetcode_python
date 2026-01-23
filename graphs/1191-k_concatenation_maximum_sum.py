#1191. K-Concatenation Maximum Sum
#Medium
#
#Given an integer array arr and an integer k, modify the array by repeating it
#k times.
#
#For example, if arr = [1, 2] and k = 3 then the modified array will be
#[1, 2, 1, 2, 1, 2].
#
#Return the maximum sub-array sum in the modified array. Note that the length
#of the sub-array can be 0 and its sum in that case is 0.
#
#As the answer can be very large, return the answer modulo 10^9 + 7.
#
#Example 1:
#Input: arr = [1,2], k = 3
#Output: 9
#
#Example 2:
#Input: arr = [1,-2,1], k = 5
#Output: 2
#
#Example 3:
#Input: arr = [-1,-2], k = 7
#Output: 0
#
#Constraints:
#    1 <= arr.length <= 10^5
#    1 <= k <= 10^5
#    -10^4 <= arr[i] <= 10^4

from typing import List

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        """
        Key insight:
        - If k=1: Standard Kadane's algorithm
        - If k>=2: Consider max subarray that:
          1. Stays within one copy
          2. Spans end of one copy + start of next copy
          3. If total sum > 0 and k > 2: Can add (k-2) full copies in middle

        So we need:
        - max_kadane: max subarray in single copy
        - max_prefix: max sum starting from index 0
        - max_suffix: max sum ending at last index
        - total: sum of entire array
        """
        MOD = 10**9 + 7
        n = len(arr)

        # Kadane's algorithm for single array
        def kadane(a):
            max_sum = 0
            current = 0
            for x in a:
                current = max(0, current + x)
                max_sum = max(max_sum, current)
            return max_sum

        max_kadane = kadane(arr)

        if k == 1:
            return max_kadane % MOD

        # Calculate prefix max, suffix max, and total sum
        total = sum(arr)

        # Max prefix sum (starting from index 0)
        max_prefix = 0
        current = 0
        for x in arr:
            current += x
            max_prefix = max(max_prefix, current)

        # Max suffix sum (ending at last index)
        max_suffix = 0
        current = 0
        for x in reversed(arr):
            current += x
            max_suffix = max(max_suffix, current)

        # Case 1: Max subarray within single copy
        result = max_kadane

        # Case 2: Suffix of one copy + prefix of next copy
        result = max(result, max_suffix + max_prefix)

        # Case 3: If total > 0 and k > 2, add (k-2) full copies
        if total > 0 and k > 2:
            result = max(result, max_suffix + (k - 2) * total + max_prefix)

        return result % MOD


class SolutionTwoCopies:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        """
        Run Kadane on at most 2 copies, then add middle copies if beneficial.
        """
        MOD = 10**9 + 7

        def kadane(a):
            max_sum = 0
            current = 0
            for x in a:
                current = max(0, current + x)
                max_sum = max(max_sum, current)
            return max_sum

        total = sum(arr)

        if k == 1:
            return kadane(arr) % MOD

        # Kadane on two copies
        two_copy_max = kadane(arr + arr)

        if k == 2 or total <= 0:
            return two_copy_max % MOD

        # k > 2 and total > 0: can add (k-2) full copies
        return (two_copy_max + (k - 2) * total) % MOD
