#674. Longest Continuous Increasing Subsequence
#Easy
#
#Given an unsorted array of integers nums, return the length of the longest
#continuous increasing subsequence (i.e. subarray). The subsequence must be
#strictly increasing.
#
#A continuous increasing subsequence is defined by two indices l and r (l < r)
#such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each
#l <= i < r, nums[i] < nums[i + 1].
#
#Example 1:
#Input: nums = [1,3,5,4,7]
#Output: 3
#Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
#
#Example 2:
#Input: nums = [2,2,2,2,2]
#Output: 1
#Explanation: The longest continuous increasing subsequence is [2] with length 1.
#
#Constraints:
#    1 <= nums.length <= 10^4
#    -10^9 <= nums[i] <= 10^9

from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        Simple one-pass solution.
        """
        if not nums:
            return 0

        max_len = 1
        curr_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1

        return max_len


class SolutionSlidingWindow:
    """Sliding window approach"""

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_len = 0
        start = 0

        for end in range(len(nums)):
            if end > 0 and nums[end] <= nums[end - 1]:
                start = end

            max_len = max(max_len, end - start + 1)

        return max_len


class SolutionDP:
    """DP approach (more explicit)"""

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        # dp[i] = length of LCIS ending at index i
        dp = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1

        return max(dp)
