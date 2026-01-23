#1898. Maximum Number of Removable Characters
#Medium
#
#You are given two strings s and p where p is a subsequence of s. You are also
#given a distinct 0-indexed integer array removable containing a subset of
#indices of s (s is also 0-indexed).
#
#You want to choose an integer k (0 <= k <= removable.length) such that, after
#removing k characters from s using the first k indices in removable, p is
#still a subsequence of s. More formally, you will mark the character at
#s[removable[i]] for each 0 <= i < k, then remove all marked characters and
#check if p is still a subsequence.
#
#Return the maximum k you can choose such that p is still a subsequence of s
#after the removals.
#
#A subsequence of a string is a new string generated from the original string
#with some characters (can be none) deleted without changing the relative order
#of the remaining characters.
#
#Example 1:
#Input: s = "abcacb", p = "ab", removable = [3,1,0]
#Output: 2
#
#Example 2:
#Input: s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
#Output: 1
#
#Example 3:
#Input: s = "abcab", p = "abc", removable = [0,1,2,3,4]
#Output: 0
#
#Constraints:
#    1 <= p.length <= s.length <= 10^5
#    0 <= removable.length < s.length
#    0 <= removable[i] < s.length
#    p is a subsequence of s.
#    s and p both consist of lowercase English letters.
#    The elements in removable are distinct.

from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        """
        Binary search on k.
        """
        def is_subsequence(k: int) -> bool:
            """Check if p is subsequence after removing first k indices."""
            removed = set(removable[:k])
            j = 0  # Pointer for p

            for i, c in enumerate(s):
                if i in removed:
                    continue
                if c == p[j]:
                    j += 1
                    if j == len(p):
                        return True

            return j == len(p)

        left, right = 0, len(removable)

        while left < right:
            mid = (left + right + 1) // 2
            if is_subsequence(mid):
                left = mid
            else:
                right = mid - 1

        return left


class SolutionOptimized:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        """
        Optimized with array instead of set for checking removed.
        """
        n = len(s)

        def check(k: int) -> bool:
            removed = [False] * n
            for i in range(k):
                removed[removable[i]] = True

            pi = 0
            for i in range(n):
                if removed[i]:
                    continue
                if s[i] == p[pi]:
                    pi += 1
                    if pi == len(p):
                        return True

            return pi == len(p)

        lo, hi = 0, len(removable)

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
