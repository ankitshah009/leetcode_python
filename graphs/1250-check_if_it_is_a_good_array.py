#1250. Check If It Is a Good Array
#Hard
#
#Given an array nums of positive integers. Your task is to select some subset
#of nums, multiply each element by an integer and add all these numbers. The
#array is said to be good if you can obtain a sum of 1 from the array by any
#possible subset and multiplicand.
#
#Return True if the array is good otherwise return False.
#
#Example 1:
#Input: nums = [12,5,7,23]
#Output: true
#Explanation: Pick numbers 5 and 7.
#5*3 + 7*(-2) = 1
#
#Example 2:
#Input: nums = [29,6,10]
#Output: true
#Explanation: Pick numbers 29, 6 and 10.
#29*1 + 6*(-3) + 10*(-1) = 1
#
#Example 3:
#Input: nums = [3,6]
#Output: false
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^9

from typing import List
from math import gcd
from functools import reduce

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        """
        Bezout's Identity: For integers a, b, there exist integers x, y such
        that ax + by = gcd(a, b).

        Extended: We can reach any multiple of gcd(all numbers).

        To reach 1, we need gcd(all numbers) = 1.
        """
        return reduce(gcd, nums) == 1


class SolutionExplicit:
    def isGoodArray(self, nums: List[int]) -> bool:
        """Explicit GCD computation"""
        g = nums[0]
        for num in nums[1:]:
            g = gcd(g, num)
            if g == 1:
                return True  # Early termination

        return g == 1
