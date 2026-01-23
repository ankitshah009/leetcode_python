#1111. Maximum Nesting Depth of Two Valid Parentheses Strings
#Medium
#
#A string is a valid parentheses string (denoted VPS) if and only if it
#consists of "(" and ")" characters only, and:
#    It is the empty string, or
#    It can be written as AB (A concatenated with B), where A and B are VPS's, or
#    It can be written as (A), where A is a VPS.
#
#We can similarly define the nesting depth depth(S) of any VPS S as follows:
#    depth("") = 0
#    depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
#    depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
#
#For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0,
#1, and 2), and ")(" and "(()" are not VPS's.
#
#Given a VPS seq, split it into two disjoint subsequences A and B, such that
#A and B are VPS's (and A.length + B.length = seq.length).
#
#Now choose any such A and B such that max(depth(A), depth(B)) is the minimum
#possible value.
#
#Return an answer array (of length seq.length) that encodes such a choice
#of A and B: answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.
#
#Example 1:
#Input: seq = "(()())"
#Output: [0,1,1,1,1,0]
#
#Example 2:
#Input: seq = "()(())()"
#Output: [0,0,0,1,1,0,1,1]
#
#Constraints:
#    1 <= seq.size <= 10^4
#    seq is a valid parentheses string.

from typing import List

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        """
        Distribute parentheses at odd depths to one group,
        even depths to the other. This balances the max depth.
        """
        result = []
        depth = 0

        for c in seq:
            if c == '(':
                depth += 1
                result.append(depth % 2)
            else:
                result.append(depth % 2)
                depth -= 1

        return result


class SolutionAlternate:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        """
        Alternate open parentheses between groups.
        """
        result = []
        count = [0, 0]  # Depth of each group

        for c in seq:
            if c == '(':
                # Add to group with smaller depth
                group = 0 if count[0] <= count[1] else 1
                count[group] += 1
                result.append(group)
            else:
                # Remove from group with larger depth
                group = 0 if count[0] > count[1] else 1
                count[group] -= 1
                result.append(group)

        return result


class SolutionSimple:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        """Based on index parity"""
        return [i & 1 if c == '(' else (i + 1) & 1 for i, c in enumerate(seq)]
