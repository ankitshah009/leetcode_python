#730. Count Different Palindromic Subsequences
#Hard
#
#Given a string s, return the number of different non-empty palindromic
#subsequences in s. Since the answer may be very large, return it modulo
#10^9 + 7.
#
#A subsequence of a string is obtained by deleting zero or more characters
#from the string.
#
#A sequence is palindromic if it is equal to the sequence reversed.
#
#Two sequences a1, a2, ... and b1, b2, ... are different if there is some i
#for which ai != bi.
#
#Example 1:
#Input: s = "bccb"
#Output: 6
#Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c',
#'bb', 'cc', 'bcb', 'bccb'. Note that 'bcb' is counted only once, even though
#it occurs twice.
#
#Example 2:
#Input: s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
#Output: 104860361
#Explanation: There are 3104860382 different non-empty palindromic subsequences,
#which is 104860361 modulo 10^9 + 7.
#
#Constraints:
#    1 <= s.length <= 1000
#    s[i] is either 'a', 'b', 'c', or 'd'.

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        """
        DP with memoization: count palindromes in range [i, j].
        """
        MOD = 10**9 + 7
        n = len(s)

        # Precompute next/prev occurrence of each character
        next_char = [[n] * 4 for _ in range(n + 1)]
        prev_char = [[-1] * 4 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for c in range(4):
                next_char[i][c] = next_char[i + 1][c]
            next_char[i][ord(s[i]) - ord('a')] = i

        for i in range(n):
            for c in range(4):
                prev_char[i + 1][c] = prev_char[i][c]
            prev_char[i + 1][ord(s[i]) - ord('a')] = i

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i > j:
                return 0

            count = 0

            # Try each character as the outer character
            for c in range(4):
                # Find first and last occurrence of c in [i, j]
                left = next_char[i][c]
                right = prev_char[j + 1][c]

                if left > j:
                    continue  # Character c not in range

                count += 1  # Single character "c"

                if left < right:
                    count += 1  # "cc"
                    count += dp(left + 1, right - 1)  # "c...c" with middle

            return count % MOD

        return dp(0, n - 1)


class SolutionBottomUp:
    """Bottom-up DP"""

    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # dp[i][j] = count of palindromic subsequences in s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters
        for i in range(n):
            dp[i][i] = 1

        # Fill for increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    # Find inner occurrences of s[i]
                    left, right = i + 1, j - 1

                    while left <= right and s[left] != s[i]:
                        left += 1
                    while left <= right and s[right] != s[i]:
                        right -= 1

                    if left > right:
                        # No s[i] in middle
                        dp[i][j] = 2 * dp[i + 1][j - 1] + 2
                    elif left == right:
                        # One s[i] in middle
                        dp[i][j] = 2 * dp[i + 1][j - 1] + 1
                    else:
                        # Multiple s[i] in middle
                        dp[i][j] = 2 * dp[i + 1][j - 1] - dp[left + 1][right - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]

                dp[i][j] = (dp[i][j] % MOD + MOD) % MOD

        return dp[0][n - 1]
