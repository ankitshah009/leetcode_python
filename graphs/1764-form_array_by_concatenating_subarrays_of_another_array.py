#1764. Form Array by Concatenating Subarrays of Another Array
#Medium
#
#You are given a 2D integer array groups of length n. You are also given an
#integer array nums.
#
#You are asked if you can choose n disjoint subarrays from the array nums such
#that the ith subarray is equal to groups[i] (0-indexed), and if i > 0, the
#(i-1)th subarray appears before the ith subarray in nums (i.e., the subarrays
#must be in the same order as groups).
#
#Return true if you can do this task, and false otherwise.
#
#Example 1:
#Input: groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]
#Output: true
#
#Example 2:
#Input: groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]
#Output: false
#
#Example 3:
#Input: groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]
#Output: false
#
#Constraints:
#    groups.length == n
#    1 <= n <= 10^3
#    1 <= groups[i].length, sum(groups[i].length) <= 10^3
#    1 <= nums.length <= 10^3
#    -10^7 <= groups[i][j], nums[k] <= 10^7

from typing import List

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        """
        Greedy: find each group in order.
        """
        n = len(nums)
        i = 0  # Current position in nums

        for group in groups:
            found = False
            g_len = len(group)

            while i <= n - g_len:
                if nums[i:i + g_len] == group:
                    found = True
                    i += g_len  # Move past this group
                    break
                i += 1

            if not found:
                return False

        return True


class SolutionKMP:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        """
        Using KMP for pattern matching.
        """
        def kmp_search(text: List[int], pattern: List[int], start: int) -> int:
            """Return first occurrence of pattern in text[start:], or -1."""
            if not pattern:
                return start

            # Build failure function
            m = len(pattern)
            fail = [0] * m
            k = 0
            for i in range(1, m):
                while k > 0 and pattern[k] != pattern[i]:
                    k = fail[k - 1]
                if pattern[k] == pattern[i]:
                    k += 1
                fail[i] = k

            # Search
            k = 0
            for i in range(start, len(text)):
                while k > 0 and pattern[k] != text[i]:
                    k = fail[k - 1]
                if pattern[k] == text[i]:
                    k += 1
                if k == m:
                    return i - m + 1

            return -1

        pos = 0
        for group in groups:
            idx = kmp_search(nums, group, pos)
            if idx == -1:
                return False
            pos = idx + len(group)

        return True


class SolutionSimple:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        """
        Simpler implementation using string conversion (works for small values).
        """
        pos = 0

        for group in groups:
            while pos <= len(nums) - len(group):
                if nums[pos:pos + len(group)] == group:
                    pos += len(group)
                    break
                pos += 1
            else:
                return False

        return True
