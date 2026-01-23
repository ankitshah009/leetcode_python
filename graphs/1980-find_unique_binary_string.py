#1980. Find Unique Binary String
#Medium
#
#Given an array of strings nums containing n unique binary strings each of
#length n, return a binary string of length n that does not appear in nums. If
#there are multiple answers, you may return any of them.
#
#Example 1:
#Input: nums = ["01","10"]
#Output: "11"
#Explanation: "11" does not appear in nums. "00" would also be correct.
#
#Example 2:
#Input: nums = ["00","01"]
#Output: "11"
#
#Example 3:
#Input: nums = ["111","011","001"]
#Output: "101"
#
#Constraints:
#    n == nums.length
#    1 <= n <= 16
#    nums[i].length == n
#    nums[i] is either '0' or '1'.
#    All the strings of nums are unique.

from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Cantor's diagonal argument: differ from nums[i] at position i.
        """
        result = []

        for i, num in enumerate(nums):
            # Flip the i-th bit of the i-th string
            result.append('0' if num[i] == '1' else '1')

        return ''.join(result)


class SolutionSet:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Try all possibilities until finding one not in set.
        """
        n = len(nums)
        num_set = set(nums)

        for i in range(2 ** n):
            candidate = bin(i)[2:].zfill(n)
            if candidate not in num_set:
                return candidate

        return ""


class SolutionBacktrack:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Backtracking approach.
        """
        n = len(nums)
        num_set = set(nums)

        def backtrack(current: list) -> str:
            if len(current) == n:
                s = ''.join(current)
                return s if s not in num_set else ""

            for bit in ['0', '1']:
                current.append(bit)
                result = backtrack(current)
                if result:
                    return result
                current.pop()

            return ""

        return backtrack([])


class SolutionRandom:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Random sampling (for interview variety).
        """
        import random

        n = len(nums)
        num_set = set(nums)

        while True:
            candidate = ''.join(random.choice('01') for _ in range(n))
            if candidate not in num_set:
                return candidate
