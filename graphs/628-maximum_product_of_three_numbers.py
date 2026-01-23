#628. Maximum Product of Three Numbers
#Easy
#
#Given an integer array nums, find three numbers whose product is maximum and
#return the maximum product.
#
#Example 1:
#Input: nums = [1,2,3]
#Output: 6
#
#Example 2:
#Input: nums = [1,2,3,4]
#Output: 24
#
#Example 3:
#Input: nums = [-1,-2,-3]
#Output: -6
#
#Constraints:
#    3 <= nums.length <= 10^4
#    -1000 <= nums[i] <= 1000

from typing import List
import heapq

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Maximum is either:
        1. Three largest positives, or
        2. Two smallest negatives * largest positive
        """
        nums.sort()
        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1]
        )


class SolutionLinear:
    """O(n) without sorting"""

    def maximumProduct(self, nums: List[int]) -> int:
        # Track 3 largest and 2 smallest
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)


class SolutionHeap:
    """Using heaps"""

    def maximumProduct(self, nums: List[int]) -> int:
        # 3 largest
        largest = heapq.nlargest(3, nums)
        # 2 smallest
        smallest = heapq.nsmallest(2, nums)

        return max(
            largest[0] * largest[1] * largest[2],
            smallest[0] * smallest[1] * largest[0]
        )
