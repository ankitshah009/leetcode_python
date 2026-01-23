#1984. Minimum Difference Between Highest and Lowest of K Scores
#Easy
#
#You are given a 0-indexed integer array nums, where nums[i] represents the
#score of the ith student. You are also given an integer k.
#
#Pick the scores of any k students from the array so that the difference
#between the highest and the lowest of the k scores is minimized.
#
#Return the minimum possible difference.
#
#Example 1:
#Input: nums = [90], k = 1
#Output: 0
#Explanation: There is only one student, so the difference is 0.
#
#Example 2:
#Input: nums = [9,4,1,7], k = 2
#Output: 2
#Explanation: Pick students with scores 7 and 9. Difference = 9 - 7 = 2.
#
#Constraints:
#    1 <= k <= nums.length <= 1000
#    0 <= nums[i] <= 10^5

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        Sort and check windows of size k.
        """
        if k == 1:
            return 0

        nums.sort()
        min_diff = float('inf')

        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, diff)

        return min_diff


class SolutionOneLiner:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        One-liner solution.
        """
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))


class SolutionExplicit:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        Explicit sliding window.
        """
        n = len(nums)

        if k == 1 or n == 1:
            return 0

        nums.sort()

        result = nums[k - 1] - nums[0]  # First window

        for i in range(1, n - k + 1):
            window_diff = nums[i + k - 1] - nums[i]
            result = min(result, window_diff)

        return result
