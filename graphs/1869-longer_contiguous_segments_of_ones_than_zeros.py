#1869. Longer Contiguous Segments of Ones than Zeros
#Easy
#
#Given a binary string s, return true if the longest contiguous segment of 1s
#is strictly longer than the longest contiguous segment of 0s in s, or return
#false otherwise.
#
#Note that if there are no 0s, then the longest contiguous segment of 0s is
#considered to have length 0.
#
#Example 1:
#Input: s = "1101"
#Output: true
#
#Example 2:
#Input: s = "111000"
#Output: false
#
#Example 3:
#Input: s = "110100010"
#Output: false
#
#Constraints:
#    1 <= s.length <= 100
#    s[i] is either '0' or '1'.

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        """
        Track longest runs of 0s and 1s.
        """
        max_ones = max_zeros = 0
        current_ones = current_zeros = 0

        for c in s:
            if c == '1':
                current_ones += 1
                current_zeros = 0
                max_ones = max(max_ones, current_ones)
            else:
                current_zeros += 1
                current_ones = 0
                max_zeros = max(max_zeros, current_zeros)

        return max_ones > max_zeros


class SolutionSplit:
    def checkZeroOnes(self, s: str) -> bool:
        """
        Using split to find segments.
        """
        ones_segments = s.split('0')
        zeros_segments = s.split('1')

        max_ones = max(len(seg) for seg in ones_segments) if ones_segments else 0
        max_zeros = max(len(seg) for seg in zeros_segments) if zeros_segments else 0

        return max_ones > max_zeros


class SolutionGroupby:
    def checkZeroOnes(self, s: str) -> bool:
        """
        Using itertools groupby.
        """
        from itertools import groupby

        max_ones = max_zeros = 0

        for char, group in groupby(s):
            length = len(list(group))
            if char == '1':
                max_ones = max(max_ones, length)
            else:
                max_zeros = max(max_zeros, length)

        return max_ones > max_zeros


class SolutionRegex:
    def checkZeroOnes(self, s: str) -> bool:
        """
        Using regex to find all runs.
        """
        import re

        ones = re.findall(r'1+', s)
        zeros = re.findall(r'0+', s)

        max_ones = max((len(x) for x in ones), default=0)
        max_zeros = max((len(x) for x in zeros), default=0)

        return max_ones > max_zeros
