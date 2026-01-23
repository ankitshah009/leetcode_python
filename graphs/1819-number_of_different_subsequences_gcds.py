#1819. Number of Different Subsequences GCDs
#Hard
#
#You are given an array nums that consists of positive integers.
#
#The GCD of a sequence of numbers is defined as the greatest integer that
#divides all the numbers in the sequence evenly.
#
#A subsequence of an array is a sequence that can be formed by removing some
#elements (possibly none) of the array.
#
#Return the number of different GCDs among all non-empty subsequences of nums.
#
#Example 1:
#Input: nums = [6,10,3]
#Output: 5
#Explanation: GCDs are 1,2,3,6,10
#
#Example 2:
#Input: nums = [5,15,40,5,6]
#Output: 7
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 2 * 10^5

from typing import List
from math import gcd

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        """
        For each possible GCD value g, check if some subsequence has GCD = g.
        A subsequence has GCD = g iff GCD of all multiples of g in nums equals g.
        """
        max_val = max(nums)
        present = set(nums)
        count = 0

        for g in range(1, max_val + 1):
            # Find GCD of all multiples of g in nums
            subseq_gcd = 0
            for multiple in range(g, max_val + 1, g):
                if multiple in present:
                    subseq_gcd = gcd(subseq_gcd, multiple)
                    if subseq_gcd == g:
                        break

            if subseq_gcd == g:
                count += 1

        return count


class SolutionOptimized:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        """
        Same approach with array instead of set.
        """
        max_val = max(nums)
        present = [False] * (max_val + 1)
        for num in nums:
            present[num] = True

        count = 0

        for g in range(1, max_val + 1):
            current_gcd = 0
            for multiple in range(g, max_val + 1, g):
                if present[multiple]:
                    current_gcd = gcd(current_gcd, multiple)
                    # Early termination
                    if current_gcd == g:
                        count += 1
                        break

        return count


class SolutionDivisors:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        """
        Alternative: for each number, mark its divisors.
        """
        max_val = max(nums)
        # gcd_val[g] = GCD of all numbers in nums that are multiples of g
        gcd_val = [0] * (max_val + 1)

        for num in nums:
            # Update GCD for all divisors of num
            d = 1
            while d * d <= num:
                if num % d == 0:
                    gcd_val[d] = gcd(gcd_val[d], num)
                    if d != num // d:
                        gcd_val[num // d] = gcd(gcd_val[num // d], num)
                d += 1

        return sum(1 for g in range(1, max_val + 1) if gcd_val[g] == g)
