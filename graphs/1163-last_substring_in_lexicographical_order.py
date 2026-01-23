#1163. Last Substring in Lexicographical Order
#Hard
#
#Given a string s, return the last substring of s in lexicographical order.
#
#Example 1:
#Input: s = "abab"
#Output: "bab"
#Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"].
#The lexicographically maximum substring is "bab".
#
#Example 2:
#Input: s = "leetcode"
#Output: "tcode"
#
#Constraints:
#    1 <= s.length <= 4 * 10^5
#    s contains only lowercase English letters.

class Solution:
    def lastSubstring(self, s: str) -> str:
        """
        Key insight: Answer is always a suffix (extending substring can only make it larger).
        Use two-pointer to find the lexicographically largest suffix.
        """
        n = len(s)
        i, j, k = 0, 1, 0  # i: best candidate, j: current candidate, k: comparison offset

        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] < s[j + k]:
                # j is better, move i
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
            else:
                # i is better, move j
                j = j + k + 1
                k = 0

        return s[i:]


class SolutionSimple:
    def lastSubstring(self, s: str) -> str:
        """
        Find suffix starting with largest char at rightmost position.
        Then compare with other suffixes starting with same char.
        """
        # Find the largest character
        max_char = max(s)

        # Find all positions where this char appears
        candidates = [i for i, c in enumerate(s) if c == max_char]

        # Among all suffixes starting with max_char, find lexicographically largest
        best = candidates[0]
        for pos in candidates[1:]:
            # Compare suffix starting at pos with suffix starting at best
            if s[pos:] > s[best:]:
                best = pos

        return s[best:]


class SolutionOptimized:
    def lastSubstring(self, s: str) -> str:
        """
        Optimized two-pointer approach.
        """
        n = len(s)
        i = 0  # Start of best suffix
        j = 1  # Start of current candidate
        offset = 0  # Current comparison offset

        while j + offset < n:
            if s[i + offset] == s[j + offset]:
                offset += 1
            elif s[i + offset] > s[j + offset]:
                # Current best is better
                j += offset + 1
                offset = 0
            else:
                # Candidate is better
                # Key optimization: i moves past the matching prefix
                i = max(i + offset + 1, j)
                j = i + 1
                offset = 0

        return s[i:]
