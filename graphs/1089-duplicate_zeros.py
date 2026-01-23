#1089. Duplicate Zeros
#Easy
#
#Given a fixed-length integer array arr, duplicate each occurrence of zero,
#shifting the remaining elements to the right.
#
#Note that elements beyond the length of the original array are not written.
#Do the above modifications to the input array in place and do not return
#anything.
#
#Example 1:
#Input: arr = [1,0,2,3,0,4,5,0]
#Output: [1,0,0,2,3,0,0,4]
#Explanation: After calling your function, the input array is modified to:
#[1,0,0,2,3,0,0,4]
#
#Example 2:
#Input: arr = [1,2,3]
#Output: [1,2,3]
#Explanation: After calling your function, the input array is modified to:
#[1,2,3]
#
#Constraints:
#    1 <= arr.length <= 10^4
#    0 <= arr[i] <= 9

from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Two-pass: First find where array would end, then fill backwards.
        """
        n = len(arr)
        zeros = arr.count(0)

        # Find the last element that will be in result
        # Simulate forward to find end position
        i = n - 1
        j = n + zeros - 1  # Position in expanded array

        while i >= 0:
            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                j -= 1
                if j < n:
                    arr[j] = 0
            else:
                if j < n:
                    arr[j] = arr[i]
            i -= 1
            j -= 1


class SolutionTwoPointer:
    def duplicateZeros(self, arr: List[int]) -> None:
        """Explicit two-pointer approach"""
        n = len(arr)

        # Count how many elements will fit
        zeros = 0
        length = 0
        for i, val in enumerate(arr):
            if val == 0:
                zeros += 1
            if i + zeros >= n:
                length = i
                break
        else:
            length = n - 1

        # Check edge case: zero at boundary
        j = n - 1
        i = length

        # Handle case where last fitting element is a zero
        if arr[i] == 0 and i + zeros == n:
            arr[j] = 0
            j -= 1
            i -= 1
            zeros -= 1

        # Fill from back
        while i >= 0:
            if arr[i] == 0:
                arr[j] = 0
                arr[j - 1] = 0
                j -= 2
            else:
                arr[j] = arr[i]
                j -= 1
            i -= 1


class SolutionSimple:
    def duplicateZeros(self, arr: List[int]) -> None:
        """Simple O(n) extra space solution for clarity"""
        n = len(arr)
        result = []

        for val in arr:
            result.append(val)
            if val == 0:
                result.append(0)
            if len(result) >= n:
                break

        for i in range(n):
            arr[i] = result[i]
