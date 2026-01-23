#1922. Count Good Numbers
#Medium
#
#A digit string is good if the digits (0-indexed) at even indices are even and
#the digits at odd indices are prime (2, 3, 5, or 7).
#
#For example, "2582" is good because the digits (2 and 8) at even positions are
#even and the digits (5 and 2) at odd positions are prime. However, "3245" is
#not good because 3 is at an even index but is not even.
#
#Given an integer n, return the total number of good digit strings of length n.
#Since the answer may be large, return it modulo 10^9 + 7.
#
#A digit string is a string consisting of digits 0 through 9 that may contain
#leading zeros.
#
#Example 1:
#Input: n = 1
#Output: 5
#
#Example 2:
#Input: n = 4
#Output: 400
#
#Example 3:
#Input: n = 50
#Output: 564908303
#
#Constraints:
#    1 <= n <= 10^15

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        Even positions: 5 choices (0, 2, 4, 6, 8)
        Odd positions: 4 choices (2, 3, 5, 7)

        Count of even positions: (n + 1) // 2
        Count of odd positions: n // 2

        Total = 5^even_count * 4^odd_count
        """
        MOD = 10**9 + 7

        even_count = (n + 1) // 2
        odd_count = n // 2

        return pow(5, even_count, MOD) * pow(4, odd_count, MOD) % MOD


class SolutionExplicit:
    def countGoodNumbers(self, n: int) -> int:
        """
        With explicit modular exponentiation.
        """
        MOD = 10**9 + 7

        def mod_pow(base: int, exp: int, mod: int) -> int:
            result = 1
            base %= mod
            while exp > 0:
                if exp & 1:
                    result = result * base % mod
                exp >>= 1
                base = base * base % mod
            return result

        even_positions = (n + 1) // 2  # Positions 0, 2, 4, ...
        odd_positions = n // 2          # Positions 1, 3, 5, ...

        return mod_pow(5, even_positions, MOD) * mod_pow(4, odd_positions, MOD) % MOD
