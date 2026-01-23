#1512. Number of Good Pairs
#Easy
#
#Given an array of integers nums, return the number of good pairs.
#
#A pair (i, j) is called good if nums[i] == nums[j] and i < j.
#
#Example 1:
#Input: nums = [1,2,3,1,1,3]
#Output: 4
#Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#
#Example 2:
#Input: nums = [1,1,1,1]
#Output: 6
#Explanation: Each pair in the array are good.
#
#Example 3:
#Input: nums = [1,2,3]
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 100
#    1 <= nums[i] <= 100

from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Count frequency of each number.
        For each number appearing k times, pairs = k*(k-1)/2.
        """
        freq = Counter(nums)
        return sum(count * (count - 1) // 2 for count in freq.values())


class SolutionOnePass:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        One pass: for each new occurrence, it forms pairs with all previous.
        """
        count = {}
        pairs = 0

        for num in nums:
            if num in count:
                pairs += count[num]  # Forms pairs with all previous occurrences
                count[num] += 1
            else:
                count[num] = 1

        return pairs


class SolutionBruteForce:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """Brute force O(n^2)"""
        n = len(nums)
        pairs = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    pairs += 1

        return pairs


class SolutionMath:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Mathematical: use combination formula.
        If a number appears k times, we can choose 2 from k: C(k,2) = k(k-1)/2
        """
        from collections import Counter
        from math import comb

        freq = Counter(nums)
        return sum(comb(count, 2) for count in freq.values())


class SolutionCompact:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """Compact solution"""
        seen = {}
        result = 0
        for num in nums:
            result += seen.get(num, 0)
            seen[num] = seen.get(num, 0) + 1
        return result
