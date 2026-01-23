#1877. Minimize Maximum Pair Sum in Array
#Medium
#
#The pair sum of a pair (a, b) is equal to a + b. The maximum pair sum is the
#largest pair sum in a list of pairs.
#
#For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum
#would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
#
#Given an array nums of even length n, pair up the elements of nums into n/2
#pairs such that:
#- Each element of nums is in exactly one pair, and
#- The maximum pair sum is minimized.
#
#Return the minimized maximum pair sum after optimally pairing up the elements.
#
#Example 1:
#Input: nums = [3,5,2,3]
#Output: 7
#
#Example 2:
#Input: nums = [3,5,4,2,4,6]
#Output: 8
#
#Constraints:
#    n == nums.length
#    2 <= n <= 10^5
#    n is even.
#    1 <= nums[i] <= 10^5

from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
        Greedy: pair smallest with largest.
        """
        nums.sort()
        n = len(nums)

        max_sum = 0
        for i in range(n // 2):
            max_sum = max(max_sum, nums[i] + nums[n - 1 - i])

        return max_sum


class SolutionTwoPointers:
    def minPairSum(self, nums: List[int]) -> int:
        """
        Two pointers approach.
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        max_sum = 0

        while left < right:
            max_sum = max(max_sum, nums[left] + nums[right])
            left += 1
            right -= 1

        return max_sum


class SolutionOneLiner:
    def minPairSum(self, nums: List[int]) -> int:
        """
        One-liner using zip.
        """
        nums.sort()
        return max(a + b for a, b in zip(nums, reversed(nums[:len(nums)//2*2])))


class SolutionZip:
    def minPairSum(self, nums: List[int]) -> int:
        """
        Using zip with sorted array.
        """
        nums.sort()
        n = len(nums)
        return max(nums[i] + nums[n - 1 - i] for i in range(n // 2))
