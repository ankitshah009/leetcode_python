#1865. Finding Pairs With a Certain Sum
#Medium
#
#You are given two integer arrays nums1 and nums2. You are tasked to implement
#a data structure that supports queries of two types:
#
#1. Add a positive integer to an element of a given index in the array nums2.
#2. Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a
#   given value (0 <= i < nums1.length and 0 <= j < nums2.length).
#
#Implement the FindSumPairs class:
#- FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object
#  with two integer arrays nums1 and nums2.
#- void add(int index, int val) Adds val to nums2[index], i.e.,
#  apply nums2[index] += val.
#- int count(int tot) Returns the number of pairs (i, j) such that
#  nums1[i] + nums2[j] == tot.
#
#Example 1:
#Input:
#["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
#[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
#Output:
#[null, 8, null, 2, 1, null, null, 11]
#
#Constraints:
#    1 <= nums1.length <= 1000
#    1 <= nums2.length <= 10^5
#    1 <= nums1[i] <= 10^9
#    1 <= nums2[j] <= 10^9
#    0 <= index < nums2.length
#    1 <= val <= 10^5
#    1 <= tot <= 10^9
#    At most 1000 calls are made to add and count each.

from typing import List
from collections import Counter

class FindSumPairs:
    """
    Store frequency of nums2, update on add.
    For count, iterate through nums1.
    """

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        # Update frequency map
        old_val = self.nums2[index]
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]

        self.nums2[index] += val
        self.freq2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        # For each num in nums1, find complement in nums2
        result = 0
        for num in self.nums1:
            complement = tot - num
            result += self.freq2.get(complement, 0)
        return result


class FindSumPairsOptimized:
    """
    Same approach with Counter on nums1 too for deduplication.
    """

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.freq1 = Counter(nums1)
        self.nums2 = nums2
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.freq2[old_val] -= 1

        new_val = old_val + val
        self.nums2[index] = new_val
        self.freq2[new_val] += 1

    def count(self, tot: int) -> int:
        result = 0
        for num, cnt in self.freq1.items():
            complement = tot - num
            result += cnt * self.freq2.get(complement, 0)
        return result
