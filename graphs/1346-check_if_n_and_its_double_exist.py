#1346. Check If N and Its Double Exist
#Easy
#
#Given an array arr of integers, check if there exist two indices i and j such that:
#    i != j
#    0 <= i, j < arr.length
#    arr[i] == 2 * arr[j]
#
#Example 1:
#Input: arr = [10,2,5,3]
#Output: true
#Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
#
#Example 2:
#Input: arr = [3,1,7,11]
#Output: false
#Explanation: There is no i and j that satisfy the conditions.
#
#Constraints:
#    2 <= arr.length <= 500
#    -10^3 <= arr[i] <= 10^3

from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        Use set to check for existence of double or half.
        """
        seen = set()

        for num in arr:
            # Check if double exists or half exists
            if 2 * num in seen:
                return True
            if num % 2 == 0 and num // 2 in seen:
                return True
            seen.add(num)

        return False


class SolutionSet:
    def checkIfExist(self, arr: List[int]) -> bool:
        """Build set first, then check"""
        s = set(arr)

        for num in arr:
            if num != 0 and 2 * num in s:
                return True

        # Handle zero case separately
        return arr.count(0) >= 2


class SolutionBruteForce:
    def checkIfExist(self, arr: List[int]) -> bool:
        """O(n^2) brute force"""
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False


class SolutionBinarySearch:
    def checkIfExist(self, arr: List[int]) -> bool:
        """Sort and binary search"""
        import bisect

        arr_sorted = sorted(arr)
        n = len(arr_sorted)

        for i, num in enumerate(arr_sorted):
            target = 2 * num
            # Binary search for target
            j = bisect.bisect_left(arr_sorted, target)
            if j < n and arr_sorted[j] == target and j != i:
                return True

        return False
