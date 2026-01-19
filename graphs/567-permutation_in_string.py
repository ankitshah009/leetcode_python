#567. Permutation in String
#Medium
#
#Given two strings s1 and s2, return true if s2 contains a permutation of s1,
#or false otherwise.
#
#In other words, return true if one of s1's permutations is the substring of s2.
#
#Example 1:
#Input: s1 = "ab", s2 = "eidbaooo"
#Output: true
#Explanation: s2 contains one permutation of s1 ("ba").
#
#Example 2:
#Input: s1 = "ab", s2 = "eidboaoo"
#Output: false
#
#Constraints:
#    1 <= s1.length, s2.length <= 10^4
#    s1 and s2 consist of lowercase English letters.

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Sliding window with character count comparison"""
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if window_count == s1_count:
            return True

        for i in range(len(s1), len(s2)):
            # Add new character
            window_count[s2[i]] += 1

            # Remove old character
            old_char = s2[i - len(s1)]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]

            if window_count == s1_count:
                return True

        return False


class SolutionMatches:
    """Track number of matching character frequencies"""

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        matches = 0

        for i in range(len(s2)):
            idx = ord(s2[i]) - ord('a')
            s2_count[idx] += 1

            if s2_count[idx] == s1_count[idx]:
                matches += 1
            elif s2_count[idx] == s1_count[idx] + 1:
                matches -= 1

            if i >= len(s1):
                old_idx = ord(s2[i - len(s1)]) - ord('a')
                if s2_count[old_idx] == s1_count[old_idx]:
                    matches += 1
                elif s2_count[old_idx] == s1_count[old_idx] + 1:
                    matches -= 1
                s2_count[old_idx] -= 1

            if matches == 26:
                return True

        return False


class SolutionArray:
    """Using array comparison"""

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        for i in range(len(s2)):
            s2_count[ord(s2[i]) - ord('a')] += 1

            if i >= len(s1):
                s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1_count == s2_count:
                return True

        return False
