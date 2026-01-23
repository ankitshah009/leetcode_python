#1221. Split a String in Balanced Strings
#Easy
#
#Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
#
#Given a balanced string s, split it into some number of substrings such that:
#    Each substring is balanced.
#
#Return the maximum number of balanced strings you can obtain.
#
#Example 1:
#Input: s = "RLRRLLRLRL"
#Output: 4
#Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring
#contains same number of 'L' and 'R'.
#
#Example 2:
#Input: s = "RLRRRLLRLL"
#Output: 2
#Explanation: s can be split into "RL", "RRRLLRLL".
#
#Example 3:
#Input: s = "LLLLRRRR"
#Output: 1
#Explanation: s can be split into "LLLLRRRR".
#
#Constraints:
#    2 <= s.length <= 1000
#    s[i] is either 'L' or 'R'.
#    s is a balanced string.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        Greedy: Count balance as we go.
        Each time balance reaches 0, we have a balanced substring.
        """
        balance = 0
        count = 0

        for c in s:
            if c == 'L':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                count += 1

        return count


class SolutionExplicit:
    def balancedStringSplit(self, s: str) -> int:
        """More explicit counting"""
        l_count = r_count = 0
        result = 0

        for c in s:
            if c == 'L':
                l_count += 1
            else:
                r_count += 1

            if l_count == r_count:
                result += 1

        return result
