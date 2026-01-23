#1694. Reformat Phone Number
#Easy
#
#You are given a phone number as a string number. number consists of digits,
#spaces ' ', and/or dashes '-'.
#
#You would like to reformat the phone number in a certain manner. Firstly,
#remove all spaces and dashes. Then, group the digits from left to right into
#blocks of length 3 until there are 4 or fewer digits. The final digits are
#then grouped as follows:
#- 2 digits: A single block of length 2.
#- 3 digits: A single block of length 3.
#- 4 digits: Two blocks of length 2 each.
#
#The blocks are then joined by dashes.
#
#Example 1:
#Input: number = "1-23-45 6"
#Output: "123-456"
#
#Example 2:
#Input: number = "123 4-567"
#Output: "123-45-67"
#
#Example 3:
#Input: number = "123 4-5678"
#Output: "123-456-78"
#
#Constraints:
#    2 <= number.length <= 100
#    number consists of digits and the characters '-' and ' '.
#    There are at least two digits in number.

class Solution:
    def reformatNumber(self, number: str) -> str:
        """
        Remove non-digits, then format according to rules.
        """
        # Extract digits
        digits = ''.join(c for c in number if c.isdigit())

        result = []
        i = 0
        n = len(digits)

        while n - i > 4:
            result.append(digits[i:i+3])
            i += 3

        # Handle remaining digits
        remaining = n - i
        if remaining == 4:
            result.append(digits[i:i+2])
            result.append(digits[i+2:i+4])
        else:  # 2 or 3
            result.append(digits[i:])

        return '-'.join(result)


class SolutionRegex:
    def reformatNumber(self, number: str) -> str:
        """
        Using regex for digit extraction.
        """
        import re

        digits = re.sub(r'\D', '', number)
        parts = []
        i = 0
        n = len(digits)

        while n - i > 4:
            parts.append(digits[i:i+3])
            i += 3

        if n - i == 4:
            parts.extend([digits[i:i+2], digits[i+2:]])
        else:
            parts.append(digits[i:])

        return '-'.join(parts)


class SolutionList:
    def reformatNumber(self, number: str) -> str:
        """
        Building result list step by step.
        """
        digits = [c for c in number if c.isdigit()]
        n = len(digits)
        result = []

        idx = 0
        while idx < n:
            remaining = n - idx

            if remaining > 4:
                result.append(''.join(digits[idx:idx+3]))
                idx += 3
            elif remaining == 4:
                result.append(''.join(digits[idx:idx+2]))
                result.append(''.join(digits[idx+2:idx+4]))
                idx += 4
            else:
                result.append(''.join(digits[idx:]))
                break

        return '-'.join(result)


class SolutionCompact:
    def reformatNumber(self, number: str) -> str:
        """
        Compact solution.
        """
        d = ''.join(filter(str.isdigit, number))
        n, res, i = len(d), [], 0

        while n - i > 4:
            res.append(d[i:i+3])
            i += 3

        rem = n - i
        if rem == 4:
            res += [d[i:i+2], d[i+2:]]
        else:
            res.append(d[i:])

        return '-'.join(res)


class SolutionIterative:
    def reformatNumber(self, number: str) -> str:
        """
        Simple iterative approach.
        """
        digits = number.replace(' ', '').replace('-', '')
        parts = []

        while len(digits) > 4:
            parts.append(digits[:3])
            digits = digits[3:]

        if len(digits) == 4:
            parts.append(digits[:2])
            parts.append(digits[2:])
        else:
            parts.append(digits)

        return '-'.join(parts)
