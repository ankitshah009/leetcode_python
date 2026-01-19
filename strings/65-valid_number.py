#65. Valid Number
#Hard
#
#A valid number can be split up into these components (in order):
#    A decimal number or an integer.
#    (Optional) An 'e' or 'E', followed by an integer.
#
#A decimal number can be split up into these components (in order):
#    (Optional) A sign character (either '+' or '-').
#    One of the following formats:
#        One or more digits, followed by a dot '.'.
#        One or more digits, followed by a dot '.', followed by one or more digits.
#        A dot '.', followed by one or more digits.
#
#An integer can be split up into these components (in order):
#    (Optional) A sign character (either '+' or '-').
#    One or more digits.
#
#Example 1:
#Input: s = "0"
#Output: true
#
#Example 2:
#Input: s = "e"
#Output: false
#
#Example 3:
#Input: s = "."
#Output: false
#
#Constraints:
#    1 <= s.length <= 20
#    s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.

class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_e = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ['+', '-']:
                if i > 0 and s[i - 1].lower() != 'e':
                    return False
            elif char == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif char.lower() == 'e':
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False
            else:
                return False

        return seen_digit
