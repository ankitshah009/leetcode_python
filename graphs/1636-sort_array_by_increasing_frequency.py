#1636. Sort Array by Increasing Frequency
#Easy
#
#Given an array of integers nums, sort the array in increasing order based on
#the frequency of the values. If multiple values have the same frequency, sort
#them in decreasing order.
#
#Return the sorted array.
#
#Example 1:
#Input: nums = [1,1,2,2,2,3]
#Output: [3,1,1,2,2,2]
#Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has
#a frequency of 3.
#
#Example 2:
#Input: nums = [2,3,1,3,2]
#Output: [1,3,3,2,2]
#Explanation: '2' and '3' both have a frequency of 2, so they are sorted in
#decreasing order.
#
#Example 3:
#Input: nums = [-1,1,-6,4,5,-6,1,4,1]
#Output: [5,-1,4,4,-6,-6,1,1,1]
#
#Constraints:
#    1 <= nums.length <= 100
#    -100 <= nums[i] <= 100

from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Count frequencies, sort by (frequency, -value).
        """
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))


class SolutionDetailed:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Detailed approach with explicit sorting.
        """
        # Count frequency of each number
        count = Counter(nums)

        # Sort by:
        # 1. Frequency (ascending)
        # 2. Value (descending, for tie-breaking)
        nums.sort(key=lambda x: (count[x], -x))

        return nums


class SolutionManual:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Manual counting without Counter.
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Group by frequency
        freq_groups = {}
        for num, count in freq.items():
            if count not in freq_groups:
                freq_groups[count] = []
            freq_groups[count].append(num)

        # Sort groups by frequency ascending
        # Within each group, sort values descending
        result = []
        for count in sorted(freq_groups.keys()):
            values = sorted(freq_groups[count], reverse=True)
            for val in values:
                result.extend([val] * count)

        return result


class SolutionCompact:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Compact one-liner.
        """
        c = Counter(nums)
        return sorted(nums, key=lambda x: (c[x], -x))
