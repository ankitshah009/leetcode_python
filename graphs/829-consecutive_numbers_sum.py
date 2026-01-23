#829. Consecutive Numbers Sum
#Hard
#
#Given an integer n, return the number of ways you can write n as the sum of
#consecutive positive integers.
#
#Example 1:
#Input: n = 5
#Output: 2
#Explanation: 5 = 2 + 3
#
#Example 2:
#Input: n = 9
#Output: 3
#Explanation: 9 = 4 + 5 = 2 + 3 + 4
#
#Example 3:
#Input: n = 15
#Output: 4
#Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
#
#Constraints:
#    1 <= n <= 10^9

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        """
        Sum of k consecutive integers starting from x:
        n = x + (x+1) + ... + (x+k-1) = k*x + k*(k-1)/2

        So: k*x = n - k*(k-1)/2
        x = (n - k*(k-1)/2) / k

        x must be positive integer.
        """
        count = 0
        k = 1

        while k * (k - 1) // 2 < n:
            # n - k*(k-1)/2 must be divisible by k and positive
            remainder = n - k * (k - 1) // 2
            if remainder > 0 and remainder % k == 0:
                count += 1
            k += 1

        return count


class SolutionMath:
    """Mathematical approach with optimization"""

    def consecutiveNumbersSum(self, n: int) -> int:
        """
        From n = k*x + k*(k-1)/2:
        2n = k*(2x + k - 1)

        Let 2x + k - 1 = m, then 2n = k*m
        Since x >= 1: m >= k
        Also m and k have different parities (one odd, one even)

        Count odd divisors k of 2n where k <= sqrt(2n) and (2n/k - k + 1) is even and positive
        """
        count = 0
        k = 1

        # k * (k + 1) / 2 <= n means we need k where k*(k-1)/2 < n
        # Roughly k <= sqrt(2n)
        while k * k <= 2 * n:
            # Check if (2n - k^2 + k) / (2k) is positive integer
            # Equivalent to (2n/k - k + 1) / 2 being positive integer
            # Which means 2n % k == 0 and (2n/k - k + 1) even and positive

            numerator = 2 * n - k * (k - 1)
            if numerator > 0 and numerator % (2 * k) == 0:
                count += 1
            k += 1

        return count


class SolutionOddDivisors:
    """Count odd divisors approach"""

    def consecutiveNumbersSum(self, n: int) -> int:
        """
        Equivalent to counting odd divisors of n (after removing factors of 2).
        """
        # Remove factors of 2
        while n % 2 == 0:
            n //= 2

        # Count divisors of remaining odd number
        count = 1
        d = 3

        while d * d <= n:
            power = 0
            while n % d == 0:
                n //= d
                power += 1
            count *= (power + 1)
            d += 2

        if n > 1:
            count *= 2  # n is a prime factor

        return count
