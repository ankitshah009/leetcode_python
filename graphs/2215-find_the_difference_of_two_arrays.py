#2215. Find the Difference of Two Arrays
#Easy
#
#Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size
#2 where:
#- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
#- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
#
#Note that the integers in the lists may be returned in any order.
#
#Example 1:
#Input: nums1 = [1,2,3], nums2 = [2,4,6]
#Output: [[1,3],[4,6]]
#Explanation:
#For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and
#nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
#For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and
#nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
#
#Example 2:
#Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
#Output: [[3],[]]
#
#Constraints:
#    1 <= nums1.length, nums2.length <= 1000
#    -1000 <= nums1[i], nums2[i] <= 1000

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """Set difference"""
        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1 - set2), list(set2 - set1)]


class SolutionExplicit:
    """Explicit iteration"""

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        diff1 = [x for x in set1 if x not in set2]
        diff2 = [x for x in set2 if x not in set1]

        return [diff1, diff2]


class SolutionSymmetric:
    """Using symmetric difference"""

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        symmetric = set1 ^ set2

        return [
            [x for x in symmetric if x in set1],
            [x for x in symmetric if x in set2]
        ]
