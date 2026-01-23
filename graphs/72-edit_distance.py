#72. Edit Distance
#Medium
#
#Given two strings word1 and word2, return the minimum number of operations
#required to convert word1 to word2.
#
#You have the following three operations permitted on a word:
#- Insert a character
#- Delete a character
#- Replace a character
#
#Example 1:
#Input: word1 = "horse", word2 = "ros"
#Output: 3
#Explanation:
#horse -> rorse (replace 'h' with 'r')
#rorse -> rose (remove 'r')
#rose -> ros (remove 'e')
#
#Example 2:
#Input: word1 = "intention", word2 = "execution"
#Output: 5
#
#Constraints:
#    0 <= word1.length, word2.length <= 500
#    word1 and word2 consist of lowercase English letters.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        DP with 2D array - classic Levenshtein distance.
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # Delete
                        dp[i][j - 1],      # Insert
                        dp[i - 1][j - 1]   # Replace
                    )

        return dp[m][n]


class SolutionSpaceOptimized:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Space-optimized DP - O(n) space.
        """
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))

        for i in range(1, m + 1):
            curr = [i] + [0] * n

            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])

            prev = curr

        return prev[n]


class SolutionMemoization:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Top-down DP with memoization.
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i == 0:
                return j
            if j == 0:
                return i

            if word1[i - 1] == word2[j - 1]:
                return dp(i - 1, j - 1)

            return 1 + min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1))

        return dp(len(word1), len(word2))
