#8. String to Integer (atoi)
#Medium
#
#Implement the myAtoi(string s) function, which converts a string to a 32-bit
#signed integer.
#
#The algorithm for myAtoi(string s) is as follows:
#1. Whitespace: Ignore any leading whitespace (" ").
#2. Signedness: Determine the sign by checking if the next character is '-' or
#   '+', assuming positivity if neither present.
#3. Conversion: Read the integer by skipping leading zeros until a non-digit
#   character is encountered or the end of the string is reached.
#4. Rounding: If the integer is out of the 32-bit signed integer range
#   [-2^31, 2^31 - 1], then round the integer to remain in the range.
#
#Example 1:
#Input: s = "42"
#Output: 42
#
#Example 2:
#Input: s = " -042"
#Output: -42
#
#Example 3:
#Input: s = "1337c0d3"
#Output: 1337
#
#Example 4:
#Input: s = "0-1"
#Output: 0
#
#Example 5:
#Input: s = "words and 987"
#Output: 0
#
#Constraints:
#    0 <= s.length <= 200
#    s consists of English letters, digits, ' ', '+', '-', and '.'.

class Solution:
    def myAtoi(self, s: str) -> int:
        """
        State machine approach following the algorithm description.
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        s = s.lstrip()  # Remove leading whitespace

        if not s:
            return 0

        # Handle sign
        sign = 1
        index = 0

        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            index = 1

        # Convert digits
        result = 0

        while index < len(s) and s[index].isdigit():
            digit = int(s[index])

            # Check overflow before adding digit
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            index += 1

        return sign * result


class SolutionStateMachine:
    def myAtoi(self, s: str) -> int:
        """
        Explicit finite state machine.
        States: start, signed, number, end
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        state = 'start'
        sign = 1
        result = 0

        for char in s:
            if state == 'start':
                if char == ' ':
                    continue
                elif char == '+':
                    state = 'signed'
                elif char == '-':
                    state = 'signed'
                    sign = -1
                elif char.isdigit():
                    state = 'number'
                    result = int(char)
                else:
                    break
            elif state == 'signed':
                if char.isdigit():
                    state = 'number'
                    result = int(char)
                else:
                    break
            elif state == 'number':
                if char.isdigit():
                    result = result * 10 + int(char)
                    # Early termination on overflow
                    if sign * result <= INT_MIN:
                        return INT_MIN
                    if sign * result >= INT_MAX:
                        return INT_MAX
                else:
                    break

        result = sign * result
        return max(INT_MIN, min(INT_MAX, result))


class SolutionRegex:
    def myAtoi(self, s: str) -> int:
        """
        Using regular expression.
        """
        import re

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        match = re.match(r'^\s*([+-]?\d+)', s)

        if not match:
            return 0

        result = int(match.group(1))
        return max(INT_MIN, min(INT_MAX, result))
