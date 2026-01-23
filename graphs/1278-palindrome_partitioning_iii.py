#1278. Palindrome Partitioning III
#Hard
#
#You are given a string s containing lowercase letters and an integer k. You
#need to:
#    First, change some characters of s to other lowercase English letters.
#    Then divide s into k non-empty disjoint substrings such that each substring
#    is a palindrome.
#
#Return the minimal number of characters that you need to change to divide the
#string.
#
#Example 1:
#Input: s = "abc", k = 2
#Output: 1
#Explanation: You can split the string into "ab" and "c", and change 1 character
#in "ab" to make it palindrome.
#
#Example 2:
#Input: s = "aabbc", k = 3
#Output: 0
#Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
#
#Example 3:
#Input: s = "leetcode", k = 8
#Output: 0
#
#Constraints:
#    1 <= k <= s.length <= 100.
#    s only contains lowercase English letters.

from functools import lru_cache

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """
        Precompute cost to make any substring a palindrome.
        DP: dp[i][j] = min changes to partition s[0:i] into j palindromes.
        """
        n = len(s)

        # Precompute cost to make s[i:j+1] a palindrome
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + (0 if s[i] == s[j] else 1)

        # DP: dp[i][parts] = min changes to partition s[0:i] into 'parts' palindromes
        @lru_cache(maxsize=None)
        def dp(end, parts):
            if parts == 1:
                return cost[0][end - 1]

            result = float('inf')
            # Try all possible last palindrome starting positions
            for start in range(parts - 1, end):
                result = min(result, dp(start, parts - 1) + cost[start][end - 1])

            return result

        return dp(n, k)


class Solution2D:
    def palindromePartition(self, s: str, k: int) -> int:
        """Bottom-up DP"""
        n = len(s)

        # Precompute palindrome costs
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + (0 if s[i] == s[j] else 1)

        # dp[i][j] = min changes to partition s[0:i] into j parts
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for parts in range(1, min(i, k) + 1):
                if parts == 1:
                    dp[i][1] = cost[0][i - 1]
                else:
                    for j in range(parts - 1, i):
                        dp[i][parts] = min(dp[i][parts], dp[j][parts - 1] + cost[j][i - 1])

        return dp[n][k]
