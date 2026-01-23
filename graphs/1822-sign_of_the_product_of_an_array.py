#1822. Sign of the Product of an Array
#Easy
#
#There is a function signFunc(x) that returns:
#- 1 if x is positive.
#- -1 if x is negative.
#- 0 if x is equal to 0.
#
#You are given an integer array nums. Let product be the product of all values
#in the array nums.
#
#Return signFunc(product).
#
#Example 1:
#Input: nums = [-1,-2,-3,-4,3,2,1]
#Output: 1
#
#Example 2:
#Input: nums = [1,5,0,2,-3]
#Output: 0
#
#Example 3:
#Input: nums = [-1,1,-1,1,-1]
#Output: -1
#
#Constraints:
#    1 <= nums.length <= 1000
#    -100 <= nums[i] <= 100

from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        Count negative numbers, check for zeros.
        """
        neg_count = 0

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                neg_count += 1

        return -1 if neg_count % 2 else 1


class SolutionSign:
    def arraySign(self, nums: List[int]) -> int:
        """
        Track running sign.
        """
        sign = 1

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = -sign

        return sign


class SolutionFunctional:
    def arraySign(self, nums: List[int]) -> int:
        """
        Functional approach.
        """
        from functools import reduce

        if 0 in nums:
            return 0

        neg_count = sum(1 for x in nums if x < 0)
        return -1 if neg_count % 2 else 1


class SolutionMath:
    def arraySign(self, nums: List[int]) -> int:
        """
        Using math.prod with sign function.
        """
        from math import prod

        def sign(x):
            return (x > 0) - (x < 0)

        return sign(prod(sign(x) for x in nums))
