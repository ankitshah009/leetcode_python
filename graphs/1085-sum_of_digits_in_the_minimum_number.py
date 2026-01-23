#1085. Sum of Digits in the Minimum Number
#Easy
#
#Given an integer array nums, return 0 if the sum of the digits of the
#minimum integer in nums is odd, or 1 otherwise.
#
#Example 1:
#Input: nums = [34,23,1,24,75,33,54,8]
#Output: 0
#Explanation: The minimum element is 1, and the sum of those digits is 1
#which is odd, so the answer is 0.
#
#Example 2:
#Input: nums = [99,77,33,66,55]
#Output: 1
#Explanation: The minimum element is 33, and the sum of those digits is
#3 + 3 = 6 which is even, so the answer is 1.
#
#Constraints:
#    1 <= nums.length <= 100
#    1 <= nums[i] <= 100

from typing import List

class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        """
        Find minimum, sum its digits, return 1 if even, 0 if odd.
        """
        min_num = min(nums)
        digit_sum = sum(int(d) for d in str(min_num))
        return 1 if digit_sum % 2 == 0 else 0


class SolutionMath:
    def sumOfDigits(self, nums: List[int]) -> int:
        """Mathematical digit sum"""
        min_num = min(nums)
        digit_sum = 0

        while min_num > 0:
            digit_sum += min_num % 10
            min_num //= 10

        return 1 - digit_sum % 2


class SolutionOneLiner:
    def sumOfDigits(self, nums: List[int]) -> int:
        """One-liner"""
        return 1 - sum(int(d) for d in str(min(nums))) % 2
