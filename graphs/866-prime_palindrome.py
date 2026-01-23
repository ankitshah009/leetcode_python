#866. Prime Palindrome
#Medium
#
#Given an integer n, return the smallest prime palindrome greater than or equal to n.
#
#An integer is prime if it has exactly two divisors: 1 and itself. Note that 1
#is not a prime number.
#
#An integer is a palindrome if it reads the same from left to right as it does
#from right to left.
#
#Example 1:
#Input: n = 6
#Output: 7
#
#Example 2:
#Input: n = 8
#Output: 11
#
#Example 3:
#Input: n = 13
#Output: 101
#
#Constraints:
#    1 <= n <= 10^8

class Solution:
    def primePalindrome(self, n: int) -> int:
        """
        Generate palindromes and check primality.
        Key insight: all even-length palindromes (except 11) are divisible by 11.
        """
        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True

        def generate_palindromes():
            """Generate odd-length palindromes and 11"""
            yield 2
            yield 11

            for length in range(1, 6):  # Generates up to 10^9
                # Odd length palindromes
                for half in range(10**(length-1) if length > 1 else 1, 10**length):
                    s = str(half)
                    pal = int(s + s[-2::-1])
                    yield pal

        for pal in generate_palindromes():
            if pal >= n and is_prime(pal):
                return pal


class SolutionBruteForce:
    """Check each number (slow but simple)"""

    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True

        def is_palindrome(x):
            return str(x) == str(x)[::-1]

        while True:
            # Skip even-length numbers > 11 (divisible by 11)
            if 10**7 < n < 10**8:
                n = 10**8

            if is_palindrome(n) and is_prime(n):
                return n
            n += 1


class SolutionOptimized:
    """Generate palindromes directly"""

    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True

        # Special cases
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11

        # Generate odd-length palindromes
        for length in range(1, 6):
            start = max(10**(length-1) if length > 1 else 1,
                       int(str(n)[:length]) if len(str(n)) == 2*length-1 else 10**(length-1))

            for half in range(start, 10**length):
                s = str(half)
                pal = int(s + s[-2::-1])
                if pal >= n and is_prime(pal):
                    return pal

        return -1
