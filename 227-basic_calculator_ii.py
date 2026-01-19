#227. Basic Calculator II
#Medium
#
#Given a string s which represents an expression, calculate this expression and return its value.
#
#The integer division should truncate toward zero.
#
#You may assume that the given expression is always valid. All intermediate results will be
#in the range of [-2^31, 2^31 - 1].
#
#Note: You are not allowed to use any built-in function which evaluates strings as mathematical
#expressions.
#
#Example 1:
#Input: s = "3+2*2"
#Output: 7
#
#Example 2:
#Input: s = " 3/2 "
#Output: 1
#
#Example 3:
#Input: s = " 3+5 / 2 "
#Output: 5
#
#Constraints:
#    1 <= s.length <= 3 * 10^5
#    s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
#    s represents a valid expression.
#    All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
#    The answer is guaranteed to fit in a 32-bit integer.

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))

                sign = char
                num = 0

        return sum(stack)
