#1247. Minimum Swaps to Make Strings Equal
#Medium
#
#You are given two strings s1 and s2 of equal length consisting of letters "x"
#and "y" only. Your task is to make these two strings equal to each other. You
#can swap any two characters that belong to different strings, which means:
#swap s1[i] and s2[j].
#
#Return the minimum number of swaps required to make s1 and s2 equal, or return
#-1 if it is impossible to do so.
#
#Example 1:
#Input: s1 = "xx", s2 = "yy"
#Output: 1
#Explanation: Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
#
#Example 2:
#Input: s1 = "xy", s2 = "yx"
#Output: 2
#Explanation: Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
#Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
#
#Example 3:
#Input: s1 = "xx", s2 = "xy"
#Output: -1
#
#Constraints:
#    1 <= s1.length, s2.length <= 1000
#    s1.length == s2.length
#    s1, s2 only contain 'x' or 'y'.

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """
        Count mismatches:
        - xy: s1[i]='x', s2[i]='y'
        - yx: s1[i]='y', s2[i]='x'

        Two xy's can be fixed with 1 swap (swap s1[i] and s2[j])
        Two yx's can be fixed with 1 swap
        One xy and one yx need 2 swaps

        If (xy + yx) is odd, impossible.
        Answer = xy//2 + yx//2 + (1 if xy%2==1 else 0) * 2
        """
        xy = yx = 0

        for c1, c2 in zip(s1, s2):
            if c1 == 'x' and c2 == 'y':
                xy += 1
            elif c1 == 'y' and c2 == 'x':
                yx += 1

        # Total mismatches must be even
        if (xy + yx) % 2 == 1:
            return -1

        # Pair up same type mismatches (1 swap each)
        # Remaining one of each type needs 2 swaps
        return xy // 2 + yx // 2 + (xy % 2) * 2


class SolutionExplicit:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """More explicit reasoning"""
        xy = 0  # Positions where s1='x', s2='y'
        yx = 0  # Positions where s1='y', s2='x'

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    xy += 1
                else:
                    yx += 1

        # For valid transformation, total x's and y's must be even
        # (xy + yx must be even)
        if (xy + yx) % 2 == 1:
            return -1

        # Optimal strategy:
        # - Pair two xy mismatches: 1 swap fixes both
        # - Pair two yx mismatches: 1 swap fixes both
        # - One xy + one yx: need 2 swaps

        swaps = xy // 2 + yx // 2  # Handle pairs
        if xy % 2 == 1:  # One xy and one yx remaining
            swaps += 2

        return swaps
