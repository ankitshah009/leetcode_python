#217. Contains Duplicate
#Easy
#
#Given an integer array nums, return true if any value appears at least twice
#in the array, and return false if every element is distinct.
#
#Example 1:
#Input: nums = [1,2,3,1]
#Output: true
#
#Example 2:
#Input: nums = [1,2,3,4]
#Output: false
#
#Example 3:
#Input: nums = [1,1,1,3,3,4,3,2,4,2]
#Output: true
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^9 <= nums[i] <= 10^9

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """O(n) using set"""
        return len(nums) != len(set(nums))


class SolutionHashSet:
    """Build set incrementally - can exit early"""

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


class SolutionSort:
    """Sort and check adjacent elements - O(n log n)"""

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False


class SolutionCounter:
    """Using Counter"""

    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        return max(Counter(nums).values()) > 1
