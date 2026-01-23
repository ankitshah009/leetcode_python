#1287. Element Appearing More Than 25% In Sorted Array
#Easy
#
#Given an integer array sorted in non-decreasing order, there is exactly one
#integer in the array that occurs more than 25% of the time, return that integer.
#
#Example 1:
#Input: arr = [1,2,2,6,6,6,6,7,10]
#Output: 6
#
#Example 2:
#Input: arr = [1,1]
#Output: 1
#
#Constraints:
#    1 <= arr.length <= 10^4
#    0 <= arr[i] <= 10^5

from typing import List
import bisect

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        """
        Check elements at 25%, 50%, 75% positions.
        One of them must be the answer.
        """
        n = len(arr)
        threshold = n // 4

        for idx in [n // 4, n // 2, 3 * n // 4]:
            candidate = arr[idx]
            # Find range of candidate using binary search
            left = bisect.bisect_left(arr, candidate)
            right = bisect.bisect_right(arr, candidate)
            if right - left > threshold:
                return candidate

        return arr[0]  # Edge case: single element


class SolutionLinear:
    def findSpecialInteger(self, arr: List[int]) -> int:
        """Linear scan comparing with element n/4 positions ahead."""
        n = len(arr)
        threshold = n // 4

        for i in range(n - threshold):
            if arr[i] == arr[i + threshold]:
                return arr[i]

        return arr[-1]


class SolutionCount:
    def findSpecialInteger(self, arr: List[int]) -> int:
        """Simple counting approach."""
        n = len(arr)
        threshold = n // 4
        count = 1

        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                count += 1
            else:
                count = 1

            if count > threshold:
                return arr[i]

        return arr[0]
