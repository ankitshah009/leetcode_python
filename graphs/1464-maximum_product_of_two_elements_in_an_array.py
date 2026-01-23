#1464. Maximum Product of Two Elements in an Array
#Easy
#
#Given the array of integers nums, you will choose two different indices i and j
#of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
#
#Example 1:
#Input: nums = [3,4,5,2]
#Output: 12
#Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will
#get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
#
#Example 2:
#Input: nums = [1,5,4,5]
#Output: 16
#Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get
#the maximum value of (5-1)*(5-1) = 16.
#
#Example 3:
#Input: nums = [3,7]
#Output: 12
#
#Constraints:
#    2 <= nums.length <= 500
#    1 <= nums[i] <= 10^3

from typing import List
import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Find two largest elements and compute (max1 - 1) * (max2 - 1).
        Single pass tracking two largest values.
        """
        max1 = max2 = 0

        for num in nums:
            if num >= max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)


class SolutionSort:
    def maxProduct(self, nums: List[int]) -> int:
        """Sort and take two largest"""
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)


class SolutionHeap:
    def maxProduct(self, nums: List[int]) -> int:
        """Use heap to find two largest"""
        two_largest = heapq.nlargest(2, nums)
        return (two_largest[0] - 1) * (two_largest[1] - 1)


class SolutionBruteForce:
    def maxProduct(self, nums: List[int]) -> int:
        """Brute force: try all pairs"""
        n = len(nums)
        max_product = 0

        for i in range(n):
            for j in range(i + 1, n):
                product = (nums[i] - 1) * (nums[j] - 1)
                max_product = max(max_product, product)

        return max_product
