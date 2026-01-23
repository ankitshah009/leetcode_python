#1977. Number of Ways to Separate Numbers
#Hard
#
#You wrote down many positive integers in a string called num. However, you
#realized that you forgot to add commas to separate the different numbers.
#You remember that the list of integers was non-decreasing and that no integer
#had leading zeros.
#
#Return the number of possible lists of integers that you could have written
#down to get the string num. Since the answer may be large, return it modulo
#10^9 + 7.
#
#Example 1:
#Input: num = "327"
#Output: 2
#Explanation: Possible lists: ["327"], ["3","27"]
#
#Example 2:
#Input: num = "094"
#Output: 0
#Explanation: Leading zeros are not allowed.
#
#Example 3:
#Input: num = "0"
#Output: 0
#
#Example 4:
#Input: num = "9999999999999"
#Output: 101
#
#Constraints:
#    1 <= num.length <= 3500
#    num consists of digits '0' through '9'.

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        """
        DP with LCP optimization.
        dp[i][j] = number of ways to partition num[0:i] where last number has length j
        """
        MOD = 10**9 + 7
        n = len(num)

        if num[0] == '0':
            return 0

        # Precompute Longest Common Prefix for comparisons
        # lcp[i][j] = length of longest common prefix starting at i and j
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        def compare(i1: int, len1: int, i2: int, len2: int) -> bool:
            """Check if num[i1:i1+len1] <= num[i2:i2+len2]"""
            if len1 != len2:
                return len1 < len2

            l = lcp[i1][i2]
            if l >= len1:
                return True  # Equal

            return num[i1 + l] <= num[i2 + l]

        # dp[i][j] = ways for num[0:i] with last number of length j
        # prefix[i][j] = sum of dp[i][1..j]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        prefix = [[0] * (n + 1) for _ in range(n + 1)]

        # Base case: entire prefix is one number
        for i in range(1, n + 1):
            if num[0] != '0':
                dp[i][i] = 1

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                prefix[i][j] = (prefix[i][j - 1] + dp[i][j]) % MOD

        # Fill DP table
        for i in range(1, n + 1):
            for length in range(1, i + 1):
                start = i - length
                if num[start] == '0':  # No leading zeros
                    continue

                prev_end = start

                if length <= prev_end:
                    # Previous numbers of length < current length
                    dp[i][length] = (dp[i][length] + prefix[prev_end][length - 1]) % MOD

                    # Previous number of same length, check if <=
                    prev_start = prev_end - length
                    if prev_start >= 0 and num[prev_start] != '0':
                        if compare(prev_start, length, start, length):
                            dp[i][length] = (dp[i][length] + dp[prev_end][length]) % MOD
                else:
                    # Previous partition can be any valid partition
                    dp[i][length] = (dp[i][length] + prefix[prev_end][prev_end]) % MOD

            for j in range(1, n + 1):
                prefix[i][j] = (prefix[i][j - 1] + dp[i][j]) % MOD

        return prefix[n][n]
