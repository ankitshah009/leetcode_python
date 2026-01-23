#1692. Count Ways to Distribute Candies
#Hard
#
#There are n unique candies (labeled 1 through n) and k bags. You are asked to
#distribute all the candies into the bags such that every bag has at least one
#candy.
#
#There can be multiple ways to distribute the candies. Two ways are considered
#different if the candies in one bag in the first way are not all in the same
#bag in the second way. The order of the bags and the order of the candies in
#each bag do not matter.
#
#For example, (1), (2,3) and (2), (1,3) are considered different because candies
#2 and 3 are in the same bag in the first way but not in the second way.
#
#Given two integers, n and k, return the number of different ways to distribute
#the candies. As the answer may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: n = 3, k = 2
#Output: 3
#Explanation: You can distribute 3 candies into 2 bags in 3 ways:
#(1), (2,3), (1,2), (3), (1,3), (2)
#
#Example 2:
#Input: n = 4, k = 2
#Output: 7
#
#Example 3:
#Input: n = 20, k = 5
#Output: 206085257
#
#Constraints:
#    1 <= k <= n <= 1000

class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        """
        This is the Stirling number of the second kind: S(n, k).
        S(n, k) = k * S(n-1, k) + S(n-1, k-1)
        - Put candy n in existing bag: k * S(n-1, k)
        - Put candy n in new bag: S(n-1, k-1)
        """
        MOD = 10**9 + 7

        # dp[i][j] = number of ways to distribute i candies into j bags
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                # Put candy i in new bag by itself
                dp[i][j] = dp[i-1][j-1]
                # Put candy i in one of j existing bags
                dp[i][j] = (dp[i][j] + j * dp[i-1][j]) % MOD

        return dp[n][k]


class SolutionSpaceOptimized:
    def waysToDistribute(self, n: int, k: int) -> int:
        """
        Space optimized to O(k).
        """
        MOD = 10**9 + 7

        # dp[j] = number of ways to distribute current candies into j bags
        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            # Process in reverse to avoid overwriting
            for j in range(min(i, k), 0, -1):
                dp[j] = (dp[j-1] + j * dp[j]) % MOD

        return dp[k]


class SolutionRecursive:
    def waysToDistribute(self, n: int, k: int) -> int:
        """
        Recursive with memoization.
        """
        MOD = 10**9 + 7
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def stirling(n: int, k: int) -> int:
            if n == k:
                return 1
            if k == 0 or k > n:
                return 0

            return (k * stirling(n-1, k) + stirling(n-1, k-1)) % MOD

        return stirling(n, k)


class SolutionFormula:
    def waysToDistribute(self, n: int, k: int) -> int:
        """
        Using explicit Stirling number formula:
        S(n,k) = (1/k!) * sum_{j=0}^{k} (-1)^j * C(k,j) * (k-j)^n
        """
        MOD = 10**9 + 7

        # Precompute factorials and inverse factorials
        fact = [1] * (k + 1)
        for i in range(1, k + 1):
            fact[i] = fact[i-1] * i % MOD

        inv_fact = [1] * (k + 1)
        inv_fact[k] = pow(fact[k], MOD - 2, MOD)
        for i in range(k - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        result = 0
        for j in range(k + 1):
            # C(k, j) = fact[k] / (fact[j] * fact[k-j])
            comb = fact[k] * inv_fact[j] % MOD * inv_fact[k-j] % MOD
            term = comb * pow(k - j, n, MOD) % MOD

            if j % 2 == 0:
                result = (result + term) % MOD
            else:
                result = (result - term + MOD) % MOD

        return result * inv_fact[k] % MOD
