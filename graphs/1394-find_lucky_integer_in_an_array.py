#1394. Find Lucky Integer in an Array
#Easy
#
#Given an array of integers arr, a lucky integer is an integer that has a
#frequency in the array equal to its value.
#
#Return the largest lucky integer in the array. If there is no lucky integer
#return -1.
#
#Example 1:
#Input: arr = [2,2,3,4]
#Output: 2
#Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
#
#Example 2:
#Input: arr = [1,2,2,3,3,3]
#Output: 3
#Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
#
#Example 3:
#Input: arr = [2,2,2,3,3]
#Output: -1
#Explanation: There are no lucky numbers in the array.
#
#Constraints:
#    1 <= arr.length <= 500
#    1 <= arr[i] <= 500

from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """
        Count frequencies and find numbers where value == frequency.
        Return the largest such number.
        """
        freq = Counter(arr)

        result = -1
        for num, count in freq.items():
            if num == count:
                result = max(result, num)

        return result


class SolutionOneLiner:
    def findLucky(self, arr: List[int]) -> int:
        """Pythonic one-liner"""
        freq = Counter(arr)
        lucky = [num for num, count in freq.items() if num == count]
        return max(lucky) if lucky else -1


class SolutionSorted:
    def findLucky(self, arr: List[int]) -> int:
        """Check from largest to smallest"""
        freq = Counter(arr)

        # Sort by value descending
        for num in sorted(freq.keys(), reverse=True):
            if num == freq[num]:
                return num

        return -1


class SolutionArray:
    def findLucky(self, arr: List[int]) -> int:
        """Using array for frequency count"""
        max_val = max(arr) if arr else 0
        freq = [0] * (max_val + 1)

        for num in arr:
            freq[num] += 1

        # Find largest lucky integer
        result = -1
        for i in range(1, max_val + 1):
            if i == freq[i]:
                result = i

        return result
