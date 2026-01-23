#1808. Maximize Number of Nice Divisors
#Hard
#
#You are given a positive integer primeFactors. You are asked to construct a
#positive integer n that satisfies the following conditions:
#- The number of prime factors of n (not necessarily distinct) is at most
#  primeFactors.
#- The number of nice divisors of n is maximized. Note that a divisor of n is
#  nice if it is divisible by every prime factor of n.
#
#Return the number of nice divisors of the constructed integer n. Since that
#number can be too large, return it modulo 10^9 + 7.
#
#Note that a prime number can divide itself.
#
#Example 1:
#Input: primeFactors = 5
#Output: 6
#Explanation: 200 = 2^3 * 5^2 = 2^3 * 5^2
#Nice divisors: 200, 100, 40, 20, 8, 4 (divisible by 2*5=10)
#Or equivalently, n = p1^a1 * p2^a2 * ... with a1+a2+...=5
#Number of nice divisors = a1 * a2 * ...
#Maximum is 3 * 2 = 6
#
#Example 2:
#Input: primeFactors = 8
#Output: 18
#
#Constraints:
#    1 <= primeFactors <= 10^9

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        """
        Maximize product of parts summing to primeFactors.
        Use 3s as much as possible, similar to Integer Break problem.
        """
        MOD = 10**9 + 7

        if primeFactors <= 3:
            return primeFactors

        # Remainder when dividing by 3
        remainder = primeFactors % 3
        quotient = primeFactors // 3

        if remainder == 0:
            # All 3s
            return pow(3, quotient, MOD)
        elif remainder == 1:
            # Use one 4 (= 2*2) instead of 3+1
            return (pow(3, quotient - 1, MOD) * 4) % MOD
        else:  # remainder == 2
            # Use one 2
            return (pow(3, quotient, MOD) * 2) % MOD


class SolutionExplained:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        """
        Detailed explanation:

        If n = p1^a1 * p2^a2 * ... * pk^ak, then:
        - Total prime factors = a1 + a2 + ... + ak = primeFactors
        - Nice divisors = a1 * a2 * ... * ak

        Problem reduces to: maximize product of integers summing to primeFactors.

        Mathematical insight:
        - 2 = 2 (product 2)
        - 3 = 3 (product 3)
        - 4 = 2+2 = 2*2 (product 4)
        - 5 = 2+3 = 2*3 (product 6)
        - 6 = 3+3 = 3*3 (product 9) > 2+2+2 = 8

        So use 3s as much as possible, use 2s for remainder.
        """
        MOD = 10**9 + 7

        if primeFactors == 1:
            return 1
        if primeFactors == 2:
            return 2
        if primeFactors == 3:
            return 3

        q, r = divmod(primeFactors, 3)

        if r == 0:
            return pow(3, q, MOD)
        elif r == 1:
            # 3*1 < 2*2, so convert one 3 to two 2s
            return pow(3, q - 1, MOD) * 4 % MOD
        else:
            return pow(3, q, MOD) * 2 % MOD
