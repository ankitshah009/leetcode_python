#678. Valid Parenthesis String
#Medium
#
#Given a string s containing only three types of characters: '(', ')' and '*',
#return true if s is valid.
#
#The following rules define a valid string:
#- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#- Any right parenthesis ')' must have a corresponding left parenthesis '('.
#- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#- '*' could be treated as a single right parenthesis ')' or a single left
#  parenthesis '(' or an empty string "".
#
#Example 1:
#Input: s = "()"
#Output: true
#
#Example 2:
#Input: s = "(*)"
#Output: true
#
#Example 3:
#Input: s = "(*))"
#Output: true
#
#Constraints:
#    1 <= s.length <= 100
#    s[i] is '(', ')' or '*'.

class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Track range of possible open parentheses count.
        lo = minimum possible open count (treat * as ) or empty)
        hi = maximum possible open count (treat * as ()
        """
        lo = hi = 0

        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:  # '*'
                lo -= 1  # Treat as )
                hi += 1  # Treat as (

            # If hi < 0, too many ) even with all * as (
            if hi < 0:
                return False

            # lo can't go negative (we'd use * as empty instead)
            lo = max(lo, 0)

        return lo == 0


class SolutionTwoPass:
    """Two-pass approach: check from both directions"""

    def checkValidString(self, s: str) -> bool:
        # Left to right: treat * as (
        balance = 0
        for c in s:
            if c in '(*':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        # Right to left: treat * as )
        balance = 0
        for c in reversed(s):
            if c in ')*':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        return True


class SolutionDP:
    """Dynamic programming with memoization"""

    def checkValidString(self, s: str) -> bool:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, balance):
            if balance < 0:
                return False
            if i == len(s):
                return balance == 0

            c = s[i]
            if c == '(':
                return dp(i + 1, balance + 1)
            elif c == ')':
                return dp(i + 1, balance - 1)
            else:  # '*'
                return (dp(i + 1, balance + 1) or
                        dp(i + 1, balance - 1) or
                        dp(i + 1, balance))

        return dp(0, 0)


class SolutionStack:
    """Stack-based approach tracking indices"""

    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []

        for i, c in enumerate(s):
            if c == '(':
                open_stack.append(i)
            elif c == '*':
                star_stack.append(i)
            else:  # ')'
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        # Match remaining ( with *
        while open_stack and star_stack:
            if open_stack[-1] > star_stack[-1]:
                return False  # ( appears after *
            open_stack.pop()
            star_stack.pop()

        return len(open_stack) == 0
