#1735. Count Ways to Make Array With Product
#Hard
#
#You are given a 2D integer array queries. For each queries[i] = [ni, ki], find
#the number of different ways you can place positive integers into an array of
#size ni such that the product of the integers is ki. As the number of ways may
#be too large, the answer to the ith query is the number of ways modulo 10^9 + 7.
#
#Return an integer array answer where answer[i] is the answer to the ith query.
#
#Example 1:
#Input: queries = [[2,6],[5,1],[73,660]]
#Output: [4,1,50734910]
#
#Example 2:
#Input: queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
#Output: [1,2,3,10,5]
#
#Constraints:
#    1 <= queries.length <= 10^4
#    1 <= ni, ki <= 10^4

from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        """
        Prime factorization + stars and bars.
        For each prime factor p with exponent e, distribute e among n positions.
        This is C(n + e - 1, e) = C(n + e - 1, n - 1).
        """
        MOD = 10**9 + 7

        # Precompute smallest prime factor for sieve
        MAX_K = 10001
        spf = list(range(MAX_K))
        for i in range(2, int(MAX_K**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAX_K, i):
                    if spf[j] == j:
                        spf[j] = i

        def factorize(k):
            """Return prime factorization as {prime: exponent}."""
            factors = Counter()
            while k > 1:
                p = spf[k]
                while k % p == 0:
                    factors[p] += 1
                    k //= p
            return factors

        # Precompute factorials and inverse factorials
        MAX_VAL = 20020  # n + max_exponent
        fact = [1] * MAX_VAL
        for i in range(1, MAX_VAL):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * MAX_VAL
        inv_fact[MAX_VAL - 1] = pow(fact[MAX_VAL - 1], MOD - 2, MOD)
        for i in range(MAX_VAL - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

        result = []
        for n, k in queries:
            factors = factorize(k)

            ways = 1
            for exp in factors.values():
                # Distribute exp items among n bins: C(n + exp - 1, exp)
                ways = ways * comb(n + exp - 1, exp) % MOD

            result.append(ways)

        return result


class SolutionMemo:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        """
        Using memoization for combinations.
        """
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def comb(n, r):
            if r == 0 or r == n:
                return 1
            if r > n:
                return 0
            return (comb(n - 1, r - 1) + comb(n - 1, r)) % MOD

        def factorize(k):
            factors = Counter()
            d = 2
            while d * d <= k:
                while k % d == 0:
                    factors[d] += 1
                    k //= d
                d += 1
            if k > 1:
                factors[k] += 1
            return factors

        result = []
        for n, k in queries:
            factors = factorize(k)
            ways = 1
            for exp in factors.values():
                ways = ways * comb(n + exp - 1, exp) % MOD
            result.append(ways)

        return result
