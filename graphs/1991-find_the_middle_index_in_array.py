#1991. Find the Middle Index in Array
#Easy
#
#Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the
#smallest amongst all the possible ones).
#
#A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1]
#== nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].
#
#If middleIndex == 0, the left side sum is considered to be 0. Similarly, if
#middleIndex == nums.length - 1, the right side sum is considered to be 0.
#
#Return the leftmost middleIndex that satisfies the condition, or -1 if there
#is no such index.
#
#Example 1:
#Input: nums = [2,3,-1,8,4]
#Output: 3
#Explanation: Left sum = 2 + 3 + -1 = 4, Right sum = 4.
#
#Example 2:
#Input: nums = [1,-1,4]
#Output: 2
#
#Example 3:
#Input: nums = [2,5]
#Output: -1
#
#Constraints:
#    1 <= nums.length <= 100
#    -1000 <= nums[i] <= 1000

from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        """
        Track left sum; right sum = total - left - current.
        """
        total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num

        return -1


class SolutionPrefixSum:
    def findMiddleIndex(self, nums: List[int]) -> int:
        """
        Using prefix sums array.
        """
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        total = prefix[n]

        for i in range(n):
            left = prefix[i]
            right = total - prefix[i + 1]
            if left == right:
                return i

        return -1


class SolutionExplicit:
    def findMiddleIndex(self, nums: List[int]) -> int:
        """
        Explicit left/right computation.
        """
        n = len(nums)

        for i in range(n):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i + 1:])

            if left_sum == right_sum:
                return i

        return -1
