#1556. Thousand Separator
#Easy
#
#Given an integer n, add a dot (".") as the thousands separator and return it
#in string format.
#
#Example 1:
#Input: n = 987
#Output: "987"
#
#Example 2:
#Input: n = 1234
#Output: "1.234"
#
#Example 3:
#Input: n = 123456789
#Output: "123.456.789"
#
#Constraints:
#    0 <= n <= 2^31 - 1

class Solution:
    def thousandSeparator(self, n: int) -> str:
        """
        Build result from right to left, inserting dots every 3 digits.
        """
        s = str(n)
        result = []

        for i, char in enumerate(reversed(s)):
            if i > 0 and i % 3 == 0:
                result.append('.')
            result.append(char)

        return ''.join(reversed(result))


class SolutionSlicing:
    def thousandSeparator(self, n: int) -> str:
        """
        Using string slicing.
        """
        s = str(n)
        parts = []

        while len(s) > 3:
            parts.append(s[-3:])
            s = s[:-3]

        parts.append(s)

        return '.'.join(reversed(parts))


class SolutionFormat:
    def thousandSeparator(self, n: int) -> str:
        """
        Using Python's format with custom separator.
        """
        # Python's format uses comma by default
        formatted = f'{n:,}'
        # Replace comma with dot
        return formatted.replace(',', '.')


class SolutionLocale:
    def thousandSeparator(self, n: int) -> str:
        """
        Using locale (for systems with dot as separator).
        """
        import locale
        # This is system-dependent, so we use format as fallback
        return f'{n:,}'.replace(',', '.')


class SolutionRecursive:
    def thousandSeparator(self, n: int) -> str:
        """
        Recursive approach.
        """
        s = str(n)
        if len(s) <= 3:
            return s

        return self.thousandSeparator(int(s[:-3])) + '.' + s[-3:]


class SolutionRegex:
    def thousandSeparator(self, n: int) -> str:
        """
        Using regex for insertion.
        """
        import re

        s = str(n)
        # Insert dot before every group of 3 digits from the right
        # Lookahead to find positions
        return re.sub(r'(?=(?:\d{3})+$)(?!^)', '.', s)


class SolutionManual:
    def thousandSeparator(self, n: int) -> str:
        """
        Manual character-by-character construction.
        """
        if n == 0:
            return "0"

        s = str(n)
        length = len(s)
        result = []

        for i, digit in enumerate(s):
            result.append(digit)
            # Add dot after this digit if:
            # - Not the last digit
            # - Remaining digits form groups of 3
            remaining = length - i - 1
            if remaining > 0 and remaining % 3 == 0:
                result.append('.')

        return ''.join(result)
