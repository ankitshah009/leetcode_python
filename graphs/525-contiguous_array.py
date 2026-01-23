#525. Contiguous Array
#Medium
#
#Given a binary array nums, return the maximum length of a contiguous subarray
#with an equal number of 0 and 1.
#
#Example 1:
#Input: nums = [0,1]
#Output: 2
#Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
#
#Example 2:
#Input: nums = [0,1,0]
#Output: 2
#Explanation: [0, 1] (or [1, 0]) is the longest contiguous subarray with equal
#number of 0 and 1.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    nums[i] is either 0 or 1.

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Replace 0 with -1, find longest subarray with sum 0.
        Use prefix sum and hash map.
        """
        count_idx = {0: -1}  # prefix sum -> first index
        max_len = 0
        count = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1

            if count in count_idx:
                max_len = max(max_len, i - count_idx[count])
            else:
                count_idx[count] = i

        return max_len


class SolutionExplicit:
    """More explicit counting"""

    def findMaxLength(self, nums: List[int]) -> int:
        # Track difference: count(1) - count(0)
        diff_to_idx = {0: -1}
        diff = 0
        max_len = 0

        for i, num in enumerate(nums):
            if num == 1:
                diff += 1
            else:
                diff -= 1

            if diff in diff_to_idx:
                length = i - diff_to_idx[diff]
                max_len = max(max_len, length)
            else:
                diff_to_idx[diff] = i

        return max_len


class SolutionBruteForce:
    """O(n^2) brute force"""

    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            zeros = ones = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1
                else:
                    ones += 1

                if zeros == ones:
                    max_len = max(max_len, j - i + 1)

        return max_len
