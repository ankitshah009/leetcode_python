#1979. Find Greatest Common Divisor of Array
#Easy
#
#Given an integer array nums, return the greatest common divisor of the smallest
#number and largest number in nums.
#
#The greatest common divisor of two numbers is the largest positive integer
#that evenly divides both numbers.
#
#Example 1:
#Input: nums = [2,5,6,9,10]
#Output: 2
#Explanation: The smallest number is 2.
#The largest number is 10.
#The GCD of 2 and 10 is 2.
#
#Example 2:
#Input: nums = [7,5,6,8,3]
#Output: 1
#
#Example 3:
#Input: nums = [3,3]
#Output: 3
#
#Constraints:
#    2 <= nums.length <= 1000
#    1 <= nums[i] <= 1000

from typing import List
from math import gcd

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        """
        Find GCD of min and max elements.
        """
        return gcd(min(nums), max(nums))


class SolutionManualGCD:
    def findGCD(self, nums: List[int]) -> int:
        """
        Manual GCD implementation using Euclidean algorithm.
        """
        def euclidean_gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        return euclidean_gcd(min(nums), max(nums))


class SolutionExplicit:
    def findGCD(self, nums: List[int]) -> int:
        """
        Explicit min/max finding.
        """
        min_val = min(nums)
        max_val = max(nums)

        # GCD using Euclidean algorithm
        while min_val:
            max_val, min_val = min_val, max_val % min_val

        return max_val


class SolutionReduce:
    def findGCD(self, nums: List[int]) -> int:
        """
        Using functools.reduce for one-liner.
        """
        from functools import reduce

        min_val = reduce(lambda a, b: a if a < b else b, nums)
        max_val = reduce(lambda a, b: a if a > b else b, nums)

        return gcd(min_val, max_val)
