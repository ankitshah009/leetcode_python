#1471. The k Strongest Values in an Array
#Medium
#
#Given an array of integers arr and an integer k.
#
#A value arr[i] is said to be stronger than a value arr[j] if
#|arr[i] - m| > |arr[j] - m| where m is the median of the array.
#If |arr[i] - m| == |arr[j] - m|, then arr[i] is said to be stronger than arr[j]
#if arr[i] > arr[j].
#
#Return a list of the strongest k values in the array. Return the answer in any order.
#
#Median is the middle value in an ordered integer list. More formally, if the
#length of the list is n, the median is the element in position ((n - 1) / 2)
#in the sorted list (0-indexed).
#
#Example 1:
#Input: arr = [1,2,3,4,5], k = 2
#Output: [5,1]
#Explanation: Median is 3, the elements of the array sorted by the strongest are
#[5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also accepted.
#
#Example 2:
#Input: arr = [1,1,3,5,5], k = 2
#Output: [5,5]
#Explanation: Median is 3, the elements of the array sorted by the strongest are
#[5,5,1,1,3]. The strongest 2 elements are [5, 5].
#
#Example 3:
#Input: arr = [6,7,11,7,6,8], k = 5
#Output: [11,8,6,6,7]
#Explanation: Median is 7, the elements of the array sorted by the strongest are
#[11,8,6,6,7,7]. Any permutation of [11,8,6,6,7] is accepted.
#
#Constraints:
#    1 <= arr.length <= 10^5
#    -10^5 <= arr[i] <= 10^5
#    1 <= k <= arr.length

from typing import List
import heapq

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        """
        Sort to find median, then use two pointers.
        After sorting, strongest values are at ends.
        """
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]

        # Two pointers: strongest values are at extremes
        left, right = 0, n - 1
        result = []

        while len(result) < k:
            if abs(arr[right] - median) >= abs(arr[left] - median):
                result.append(arr[right])
                right -= 1
            else:
                result.append(arr[left])
                left += 1

        return result


class SolutionSort:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        """Sort by strength and take top k"""
        arr.sort()
        median = arr[(len(arr) - 1) // 2]

        # Sort by strength (desc), then by value (desc)
        arr.sort(key=lambda x: (-abs(x - median), -x))

        return arr[:k]


class SolutionHeap:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        """Use heap to find k strongest"""
        arr.sort()
        median = arr[(len(arr) - 1) // 2]

        # Use nlargest with custom key
        return heapq.nlargest(k, arr, key=lambda x: (abs(x - median), x))


class SolutionQuickSelect:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        """
        Use quickselect to find median, then quickselect again
        to find k strongest. Average O(n) time.
        """
        import random

        def quickselect(nums: List[int], k: int) -> int:
            """Find kth smallest element"""
            pivot = random.choice(nums)
            less = [x for x in nums if x < pivot]
            equal = [x for x in nums if x == pivot]
            greater = [x for x in nums if x > pivot]

            if k < len(less):
                return quickselect(less, k)
            elif k < len(less) + len(equal):
                return pivot
            else:
                return quickselect(greater, k - len(less) - len(equal))

        # Find median
        n = len(arr)
        median = quickselect(arr, (n - 1) // 2)

        # Sort by strength and take k strongest
        arr.sort(key=lambda x: (-abs(x - median), -x))
        return arr[:k]
