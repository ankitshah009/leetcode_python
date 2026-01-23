#1480. Running Sum of 1d Array
#Easy
#
#Given an array nums. We define a running sum of an array as
#runningSum[i] = sum(nums[0]...nums[i]).
#
#Return the running sum of nums.
#
#Example 1:
#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
#Example 2:
#Input: nums = [1,1,1,1,1]
#Output: [1,2,3,4,5]
#Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
#
#Example 3:
#Input: nums = [3,1,2,10,1]
#Output: [3,4,6,16,17]
#
#Constraints:
#    1 <= nums.length <= 1000
#    -10^6 <= nums[i] <= 10^6

from typing import List
from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Simple prefix sum calculation.
        """
        result = []
        total = 0
        for num in nums:
            total += num
            result.append(total)
        return result


class SolutionInPlace:
    def runningSum(self, nums: List[int]) -> List[int]:
        """In-place modification"""
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


class SolutionItertools:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Using itertools.accumulate"""
        return list(accumulate(nums))


class SolutionComprehension:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Using list comprehension with walrus operator (Python 3.8+)"""
        total = 0
        return [(total := total + num) for num in nums]


class SolutionReduce:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Using reduce-like approach"""
        from functools import reduce

        result = []

        def accumulator(total, num):
            new_total = total + num
            result.append(new_total)
            return new_total

        reduce(accumulator, nums, 0)
        return result
