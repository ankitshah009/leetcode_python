#678. Valid Parenthesis String
#Medium
#
#Given a string s containing only three types of characters: '(', ')' and '*', return true
#if s is valid.
#
#The following rules define a valid string:
#    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#    Any right parenthesis ')' must have a corresponding left parenthesis '('.
#    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '('
#        or an empty string "".
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
        # Track the possible range of open parentheses count
        min_open = 0  # Minimum possible open count
        max_open = 0  # Maximum possible open count

        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:  # char == '*'
                min_open -= 1  # * as )
                max_open += 1  # * as (

            # max_open < 0 means too many ) even treating all * as (
            if max_open < 0:
                return False

            # Keep min_open non-negative
            min_open = max(min_open, 0)

        return min_open == 0
