#639. Decode Ways II
#Hard
#
#A message containing letters from A-Z can be encoded into numbers using the mapping:
#'A' -> "1"
#'B' -> "2"
#...
#'Z' -> "26"
#
#To decode an encoded message, all the digits must be grouped then mapped back
#into letters using the reverse of the mapping above.
#
#In addition to the mapping above, an encoded message may contain the '*' character,
#which can represent any digit from '1' to '9' ('0' is excluded).
#
#Given a string s consisting of digits and '*' characters, return the number of
#ways to decode it. Return the answer modulo 10^9 + 7.
#
#Example 1:
#Input: s = "*"
#Output: 9
#
#Example 2:
#Input: s = "1*"
#Output: 18
#
#Example 3:
#Input: s = "2*"
#Output: 15
#
#Constraints:
#    1 <= s.length <= 10^5
#    s[i] is a digit or '*'.

class Solution:
    def numDecodings(self, s: str) -> int:
        """DP with O(1) space"""
        MOD = 10**9 + 7

        if not s or s[0] == '0':
            return 0

        def single_digit_ways(c):
            """Ways to decode single character"""
            if c == '*':
                return 9  # 1-9
            return 0 if c == '0' else 1

        def two_digit_ways(c1, c2):
            """Ways to decode two characters as one number"""
            if c1 == '*' and c2 == '*':
                return 15  # 11-19, 21-26
            elif c1 == '*':
                if c2 <= '6':
                    return 2  # 1X or 2X
                else:
                    return 1  # only 1X
            elif c2 == '*':
                if c1 == '1':
                    return 9  # 11-19
                elif c1 == '2':
                    return 6  # 21-26
                else:
                    return 0
            else:
                num = int(c1 + c2)
                return 1 if 10 <= num <= 26 else 0

        # dp[i] = ways to decode s[0:i]
        prev2 = 1  # dp[i-2]
        prev1 = single_digit_ways(s[0])  # dp[i-1]

        for i in range(1, len(s)):
            curr = 0

            # Single digit decode
            curr += prev1 * single_digit_ways(s[i])

            # Two digit decode
            curr += prev2 * two_digit_ways(s[i-1], s[i])

            curr %= MOD
            prev2, prev1 = prev1, curr

        return prev1


class SolutionDP:
    """DP with array"""

    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        if not s or s[0] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 9 if s[0] == '*' else (0 if s[0] == '0' else 1)

        for i in range(2, n + 1):
            c1, c2 = s[i-2], s[i-1]

            # Single digit
            if c2 == '*':
                dp[i] = 9 * dp[i-1]
            elif c2 != '0':
                dp[i] = dp[i-1]

            # Two digits
            if c1 == '*' and c2 == '*':
                dp[i] += 15 * dp[i-2]
            elif c1 == '*':
                dp[i] += (2 if c2 <= '6' else 1) * dp[i-2]
            elif c2 == '*':
                if c1 == '1':
                    dp[i] += 9 * dp[i-2]
                elif c1 == '2':
                    dp[i] += 6 * dp[i-2]
            else:
                num = int(c1 + c2)
                if 10 <= num <= 26:
                    dp[i] += dp[i-2]

            dp[i] %= MOD

        return dp[n]
