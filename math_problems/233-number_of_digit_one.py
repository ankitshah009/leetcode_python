#233. Number of Digit One
#Hard
#
#Given an integer n, count the total number of digit 1 appearing in all
#non-negative integers less than or equal to n.
#
#Example 1:
#Input: n = 13
#Output: 6
#
#Example 2:
#Input: n = 0
#Output: 0
#
#Constraints:
#    0 <= n <= 10^9

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        count = 0
        position = 1  # 1, 10, 100, 1000, ...

        while position <= n:
            # For each position, calculate contribution of 1s

            # higher: digits to the left of current position
            # current: digit at current position
            # lower: digits to the right of current position

            higher = n // (position * 10)
            current = (n // position) % 10
            lower = n % position

            # Count 1s at current position
            if current == 0:
                # Only from complete rounds
                count += higher * position
            elif current == 1:
                # Complete rounds + partial count
                count += higher * position + lower + 1
            else:  # current > 1
                # Complete rounds + full position (all numbers 0 to position-1)
                count += (higher + 1) * position

            position *= 10

        return count

    # Alternative recursive approach using digit DP
    def countDigitOneDP(self, n: int) -> int:
        if n <= 0:
            return 0

        s = str(n)
        memo = {}

        def dp(pos, count_ones, tight, started):
            if pos == len(s):
                return count_ones

            if (pos, count_ones, tight, started) in memo:
                return memo[(pos, count_ones, tight, started)]

            limit = int(s[pos]) if tight else 9
            result = 0

            for digit in range(0, limit + 1):
                new_tight = tight and (digit == limit)
                new_started = started or (digit > 0)
                new_count = count_ones + (1 if digit == 1 else 0)

                result += dp(pos + 1, new_count, new_tight, new_started)

            memo[(pos, count_ones, tight, started)] = result
            return result

        return dp(0, 0, True, False)
