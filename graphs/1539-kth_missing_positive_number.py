#1539. Kth Missing Positive Number
#Easy
#
#Given an array arr of positive integers sorted in a strictly increasing order,
#and an integer k.
#
#Return the kth positive integer that is missing from this array.
#
#Example 1:
#Input: arr = [2,3,4,7,11], k = 5
#Output: 9
#Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...].
#The 5th missing positive integer is 9.
#
#Example 2:
#Input: arr = [1,2,3,4], k = 2
#Output: 6
#Explanation: The missing positive integers are [5,6,7,...].
#The 2nd missing positive integer is 6.
#
#Constraints:
#    1 <= arr.length <= 1000
#    1 <= arr[i] <= 1000
#    1 <= k <= 1000
#    arr[i] < arr[j] for 1 <= i < j <= arr.length

from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Binary search: At index i, arr[i] - (i+1) numbers are missing before arr[i].
        Find the smallest index where missing count >= k.
        """
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2
            # Missing count before arr[mid] is arr[mid] - (mid + 1)
            missing = arr[mid] - (mid + 1)

            if missing < k:
                left = mid + 1
            else:
                right = mid

        # left is the first index where missing >= k
        # Answer is k + left (since left elements from arr are <= answer)
        return k + left


class SolutionLinear:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Linear scan: Track missing count as we go through arr.
        """
        missing = 0
        prev = 0

        for num in arr:
            # Count missing numbers between prev and num
            gap = num - prev - 1

            if missing + gap >= k:
                # The kth missing is in this gap
                return prev + (k - missing)

            missing += gap
            prev = num

        # kth missing is after the array
        return arr[-1] + (k - missing)


class SolutionSet:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Using set for O(1) lookup (less efficient but simple).
        """
        arr_set = set(arr)
        count = 0
        num = 0

        while count < k:
            num += 1
            if num not in arr_set:
                count += 1

        return num


class SolutionMath:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Mathematical approach with binary search.
        """
        # If k missing numbers are before arr[0], answer is k
        if arr[0] > k:
            return k

        n = len(arr)

        # If k missing numbers include all after arr[-1]
        missing_before_end = arr[-1] - n
        if missing_before_end < k:
            return arr[-1] + (k - missing_before_end)

        # Binary search for position
        left, right = 0, n - 1

        while left < right:
            mid = (left + right + 1) // 2
            missing_before_mid = arr[mid] - (mid + 1)

            if missing_before_mid < k:
                left = mid
            else:
                right = mid - 1

        # The answer is between arr[left] and arr[left+1]
        missing_before_left = arr[left] - (left + 1)
        return arr[left] + (k - missing_before_left)


class SolutionIterative:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Simple iterative approach.
        """
        # Adjust k for each element in arr that's <= current answer
        for num in arr:
            if num <= k:
                k += 1
            else:
                break

        return k
