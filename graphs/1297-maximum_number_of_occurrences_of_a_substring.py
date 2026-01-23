#1297. Maximum Number of Occurrences of a Substring
#Medium
#
#Given a string s, return the maximum number of occurrences of any substring
#under the following rules:
#    The number of unique characters in the substring must be less than or
#    equal to maxLetters.
#    The substring size must be between minSize and maxSize inclusive.
#
#Example 1:
#Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
#Output: 2
#Explanation: Substring "aab" has 2 occurrences in the original string.
#It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
#
#Example 2:
#Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
#Output: 2
#Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
#
#Constraints:
#    1 <= s.length <= 10^5
#    1 <= maxLetters <= 26
#    1 <= minSize <= maxSize <= min(26, s.length)
#    s consists of only lowercase English letters.

from collections import Counter, defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """
        Key insight: Only check minSize substrings.
        If a larger substring appears k times, its minSize prefix also appears k times.
        """
        count = defaultdict(int)
        n = len(s)

        for i in range(n - minSize + 1):
            sub = s[i:i + minSize]
            if len(set(sub)) <= maxLetters:
                count[sub] += 1

        return max(count.values()) if count else 0


class SolutionSlidingWindow:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """Sliding window with character count"""
        n = len(s)
        if n < minSize:
            return 0

        count = defaultdict(int)
        char_count = Counter(s[:minSize])

        # Check first window
        if len(char_count) <= maxLetters:
            count[s[:minSize]] += 1

        # Slide window
        for i in range(minSize, n):
            # Add new char
            char_count[s[i]] += 1
            # Remove old char
            old_char = s[i - minSize]
            char_count[old_char] -= 1
            if char_count[old_char] == 0:
                del char_count[old_char]

            # Check current window
            if len(char_count) <= maxLetters:
                sub = s[i - minSize + 1:i + 1]
                count[sub] += 1

        return max(count.values()) if count else 0
