#1763. Longest Nice Substring
#Easy
#
#A string s is nice if, for every letter of the alphabet that s contains, it
#appears both in uppercase and lowercase. For example, "abABB" is nice because
#'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b'
#appears, but 'B' does not.
#
#Given a string s, return the longest substring of s that is nice. If there are
#multiple, return the substring of the earliest occurrence. If there are none,
#return an empty string.
#
#Example 1:
#Input: s = "YazaAay"
#Output: "aAa"
#
#Example 2:
#Input: s = "Bb"
#Output: "Bb"
#
#Example 3:
#Input: s = "c"
#Output: ""
#
#Constraints:
#    1 <= s.length <= 100
#    s consists of uppercase and lowercase English letters.

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        """
        Divide and conquer: split at characters that can't be nice.
        """
        if len(s) < 2:
            return ""

        char_set = set(s)

        # Find a character that doesn't have its pair
        for i, c in enumerate(s):
            if c.swapcase() not in char_set:
                # Split here and recurse
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                return left if len(left) >= len(right) else right

        # All characters have pairs - entire string is nice
        return s


class SolutionBruteForce:
    def longestNiceSubstring(self, s: str) -> str:
        """
        Check all substrings.
        """
        def is_nice(substr: str) -> bool:
            chars = set(substr)
            for c in chars:
                if c.swapcase() not in chars:
                    return False
            return True

        n = len(s)
        result = ""

        for i in range(n):
            for j in range(i + 2, n + 1):
                substr = s[i:j]
                if len(substr) > len(result) and is_nice(substr):
                    result = substr

        return result


class SolutionBitMask:
    def longestNiceSubstring(self, s: str) -> str:
        """
        Using bitmasks for character presence.
        """
        n = len(s)
        result = ""

        for i in range(n):
            lower_mask = 0
            upper_mask = 0

            for j in range(i, n):
                c = s[j]
                if c.islower():
                    lower_mask |= (1 << (ord(c) - ord('a')))
                else:
                    upper_mask |= (1 << (ord(c) - ord('A')))

                # Nice if lower and upper masks match
                if lower_mask == upper_mask and j - i + 1 > len(result):
                    result = s[i:j + 1]

        return result
