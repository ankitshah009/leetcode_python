#1881. Maximum Value after Insertion
#Medium
#
#You are given a very large integer n, represented as a string, and an integer
#digit x. The digits in n and the digit x are in the inclusive range [1, 9],
#and n may represent a negative number.
#
#You want to maximize n's numerical value by inserting x anywhere in the
#decimal representation of n. You cannot insert x to the left of the negative
#sign.
#
#Return a string representing the maximum value of n after the insertion.
#
#Example 1:
#Input: n = "99", x = 9
#Output: "999"
#
#Example 2:
#Input: n = "-13", x = 2
#Output: "-123"
#
#Constraints:
#    1 <= n.length <= 10^5
#    1 <= x <= 9
#    The digits in n are in the range [1, 9].
#    n is a valid representation of an integer.
#    In the case of a negative n, it will begin with '-'.

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        """
        For positive: insert x before first digit smaller than x.
        For negative: insert x before first digit larger than x.
        """
        x_str = str(x)

        if n[0] == '-':
            # Negative: want to minimize absolute value
            # Insert before first digit > x
            for i in range(1, len(n)):
                if n[i] > x_str:
                    return n[:i] + x_str + n[i:]
            return n + x_str
        else:
            # Positive: want to maximize value
            # Insert before first digit < x
            for i in range(len(n)):
                if n[i] < x_str:
                    return n[:i] + x_str + n[i:]
            return n + x_str


class SolutionExplicit:
    def maxValue(self, n: str, x: int) -> str:
        """
        Same logic with more explicit handling.
        """
        x_char = str(x)
        is_negative = n[0] == '-'

        if is_negative:
            # For negative, smaller absolute value is better
            # Find first position where digit > x
            for i in range(1, len(n)):
                if n[i] > x_char:
                    return n[:i] + x_char + n[i:]
        else:
            # For positive, larger value is better
            # Find first position where digit < x
            for i in range(len(n)):
                if n[i] < x_char:
                    return n[:i] + x_char + n[i:]

        # Append at end if no position found
        return n + x_char


class SolutionList:
    def maxValue(self, n: str, x: int) -> str:
        """
        Using list for insertion.
        """
        chars = list(n)
        x_char = str(x)
        negative = chars[0] == '-'

        start = 1 if negative else 0

        for i in range(start, len(chars)):
            if (not negative and chars[i] < x_char) or \
               (negative and chars[i] > x_char):
                chars.insert(i, x_char)
                return ''.join(chars)

        return n + x_char
