#1092. Shortest Common Supersequence
#Hard
#
#Given two strings str1 and str2, return the shortest string that has both
#str1 and str2 as subsequences. If there are multiple valid strings, return
#any of them.
#
#A string s is a subsequence of string t if deleting some number of characters
#from t (possibly 0) results in the string s.
#
#Example 1:
#Input: str1 = "abac", str2 = "cab"
#Output: "cabac"
#Explanation:
#str1 = "abac" is a subsequence of "cabac" (ca[b]a[c]).
#str2 = "cab" is a subsequence of "cabac" ([c]a[b]ac).
#
#Example 2:
#Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
#Output: "aaaaaaaa"
#
#Constraints:
#    1 <= str1.length, str2.length <= 1000
#    str1 and str2 consist of lowercase English letters.

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        1. Find LCS using DP
        2. Build result by including all chars from both strings,
           using LCS only once.
        """
        m, n = len(str1), len(str2)

        # DP for LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Build result by backtracking
        result = []
        i, j = m, n

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                result.append(str1[i - 1])
                i -= 1
            else:
                result.append(str2[j - 1])
                j -= 1

        # Add remaining characters
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        while j > 0:
            result.append(str2[j - 1])
            j -= 1

        return ''.join(reversed(result))


class SolutionLCS:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        Alternative: First find LCS, then merge strings around LCS.
        """
        def lcs(s1, s2):
            m, n = len(s1), len(s2)
            dp = [[""] * (n + 1) for _ in range(m + 1)]

            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if s1[i - 1] == s2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

            return dp[m][n]

        common = lcs(str1, str2)

        result = []
        i, j = 0, 0

        for c in common:
            while str1[i] != c:
                result.append(str1[i])
                i += 1
            while str2[j] != c:
                result.append(str2[j])
                j += 1
            result.append(c)
            i += 1
            j += 1

        return ''.join(result) + str1[i:] + str2[j:]
