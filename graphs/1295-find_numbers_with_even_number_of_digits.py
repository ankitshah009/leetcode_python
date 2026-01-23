#1295. Find Numbers with Even Number of Digits
#Easy
#
#Given an array nums of integers, return how many of them contain an even
#number of digits.
#
#Example 1:
#Input: nums = [12,345,2,6,7896]
#Output: 2
#Explanation:
#12 contains 2 digits (even number of digits).
#345 contains 3 digits (odd number of digits).
#2 contains 1 digit (odd number of digits).
#6 contains 1 digit (odd number of digits).
#7896 contains 4 digits (even number of digits).
#Therefore only 12 and 7896 contain an even number of digits.
#
#Example 2:
#Input: nums = [555,901,482,1771]
#Output: 1
#Explanation: Only 1771 contains an even number of digits.
#
#Constraints:
#    1 <= nums.length <= 500
#    1 <= nums[i] <= 10^5

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """Count numbers with even number of digits using string conversion."""
        return sum(1 for num in nums if len(str(num)) % 2 == 0)


class SolutionMath:
    def findNumbers(self, nums: List[int]) -> int:
        """Count digits using logarithm"""
        import math

        count = 0
        for num in nums:
            digits = int(math.log10(num)) + 1
            if digits % 2 == 0:
                count += 1
        return count


class SolutionLoop:
    def findNumbers(self, nums: List[int]) -> int:
        """Count digits by division"""
        def count_digits(n):
            count = 0
            while n > 0:
                count += 1
                n //= 10
            return count

        return sum(1 for num in nums if count_digits(num) % 2 == 0)


class SolutionRanges:
    def findNumbers(self, nums: List[int]) -> int:
        """
        Even digit numbers in range [1, 10^5]:
        10-99 (2 digits), 1000-9999 (4 digits)
        """
        return sum(1 for num in nums if 10 <= num <= 99 or 1000 <= num <= 9999 or num == 100000)
