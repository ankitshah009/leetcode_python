#413. Arithmetic Slices
#Medium
#
#An integer array is called arithmetic if it consists of at least three
#elements and if the difference between any two consecutive elements is the
#same.
#
#For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
#
#Given an integer array nums, return the number of arithmetic subarrays of nums.
#
#A subarray is a contiguous subsequence of the array.
#
#Example 1:
#Input: nums = [1,2,3,4]
#Output: 3
#Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and
#[1,2,3,4] itself.
#
#Example 2:
#Input: nums = [1]
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 5000
#    -1000 <= nums[i] <= 1000

from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        DP approach.
        If nums[i-2], nums[i-1], nums[i] form arithmetic sequence,
        then dp[i] = dp[i-1] + 1 (all previous sequences extended + new one)
        """
        n = len(nums)
        if n < 3:
            return 0

        dp = 0
        total = 0

        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp += 1
                total += dp
            else:
                dp = 0

        return total


class SolutionMath:
    """Count consecutive arithmetic sequences"""

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        total = 0
        i = 0

        while i < n - 2:
            j = i
            diff = nums[i + 1] - nums[i]

            # Extend while difference is same
            while j < n - 1 and nums[j + 1] - nums[j] == diff:
                j += 1

            # Length of arithmetic sequence
            length = j - i + 1

            if length >= 3:
                # Number of subarrays of length >= 3
                # From length L: (L-2) + (L-3) + ... + 1 = (L-2)(L-1)/2
                total += (length - 2) * (length - 1) // 2

            i = j

        return total


class SolutionDP:
    """Explicit DP array"""

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        # dp[i] = number of arithmetic slices ending at index i
        dp = [0] * n

        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1

        return sum(dp)
