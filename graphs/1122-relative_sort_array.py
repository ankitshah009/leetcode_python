#1122. Relative Sort Array
#Easy
#
#Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all
#elements in arr2 are also in arr1.
#
#Sort the elements of arr1 such that the relative ordering of items in arr1
#are the same as in arr2. Elements that do not appear in arr2 should be
#placed at the end of arr1 in ascending order.
#
#Example 1:
#Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
#Output: [2,2,2,1,4,3,3,9,6,7,19]
#
#Example 2:
#Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
#Output: [22,28,8,6,17,44]
#
#Constraints:
#    1 <= arr1.length, arr2.length <= 1000
#    0 <= arr1[i], arr2[i] <= 1000
#    All the elements of arr2 are distinct.
#    Each arr2[i] is in arr1.

from typing import List
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        Custom sort key: arr2 index if present, otherwise large value + element.
        """
        order = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (order.get(x, len(arr2)), x))


class SolutionCounting:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """Using counting sort"""
        count = Counter(arr1)
        result = []

        # Add elements in arr2 order
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]

        # Add remaining elements in sorted order
        for num in sorted(count.keys()):
            result.extend([num] * count[num])

        return result


class SolutionBucketSort:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """Bucket sort for bounded values"""
        count = [0] * 1001

        for num in arr1:
            count[num] += 1

        result = []

        for num in arr2:
            result.extend([num] * count[num])
            count[num] = 0

        for num in range(1001):
            result.extend([num] * count[num])

        return result
