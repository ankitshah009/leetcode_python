#761. Special Binary String
#Hard
#
#Special binary strings are binary strings with the following two properties:
#- The number of 0's is equal to the number of 1's.
#- Every prefix of the binary string has at least as many 1's as 0's.
#
#You are given a special binary string s.
#
#A move consists of choosing two consecutive, non-empty, special substrings of
#s, and swapping them. Two strings are consecutive if the last character of the
#first string is exactly one index before the first character of the second
#string.
#
#Return the lexicographically largest resulting string possible after applying
#the mentioned operations on the string.
#
#Example 1:
#Input: s = "11011000"
#Output: "11100100"
#Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are
#swapped. This is the lexicographically largest string possible after some
#number of swaps.
#
#Example 2:
#Input: s = "10"
#Output: "10"
#
#Constraints:
#    1 <= s.length <= 50
#    s[i] is either '0' or '1'.
#    s is a special binary string.

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        """
        Recursively find special substrings, sort them in descending order.
        Special strings are like balanced parentheses (1 = '(', 0 = ')').
        """
        if len(s) <= 2:
            return s

        specials = []
        count = 0
        start = 0

        for i, c in enumerate(s):
            count += 1 if c == '1' else -1

            if count == 0:
                # Found a special substring from start to i
                # Recursively process the inside (excluding outer 1 and 0)
                inner = self.makeLargestSpecial(s[start + 1:i])
                specials.append('1' + inner + '0')
                start = i + 1

        # Sort in descending order and concatenate
        specials.sort(reverse=True)
        return ''.join(specials)


class SolutionIterative:
    """Iterative approach"""

    def makeLargestSpecial(self, s: str) -> str:
        def process(s):
            if len(s) <= 2:
                return s

            specials = []
            count = 0
            start = 0

            for i in range(len(s)):
                count += 1 if s[i] == '1' else -1
                if count == 0:
                    inner = process(s[start + 1:i])
                    specials.append('1' + inner + '0')
                    start = i + 1

            specials.sort(reverse=True)
            return ''.join(specials)

        return process(s)
