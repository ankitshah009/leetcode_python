#1941. Check if All Characters Have Equal Number of Occurrences
#Easy
#
#Given a string s, return true if s is a good string, or false otherwise.
#
#A string s is good if all the characters that appear in s have the same number
#of occurrences (i.e., the same frequency).
#
#Example 1:
#Input: s = "abacbc"
#Output: true
#
#Example 2:
#Input: s = "aaabb"
#Output: false
#
#Constraints:
#    1 <= s.length <= 1000
#    s consists of lowercase English letters.

from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        """
        Check if all frequencies are equal.
        """
        freq = Counter(s)
        return len(set(freq.values())) == 1


class SolutionExplicit:
    def areOccurrencesEqual(self, s: str) -> bool:
        """
        Explicit comparison.
        """
        freq = Counter(s)
        counts = list(freq.values())
        return all(c == counts[0] for c in counts)


class SolutionManual:
    def areOccurrencesEqual(self, s: str) -> bool:
        """
        Manual frequency counting.
        """
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        values = list(freq.values())
        return min(values) == max(values)
