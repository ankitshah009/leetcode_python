#1053. Previous Permutation With One Swap
#Medium
#
#Given an array of positive integers arr (not necessarily distinct), return
#the lexicographically largest permutation that is smaller than arr, that
#can be made with exactly one swap. If it cannot be done, then return the
#same array.
#
#Note: A swap exchanges the positions of two numbers arr[i] and arr[j]
#
#Example 1:
#Input: arr = [3,2,1]
#Output: [3,1,2]
#Explanation: Swapping 2 and 1.
#
#Example 2:
#Input: arr = [1,1,5]
#Output: [1,1,5]
#Explanation: This is already the smallest permutation.
#
#Example 3:
#Input: arr = [1,9,4,6,7]
#Output: [1,7,4,6,9]
#Explanation: Swapping 9 and 7.
#
#Constraints:
#    1 <= arr.length <= 10^4
#    1 <= arr[i] <= 10^4

from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        """
        Find rightmost position i where arr[i] > arr[i+1] (decreasing pair).
        Find largest element to the right that is smaller than arr[i].
        If multiple, pick rightmost one.
        """
        n = len(arr)

        # Find rightmost decreasing pair
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1

        if i < 0:
            return arr  # Already smallest permutation

        # Find largest element to right smaller than arr[i]
        # If duplicates, take rightmost
        j = n - 1
        while arr[j] >= arr[i]:
            j -= 1

        # Skip duplicates (take rightmost occurrence of this value)
        while j > i + 1 and arr[j - 1] == arr[j]:
            j -= 1

        # Swap
        arr[i], arr[j] = arr[j], arr[i]
        return arr


class SolutionDetailed:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        """More explicit with comments"""
        n = len(arr)

        # Step 1: Find rightmost position where arr[i] > arr[i+1]
        # This is where we can make a decrease
        swap_pos = -1
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                swap_pos = i
                break

        if swap_pos == -1:
            return arr  # Array is non-decreasing, can't make smaller

        # Step 2: Find the largest value to the right that is smaller than arr[swap_pos]
        # Among duplicates, pick the leftmost (rightmost position in reversed scan)
        best_val = -1
        best_idx = -1

        for j in range(swap_pos + 1, n):
            if arr[j] < arr[swap_pos]:
                if arr[j] > best_val:
                    best_val = arr[j]
                    best_idx = j

        # Step 3: Swap
        arr[swap_pos], arr[best_idx] = arr[best_idx], arr[swap_pos]
        return arr
