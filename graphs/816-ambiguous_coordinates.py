#816. Ambiguous Coordinates
#Medium
#
#We had some 2-dimensional coordinates, like "(1, 3)" or "(2.5, 4)", Then we
#removed all commas, decimal points, and spaces and ended up with the string s.
#
#Return a list of strings representing all possibilities for what our original
#coordinates could have been.
#
#Our original representation never had extraneous zeroes, so we never started
#with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other
#number that can be represented with fewer digits. Also, a decimal point within
#a number never occurs without at least one digit occurring before it, so we
#never started with numbers like ".1".
#
#The final answer list can be returned in any order. All coordinates in the
#final answer have exactly one space between them.
#
#Example 1:
#Input: s = "(123)"
#Output: ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]
#
#Example 2:
#Input: s = "(0123)"
#Output: ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]
#
#Example 3:
#Input: s = "(00011)"
#Output: ["(0, 0.011)","(0.001, 1)"]
#
#Constraints:
#    4 <= s.length <= 12
#    s[0] == '(' and s[s.length - 1] == ')'.
#    The rest of s are digits.

class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        """
        Generate all valid numbers from a digit string.
        A valid number:
        - No leading zeros (unless it's "0" or "0.xxx")
        - No trailing zeros after decimal
        """
        def valid_numbers(digits):
            """Generate all valid numbers from digits"""
            n = len(digits)
            if n == 0:
                return []

            result = []

            # No decimal point
            if n == 1 or digits[0] != '0':
                result.append(digits)

            # With decimal point at position i (i.e., digits[:i].digits[i:])
            for i in range(1, n):
                left = digits[:i]
                right = digits[i:]

                # Check for leading zero in integer part
                if len(left) > 1 and left[0] == '0':
                    continue

                # Check for trailing zero in decimal part
                if right[-1] == '0':
                    continue

                result.append(left + '.' + right)

            return result

        # Remove parentheses
        s = s[1:-1]
        result = []

        # Try all splits into (x, y)
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]

            left_nums = valid_numbers(left)
            right_nums = valid_numbers(right)

            for x in left_nums:
                for y in right_nums:
                    result.append(f"({x}, {y})")

        return result


class SolutionGenerator:
    """Using generators"""

    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(digits):
            n = len(digits)
            for i in range(1, n + 1):
                left, right = digits[:i], digits[i:]
                if (not left.startswith('00') and
                    (left == '0' or not left.startswith('0')) and
                    not right.endswith('0')):
                    yield left + ('.' if right else '') + right

        s = s[1:-1]
        return [
            f"({x}, {y})"
            for i in range(1, len(s))
            for x in make(s[:i])
            for y in make(s[i:])
        ]
