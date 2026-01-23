#1071. Greatest Common Divisor of Strings
#Easy
#
#For two strings s and t, we say "t divides s" if and only if
#s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or
#more times).
#
#Given two strings str1 and str2, return the largest string x such that x
#divides both str1 and str2.
#
#Example 1:
#Input: str1 = "ABCABC", str2 = "ABC"
#Output: "ABC"
#
#Example 2:
#Input: str1 = "ABABAB", str2 = "ABAB"
#Output: "AB"
#
#Example 3:
#Input: str1 = "LEET", str2 = "CODE"
#Output: ""
#
#Constraints:
#    1 <= str1.length, str2.length <= 1000
#    str1 and str2 consist of English uppercase letters.

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        If str1 + str2 == str2 + str1, then GCD exists.
        Length of GCD = gcd(len(str1), len(str2))
        """
        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]


class SolutionIterative:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Try all possible divisor lengths (divisors of both lengths).
        """
        def divides(s, t):
            """Check if t divides s"""
            if len(s) % len(t) != 0:
                return False
            return s == t * (len(s) // len(t))

        for length in range(min(len(str1), len(str2)), 0, -1):
            if len(str1) % length == 0 and len(str2) % length == 0:
                candidate = str1[:length]
                if divides(str1, candidate) and divides(str2, candidate):
                    return candidate

        return ""


class SolutionRecursive:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """Euclidean algorithm style"""
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        if not str2:
            return str1

        if not str1.startswith(str2):
            return ""

        return self.gcdOfStrings(str1[len(str2):], str2)
