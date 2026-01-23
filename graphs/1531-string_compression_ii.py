#1531. String Compression II
#Hard
#
#Run-length encoding is a string compression method that works by replacing
#consecutive identical characters (repeated 2 or more times) with the
#concatenation of the character and the number marking the count of the
#characters (length of the run). For example, to compress the string "aabccc"
#we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string
#becomes "a2bc3".
#
#Notice that in this problem, we are not adding '1' after single characters.
#
#Given a string s and an integer k. You need to delete at most k characters
#from s such that the run-length encoded version of s has minimum length.
#
#Find the minimum length of the run-length encoded version of s after deleting
#at most k characters.
#
#Example 1:
#Input: s = "aaabcccd", k = 2
#Output: 4
#Explanation: Compressing s without deleting anything will give us "a3bc3d" of
#length 6. Deleting any of the characters 'a' or 'c' would at most decrease the
#length of the compressed string to 5. The best way is to delete 'b' and 'd',
#then the compressed version of s will be "a3c3" of length 4.
#
#Example 2:
#Input: s = "aabbaa", k = 2
#Output: 2
#Explanation: If we delete both 'b' characters, the resulting compressed string
#would be "a4" of length 2.
#
#Example 3:
#Input: s = "aaaaaaaaaaa", k = 0
#Output: 3
#Explanation: Since k is zero, we cannot delete anything. The compressed string
#is "a11" of length 3.
#
#Constraints:
#    1 <= s.length <= 100
#    0 <= k <= s.length
#    s contains only lowercase English letters.

from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        DP with memoization.
        State: (index, last_char, last_count, deletions_left)

        At each position, either:
        1. Delete current character (if deletions left)
        2. Keep current character
        """
        n = len(s)

        def encoded_len(count: int) -> int:
            if count == 0:
                return 0
            if count == 1:
                return 1
            if count < 10:
                return 2
            if count < 100:
                return 3
            return 4

        @lru_cache(maxsize=None)
        def dp(i: int, last: str, count: int, rem: int) -> int:
            if rem < 0:
                return float('inf')
            if i == n:
                return encoded_len(count)

            # Option 1: Delete s[i]
            delete = dp(i + 1, last, count, rem - 1)

            # Option 2: Keep s[i]
            if s[i] == last:
                # Extend current run
                keep = dp(i + 1, last, count + 1, rem)
            else:
                # Start new run (finalize previous)
                keep = encoded_len(count) + dp(i + 1, s[i], 1, rem)

            return min(delete, keep)

        return dp(0, '', 0, k)


class SolutionDP2D:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        Alternative DP formulation.
        dp[i][j] = min length using s[0:i] with j deletions.
        """
        n = len(s)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            # j = deletions remaining
            if j < 0:
                return float('inf')
            if i <= j:
                return 0  # Can delete all remaining

            # Option 1: Delete s[i-1]
            result = dp(i - 1, j - 1)

            # Option 2: Keep s[i-1] and possibly delete different chars
            # Try all possible "groups" ending at i-1
            count = 0
            deletions = 0

            for left in range(i - 1, -1, -1):
                if s[left] == s[i - 1]:
                    count += 1
                else:
                    deletions += 1

                if deletions > j:
                    break

                # Length contribution from this group
                add = 1 + (0 if count == 1 else 1 if count < 10 else 2 if count < 100 else 3)
                result = min(result, dp(left, j - deletions) + add)

            return result

        return dp(n, k)


class SolutionIterative:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        Iterative DP with tabulation.
        """
        n = len(s)
        INF = float('inf')

        # dp[i][j] = min length for s[0:i] with j deletions used
        dp = [[INF] * (k + 2) for _ in range(n + 1)]
        dp[0][0] = 0

        def encoded_length(count):
            if count == 0:
                return 0
            if count == 1:
                return 1
            if count < 10:
                return 2
            if count < 100:
                return 3
            return 4

        for i in range(1, n + 1):
            for j in range(min(i, k) + 1):
                # Delete s[i-1]
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

                # Keep s[i-1], look back
                count = 0
                deletions = 0

                for left in range(i, 0, -1):
                    if s[left - 1] == s[i - 1]:
                        count += 1
                    else:
                        deletions += 1

                    if j - deletions >= 0:
                        dp[i][j] = min(
                            dp[i][j],
                            dp[left - 1][j - deletions] + encoded_length(count)
                        )

        return dp[n][k]
