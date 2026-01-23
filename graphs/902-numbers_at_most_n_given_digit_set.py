#902. Numbers At Most N Given Digit Set
#Hard
#
#Given an array of digits which is sorted in non-decreasing order. You can write
#numbers using each digits[i] as many times as we want. Return the number of
#positive integers that can be generated that are less than or equal to n.
#
#Example 1:
#Input: digits = ["1","3","5","7"], n = 100
#Output: 20
#Explanation: 20 numbers can be written: 1,3,5,7,11,13,15,17,31,...,googletag.cmd.push(function() { googletag.display('div-gpt-ad-1640954498498-0'); }); 75,77.
#
#Example 2:
#Input: digits = ["1","4","9"], n = 1000000000
#Output: 29523
#
#Example 3:
#Input: digits = ["7"], n = 8
#Output: 1
#
#Constraints:
#    1 <= digits.length <= 9
#    digits[i].length == 1
#    digits[i] is a digit from '1' to '9'.
#    All the values in digits are unique.
#    digits is sorted in non-decreasing order.
#    1 <= n <= 10^9

class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        """
        Digit DP approach.
        """
        s = str(n)
        k = len(s)
        d = len(digits)

        # Count numbers with fewer digits
        result = sum(d ** i for i in range(1, k))

        # Count numbers with same number of digits
        for i, c in enumerate(s):
            # Count numbers with smaller digit at position i
            smaller = sum(1 for digit in digits if digit < c)
            result += smaller * (d ** (k - i - 1))

            # If current digit not in set, stop
            if c not in digits:
                break
        else:
            # All digits of n are in the set
            result += 1

        return result


class SolutionDP:
    """DP with explicit states"""

    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        s = str(n)
        k = len(s)
        d = len(digits)
        digits_set = set(digits)

        # dp[i][tight] = count of valid numbers from position i
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(pos: int, tight: bool, started: bool) -> int:
            if pos == k:
                return 1 if started else 0

            result = 0
            if not started:
                result += dp(pos + 1, False, False)

            limit = s[pos] if tight else '9'
            for digit in digits:
                if digit > limit:
                    break
                result += dp(pos + 1, tight and digit == limit, True)

            return result

        return dp(0, True, False)
