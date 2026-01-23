#1502. Can Make Arithmetic Progression From Sequence
#Easy
#
#A sequence of numbers is called an arithmetic progression if the difference
#between any two consecutive elements is the same.
#
#Given an array of numbers arr, return true if the array can be rearranged to
#form an arithmetic progression. Otherwise, return false.
#
#Example 1:
#Input: arr = [3,5,1]
#Output: true
#Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences
#2 and -2 respectively, between each consecutive elements.
#
#Example 2:
#Input: arr = [1,2,4]
#Output: false
#Explanation: There is no way to reorder the elements to obtain an arithmetic
#progression.
#
#Constraints:
#    2 <= arr.length <= 1000
#    -10^6 <= arr[i] <= 10^6

from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        Sort and check if differences are constant.
        """
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False

        return True


class SolutionSet:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        O(n) solution using math and set.
        AP: a, a+d, a+2d, ..., a+(n-1)d
        Min = a, Max = a + (n-1)d
        d = (max - min) / (n - 1)
        All elements should be min + k*d for some integer k.
        """
        n = len(arr)
        min_val, max_val = min(arr), max(arr)

        # Check if difference divides evenly
        if (max_val - min_val) % (n - 1) != 0:
            return False

        d = (max_val - min_val) // (n - 1)

        # Special case: all elements same
        if d == 0:
            return len(set(arr)) == 1

        # Check all elements fit the pattern
        seen = set(arr)

        for i in range(n):
            expected = min_val + i * d
            if expected not in seen:
                return False

        return True


class SolutionInPlace:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        O(n) time O(1) space using in-place bucket placement.
        """
        n = len(arr)
        min_val, max_val = min(arr), max(arr)

        if max_val == min_val:
            return True

        if (max_val - min_val) % (n - 1) != 0:
            return False

        d = (max_val - min_val) // (n - 1)

        # Try to place each element in its correct position
        i = 0
        while i < n:
            if (arr[i] - min_val) % d != 0:
                return False

            pos = (arr[i] - min_val) // d

            if pos < 0 or pos >= n:
                return False

            if pos == i:
                i += 1
            elif arr[pos] == arr[i]:
                if pos != i:
                    return False  # Duplicate at wrong position
                i += 1
            else:
                arr[i], arr[pos] = arr[pos], arr[i]

        return True


class SolutionCompact:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """Compact solution"""
        arr.sort()
        return len(set(arr[i + 1] - arr[i] for i in range(len(arr) - 1))) == 1
