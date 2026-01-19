#350. Intersection of Two Arrays II
#Easy
#
#Given two integer arrays nums1 and nums2, return an array of their
#intersection. Each element in the result must appear as many times as it shows
#in both arrays and you may return the result in any order.
#
#Example 1:
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]
#
#Example 2:
#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [4,9]
#Explanation: [9,4] is also accepted.
#
#Constraints:
#    1 <= nums1.length, nums2.length <= 1000
#    0 <= nums1[i], nums2[i] <= 1000
#
#Follow up:
#- What if the given array is already sorted? How would you optimize your
#  algorithm?
#- What if nums1's size is small compared to nums2's size? Which algorithm is
#  better?
#- What if elements of nums2 are stored on disk, and the memory is limited such
#  that you cannot load all elements into the memory at once?

from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Using Counter"""
        count1 = Counter(nums1)
        result = []

        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1

        return result


class SolutionTwoPointer:
    """Two pointer approach for sorted arrays"""

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        result = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1

        return result


class SolutionCounterIntersection:
    """Using Counter intersection"""

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        # & gives minimum counts
        intersection = count1 & count2

        result = []
        for num, count in intersection.items():
            result.extend([num] * count)

        return result


class SolutionSmallArray:
    """Optimized for when nums1 is much smaller"""

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use smaller array for counter
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        count = Counter(nums1)
        result = []

        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result
