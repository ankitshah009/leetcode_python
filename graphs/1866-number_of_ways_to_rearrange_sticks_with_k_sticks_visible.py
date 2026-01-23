#1866. Number of Ways to Rearrange Sticks With K Sticks Visible
#Hard
#
#There are n uniquely-sized sticks whose lengths are integers from 1 to n. You
#want to arrange the sticks such that exactly k sticks are visible from the
#left. A stick is visible from the left if there are no longer sticks to the
#left of it.
#
#Return the number of such arrangements. Since the answer may be large, return
#it modulo 10^9 + 7.
#
#Example 1:
#Input: n = 3, k = 2
#Output: 3
#
#Example 2:
#Input: n = 5, k = 5
#Output: 1
#
#Example 3:
#Input: n = 20, k = 11
#Output: 647427950
#
#Constraints:
#    1 <= n <= 1000
#    1 <= k <= n

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        DP: dp[i][j] = ways to arrange i sticks with j visible.

        For stick of height i (the tallest among i sticks):
        - If placed leftmost: contributes to visibility, dp[i-1][j-1]
        - If placed elsewhere: (i-1) positions, doesn't contribute, dp[i-1][j]

        dp[i][j] = dp[i-1][j-1] + (i-1) * dp[i-1][j]
        """
        MOD = 10**9 + 7

        # dp[j] = ways with j visible sticks
        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            # Process in reverse to avoid overwriting
            new_dp = [0] * (k + 1)
            for j in range(1, min(i, k) + 1):
                new_dp[j] = (dp[j - 1] + (i - 1) * dp[j]) % MOD
            dp = new_dp

        return dp[k]


class SolutionMemo:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        Top-down DP with memoization.
        """
        MOD = 10**9 + 7
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(sticks: int, visible: int) -> int:
            if sticks == visible:
                return 1
            if visible == 0 or sticks == 0:
                return 0

            # Place tallest stick leftmost (visible) or not
            return (dp(sticks - 1, visible - 1) +
                    (sticks - 1) * dp(sticks - 1, visible)) % MOD

        return dp(n, k)


class SolutionStirling:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        This is unsigned Stirling numbers of the first kind.
        |S(n, k)| = number of permutations of n with k cycles.
        (Viewing tallest in each "prefix maximum group" as cycle leaders)
        """
        MOD = 10**9 + 7

        # Stirling recurrence: S(n,k) = S(n-1,k-1) + (n-1)*S(n-1,k)
        prev = [0] * (k + 1)
        prev[0] = 1

        for i in range(1, n + 1):
            curr = [0] * (k + 1)
            for j in range(1, min(i, k) + 1):
                curr[j] = (prev[j - 1] + (i - 1) * prev[j]) % MOD
            prev = curr

        return prev[k]
