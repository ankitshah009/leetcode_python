#1708. Largest Subarray Length K
#Easy
#
#An array A is larger than some array B if for the first index i where A[i] != B[i],
#A[i] > B[i].
#
#For example, consider 0-indexing:
#- [1,3,2,4] > [1,2,2,4], since at index 1, 3 > 2.
#- [1,4,4,4] < [2,1,1,1], since at index 0, 1 < 2.
#
#A subarray is a contiguous part of an array.
#
#Given an integer array nums of distinct integers, return the largest subarray
#of nums of length k.
#
#Example 1:
#Input: nums = [1,4,5,2,3], k = 3
#Output: [5,2,3]
#
#Example 2:
#Input: nums = [1,4,5,2,3], k = 4
#Output: [4,5,2,3]
#
#Example 3:
#Input: nums = [1,4,5,2,3], k = 1
#Output: [5]
#
#Constraints:
#    1 <= k <= nums.length <= 10^5
#    1 <= nums[i] <= 10^9
#    All the integers of nums are unique.

from typing import List

class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        """
        Find max element in valid starting range, return k elements from there.
        Since all elements are distinct, the subarray starting with max element
        is lexicographically largest.
        """
        n = len(nums)
        # Valid starting positions: 0 to n-k
        max_idx = 0

        for i in range(1, n - k + 1):
            if nums[i] > nums[max_idx]:
                max_idx = i

        return nums[max_idx:max_idx + k]


class SolutionBuiltin:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        """
        Using max with index.
        """
        n = len(nums)
        max_val = max(nums[:n - k + 1])
        start = nums.index(max_val)
        return nums[start:start + k]


class SolutionOneLiner:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        """
        Compact version.
        """
        return max(nums[i:i + k] for i in range(len(nums) - k + 1))
