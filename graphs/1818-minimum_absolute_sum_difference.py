#1818. Minimum Absolute Sum Difference
#Medium
#
#You are given two positive integer arrays nums1 and nums2, both of length n.
#
#The absolute sum difference of arrays nums1 and nums2 is defined as the sum of
#|nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).
#
#You can replace at most one element of nums1 with any other element in nums1
#to minimize the absolute sum difference.
#
#Return the minimum absolute sum difference after replacing at most one element
#in the array nums1. Since the answer may be large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: nums1 = [1,7,5], nums2 = [2,3,5]
#Output: 3
#
#Example 2:
#Input: nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
#Output: 0
#
#Example 3:
#Input: nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
#Output: 20
#
#Constraints:
#    n == nums1.length
#    n == nums2.length
#    1 <= n <= 10^5
#    1 <= nums1[i], nums2[i] <= 10^5

from typing import List
import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Binary search to find best replacement for each position.
        """
        MOD = 10**9 + 7
        n = len(nums1)

        # Sort nums1 for binary search
        sorted_nums1 = sorted(nums1)

        total_diff = sum(abs(a - b) for a, b in zip(nums1, nums2))
        max_improvement = 0

        for i in range(n):
            current_diff = abs(nums1[i] - nums2[i])

            if current_diff == 0:
                continue

            # Find closest value in nums1 to nums2[i]
            target = nums2[i]
            pos = bisect.bisect_left(sorted_nums1, target)

            # Check both neighbors
            for j in [pos - 1, pos]:
                if 0 <= j < n:
                    new_diff = abs(sorted_nums1[j] - target)
                    improvement = current_diff - new_diff
                    max_improvement = max(max_improvement, improvement)

        return (total_diff - max_improvement) % MOD


class SolutionExplained:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Same approach with detailed comments.
        """
        MOD = 10**9 + 7

        # Calculate original sum
        original_sum = 0
        diffs = []
        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            original_sum += d
            diffs.append(d)

        # Sort for binary search
        sorted_vals = sorted(nums1)

        # Find maximum possible reduction
        max_reduction = 0
        for i, (diff, target) in enumerate(zip(diffs, nums2)):
            if diff == 0:
                continue

            # Binary search for closest value
            idx = bisect.bisect_left(sorted_vals, target)

            # Check value at idx (>= target)
            if idx < len(sorted_vals):
                new_diff = abs(sorted_vals[idx] - target)
                max_reduction = max(max_reduction, diff - new_diff)

            # Check value at idx-1 (< target)
            if idx > 0:
                new_diff = abs(sorted_vals[idx - 1] - target)
                max_reduction = max(max_reduction, diff - new_diff)

        return (original_sum - max_reduction) % MOD
