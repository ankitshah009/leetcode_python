#1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
#Hard
#
#You are given three integers n, m and k. Consider the following algorithm to
#find the maximum element of an array of positive integers:
#
#maximum_value = -1
#maximum_index = -1
#search_cost = 0
#n = arr.length
#for (i = 0; i < n; i++) {
#    if (arr[i] > maximum_value) {
#        maximum_value = arr[i]
#        maximum_index = i
#        search_cost = search_cost + 1
#    }
#}
#return maximum_index
#
#You should build the array arr which has the following properties:
#    arr has exactly n integers.
#    1 <= arr[i] <= m where (0 <= i < n).
#    After applying the mentioned algorithm to arr, the value search_cost is
#    equal to k.
#
#Return the number of ways to build the array arr under the mentioned conditions.
#As the answer may grow large, the answer must be computed modulo 10^9 + 7.
#
#Example 1:
#Input: n = 2, m = 3, k = 1
#Output: 6
#Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
#
#Example 2:
#Input: n = 5, m = 2, k = 3
#Output: 0
#Explanation: There are no possible arrays that satisfy the mentioned conditions.
#
#Example 3:
#Input: n = 9, m = 1, k = 1
#Output: 1
#Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
#
#Constraints:
#    1 <= n <= 50
#    1 <= m <= 100
#    0 <= k <= n

from functools import lru_cache

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """
        DP with states: (position, current_max, search_cost)
        dp[i][j][c] = ways to fill positions 0..i-1 with max value j
        and search cost c.
        """
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def dp(pos: int, max_val: int, cost: int) -> int:
            # Base case: filled all positions
            if pos == n:
                return 1 if cost == k else 0

            # Pruning: cost exceeded k
            if cost > k:
                return 0

            ways = 0

            # Place value <= max_val (no cost increase)
            # There are max_val choices
            ways = (max_val * dp(pos + 1, max_val, cost)) % MOD

            # Place value > max_val (cost increases by 1)
            for new_max in range(max_val + 1, m + 1):
                ways = (ways + dp(pos + 1, new_max, cost + 1)) % MOD

            return ways

        return dp(0, 0, 0)


class SolutionIterative:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """Iterative DP with optimization"""
        MOD = 10**9 + 7

        # dp[i][j][c] = ways to fill first i positions with max value j and cost c
        # Transition: dp[i][j][c] contributes to:
        #   - dp[i+1][j][c] * j (place any value <= j)
        #   - dp[i+1][j'][c+1] for each j' > j (place new max)

        # Use suffix sum for optimization
        # dp[i][j][c] = dp_exact[i][j][c] where max is exactly j

        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        # Base case: first position, max is that value, cost is 1
        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(1, n):
            for j in range(1, m + 1):
                for c in range(1, k + 1):
                    if dp[i][j][c] == 0:
                        continue

                    # Place value <= j (no new max)
                    dp[i + 1][j][c] = (dp[i + 1][j][c] + dp[i][j][c] * j) % MOD

                    # Place value > j (new max)
                    for new_j in range(j + 1, m + 1):
                        dp[i + 1][new_j][c + 1] = (dp[i + 1][new_j][c + 1] + dp[i][j][c]) % MOD

        return sum(dp[n][j][k] for j in range(1, m + 1)) % MOD


class SolutionOptimized:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """
        Optimized with prefix sums.
        O(n * m * k) time.
        """
        MOD = 10**9 + 7

        # dp[j][c] = ways to fill current positions with max exactly j and cost c
        dp = [[0] * (k + 1) for _ in range(m + 1)]

        # Base: first position
        for j in range(1, m + 1):
            dp[j][1] = 1

        for _ in range(1, n):
            new_dp = [[0] * (k + 1) for _ in range(m + 1)]

            # Prefix sum of dp[1..j][c] for new max transitions
            prefix = [[0] * (k + 1) for _ in range(m + 2)]
            for j in range(1, m + 1):
                for c in range(k + 1):
                    prefix[j][c] = (prefix[j - 1][c] + dp[j][c]) % MOD

            for j in range(1, m + 1):
                for c in range(1, k + 1):
                    # Place value <= j (same max)
                    new_dp[j][c] = (new_dp[j][c] + dp[j][c] * j) % MOD

                    # Place new max j (from any max < j)
                    if c > 0:
                        new_dp[j][c] = (new_dp[j][c] + prefix[j - 1][c - 1]) % MOD

            dp = new_dp

        return sum(dp[j][k] for j in range(1, m + 1)) % MOD
