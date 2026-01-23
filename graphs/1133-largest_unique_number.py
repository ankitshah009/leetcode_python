#1133. Largest Unique Number
#Easy
#
#Given an integer array nums, return the largest integer that only occurs
#once. If no integer occurs once, return -1.
#
#Example 1:
#Input: nums = [5,7,3,9,4,9,8,3,1]
#Output: 8
#Explanation: The maximum integer in the array is 9 but it is repeated.
#The number 8 occurs only once, so it is the answer.
#
#Example 2:
#Input: nums = [9,9,8,8]
#Output: -1
#Explanation: There is no number that occurs only once.
#
#Constraints:
#    1 <= nums.length <= 2000
#    0 <= nums[i] <= 1000

from typing import List
from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """
        Count occurrences, find max with count 1.
        """
        count = Counter(nums)
        unique = [num for num, cnt in count.items() if cnt == 1]
        return max(unique) if unique else -1


class SolutionOneLiner:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """One-liner"""
        count = Counter(nums)
        return max((n for n, c in count.items() if c == 1), default=-1)


class SolutionSorted:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """Sort and find largest with single occurrence"""
        count = Counter(nums)
        for num in sorted(count.keys(), reverse=True):
            if count[num] == 1:
                return num
        return -1
