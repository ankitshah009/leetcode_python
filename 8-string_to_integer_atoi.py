#8. String to Integer (atoi)
#Medium
#
#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
#
#The algorithm for myAtoi(string s) is as follows:
#1. Whitespace: Ignore any leading whitespace (" ").
#2. Signedness: Determine the sign by checking if the next character is '-' or '+'.
#3. Conversion: Read the integer by skipping leading zeros until a non-digit character
#   is encountered or the end of the string is reached.
#4. Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1],
#   then round the integer to remain in the range.
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
#    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        index = 0
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            index = 1

        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        result *= sign

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
