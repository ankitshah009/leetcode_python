#1513. Number of Substrings With Only 1s
#Medium
#
#Given a binary string s, return the number of substrings with all characters 1's.
#Since the answer may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: s = "0110111"
#Output: 9
#Explanation: There are 9 substring in total with only 1's characters.
#"1" -> 5 times.
#"11" -> 3 times.
#"111" -> 1 time.
#
#Example 2:
#Input: s = "101"
#Output: 2
#Explanation: Substring "1" is shown 2 times in s.
#
#Example 3:
#Input: s = "111111"
#Output: 21
#Explanation: Each substring contains only 1's characters.
#
#Constraints:
#    1 <= s.length <= 10^5
#    s[i] is either '0' or '1'.

class Solution:
    def numSub(self, s: str) -> int:
        """
        For a consecutive run of k ones, number of substrings = k*(k+1)/2.
        Sum over all runs of 1s.
        """
        MOD = 10**9 + 7
        total = 0
        current_run = 0

        for char in s:
            if char == '1':
                current_run += 1
                total = (total + current_run) % MOD
            else:
                current_run = 0

        return total


class SolutionRuns:
    def numSub(self, s: str) -> int:
        """
        Find all runs of 1s and use formula k*(k+1)/2.
        """
        MOD = 10**9 + 7
        total = 0
        k = 0

        for char in s + '0':  # Add '0' to flush last run
            if char == '1':
                k += 1
            else:
                if k > 0:
                    total = (total + k * (k + 1) // 2) % MOD
                    k = 0

        return total


class SolutionSplit:
    def numSub(self, s: str) -> int:
        """
        Split by '0' and count substrings in each segment.
        """
        MOD = 10**9 + 7
        total = 0

        for segment in s.split('0'):
            k = len(segment)
            total = (total + k * (k + 1) // 2) % MOD

        return total


class SolutionIterator:
    def numSub(self, s: str) -> int:
        """
        Using groupby from itertools.
        """
        from itertools import groupby

        MOD = 10**9 + 7
        total = 0

        for char, group in groupby(s):
            if char == '1':
                k = sum(1 for _ in group)
                total = (total + k * (k + 1) // 2) % MOD

        return total


class SolutionOneLiner:
    def numSub(self, s: str) -> int:
        """One-liner solution"""
        MOD = 10**9 + 7
        return sum(len(seg) * (len(seg) + 1) // 2 for seg in s.split('0')) % MOD
