#1784. Check if Binary String Has at Most One Segment of Ones
#Easy
#
#Given a binary string s without leading zeros, return true if s contains at most
#one contiguous segment of ones. Otherwise, return false.
#
#Example 1:
#Input: s = "1001"
#Output: false
#
#Example 2:
#Input: s = "110"
#Output: true
#
#Constraints:
#    1 <= s.length <= 100
#    s[i] is either '0' or '1'.
#    s[0] is '1'.

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """
        Check if there's no '01' pattern (which would mean a new segment of 1s).
        """
        return '01' not in s


class SolutionCount:
    def checkOnesSegment(self, s: str) -> bool:
        """
        Count segments of 1s.
        """
        segments = 0
        prev = '0'

        for c in s:
            if c == '1' and prev == '0':
                segments += 1
            prev = c

        return segments <= 1


class SolutionSplit:
    def checkOnesSegment(self, s: str) -> bool:
        """
        Split by '0' and count non-empty segments.
        """
        parts = s.split('0')
        one_segments = sum(1 for p in parts if p)
        return one_segments <= 1


class SolutionFind:
    def checkOnesSegment(self, s: str) -> bool:
        """
        Check if there's a '1' after seeing a '0'.
        Since string starts with '1', we just need to check for '01'.
        """
        saw_zero = False
        for c in s:
            if c == '0':
                saw_zero = True
            elif saw_zero:  # c == '1' and saw_zero
                return False
        return True
