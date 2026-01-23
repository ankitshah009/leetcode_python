#1416. Restore The Array
#Hard
#
#A program was supposed to print an array of integers. The program forgot to
#print whitespaces and the array is printed as a string of digits s and all we
#know is that all integers in the array were in the range [1, k] and there are
#no leading zeros in the array.
#
#Given the string s and the integer k, return the number of the possible arrays
#that can be printed as s using the mentioned program. Since the answer may be
#very large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: s = "1000", k = 10000
#Output: 1
#Explanation: The only possible array is [1000]
#
#Example 2:
#Input: s = "1000", k = 10
#Output: 0
#Explanation: There cannot be an array that was printed this way and has all
#integer >= 1 and <= 10.
#
#Example 3:
#Input: s = "1317", k = 2000
#Output: 8
#Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],
#[1,31,7],[1,3,17],[1,3,1,7]
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists of only digits and does not contain leading zeros.
#    1 <= k <= 10^9

from functools import lru_cache

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        """
        DP where dp[i] = number of ways to split s[i:].
        At each position, try taking numbers of length 1 to len(k).
        """
        MOD = 10**9 + 7
        n = len(s)
        max_len = len(str(k))

        @lru_cache(maxsize=None)
        def dp(i: int) -> int:
            if i == n:
                return 1

            # Leading zero not allowed
            if s[i] == '0':
                return 0

            ways = 0
            # Try different lengths
            for length in range(1, min(max_len + 1, n - i + 1)):
                num_str = s[i:i + length]
                num = int(num_str)

                if num > k:
                    break

                ways = (ways + dp(i + length)) % MOD

            return ways

        return dp(0)


class SolutionIterative:
    def numberOfArrays(self, s: str, k: int) -> int:
        """Iterative DP"""
        MOD = 10**9 + 7
        n = len(s)
        max_len = len(str(k))

        # dp[i] = number of ways to split s[i:]
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                continue

            num = 0
            for j in range(i, min(i + max_len, n)):
                num = num * 10 + int(s[j])
                if num > k:
                    break
                dp[i] = (dp[i] + dp[j + 1]) % MOD

        return dp[0]


class SolutionOptimized:
    def numberOfArrays(self, s: str, k: int) -> int:
        """Space-optimized using rolling array"""
        MOD = 10**9 + 7
        n = len(s)
        max_len = len(str(k))

        # Only need last max_len values
        dp = [0] * (max_len + 1)
        dp[0] = 1  # dp[0] represents position n

        for i in range(n - 1, -1, -1):
            current = 0

            if s[i] != '0':
                num = 0
                for j in range(i, min(i + max_len, n)):
                    num = num * 10 + int(s[j])
                    if num > k:
                        break
                    # dp[j+1] is at offset (j+1 - i - 1 + 1) = j - i + 1 from current position
                    offset = j - i
                    current = (current + dp[offset]) % MOD

            # Shift: dp[max_len] = dp[max_len-1] = ... = dp[1] = dp[0], dp[0] = current
            for j in range(max_len, 0, -1):
                dp[j] = dp[j - 1]
            dp[0] = current

        return dp[0]
