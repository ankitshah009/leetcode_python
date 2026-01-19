#1004. Max Consecutive Ones III
#Medium
#
#Given a binary array nums and an integer k, return the maximum number of
#consecutive 1's in the array if you can flip at most k 0's.
#
#Example 1:
#Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#Output: 6
#Explanation: [1,1,1,0,0,1,1,1,1,1,1]
#Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
#
#Example 2:
#Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
#Output: 10
#
#Constraints:
#    1 <= nums.length <= 10^5
#    nums[i] is either 0 or 1.
#    0 <= k <= nums.length

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """Sliding window - count zeros in window"""
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


class SolutionNoShrink:
    """Window never shrinks - more efficient"""

    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

        return len(nums) - left


class SolutionPrefixSum:
    """Using prefix sum of zeros"""

    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # prefix[i] = number of zeros in nums[0:i]
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 - nums[i])

        max_len = 0

        for right in range(n):
            # Binary search for leftmost position where zeros <= k
            # zeros in [left, right] = prefix[right + 1] - prefix[left]
            # We want prefix[right + 1] - prefix[left] <= k
            # i.e., prefix[left] >= prefix[right + 1] - k

            lo, hi = 0, right + 1
            target = prefix[right + 1] - k

            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1

            max_len = max(max_len, right - lo + 1)

        return max_len
