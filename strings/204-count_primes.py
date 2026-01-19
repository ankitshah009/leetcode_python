#204. Count Primes
#Medium
#
#Given an integer n, return the number of prime numbers that are strictly less
#than n.
#
#Example 1:
#Input: n = 10
#Output: 4
#Explanation: There are 4 prime numbers less than 10: 2, 3, 5, 7.
#
#Example 2:
#Input: n = 0
#Output: 0
#
#Example 3:
#Input: n = 1
#Output: 0
#
#Constraints:
#    0 <= n <= 5 * 10^6

class Solution:
    def countPrimes(self, n: int) -> int:
        """Sieve of Eratosthenes"""
        if n < 2:
            return 0

        # Initialize all as prime
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        # Mark multiples of each prime as not prime
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Start from i*i because smaller multiples already marked
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)


class SolutionOptimized:
    """Optimized sieve with only odd numbers"""

    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        # Only track odd numbers: index i represents 2*i + 1
        # is_prime[i] = True means (2*i + 1) is prime
        size = (n - 1) // 2
        is_prime = [True] * size

        # Sieve
        for i in range(int(n ** 0.5) // 2):
            if is_prime[i]:
                # Number represented by index i
                p = 2 * i + 3
                # Mark multiples of p starting from p*p
                start = (p * p - 3) // 2
                for j in range(start, size, p):
                    is_prime[j] = False

        # Count primes: 2 + all odd primes
        return sum(is_prime) + 1


class SolutionBitArray:
    """Using bit manipulation for memory efficiency"""

    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        # Use bytes instead of list of booleans
        is_composite = bytearray(n)

        count = 0
        for i in range(2, n):
            if not is_composite[i]:
                count += 1
                for j in range(i * i, n, i):
                    is_composite[j] = 1

        return count
