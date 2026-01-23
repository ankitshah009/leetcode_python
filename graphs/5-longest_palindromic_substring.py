#5. Longest Palindromic Substring
#Medium
#
#Given a string s, return the longest palindromic substring in s.
#
#Example 1:
#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.
#
#Example 2:
#Input: s = "cbbd"
#Output: "bb"
#
#Constraints:
#    1 <= s.length <= 1000
#    s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Expand around center approach - O(n^2) time, O(1) space.
        """
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        result = ""

        for i in range(len(s)):
            # Odd length palindrome
            odd = expand(i, i)
            if len(odd) > len(result):
                result = odd

            # Even length palindrome
            even = expand(i, i + 1)
            if len(even) > len(result):
                result = even

        return result


class SolutionDP:
    def longestPalindrome(self, s: str) -> str:
        """
        Dynamic Programming - O(n^2) time, O(n^2) space.
        dp[i][j] = True if s[i:j+1] is palindrome.
        """
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        # All single characters are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check for length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check for lengths > 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length

        return s[start:start + max_len]


class SolutionManacher:
    def longestPalindrome(self, s: str) -> str:
        """
        Manacher's Algorithm - O(n) time.
        """
        # Transform string: "abc" -> "#a#b#c#"
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n  # Palindrome radii
        center = right = 0

        for i in range(n):
            if i < right:
                mirror = 2 * center - i
                p[i] = min(right - i, p[mirror])

            # Expand around i
            while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 and
                   t[i + p[i] + 1] == t[i - p[i] - 1]):
                p[i] += 1

            # Update center and right boundary
            if i + p[i] > right:
                center = i
                right = i + p[i]

        # Find maximum
        max_len, center_idx = max((v, i) for i, v in enumerate(p))
        start = (center_idx - max_len) // 2

        return s[start:start + max_len]
