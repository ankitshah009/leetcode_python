#712. Minimum ASCII Delete Sum for Two Strings
#Medium
#
#Given two strings s1 and s2, return the lowest ASCII sum of deleted characters
#to make two strings equal.
#
#Example 1:
#Input: s1 = "sea", s2 = "eat"
#Output: 231
#Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
#sum. Deleting "t" from "eat" adds 116 to the sum. At the end, both strings are
#equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
#
#Example 2:
#Input: s1 = "delete", s2 = "leet"
#Output: 403
#Explanation: Deleting "dee" from "delete" to turn the string into "let",
#adds 100[d] + 101[e] + 101[e] to the sum.
#Deleting "e" from "leet" adds 101[e] to the sum.
#At the end, both strings are equal to "let", and the answer is
#100+101+101+101 = 403.
#
#Constraints:
#    1 <= s1.length, s2.length <= 1000
#    s1 and s2 consist of lowercase English letters.

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        DP: Find max ASCII sum of LCS, then subtract from total.
        Or directly compute min delete sum.
        """
        m, n = len(s1), len(s2)

        # dp[i][j] = min delete sum to make s1[:i] and s2[:j] equal
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases: delete all characters
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + ord(s1[i-1]),  # Delete from s1
                        dp[i][j-1] + ord(s2[j-1])   # Delete from s2
                    )

        return dp[m][n]


class SolutionLCS:
    """Find max ASCII LCS and subtract from total"""

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        # Find max ASCII sum of LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        lcs_sum = dp[m][n]
        total = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)

        return total - 2 * lcs_sum


class SolutionSpaceOptimized:
    """O(n) space using rolling array"""

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s2)
        dp = [0] * (n + 1)

        # Base case: delete all of s2
        for j in range(1, n + 1):
            dp[j] = dp[j-1] + ord(s2[j-1])

        for i in range(1, len(s1) + 1):
            new_dp = [dp[0] + ord(s1[i-1])]

            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    new_dp.append(dp[j-1])
                else:
                    new_dp.append(min(
                        dp[j] + ord(s1[i-1]),
                        new_dp[j-1] + ord(s2[j-1])
                    ))

            dp = new_dp

        return dp[n]
