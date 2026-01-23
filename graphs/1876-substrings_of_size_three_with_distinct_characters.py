#1876. Substrings of Size Three with Distinct Characters
#Easy
#
#A string is good if there are no repeated characters.
#
#Given a string s, return the number of good substrings of length three in s.
#
#Note that if there are multiple occurrences of the same substring, every
#occurrence should be counted.
#
#A substring is a contiguous sequence of characters in a string.
#
#Example 1:
#Input: s = "xyzzaz"
#Output: 1
#
#Example 2:
#Input: s = "aababcabc"
#Output: 4
#
#Constraints:
#    1 <= s.length <= 100
#    s consists of lowercase English letters.

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """
        Check each substring of length 3.
        """
        count = 0

        for i in range(len(s) - 2):
            substring = s[i:i+3]
            if len(set(substring)) == 3:
                count += 1

        return count


class SolutionDirect:
    def countGoodSubstrings(self, s: str) -> int:
        """
        Direct comparison without creating substring.
        """
        count = 0

        for i in range(len(s) - 2):
            if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:
                count += 1

        return count


class SolutionSlidingWindow:
    def countGoodSubstrings(self, s: str) -> int:
        """
        Sliding window with character count.
        """
        if len(s) < 3:
            return 0

        count = 0
        freq = {}

        # Initialize window
        for i in range(3):
            freq[s[i]] = freq.get(s[i], 0) + 1

        if len(freq) == 3:
            count += 1

        # Slide window
        for i in range(3, len(s)):
            # Add new character
            freq[s[i]] = freq.get(s[i], 0) + 1

            # Remove old character
            old = s[i - 3]
            freq[old] -= 1
            if freq[old] == 0:
                del freq[old]

            if len(freq) == 3:
                count += 1

        return count


class SolutionOneLiner:
    def countGoodSubstrings(self, s: str) -> int:
        """
        One-liner using sum and set.
        """
        return sum(len(set(s[i:i+3])) == 3 for i in range(len(s) - 2))
