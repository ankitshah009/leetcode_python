#1588. Sum of All Odd Length Subarrays
#Easy
#
#Given an array of positive integers arr, return the sum of all possible
#odd-length subarrays of arr.
#
#A subarray is a contiguous subsequence of the array.
#
#Example 1:
#Input: arr = [1,4,2,5,3]
#Output: 58
#Explanation: The odd-length subarrays of arr and their sums are:
#[1] = 1
#[4] = 4
#[2] = 2
#[5] = 5
#[3] = 3
#[1,4,2] = 7
#[4,2,5] = 11
#[2,5,3] = 10
#[1,4,2,5,3] = 15
#Total = 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
#
#Example 2:
#Input: arr = [1,2]
#Output: 3
#Explanation: There are only 2 subarrays of odd length, [1] and [2].
#
#Example 3:
#Input: arr = [10,11,12]
#Output: 66
#
#Constraints:
#    1 <= arr.length <= 100
#    1 <= arr[i] <= 1000

from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        Count how many times each element appears in odd-length subarrays.

        For element at index i:
        - Number of subarrays starting at or before i: i + 1
        - Number of subarrays ending at or after i: n - i
        - Total subarrays containing arr[i]: (i + 1) * (n - i)

        Among these, roughly half are odd-length and half are even-length.
        Actually: odd_count = (total + 1) // 2
        """
        n = len(arr)
        total = 0

        for i in range(n):
            # Number of subarrays containing arr[i]
            start_choices = i + 1  # Can start at 0, 1, ..., i
            end_choices = n - i     # Can end at i, i+1, ..., n-1

            total_containing = start_choices * end_choices

            # Number of odd-length subarrays containing arr[i]
            odd_count = (total_containing + 1) // 2

            total += arr[i] * odd_count

        return total


class SolutionBruteForce:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        Brute force: enumerate all odd-length subarrays.
        O(n^3) time but acceptable for n <= 100.
        """
        n = len(arr)
        total = 0

        for length in range(1, n + 1, 2):  # Odd lengths only
            for start in range(n - length + 1):
                total += sum(arr[start:start + length])

        return total


class SolutionPrefixSum:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        Use prefix sum to compute subarray sums in O(1).
        """
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        total = 0
        for length in range(1, n + 1, 2):
            for start in range(n - length + 1):
                total += prefix[start + length] - prefix[start]

        return total


class SolutionMath:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        Mathematical approach with contribution counting.

        For index i, the number of odd-length subarrays containing it is:
        - left choices: i + 1 (positions 0 to i)
        - right choices: n - i (positions i to n-1)

        For a subarray from l to r containing i (l <= i <= r):
        - Length is r - l + 1
        - Odd length means (r - l + 1) is odd
        - Which means (r - l) is even
        - Which means r and l have same parity

        Count odd-length subarrays = odd_left * odd_right + even_left * even_right
        """
        n = len(arr)
        total = 0

        for i in range(n):
            # Left positions: 0 to i
            left_count = i + 1
            odd_left = (left_count + 1) // 2   # 1, 3, 5, ... (0-indexed: 0, 2, 4, ...)
            even_left = left_count // 2         # 2, 4, 6, ... (0-indexed: 1, 3, 5, ...)

            # Right positions: i to n-1
            right_count = n - i
            odd_right = (right_count + 1) // 2
            even_right = right_count // 2

            # Odd length = same parity on both sides
            odd_subarrays = odd_left * odd_right + even_left * even_right

            total += arr[i] * odd_subarrays

        return total
