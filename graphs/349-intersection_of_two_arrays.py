#349. Intersection of Two Arrays
#Easy
#
#Given two integer arrays nums1 and nums2, return an array of their
#intersection. Each element in the result must be unique and you may return the
#result in any order.
#
#Example 1:
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2]
#
#Example 2:
#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [9,4]
#Explanation: [4,9] is also accepted.
#
#Constraints:
#    1 <= nums1.length, nums2.length <= 1000
#    0 <= nums1[i], nums2[i] <= 1000

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Using set intersection"""
        return list(set(nums1) & set(nums2))


class SolutionTwoPointer:
    """Two pointer approach after sorting"""

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
                # Found common element
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1

        return result


class SolutionBinarySearch:
    """Binary search approach"""

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        import bisect

        set1 = set(nums1)
        nums2.sort()
        result = []

        for num in set1:
            idx = bisect.bisect_left(nums2, num)
            if idx < len(nums2) and nums2[idx] == num:
                result.append(num)

        return result


class SolutionHashMap:
    """Using hash map"""

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        result = []

        for num in nums2:
            if num in seen:
                result.append(num)
                seen.remove(num)  # Ensure uniqueness

        return result
