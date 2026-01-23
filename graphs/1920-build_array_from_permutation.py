#1920. Build Array from Permutation
#Easy
#
#Given a zero-based permutation nums (0-indexed), build an array ans of the
#same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and
#return it.
#
#A zero-based permutation nums is an array of distinct integers from 0 to
#nums.length - 1 (inclusive).
#
#Example 1:
#Input: nums = [0,2,1,5,3,4]
#Output: [0,1,2,4,5,3]
#
#Example 2:
#Input: nums = [5,0,1,2,3,4]
#Output: [4,5,0,1,2,3]
#
#Constraints:
#    1 <= nums.length <= 1000
#    0 <= nums[i] < nums.length
#    The elements in nums are distinct.

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Simple O(n) with O(n) space.
        """
        return [nums[nums[i]] for i in range(len(nums))]


class SolutionInPlace:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        O(1) extra space using encoding.
        Store both old and new value: nums[i] = old + n * new
        """
        n = len(nums)

        # First pass: encode both values
        for i in range(n):
            # nums[nums[i]] might already be modified, so get original
            original = nums[nums[i]] % n
            nums[i] = nums[i] + n * original

        # Second pass: decode to get new values
        for i in range(n):
            nums[i] = nums[i] // n

        return nums


class SolutionMap:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Using map function.
        """
        return list(map(lambda i: nums[nums[i]], range(len(nums))))
