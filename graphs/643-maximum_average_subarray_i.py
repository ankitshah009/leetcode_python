#643. Maximum Average Subarray I
#Easy
#
#You are given an integer array nums consisting of n elements, and an integer k.
#
#Find a contiguous subarray whose length is equal to k that has the maximum average
#value and return this value. Any answer with a calculation error less than 10^-5
#will be accepted.
#
#Example 1:
#Input: nums = [1,12,-5,-6,50,3], k = 4
#Output: 12.75000
#Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
#Example 2:
#Input: nums = [5], k = 1
#Output: 5.00000
#
#Constraints:
#    n == nums.length
#    1 <= k <= n <= 10^5
#    -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """Sliding window"""
        # Initial window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide window
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k


class SolutionExplicit:
    """More explicit sliding window"""

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        # Calculate first window
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]

        max_sum = curr_sum

        # Slide the window
        for i in range(k, n):
            curr_sum = curr_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)

        return max_sum / k


class SolutionPrefixSum:
    """Using prefix sum"""

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        max_sum = float('-inf')
        for i in range(k, n + 1):
            window_sum = prefix[i] - prefix[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
