#903. Valid Permutations for DI Sequence
#Hard
#
#You are given a string s of length n where s[i] is either 'D' (decreasing) or
#'I' (increasing). A permutation perm of n + 1 integers of all the integers in
#the range [0, n] is called a valid permutation if for all valid i:
#- If s[i] == 'D', then perm[i] > perm[i + 1]
#- If s[i] == 'I', then perm[i] < perm[i + 1]
#
#Return the number of valid permutations. The answer may be large, return it
#modulo 10^9 + 7.
#
#Example 1:
#Input: s = "DID"
#Output: 5
#Explanation: (1,0,2), (2,0,1), (2,1,0), (3,0,2), (3,1,2) are valid.
#
#Constraints:
#    n == s.length
#    1 <= n <= 200
#    s[i] is either 'D' or 'I'.

class Solution:
    def numPermsDISequence(self, s: str) -> int:
        """
        DP where dp[i][j] = count of permutations where i-th element has rank j.
        """
        MOD = 10 ** 9 + 7
        n = len(s)

        # dp[j] = count ending with relative rank j
        dp = [1] * (n + 1)

        for i in range(n):
            new_dp = [0] * (n + 1 - i - 1)

            if s[i] == 'I':
                # Need smaller before, so prefix sum
                prefix = 0
                for j in range(n - i):
                    prefix = (prefix + dp[j]) % MOD
                    new_dp[j] = prefix
            else:
                # Need larger before, so suffix sum
                suffix = 0
                for j in range(n - i - 1, -1, -1):
                    suffix = (suffix + dp[j + 1]) % MOD
                    new_dp[j] = suffix

            dp = new_dp

        return dp[0]


class SolutionMemo:
    """Memoization approach"""

    def numPermsDISequence(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(pos: int, available: tuple) -> int:
            if pos == n + 1:
                return 1

            result = 0
            available = list(available)

            for i, num in enumerate(available):
                if pos == 0:
                    new_avail = tuple(available[:i] + available[i+1:])
                    result = (result + dp(pos + 1, new_avail)) % MOD
                elif s[pos - 1] == 'I' and num > prev:
                    new_avail = tuple(available[:i] + available[i+1:])
                    result = (result + dp(pos + 1, new_avail)) % MOD
                elif s[pos - 1] == 'D' and num < prev:
                    new_avail = tuple(available[:i] + available[i+1:])
                    result = (result + dp(pos + 1, new_avail)) % MOD

            return result

        return dp(0, tuple(range(n + 1)))


class SolutionDP2D:
    """Explicit 2D DP"""

    def numPermsDISequence(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)

        # dp[i][j] = permutations of first i+1 elements where last has rank j
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, n + 1):
            if s[i - 1] == 'I':
                cumsum = 0
                for j in range(n + 1 - i):
                    cumsum = (cumsum + dp[i - 1][j]) % MOD
                    dp[i][j] = cumsum
            else:
                cumsum = 0
                for j in range(n - i, -1, -1):
                    cumsum = (cumsum + dp[i - 1][j + 1]) % MOD
                    dp[i][j] = cumsum

        return dp[n][0]
