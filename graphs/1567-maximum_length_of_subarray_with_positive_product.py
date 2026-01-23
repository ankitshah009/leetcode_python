#1567. Maximum Length of Subarray With Positive Product
#Medium
#
#Given an array of integers nums, find the maximum length of a subarray where
#the product of all its elements is positive.
#
#A subarray of an array is a consecutive sequence of zero or more values taken
#out of that array.
#
#Return the maximum length of a subarray with positive product.
#
#Example 1:
#Input: nums = [1,-2,-3,4]
#Output: 4
#Explanation: The array nums already has a positive product of 24.
#
#Example 2:
#Input: nums = [0,1,-2,-3,-4]
#Output: 3
#Explanation: The longest subarray with positive product is [1,-2,-3] with product 6.
#
#Example 3:
#Input: nums = [-1,-2,-3,0,1]
#Output: 2
#Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^9 <= nums[i] <= 10^9

from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """
        Track length of subarray ending at i with positive/negative product.

        pos[i] = length of longest subarray ending at i with positive product
        neg[i] = length of longest subarray ending at i with negative product
        """
        n = len(nums)
        pos = neg = 0
        result = 0

        for num in nums:
            if num == 0:
                pos = neg = 0
            elif num > 0:
                pos = pos + 1
                neg = neg + 1 if neg > 0 else 0
            else:  # num < 0
                new_pos = neg + 1 if neg > 0 else 0
                neg = pos + 1
                pos = new_pos

            result = max(result, pos)

        return result


class SolutionTwoPass:
    def getMaxLen(self, nums: List[int]) -> int:
        """
        Two pass approach: left to right and right to left.
        """
        def max_len_one_direction(arr):
            result = 0
            product_sign = 1
            length = 0
            first_neg_idx = -1

            for i, num in enumerate(arr):
                if num == 0:
                    product_sign = 1
                    length = 0
                    first_neg_idx = -1
                else:
                    length += 1
                    if num < 0:
                        product_sign *= -1
                        if first_neg_idx == -1:
                            first_neg_idx = i

                    if product_sign > 0:
                        result = max(result, length)

            return result

        return max(max_len_one_direction(nums), max_len_one_direction(nums[::-1]))


class SolutionExplicit:
    def getMaxLen(self, nums: List[int]) -> int:
        """
        Explicit tracking of first negative index in each segment.
        """
        result = 0
        start = 0
        first_neg = -1
        neg_count = 0

        for i, num in enumerate(nums):
            if num == 0:
                start = i + 1
                first_neg = -1
                neg_count = 0
            else:
                if num < 0:
                    neg_count += 1
                    if first_neg == -1:
                        first_neg = i

                if neg_count % 2 == 0:
                    result = max(result, i - start + 1)
                else:
                    result = max(result, i - first_neg)

        return result


class SolutionDP:
    def getMaxLen(self, nums: List[int]) -> int:
        """
        DP with explicit arrays.
        """
        n = len(nums)
        # pos[i] = max length ending at i with positive product
        # neg[i] = max length ending at i with negative product
        pos = [0] * n
        neg = [0] * n

        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1

        result = pos[0]

        for i in range(1, n):
            if nums[i] > 0:
                pos[i] = pos[i-1] + 1
                neg[i] = neg[i-1] + 1 if neg[i-1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = neg[i-1] + 1 if neg[i-1] > 0 else 0
                neg[i] = pos[i-1] + 1
            # If nums[i] == 0, both stay 0

            result = max(result, pos[i])

        return result
