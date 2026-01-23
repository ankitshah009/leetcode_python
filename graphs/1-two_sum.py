#1. Two Sum
#Easy
#
#Given an array of integers nums and an integer target, return indices of the
#two numbers such that they add up to target.
#
#You may assume that each input would have exactly one solution, and you may
#not use the same element twice.
#
#You can return the answer in any order.
#
#Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#Example 2:
#Input: nums = [3,2,4], target = 6
#Output: [1,2]
#
#Example 3:
#Input: nums = [3,3], target = 6
#Output: [0,1]
#
#Constraints:
#    2 <= nums.length <= 10^4
#    -10^9 <= nums[i] <= 10^9
#    -10^9 <= target <= 10^9
#    Only one valid answer exists.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Hash map approach - O(n) time, O(n) space.
        Store complement and its index as we iterate.
        """
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []


class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force - O(n^2) time, O(1) space.
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


class SolutionTwoPointer:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Two pointer approach (requires sorting with index tracking).
        O(n log n) time due to sorting.
        """
        indexed = [(num, i) for i, num in enumerate(nums)]
        indexed.sort()

        left, right = 0, len(nums) - 1

        while left < right:
            curr_sum = indexed[left][0] + indexed[right][0]
            if curr_sum == target:
                return [indexed[left][1], indexed[right][1]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return []


class SolutionOnePass:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        One-pass hash table - most elegant solution.
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []
