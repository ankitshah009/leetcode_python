#523. Continuous Subarray Sum
#Medium
#
#Given an integer array nums and an integer k, return true if nums has a good
#subarray or false otherwise.
#
#A good subarray is a subarray where:
#- its length is at least two, and
#- the sum of the elements of the subarray is a multiple of k.
#
#Note that:
#- A subarray is a contiguous part of the array.
#- An integer x is a multiple of k if there exists an integer n such that x = n * k.
#  0 is always a multiple of k.
#
#Example 1:
#Input: nums = [23,2,4,6,7], k = 6
#Output: true
#Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
#
#Example 2:
#Input: nums = [23,2,6,4,7], k = 6
#Output: true
#Explanation: [23, 2, 6, 4, 7] is a subarray of size 5 whose sum is 42 which is
#a multiple of 6.
#
#Example 3:
#Input: nums = [23,2,6,4,7], k = 13
#Output: false
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= nums[i] <= 10^9
#    0 <= sum(nums[i]) <= 2^31 - 1
#    1 <= k <= 2^31 - 1

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Use prefix sum mod k.
        If prefix[j] % k == prefix[i] % k, then sum(nums[i+1:j+1]) is multiple of k.
        Need j - i >= 2 (subarray length at least 2).
        """
        # Map remainder to earliest index
        remainder_idx = {0: -1}  # Handle case where prefix sum itself is multiple
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in remainder_idx:
                if i - remainder_idx[remainder] >= 2:
                    return True
            else:
                remainder_idx[remainder] = i

        return False


class SolutionBruteForce:
    """O(n^2) brute force for reference"""

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n - 1):
            total = nums[i]
            for j in range(i + 1, n):
                total += nums[j]
                if total % k == 0:
                    return True

        return False


class SolutionPrefixArray:
    """Using prefix sum array"""

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        seen = {}
        for i in range(n + 1):
            rem = prefix[i] % k
            if rem in seen:
                if i - seen[rem] >= 2:
                    return True
            else:
                seen[rem] = i

        return False
