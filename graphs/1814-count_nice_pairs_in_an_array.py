#1814. Count Nice Pairs in an Array
#Medium
#
#You are given an array nums that consists of non-negative integers. Let us
#define rev(x) as the reverse of the non-negative integer x. For example,
#rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it
#satisfies all of the following conditions:
#- 0 <= i < j < nums.length
#- nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
#
#Return the number of nice pairs of indices. Since that number can be too
#large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: nums = [42,11,1,97]
#Output: 2
#
#Example 2:
#Input: nums = [13,10,35,24,76]
#Output: 4
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= nums[i] <= 10^9

from typing import List
from collections import defaultdict

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        Rearranging: nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        Count pairs with same diff value.
        """
        MOD = 10**9 + 7

        def rev(x: int) -> int:
            result = 0
            while x:
                result = result * 10 + x % 10
                x //= 10
            return result

        # Count frequency of (num - rev(num))
        freq = defaultdict(int)
        count = 0

        for num in nums:
            diff = num - rev(num)
            # Add pairs with existing same diff
            count = (count + freq[diff]) % MOD
            freq[diff] += 1

        return count


class SolutionCombinatorics:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        Count all, then use n choose 2 formula.
        """
        MOD = 10**9 + 7

        def rev(x: int) -> int:
            return int(str(x)[::-1])

        freq = defaultdict(int)
        for num in nums:
            diff = num - rev(num)
            freq[diff] += 1

        # For each group of k, pairs = k*(k-1)/2
        count = 0
        for k in freq.values():
            count = (count + k * (k - 1) // 2) % MOD

        return count


class SolutionCounter:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        Using Counter.
        """
        from collections import Counter

        MOD = 10**9 + 7

        diffs = [num - int(str(num)[::-1]) for num in nums]
        freq = Counter(diffs)

        return sum(v * (v - 1) // 2 for v in freq.values()) % MOD
