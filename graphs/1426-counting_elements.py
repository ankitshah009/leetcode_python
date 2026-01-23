#1426. Counting Elements
#Easy
#
#Given an integer array arr, count how many elements x there are, such that
#x + 1 is also in arr. If there are duplicates in arr, count them separately.
#
#Example 1:
#Input: arr = [1,2,3]
#Output: 2
#Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
#
#Example 2:
#Input: arr = [1,1,3,3,5,5,7,7]
#Output: 0
#Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.
#
#Constraints:
#    1 <= arr.length <= 1000
#    0 <= arr[i] <= 1000

from typing import List
from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        """
        For each element x, check if x+1 exists in arr.
        Use a set for O(1) lookup.
        """
        num_set = set(arr)
        count = 0

        for x in arr:
            if x + 1 in num_set:
                count += 1

        return count


class SolutionOneLiner:
    def countElements(self, arr: List[int]) -> int:
        """Pythonic one-liner"""
        s = set(arr)
        return sum(1 for x in arr if x + 1 in s)


class SolutionCounter:
    def countElements(self, arr: List[int]) -> int:
        """Using Counter for frequency"""
        freq = Counter(arr)
        count = 0

        for x, cnt in freq.items():
            if x + 1 in freq:
                count += cnt

        return count


class SolutionSorted:
    def countElements(self, arr: List[int]) -> int:
        """Sorting approach"""
        arr.sort()
        count = 0
        i = 0

        while i < len(arr):
            current = arr[i]
            # Count occurrences of current
            current_count = 0
            while i < len(arr) and arr[i] == current:
                current_count += 1
                i += 1

            # Check if next value is current + 1
            if i < len(arr) and arr[i] == current + 1:
                count += current_count

        return count
