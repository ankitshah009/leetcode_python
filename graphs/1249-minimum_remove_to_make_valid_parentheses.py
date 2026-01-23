#1249. Minimum Remove to Make Valid Parentheses
#Medium
#
#Given a string s of '(' , ')' and lowercase English characters.
#
#Your task is to remove the minimum number of parentheses ( '(' or ')' , in any
#positions ) so that the resulting parentheses string is valid and return any
#valid string.
#
#Formally, a parentheses string is valid if and only if:
#    It is the empty string, contains only lowercase characters, or
#    It can be written as AB (A concatenated with B), where A and B are valid
#    strings, or
#    It can be written as (A), where A is a valid string.
#
#Example 1:
#Input: s = "lee(t(c)o)de)"
#Output: "lee(t(c)o)de"
#Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#
#Example 2:
#Input: s = "a)b(c)d"
#Output: "ab(c)d"
#
#Example 3:
#Input: s = "))(("
#Output: ""
#Explanation: An empty string is also valid.
#
#Constraints:
#    1 <= s.length <= 10^5
#    s[i] is either '(' , ')', or lowercase English letter.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Two passes:
        1. Left to right: mark unmatched ')'
        2. Right to left: mark unmatched '('
        """
        # First pass: find indices of unmatched ')'
        to_remove = set()
        open_count = 0

        for i, c in enumerate(s):
            if c == '(':
                open_count += 1
            elif c == ')':
                if open_count > 0:
                    open_count -= 1
                else:
                    to_remove.add(i)

        # Second pass: find indices of unmatched '('
        close_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                close_count += 1
            elif s[i] == '(':
                if close_count > 0:
                    close_count -= 1
                else:
                    to_remove.add(i)

        return ''.join(c for i, c in enumerate(s) if i not in to_remove)


class SolutionStack:
    def minRemoveToMakeValid(self, s: str) -> str:
        """Using stack to track indices"""
        stack = []  # Stack of indices of unmatched '('
        to_remove = set()

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        # Remaining '(' in stack are unmatched
        to_remove.update(stack)

        return ''.join(c for i, c in enumerate(s) if i not in to_remove)


class SolutionTwoPasses:
    def minRemoveToMakeValid(self, s: str) -> str:
        """Two string passes"""
        def process(s, open_char, close_char):
            result = []
            balance = 0
            for c in s:
                if c == open_char:
                    balance += 1
                    result.append(c)
                elif c == close_char:
                    if balance > 0:
                        balance -= 1
                        result.append(c)
                else:
                    result.append(c)
            return result

        # Remove invalid ')'
        after_first = process(s, '(', ')')
        # Remove invalid '(' (process reversed)
        after_second = process(after_first[::-1], ')', '(')

        return ''.join(after_second[::-1])
