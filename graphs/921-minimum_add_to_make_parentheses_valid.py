#921. Minimum Add to Make Parentheses Valid
#Medium
#
#A parentheses string is valid if and only if:
#- It is the empty string,
#- It can be written as AB (A concatenated with B), where A and B are valid, or
#- It can be written as (A), where A is a valid string.
#
#Given a parentheses string s, return the minimum number of parentheses we must
#add to make the resulting string valid.
#
#Example 1:
#Input: s = "())"
#Output: 1
#
#Example 2:
#Input: s = "((("
#Output: 3
#
#Constraints:
#    1 <= s.length <= 1000
#    s[i] is either '(' or ')'.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Track unmatched open and close parentheses.
        """
        open_count = 0  # Unmatched '('
        close_needed = 0  # Unmatched ')' that need '('

        for c in s:
            if c == '(':
                open_count += 1
            else:  # ')'
                if open_count > 0:
                    open_count -= 1
                else:
                    close_needed += 1

        return open_count + close_needed


class SolutionStack:
    """Using stack"""

    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for c in s:
            if c == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)

        return len(stack)


class SolutionBalance:
    """Using balance concept"""

    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        insertions = 0

        for c in s:
            if c == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                insertions += 1
                balance = 0

        return insertions + balance
