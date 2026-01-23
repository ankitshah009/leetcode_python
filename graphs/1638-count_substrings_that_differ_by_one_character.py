#1638. Count Substrings That Differ by One Character
#Medium
#
#Given two strings s and t, find the number of ways you can choose a non-empty
#substring of s and replace a single character by a different character such
#that the resulting substring is a substring of t. In other words, find the
#number of substrings in s that differ from some substring in t by exactly one
#character.
#
#For example, the underlined substrings in "computer" and "computation" only
#differ by the 'e'/'a', so this is a valid way.
#
#Return the number of substrings that satisfy the condition above.
#
#A substring is a contiguous sequence of characters within a string.
#
#Example 1:
#Input: s = "aba", t = "baba"
#Output: 6
#Explanation: The following are the pairs of substrings from s and t that differ
#by exactly 1 character:
#("aba", "baba") - s[0:1] ("a") vs t[0:1] ("b")
#("aba", "baba") - s[0:1] ("a") vs t[2:3] ("b")
#("aba", "baba") - s[1:2] ("b") vs t[1:2] ("a")
#...
#
#Example 2:
#Input: s = "ab", t = "bb"
#Output: 3
#Explanation: The following are the pairs of substrings:
#("ab", "bb") - s[0:1] ("a") vs t[0:1] ("b")
#("ab", "bb") - s[0:2] ("ab") vs t[0:2] ("bb")
#("ab", "bb") - s[1:2] ("b") vs t[0:1] ("b") - These are same, diff=0, not counted.
#Actually: ("a", "b"), ("ab", "bb"), ("ab", "ab" doesn't exist)...
#
#Constraints:
#    1 <= s.length, t.length <= 100
#    s and t consist of lowercase English letters only.

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        """
        For each pair (i, j) where s[i] != t[j], count substrings that
        differ at exactly this position.

        For position (i, j) with s[i] != t[j]:
        - Count matching characters to the left: left
        - Count matching characters to the right: right
        - Number of valid substrings = (left + 1) * (right + 1)
        """
        m, n = len(s), len(t)
        count = 0

        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    # Count matching prefix and suffix
                    left = 0
                    while i - left - 1 >= 0 and j - left - 1 >= 0 and s[i - left - 1] == t[j - left - 1]:
                        left += 1

                    right = 0
                    while i + right + 1 < m and j + right + 1 < n and s[i + right + 1] == t[j + right + 1]:
                        right += 1

                    count += (left + 1) * (right + 1)

        return count


class SolutionDP:
    def countSubstrings(self, s: str, t: str) -> int:
        """
        DP approach: precompute left and right matching lengths.
        """
        m, n = len(s), len(t)

        # left[i][j] = length of common prefix ending at s[i-1], t[j-1]
        left = [[0] * (n + 1) for _ in range(m + 1)]
        # right[i][j] = length of common suffix starting at s[i], t[j]
        right = [[0] * (n + 1) for _ in range(m + 1)]

        # Compute left (common prefix)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    left[i][j] = left[i - 1][j - 1] + 1

        # Compute right (common suffix)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    right[i][j] = right[i + 1][j + 1] + 1

        # Count substrings
        count = 0
        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    count += (left[i][j] + 1) * (right[i + 1][j + 1] + 1)

        return count


class SolutionBruteForce:
    def countSubstrings(self, s: str, t: str) -> int:
        """
        Brute force: check all pairs of substrings.
        O(m^2 * n^2) but simple.
        """
        m, n = len(s), len(t)
        count = 0

        for i in range(m):
            for j in range(n):
                diff = 0
                k = 0
                while i + k < m and j + k < n:
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff == 1:
                        count += 1
                    elif diff > 1:
                        break
                    k += 1

        return count
