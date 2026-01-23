#1748. Sum of Unique Elements
#Easy
#
#You are given an integer array nums. The unique elements of an array are the
#elements that appear exactly once in the array.
#
#Return the sum of all the unique elements of nums.
#
#Example 1:
#Input: nums = [1,2,3,2]
#Output: 4
#
#Example 2:
#Input: nums = [1,1,1,1,1]
#Output: 0
#
#Example 3:
#Input: nums = [1,2,3,4,5]
#Output: 15
#
#Constraints:
#    1 <= nums.length <= 100
#    1 <= nums[i] <= 100

from typing import List
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        """
        Count frequency and sum elements with count 1.
        """
        count = Counter(nums)
        return sum(num for num, freq in count.items() if freq == 1)


class SolutionArray:
    def sumOfUnique(self, nums: List[int]) -> int:
        """
        Using array (nums[i] <= 100).
        """
        count = [0] * 101

        for num in nums:
            count[num] += 1

        return sum(i for i in range(101) if count[i] == 1)


class SolutionTwoSets:
    def sumOfUnique(self, nums: List[int]) -> int:
        """
        Track unique and seen elements.
        """
        unique = set()
        seen = set()

        for num in nums:
            if num in seen:
                unique.discard(num)
            else:
                unique.add(num)
                seen.add(num)

        return sum(unique)
