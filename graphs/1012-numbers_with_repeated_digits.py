#1012. Numbers With Repeated Digits
#Hard
#
#Given an integer n, return the number of positive integers in the range [1, n]
#that have at least one repeated digit.
#
#Example 1:
#Input: n = 20
#Output: 1
#Explanation: Only 11 has a repeated digit.
#
#Example 2:
#Input: n = 100
#Output: 10
#
#Example 3:
#Input: n = 1000
#Output: 262
#
#Constraints:
#    1 <= n <= 10^9

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        """
        Count numbers without repeated digits, subtract from n.
        """
        digits = [int(d) for d in str(n)]
        num_digits = len(digits)

        # Count numbers without repeated digits

        # 1. Count numbers with fewer digits
        count = 0
        for length in range(1, num_digits):
            # First digit: 1-9 (9 choices)
            # Remaining: choose from unused (9, 8, 7, ...)
            count += 9 * self.permutation(9, length - 1)

        # 2. Count numbers with same number of digits
        seen = set()
        for i, d in enumerate(digits):
            # Count numbers with smaller digit at position i
            for smaller in range(0 if i > 0 else 1, d):
                if smaller in seen:
                    continue
                # Remaining positions: permutation of unused digits
                remaining = num_digits - i - 1
                unused = 10 - i - 1
                count += self.permutation(unused, remaining)

            # If current digit already seen, no valid numbers
            if d in seen:
                break
            seen.add(d)
        else:
            # n itself has no repeated digits
            count += 1

        return n - count

    def permutation(self, n, r):
        if r > n or r < 0:
            return 0
        result = 1
        for i in range(r):
            result *= (n - i)
        return result


class SolutionDigitDP:
    """Digit DP approach"""

    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        length = len(s)

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(pos: int, mask: int, tight: bool, started: bool) -> int:
            """Count numbers without repeated digits."""
            if pos == length:
                return 1 if started else 0

            limit = int(s[pos]) if tight else 9
            result = 0

            if not started:
                # Leading zero: don't start yet
                result += dp(pos + 1, mask, False, False)
                # Start with digit 1 to limit
                for d in range(1, limit + 1):
                    result += dp(pos + 1, 1 << d, tight and d == limit, True)
            else:
                for d in range(0, limit + 1):
                    if mask & (1 << d):
                        continue  # Digit already used
                    result += dp(pos + 1, mask | (1 << d), tight and d == limit, True)

            return result

        unique = dp(0, 0, True, False)
        return n - unique
