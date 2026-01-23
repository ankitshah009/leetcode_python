#1969. Minimum Non-Zero Product of the Array Elements
#Medium
#
#You are given a positive integer p. Consider an array nums (1-indexed) that
#consists of the integers in the inclusive range [1, 2^p - 1] in their binary
#representations. You are allowed to do the following operation any number of
#times:
#
#Choose two elements x and y from nums.
#Choose a bit in x and swap it with its corresponding bit in y. Corresponding
#bits refer to bits that are in the same position in the binary representation.
#
#For example, if x = 1101 and y = 0011, after swapping the 2nd bit from the
#right, we have x = 1111 and y = 0001.
#
#Find the minimum non-zero product of nums after performing the above operation
#any number of times. Return this product modulo 10^9 + 7.
#
#Example 1:
#Input: p = 1
#Output: 1
#
#Example 2:
#Input: p = 2
#Output: 6
#Explanation: nums = [01, 10, 11]. Swap to get [00, 11, 11] -> but 0 not allowed
#Actually: [01, 10, 11] -> best is leave as [1, 2, 3] -> product = 6
#
#Example 3:
#Input: p = 3
#Output: 1512
#
#Constraints:
#    1 <= p <= 60

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        """
        Key insight:
        - We have numbers 1 to 2^p - 1
        - To minimize product, we want to create many 1s
        - Pair (k, 2^p - 1 - k) can become (1, 2^p - 2)
        - There are (2^p - 2) / 2 such pairs
        - Final product = (2^p - 1) * (2^p - 2)^((2^p - 2)/2)

        Math:
        - Numbers 1 to 2^p - 1
        - Maximum value M = 2^p - 1 (all 1s) cannot be paired down
        - We can pair (k, M-k) for k = 1 to M//2, creating (1, M-1) each
        - Number of pairs = (M-1)/2 = (2^p - 2)/2 = 2^(p-1) - 1
        - Product = M * (M-1)^(num_pairs)
        """
        MOD = 10**9 + 7

        if p == 1:
            return 1

        max_val = (1 << p) - 1  # 2^p - 1
        base = max_val - 1      # 2^p - 2
        exponent = (1 << (p - 1)) - 1  # 2^(p-1) - 1

        # Compute base^exponent mod MOD
        result = pow(base, exponent, MOD)

        # Multiply by max_val
        result = (result * max_val) % MOD

        return result


class SolutionExplained:
    def minNonZeroProduct(self, p: int) -> int:
        """
        Detailed explanation:

        For p=3: nums = [1, 2, 3, 4, 5, 6, 7]
        We can pair:
        - (1, 6) -> (1, 6) or swap bits to get different values
        - (2, 5) -> same
        - (3, 4) -> same

        Optimal strategy: move all bits to one number in each pair
        - (1, 6) -> (0 invalid, so use (1, 6) -> best is make (1, 6))
        - Actually we swap to minimize: (1, 6) -> (1, 6), (2, 5) -> (1, 6)...

        The trick: for each pair summing to 7, we can get (1, 6)
        So product = 7 * 6^3 = 7 * 216 = 1512

        General: (2^p - 1) * (2^p - 2)^(2^(p-1) - 1)
        """
        MOD = 10**9 + 7

        max_val = (1 << p) - 1
        base = max_val - 1
        num_pairs = max_val >> 1  # (2^p - 1) // 2 = 2^(p-1) - 1 when p > 1

        # Fast modular exponentiation
        def mod_pow(base, exp, mod):
            result = 1
            base %= mod
            while exp > 0:
                if exp & 1:
                    result = (result * base) % mod
                exp >>= 1
                base = (base * base) % mod
            return result

        return (max_val * mod_pow(base, num_pairs, MOD)) % MOD
