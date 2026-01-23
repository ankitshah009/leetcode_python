#1309. Decrypt String from Alphabet to Integer Mapping
#Easy
#
#You are given a string s formed by digits and '#'. We want to map s to English
#lowercase characters as follows:
#    Characters ('a' to 'i') are represented by ('1' to '9') respectively.
#    Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
#
#Return the string formed after mapping.
#
#The test cases are generated so that a unique mapping will always exist.
#
#Example 1:
#Input: s = "10#11#12"
#Output: "jkab"
#Explanation: "10#" -> "j", "11#" -> "k", "1" -> "a", "2" -> "b".
#
#Example 2:
#Input: s = "1326#"
#Output: "acz"
#
#Constraints:
#    1 <= s.length <= 1000
#    s consists of digits and the '#' letter.
#    s will be a valid string such that mapping is always possible.

class Solution:
    def freqAlphabets(self, s: str) -> str:
        """
        Process from right to left.
        If we see '#', take previous 2 digits.
        """
        result = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == '#':
                # Two digit number
                num = int(s[i-2:i])
                result.append(chr(ord('a') + num - 1))
                i -= 3
            else:
                # Single digit
                num = int(s[i])
                result.append(chr(ord('a') + num - 1))
                i -= 1

        return ''.join(reversed(result))


class SolutionForward:
    def freqAlphabets(self, s: str) -> str:
        """Process from left to right, look ahead for '#'"""
        result = []
        i = 0
        n = len(s)

        while i < n:
            # Check if this is a two-digit number (look ahead for '#')
            if i + 2 < n and s[i + 2] == '#':
                num = int(s[i:i+2])
                result.append(chr(ord('a') + num - 1))
                i += 3
            else:
                num = int(s[i])
                result.append(chr(ord('a') + num - 1))
                i += 1

        return ''.join(result)


class SolutionRegex:
    def freqAlphabets(self, s: str) -> str:
        """Using regex to find patterns"""
        import re

        def decode(match):
            code = match.group()
            if code.endswith('#'):
                num = int(code[:-1])
            else:
                num = int(code)
            return chr(ord('a') + num - 1)

        # Match two digits followed by # or single digit
        return re.sub(r'\d{2}#|\d', decode, s)
