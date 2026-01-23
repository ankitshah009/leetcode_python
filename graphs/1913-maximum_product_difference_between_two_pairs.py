#1913. Maximum Product Difference Between Two Pairs
#Easy
#
#The product difference between two pairs (a, b) and (c, d) is defined as
#(a * b) - (c * d).
#
#Given an integer array nums, choose four distinct indices w, x, y, and z such
#that the product difference between pairs (nums[w], nums[x]) and (nums[y],
#nums[z]) is maximized.
#
#Return the maximum such product difference.
#
#Example 1:
#Input: nums = [5,6,2,7,4]
#Output: 34
#
#Example 2:
#Input: nums = [4,2,5,9,7,4,8]
#Output: 64
#
#Constraints:
#    4 <= nums.length <= 10^4
#    1 <= nums[i] <= 10^4

from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        """
        Max product of two largest - product of two smallest.
        """
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]


class SolutionOnePass:
    def maxProductDifference(self, nums: List[int]) -> int:
        """
        Find two largest and two smallest in one pass.
        """
        max1 = max2 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max1 * max2 - min1 * min2


class SolutionHeap:
    def maxProductDifference(self, nums: List[int]) -> int:
        """
        Using heapq.
        """
        import heapq

        two_largest = heapq.nlargest(2, nums)
        two_smallest = heapq.nsmallest(2, nums)

        return two_largest[0] * two_largest[1] - two_smallest[0] * two_smallest[1]
