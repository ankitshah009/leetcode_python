#647. Palindromic Substrings
#Medium
#
#Given a string s, return the number of palindromic substrings in it.
#
#A string is a palindrome when it reads the same backward as forward.
#
#A substring is a contiguous sequence of characters within the string.
#
#Example 1:
#Input: s = "abc"
#Output: 3
#Explanation: Three palindromic strings: "a", "b", "c".
#
#Example 2:
#Input: s = "aaa"
#Output: 6
#Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#Constraints:
#    1 <= s.length <= 1000
#    s consists of lowercase English letters.

class Solution:
    def countSubstrings(self, s: str) -> int:
        """Expand around center - O(n^2) time, O(1) space"""
        count = 0
        n = len(s)

        def expand(left: int, right: int) -> int:
            cnt = 0
            while left >= 0 and right < n and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt

        for i in range(n):
            # Odd length palindromes
            count += expand(i, i)
            # Even length palindromes
            count += expand(i, i + 1)

        return count


class SolutionDP:
    """Dynamic programming approach"""

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        # Single characters
        for i in range(n):
            dp[i][i] = True
            count += 1

        # Two characters
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # Length 3 and above
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count


class SolutionManacher:
    """Manacher's algorithm - O(n) time"""

    def countSubstrings(self, s: str) -> int:
        # Transform string: "abc" -> "^#a#b#c#$"
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        p = [0] * n
        center = right = 0
        count = 0

        for i in range(1, n - 1):
            if i < right:
                p[i] = min(right - i, p[2 * center - i])

            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            if i + p[i] > right:
                center, right = i, i + p[i]

        # Count palindromes: each p[i] contributes (p[i] + 1) // 2
        for radius in p:
            count += (radius + 1) // 2

        return count
