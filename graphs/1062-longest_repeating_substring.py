#1062. Longest Repeating Substring
#Medium
#
#Given a string s, return the length of the longest repeating substring. If
#no repeating substring exists, return 0.
#
#Example 1:
#Input: s = "abcd"
#Output: 0
#Explanation: There is no repeating substring.
#
#Example 2:
#Input: s = "abbaba"
#Output: 2
#Explanation: The longest repeating substrings are "ab" and "ba", each of
#which occurs twice.
#
#Example 3:
#Input: s = "aabcaabdaab"
#Output: 3
#Explanation: The longest repeating substring is "aab", which occurs 3 times.
#
#Constraints:
#    1 <= s.length <= 2000
#    s consists of lowercase English letters.

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        """
        Binary search + Rabin-Karp rolling hash.
        """
        n = len(s)
        MOD = 2**63 - 1
        BASE = 26

        def has_duplicate(length):
            """Check if there's a repeating substring of given length"""
            if length == 0:
                return True

            h = 0
            for i in range(length):
                h = (h * BASE + ord(s[i]) - ord('a')) % MOD

            seen = {h}
            base_power = pow(BASE, length, MOD)

            for i in range(1, n - length + 1):
                h = (h * BASE - (ord(s[i-1]) - ord('a')) * base_power + ord(s[i+length-1]) - ord('a')) % MOD
                if h in seen:
                    return True
                seen.add(h)

            return False

        # Binary search on length
        left, right = 0, n - 1
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if has_duplicate(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result


class SolutionDP:
    def longestRepeatingSubstring(self, s: str) -> int:
        """
        DP approach: dp[i][j] = length of common suffix ending at i and j.
        """
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        result = 0

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])

        return result


class SolutionSuffixArray:
    def longestRepeatingSubstring(self, s: str) -> int:
        """
        Build suffix array, then check adjacent suffixes for LCP.
        """
        n = len(s)
        suffixes = [(s[i:], i) for i in range(n)]
        suffixes.sort()

        result = 0
        for i in range(1, n):
            s1 = suffixes[i - 1][0]
            s2 = suffixes[i][0]
            lcp = 0
            for c1, c2 in zip(s1, s2):
                if c1 == c2:
                    lcp += 1
                else:
                    break
            result = max(result, lcp)

        return result
