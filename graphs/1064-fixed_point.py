#1064. Fixed Point
#Easy
#
#Given an array of distinct integers arr, where arr is sorted in ascending
#order, return the smallest index i that satisfies arr[i] == i. If there is
#no such index, return -1.
#
#Example 1:
#Input: arr = [-10,-5,0,3,7]
#Output: 3
#Explanation: For the given array, arr[0] = -10, arr[1] = -5, arr[2] = 0,
#arr[3] = 3, thus the output is 3.
#
#Example 2:
#Input: arr = [0,2,5,8,17]
#Output: 0
#Explanation: arr[0] = 0, thus the output is 0.
#
#Example 3:
#Input: arr = [-10,-5,3,4,7,9]
#Output: -1
#Explanation: There is no such i that arr[i] == i, thus the output is -1.
#
#Constraints:
#    1 <= arr.length < 10^4
#    -10^9 <= arr[i] <= 10^9

from typing import List

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        """
        Binary search: find smallest i where arr[i] == i.

        If arr[i] < i, fixed point can only be to the right.
        If arr[i] > i, fixed point can only be to the left.
        If arr[i] == i, check if there's a smaller one to the left.
        """
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                result = mid
                right = mid - 1  # Look for smaller index
            elif arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1

        return result


class SolutionLinear:
    def fixedPoint(self, arr: List[int]) -> int:
        """Linear scan - O(n)"""
        for i, val in enumerate(arr):
            if val == i:
                return i
        return -1


class SolutionBinaryFirst:
    def fixedPoint(self, arr: List[int]) -> int:
        """Binary search finding first occurrence"""
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < mid:
                left = mid + 1
            else:
                right = mid

        return left if arr[left] == left else -1
