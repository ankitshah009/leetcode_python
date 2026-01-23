#65. Valid Number
#Hard
#
#Given a string s, return whether s is a valid number.
#
#A valid number can be split up into these components (in order):
#1. A decimal number or an integer.
#2. (Optional) An 'e' or 'E', followed by an integer.
#
#A decimal number can be split up into these components (in order):
#1. (Optional) A sign character (either '+' or '-').
#2. One of the following formats:
#   a. One or more digits, followed by a dot '.'.
#   b. One or more digits, followed by a dot '.', followed by one or more digits.
#   c. A dot '.', followed by one or more digits.
#
#An integer can be split up into these components (in order):
#1. (Optional) A sign character (either '+' or '-').
#2. One or more digits.
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
#    s consists of only English letters, digits, '+', '-', '.', and ' '.

class Solution:
    def isNumber(self, s: str) -> bool:
        """
        Finite State Machine approach.
        """
        # States: 0=start, 1=sign, 2=digit, 3=dot, 4=digit_after_dot,
        #         5=e, 6=sign_after_e, 7=digit_after_e
        transitions = {
            0: {'sign': 1, 'digit': 2, 'dot': 3},
            1: {'digit': 2, 'dot': 3},
            2: {'digit': 2, 'dot': 4, 'e': 5},
            3: {'digit': 4},
            4: {'digit': 4, 'e': 5},
            5: {'sign': 6, 'digit': 7},
            6: {'digit': 7},
            7: {'digit': 7}
        }

        valid_end_states = {2, 4, 7}
        state = 0

        for char in s:
            if char.isdigit():
                token = 'digit'
            elif char in ['+', '-']:
                token = 'sign'
            elif char in ['e', 'E']:
                token = 'e'
            elif char == '.':
                token = 'dot'
            else:
                return False

            if token not in transitions.get(state, {}):
                return False

            state = transitions[state][token]

        return state in valid_end_states


class SolutionRegex:
    def isNumber(self, s: str) -> bool:
        """
        Regular expression approach.
        """
        import re
        pattern = r'^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$'
        return bool(re.match(pattern, s))


class SolutionManual:
    def isNumber(self, s: str) -> bool:
        """
        Manual parsing approach.
        """
        s = s.strip()
        if not s:
            return False

        # Split by e/E
        parts = s.lower().split('e')
        if len(parts) > 2:
            return False

        # Validate decimal/integer part
        def is_decimal_or_integer(s: str, allow_dot: bool) -> bool:
            if not s:
                return False

            i = 0
            if s[0] in ['+', '-']:
                i = 1

            if i >= len(s):
                return False

            has_digit = False
            has_dot = False

            while i < len(s):
                if s[i].isdigit():
                    has_digit = True
                elif s[i] == '.' and allow_dot and not has_dot:
                    has_dot = True
                else:
                    return False
                i += 1

            return has_digit

        # Validate integer part
        def is_integer(s: str) -> bool:
            return is_decimal_or_integer(s, False)

        if len(parts) == 1:
            return is_decimal_or_integer(parts[0], True)
        else:
            return is_decimal_or_integer(parts[0], True) and is_integer(parts[1])


class SolutionTryExcept:
    def isNumber(self, s: str) -> bool:
        """
        Using Python's float conversion (not recommended in interviews).
        """
        try:
            float(s)
            return True
        except ValueError:
            return False
