#1338. Reduce Array Size to The Half
#Medium
#
#You are given an integer array arr. You can choose a set of integers and
#remove all the occurrences of these integers in the array.
#
#Return the minimum size of the set so that at least half of the integers of
#the array are removed.
#
#Example 1:
#Input: arr = [3,3,3,3,5,5,5,2,2,7]
#Output: 2
#Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
#Possible sets of size 2 are {3,5},{3,2},{5,2}.
#Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
#
#Example 2:
#Input: arr = [7,7,7,7,7,7]
#Output: 1
#Explanation: The only possible set you can choose is {7}. This will make the new array empty.
#
#Constraints:
#    2 <= arr.length <= 10^5
#    arr.length is even.
#    1 <= arr[i] <= 10^5

from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """
        Greedy: Remove elements with highest frequency first.
        """
        n = len(arr)
        target = n // 2

        # Count frequencies and sort descending
        freq = Counter(arr)
        sorted_freq = sorted(freq.values(), reverse=True)

        removed = 0
        set_size = 0

        for count in sorted_freq:
            removed += count
            set_size += 1
            if removed >= target:
                return set_size

        return set_size


class SolutionCountingSort:
    def minSetSize(self, arr: List[int]) -> int:
        """Use counting sort for frequencies"""
        n = len(arr)
        target = n // 2

        freq = Counter(arr)

        # Counting sort on frequencies
        freq_count = [0] * (n + 1)
        for f in freq.values():
            freq_count[f] += 1

        removed = 0
        set_size = 0

        for f in range(n, 0, -1):
            while freq_count[f] > 0 and removed < target:
                removed += f
                set_size += 1
                freq_count[f] -= 1

            if removed >= target:
                return set_size

        return set_size
