#600. Non-negative Integers without Consecutive Ones
#Hard
#
#Given a positive integer n, return the number of the integers in the range [0, n]
#whose binary representations do not contain consecutive ones.
#
#Example 1:
#Input: n = 5
#Output: 5
#Explanation:
#0 : 0
#1 : 1
#2 : 10
#3 : 11 (has consecutive ones - invalid)
#4 : 100
#5 : 101
#
#Example 2:
#Input: n = 1
#Output: 2
#
#Example 3:
#Input: n = 2
#Output: 3
#
#Constraints:
#    1 <= n <= 10^9

class Solution:
    def findIntegers(self, n: int) -> int:
        """
        Digit DP with Fibonacci-like counting.
        Count of k-bit numbers without consecutive 1s = fib(k+2)
        """
        # Precompute Fibonacci numbers
        fib = [1, 2]
        for i in range(2, 32):
            fib.append(fib[-1] + fib[-2])

        # Convert n to binary
        bits = bin(n)[2:]
        k = len(bits)

        count = 0
        prev_bit = 0

        for i, bit in enumerate(bits):
            if bit == '1':
                # Add count of all valid numbers with 0 at position i
                # This gives us numbers less than current prefix
                count += fib[k - i - 1]

                # If previous bit was also 1, we can't continue
                if prev_bit == 1:
                    return count

                prev_bit = 1
            else:
                prev_bit = 0

        # Include n itself
        return count + 1


class SolutionMemo:
    """Digit DP with memoization"""

    def findIntegers(self, n: int) -> int:
        from functools import lru_cache

        bits = bin(n)[2:]
        k = len(bits)

        @lru_cache(maxsize=None)
        def dp(pos, prev_one, tight):
            if pos == k:
                return 1

            limit = int(bits[pos]) if tight else 1
            count = 0

            for digit in range(limit + 1):
                if digit == 1 and prev_one:
                    continue  # Skip consecutive ones

                new_tight = tight and (digit == limit)
                count += dp(pos + 1, digit == 1, new_tight)

            return count

        return dp(0, False, True)
