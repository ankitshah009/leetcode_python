#1862. Sum of Floored Pairs
#Hard
#
#Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for
#all pairs of indices 0 <= i, j < nums.length in the array. Since the answer
#may be too large, return it modulo 10^9 + 7.
#
#The floor() function returns the integer part of the division.
#
#Example 1:
#Input: nums = [2,5,9]
#Output: 10
#Explanation:
#floor(2/5) = 0, floor(2/9) = 0, floor(5/2) = 2, floor(5/9) = 0,
#floor(9/2) = 4, floor(9/5) = 1, plus diagonals (1,1,1) = 3
#Total = 0+0+2+0+4+1+3 = 10
#
#Example 2:
#Input: nums = [7,7,7,7,7,7,7]
#Output: 49
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^5

from typing import List

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        """
        For each divisor d, count how many nums give floor >= 1, >= 2, etc.
        Using prefix sums on frequency array.
        """
        MOD = 10**9 + 7
        max_val = max(nums)

        # Frequency array
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1

        # Prefix sum of frequencies
        prefix = [0] * (max_val + 2)
        for i in range(1, max_val + 1):
            prefix[i] = prefix[i - 1] + freq[i]

        result = 0

        for d in range(1, max_val + 1):
            if freq[d] == 0:
                continue

            # For divisor d, count pairs where floor(num/d) = k for k = 1, 2, ...
            # Numbers in range [k*d, (k+1)*d - 1] give floor = k
            for k in range(1, max_val // d + 1):
                low = k * d
                high = min((k + 1) * d - 1, max_val)

                # Count of numbers in [low, high]
                count = prefix[high] - prefix[low - 1]
                result = (result + freq[d] * k * count) % MOD

        return result


class SolutionOptimized:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        """
        Same approach with cleaner implementation.
        """
        MOD = 10**9 + 7
        max_val = max(nums)

        # Count frequencies
        count = [0] * (max_val + 1)
        for num in nums:
            count[num] += 1

        # Prefix sum: prefix[i] = count of numbers <= i
        prefix = [0] * (max_val + 2)
        for i in range(max_val + 1):
            prefix[i + 1] = prefix[i] + count[i]

        def count_in_range(lo, hi):
            """Count of numbers in [lo, hi]."""
            hi = min(hi, max_val)
            if lo > hi:
                return 0
            return prefix[hi + 1] - prefix[lo]

        total = 0

        for d in range(1, max_val + 1):
            if count[d] == 0:
                continue

            # Sum floor(x/d) for all x
            contribution = 0
            mult = 1
            lo = d

            while lo <= max_val:
                hi = lo + d - 1
                cnt = count_in_range(lo, hi)
                contribution += mult * cnt
                mult += 1
                lo += d

            total = (total + count[d] * contribution) % MOD

        return total
