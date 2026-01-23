#869. Reordered Power of 2
#Medium
#
#You are given an integer n. We reorder the digits in any order (including the
#original order) such that the leading digit is not zero.
#
#Return true if and only if we can do this so that the resulting number is a
#power of two.
#
#Example 1:
#Input: n = 1
#Output: true
#
#Example 2:
#Input: n = 10
#Output: false
#
#Constraints:
#    1 <= n <= 10^9

from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Compare digit counts of n with all powers of 2.
        """
        n_count = Counter(str(n))

        # Check all powers of 2 up to 10^9
        power = 1
        while power <= 10**9:
            if Counter(str(power)) == n_count:
                return True
            power *= 2

        return False


class SolutionPrecompute:
    """Precompute all power of 2 signatures"""

    def reorderedPowerOf2(self, n: int) -> bool:
        def signature(x):
            return tuple(sorted(str(x)))

        # All powers of 2 up to 10^9
        powers = set()
        p = 1
        while p <= 10**9:
            powers.add(signature(p))
            p *= 2

        return signature(n) in powers


class SolutionPermutation:
    """Check all permutations (slow for large n)"""

    def reorderedPowerOf2(self, n: int) -> bool:
        from itertools import permutations

        def is_power_of_2(x):
            return x > 0 and (x & (x - 1)) == 0

        digits = str(n)

        for perm in set(permutations(digits)):
            if perm[0] != '0':
                num = int(''.join(perm))
                if is_power_of_2(num):
                    return True

        return False


class SolutionDigitCount:
    """Using digit count as key"""

    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(x):
            count = [0] * 10
            while x:
                count[x % 10] += 1
                x //= 10
            return tuple(count)

        n_count = count_digits(n)

        power = 1
        while power <= 10**9:
            if count_digits(power) == n_count:
                return True
            power *= 2

        return False
