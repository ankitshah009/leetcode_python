#1228. Missing Number In Arithmetic Progression
#Easy
#
#In some array arr, the values were in arithmetic progression: the values
#arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.
#
#A value from arr was removed that was not the first or last value in the array.
#
#Given arr, return the removed value.
#
#Example 1:
#Input: arr = [5,7,11,13]
#Output: 9
#Explanation: The previous array was [5,7,9,11,13].
#
#Example 2:
#Input: arr = [15,13,12]
#Output: 14
#Explanation: The previous array was [15,14,13,12].
#
#Constraints:
#    3 <= arr.length <= 1000
#    0 <= arr[i] <= 10^5
#    The given array is guaranteed to be a valid array.

from typing import List

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        """
        Calculate expected sum and compare with actual sum.
        """
        n = len(arr)
        # Expected common difference
        d = (arr[-1] - arr[0]) // n

        # If d is 0, all elements are same, return any
        if d == 0:
            return arr[0]

        # Find where the gap is larger than d
        for i in range(1, n):
            if arr[i] - arr[i - 1] != d:
                return arr[i - 1] + d

        return arr[0]  # Shouldn't reach here for valid input


class SolutionSum:
    def missingNumber(self, arr: List[int]) -> int:
        """Using arithmetic series sum formula"""
        n = len(arr) + 1  # Original length
        # Expected sum with n elements
        expected_sum = n * (arr[0] + arr[-1]) // 2
        actual_sum = sum(arr)
        return expected_sum - actual_sum


class SolutionBinarySearch:
    def missingNumber(self, arr: List[int]) -> int:
        """Binary search for the gap"""
        n = len(arr)
        d = (arr[-1] - arr[0]) // n

        if d == 0:
            return arr[0]

        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            # Expected value at mid position
            expected = arr[0] + mid * d

            if arr[mid] == expected:
                left = mid + 1
            else:
                right = mid

        return arr[0] + left * d
