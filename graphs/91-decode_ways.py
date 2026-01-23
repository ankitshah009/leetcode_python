#91. Decode Ways
#Medium
#
#A message containing letters from A-Z can be encoded into numbers using the
#following mapping:
#'A' -> "1"
#'B' -> "2"
#...
#'Z' -> "26"
#
#To decode an encoded message, all the digits must be grouped then mapped back
#into letters using the reverse of the mapping above.
#
#Given a string s containing only digits, return the number of ways to decode it.
#
#Example 1:
#Input: s = "12"
#Output: 2
#Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
#
#Example 2:
#Input: s = "226"
#Output: 3
#Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
#Example 3:
#Input: s = "06"
#Output: 0
#Explanation: "06" cannot be mapped to "F" because "6" is different from "06".
#
#Constraints:
#    1 <= s.length <= 100
#    s contains only digits and may contain leading zero(s).

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        DP with O(1) space - similar to climbing stairs.
        """
        if not s or s[0] == '0':
            return 0

        n = len(s)
        # prev2 = dp[i-2], prev1 = dp[i-1]
        prev2, prev1 = 1, 1

        for i in range(1, n):
            current = 0

            # Single digit decode
            if s[i] != '0':
                current = prev1

            # Two digit decode
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2

            prev2, prev1 = prev1, current

        return prev1


class SolutionDP:
    def numDecodings(self, s: str) -> int:
        """
        DP with array - explicit state.
        """
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string
        dp[1] = 1  # First char is valid (not '0')

        for i in range(2, n + 1):
            # Single digit
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Two digits
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]


class SolutionMemo:
    def numDecodings(self, s: str) -> int:
        """
        Top-down with memoization.
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def decode(index: int) -> int:
            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            # Single digit
            result = decode(index + 1)

            # Two digits
            if index + 1 < len(s) and int(s[index:index + 2]) <= 26:
                result += decode(index + 2)

            return result

        return decode(0)


class SolutionRecursive:
    def numDecodings(self, s: str) -> int:
        """
        Pure recursive (slow, for understanding).
        """
        def decode(index: int) -> int:
            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            result = decode(index + 1)

            if index + 1 < len(s) and int(s[index:index + 2]) <= 26:
                result += decode(index + 2)

            return result

        return decode(0)
