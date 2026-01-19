#567. Permutation in String
#Medium
#
#Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
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
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])

        if s1_count == s2_count:
            return True

        for i in range(len(s1), len(s2)):
            # Add new character
            s2_count[s2[i]] += 1

            # Remove old character
            old_char = s2[i - len(s1)]
            s2_count[old_char] -= 1
            if s2_count[old_char] == 0:
                del s2_count[old_char]

            if s1_count == s2_count:
                return True

        return False
