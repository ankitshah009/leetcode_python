#1855. Maximum Distance Between a Pair of Values
#Medium
#
#You are given two non-increasing 0-indexed integer arrays nums1 and nums2.
#
#A pair of indices (i, j), where 0 <= i < nums1.length and
#0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The
#distance of the pair is j - i.
#
#Return the maximum distance of any valid pair (i, j). If there are no valid
#pairs, return 0.
#
#An array arr is non-increasing if arr[i-1] >= arr[i] for every
#1 <= i < arr.length.
#
#Example 1:
#Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
#Output: 2
#
#Example 2:
#Input: nums1 = [2,2,2], nums2 = [10,10,1]
#Output: 1
#
#Example 3:
#Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
#Output: 2
#
#Constraints:
#    1 <= nums1.length, nums2.length <= 10^5
#    1 <= nums1[i], nums2[j] <= 10^5
#    Both nums1 and nums2 are non-increasing.

from typing import List
import bisect

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Two pointers: for each i, find largest j where valid.
        """
        max_dist = 0
        j = 0

        for i in range(len(nums1)):
            # Move j forward while valid
            while j < len(nums2) and nums1[i] <= nums2[j]:
                j += 1
            # j-1 is the last valid position (if j > i)
            if j - 1 >= i:
                max_dist = max(max_dist, j - 1 - i)

        return max_dist


class SolutionBinarySearch:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Binary search for each i.
        """
        max_dist = 0

        for i, val in enumerate(nums1):
            # Find rightmost j where nums2[j] >= val
            # Since nums2 is non-increasing, search from i to end
            left, right = i, len(nums2) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] >= val:
                    left = mid + 1
                else:
                    right = mid - 1

            j = right  # Largest j where nums2[j] >= val
            if j >= i:
                max_dist = max(max_dist, j - i)

        return max_dist


class SolutionTwoPointers:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Cleaner two-pointer approach.
        """
        i = j = 0
        max_dist = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                max_dist = max(max_dist, j - i)
                j += 1

        return max_dist
