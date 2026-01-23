#1067. Digit Count in Range
#Hard
#
#Given a single-digit integer d and two integers low and high, return the
#number of times that d occurs as a digit in all integers in the inclusive
#range [low, high].
#
#Example 1:
#Input: d = 1, low = 1, high = 13
#Output: 6
#Explanation: The digit d = 1 occurs 6 times in 1, 10, 11, 12, 13.
#Note that d = 1 occurs twice in 11.
#
#Example 2:
#Input: d = 3, low = 100, high = 250
#Output: 35
#Explanation: The digit d = 3 occurs 35 times in 103,113,123,130,131,...,googl.
#
#Constraints:
#    0 <= d <= 9
#    1 <= low <= high <= 2 * 10^8

class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        """
        Digit DP: Count d in [0, high] - count d in [0, low-1]
        """
        def count_up_to(n):
            if n < 0:
                return 0

            digits = [int(x) for x in str(n)]
            num_digits = len(digits)

            # dp[pos][count][tight][started]
            # - pos: current position
            # - tight: still bounded by n
            # - started: have we placed non-zero digit
            from functools import lru_cache

            @lru_cache(maxsize=None)
            def dp(pos, tight, started):
                if pos == num_digits:
                    return 0

                limit = digits[pos] if tight else 9
                result = 0

                for digit in range(0, limit + 1):
                    new_tight = tight and (digit == limit)
                    new_started = started or (digit != 0)

                    # Count d at this position
                    if digit == d and (new_started or d == 0):
                        if new_started or d != 0:
                            # Count how many numbers have this digit here
                            # Remaining positions can be anything within bounds
                            if new_tight:
                                remaining = n % (10 ** (num_digits - pos - 1)) + 1
                            else:
                                remaining = 10 ** (num_digits - pos - 1)
                            result += remaining

                    result += dp(pos + 1, new_tight, new_started)

                return result

            # Alternative: count digit d occurrences directly
            return count_digit(n, d)

        def count_digit(n, d):
            """Count occurrences of digit d in all numbers from 0 to n"""
            if n < 0:
                return 0

            count = 0
            pos = 1  # Current digit position (1, 10, 100, ...)

            while pos <= n:
                # Divide number into higher, current, lower parts
                higher = n // (pos * 10)
                current = (n // pos) % 10
                lower = n % pos

                if d == 0:
                    # Special case for 0 - can't have leading zeros
                    if higher > 0:
                        count += (higher - 1) * pos
                        if current > d:
                            count += pos
                        elif current == d:
                            count += lower + 1
                else:
                    count += higher * pos
                    if current > d:
                        count += pos
                    elif current == d:
                        count += lower + 1

                pos *= 10

            return count

        return count_digit(high, d) - count_digit(low - 1, d)


class SolutionSimple:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        """Cleaner implementation"""
        def count(n, d):
            if n < 0:
                return 0

            result = 0
            multiplier = 1

            while multiplier <= n:
                divider = multiplier * 10
                result += (n // divider) * multiplier

                current_digit = (n % divider) // multiplier

                if current_digit > d:
                    result += multiplier
                elif current_digit == d:
                    result += n % multiplier + 1

                # Handle d=0 case (no leading zeros)
                if d == 0:
                    result -= multiplier

                multiplier *= 10

            return result

        return count(high, d) - count(low - 1, d)
