#1175. Prime Arrangements
#Easy
#
#Return the number of permutations of 1 to n so that prime numbers are at
#prime indices (1-indexed.)
#
#(Recall that an integer is prime if and only if it is greater than 1, and
#cannot be written as the product of two positive integers both smaller than it.)
#
#Since the answer may be large, return the answer modulo 10^9 + 7.
#
#Example 1:
#Input: n = 5
#Output: 12
#Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1]
#is not because the prime number 5 is at index 1.
#
#Example 2:
#Input: n = 100
#Output: 682289015
#
#Constraints:
#    1 <= n <= 100

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        """
        Count primes up to n.
        Answer = (count of primes)! * (count of non-primes)!
        """
        MOD = 10**9 + 7

        def is_prime(num):
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        def factorial(k):
            result = 1
            for i in range(2, k + 1):
                result = (result * i) % MOD
            return result

        # Count primes from 1 to n
        prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))
        non_prime_count = n - prime_count

        return (factorial(prime_count) * factorial(non_prime_count)) % MOD


class SolutionSieve:
    def numPrimeArrangements(self, n: int) -> int:
        """Using Sieve of Eratosthenes for prime counting"""
        MOD = 10**9 + 7

        # Sieve of Eratosthenes
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n + 1, i):
                    is_prime[j] = False

        prime_count = sum(is_prime)
        non_prime_count = n - prime_count

        # Calculate factorials
        result = 1
        for i in range(2, prime_count + 1):
            result = (result * i) % MOD
        for i in range(2, non_prime_count + 1):
            result = (result * i) % MOD

        return result


class SolutionPrecomputed:
    def numPrimeArrangements(self, n: int) -> int:
        """Precomputed primes up to 100"""
        MOD = 10**9 + 7

        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

        prime_count = sum(1 for i in range(1, n + 1) if i in primes)
        non_prime_count = n - prime_count

        result = 1
        for i in range(2, prime_count + 1):
            result = (result * i) % MOD
        for i in range(2, non_prime_count + 1):
            result = (result * i) % MOD

        return result
