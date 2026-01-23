#1856. Maximum Subarray Min-Product
#Medium
#
#The min-product of an array is equal to the minimum value in the array
#multiplied by the array's sum.
#
#You are given an array of positive integers nums.
#
#Return the maximum min-product of any non-empty subarray of nums. Since the
#answer may be large, return it modulo 10^9 + 7.
#
#Note that the min-product should be maximized before performing the modulo
#operation. Testcases are generated such that the maximum min-product without
#modulo will fit in a 64-bit signed integer.
#
#A subarray is a contiguous part of an array.
#
#Example 1:
#Input: nums = [1,2,3,2]
#Output: 14
#
#Example 2:
#Input: nums = [2,3,3,1,2]
#Output: 18
#
#Example 3:
#Input: nums = [3,1,5,6,4,2]
#Output: 60
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^7

from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        """
        Monotonic stack: for each element as minimum, find the range.
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Left boundary: first smaller element to the left
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # Right boundary: first smaller element to the right
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # Calculate max min-product
        max_product = 0
        for i in range(n):
            # Range where nums[i] is minimum: (left[i], right[i])
            l = left[i] + 1
            r = right[i] - 1
            range_sum = prefix[r + 1] - prefix[l]
            product = nums[i] * range_sum
            max_product = max(max_product, product)

        return max_product % MOD


class SolutionSinglePass:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        """
        Single pass using stack for both boundaries.
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Prefix sum
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        max_product = 0
        stack = []  # Increasing stack of indices

        for i in range(n + 1):
            curr = nums[i] if i < n else 0

            while stack and nums[stack[-1]] >= curr:
                min_idx = stack.pop()
                left = stack[-1] + 1 if stack else 0
                right = i - 1
                range_sum = prefix[right + 1] - prefix[left]
                product = nums[min_idx] * range_sum
                max_product = max(max_product, product)

            stack.append(i)

        return max_product % MOD
