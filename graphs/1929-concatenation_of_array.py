#1929. Concatenation of Array
#Easy
#
#Given an integer array nums of length n, you want to create an array ans of
#length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for
#0 <= i < n (0-indexed).
#
#Specifically, ans is the concatenation of two nums arrays.
#
#Return the array ans.
#
#Example 1:
#Input: nums = [1,2,1]
#Output: [1,2,1,1,2,1]
#
#Example 2:
#Input: nums = [1,3,2,1]
#Output: [1,3,2,1,1,3,2,1]
#
#Constraints:
#    n == nums.length
#    1 <= n <= 1000
#    1 <= nums[i] <= 1000

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Simply concatenate nums with itself.
        """
        return nums + nums


class SolutionExtend:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Using extend method.
        """
        result = nums[:]
        result.extend(nums)
        return result


class SolutionMultiply:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Using list multiplication.
        """
        return nums * 2


class SolutionManual:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Manual construction.
        """
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans
