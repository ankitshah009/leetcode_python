#1952. Three Divisors
#Easy
#
#Given an integer n, return true if n has exactly three positive divisors.
#Otherwise, return false.
#
#An integer m is a divisor of n if there exists an integer k such that
#n = k * m.
#
#Example 1:
#Input: n = 2
#Output: false
#Explanation: 2 has only two divisors: 1 and 2.
#
#Example 2:
#Input: n = 4
#Output: true
#Explanation: 4 has three divisors: 1, 2, and 4.
#
#Constraints:
#    1 <= n <= 10^4

class Solution:
    def isThree(self, n: int) -> bool:
        """
        A number has exactly 3 divisors iff it's a square of a prime.
        Divisors would be: 1, p, p^2.
        """
        import math

        # Check if perfect square
        sqrt_n = int(math.sqrt(n))
        if sqrt_n * sqrt_n != n:
            return False

        # Check if sqrt_n is prime
        if sqrt_n < 2:
            return False

        for i in range(2, int(math.sqrt(sqrt_n)) + 1):
            if sqrt_n % i == 0:
                return False

        return True


class SolutionCountDivisors:
    def isThree(self, n: int) -> bool:
        """
        Count all divisors directly.
        """
        count = 0

        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                if count > 3:
                    return False

        return count == 3


class SolutionOptimized:
    def isThree(self, n: int) -> bool:
        """
        Count divisors up to sqrt(n).
        """
        import math

        count = 0
        sqrt_n = int(math.sqrt(n))

        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                if i == n // i:
                    count += 1
                else:
                    count += 2

        return count == 3
