#224. Basic Calculator
#Hard
#
#Given a string s representing a valid expression, implement a basic calculator
#to evaluate it, and return the result of the evaluation.
#
#Example 1:
#Input: s = "1 + 1"
#Output: 2
#
#Example 2:
#Input: s = " 2-1 + 2 "
#Output: 3
#
#Example 3:
#Input: s = "(1+(4+5+2)-3)+(6+8)"
#Output: 23
#
#Constraints:
#    1 <= s.length <= 3 * 10^5
#    s consists of digits, '+', '-', '(', ')', and ' '.
#    s represents a valid expression.
#    '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
#    '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
#    There will be no two consecutive operators in the input.
#    Every number and running calculation will fit in a signed 32-bit integer.

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':
                # Push current result and sign onto stack
                stack.append(result)
                stack.append(sign)
                # Reset for new expression
                result = 0
                sign = 1
            elif char == ')':
                result += sign * num
                num = 0
                # Pop sign and previous result
                result *= stack.pop()  # Sign before parenthesis
                result += stack.pop()  # Previous result

        # Don't forget the last number
        result += sign * num

        return result

    # Recursive approach
    def calculateRecursive(self, s: str) -> int:
        self.idx = 0

        def helper():
            result = 0
            num = 0
            sign = 1

            while self.idx < len(s):
                char = s[self.idx]
                self.idx += 1

                if char.isdigit():
                    num = num * 10 + int(char)
                elif char == '+':
                    result += sign * num
                    num = 0
                    sign = 1
                elif char == '-':
                    result += sign * num
                    num = 0
                    sign = -1
                elif char == '(':
                    num = helper()
                elif char == ')':
                    break

            result += sign * num
            return result

        return helper()
