#357. Count Numbers with Unique Digits
#Medium
#
#Given an integer n, return the count of all numbers with unique digits, x,
#where 0 <= x < 10^n.
#
#Example 1:
#Input: n = 2
#Output: 91
#Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
#excluding 11, 22, 33, 44, 55, 66, 77, 88, 99
#
#Example 2:
#Input: n = 0
#Output: 1
#
#Constraints:
#    0 <= n <= 8

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        Mathematical counting approach.

        For 1 digit: 10 (0-9)
        For 2 digits: 9 * 9 = 81 (first digit 1-9, second digit 0-9 except first)
        For 3 digits: 9 * 9 * 8 = 648
        For k digits: 9 * 9 * 8 * 7 * ... * (11-k)
        """
        if n == 0:
            return 1

        total = 10  # Single digit numbers (0-9)
        unique_digits = 9  # Choices for subsequent positions
        available_digits = 9  # First digit choices (1-9)

        for i in range(2, min(n + 1, 11)):  # Max 10 unique digits (0-9)
            unique_digits *= available_digits
            total += unique_digits
            available_digits -= 1

        return total


class SolutionDP:
    """DP approach"""

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        # dp[i] = count of i-digit numbers with unique digits
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty number (just 0)
        dp[1] = 10

        for i in range(2, n + 1):
            # First digit: 9 choices (1-9)
            # Remaining i-1 digits: 9 * 8 * ... choices
            count = 9
            multiplier = 9
            for j in range(1, i):
                count *= multiplier
                multiplier -= 1
            dp[i] = dp[i - 1] + count

        return dp[n]


class SolutionBacktrack:
    """Backtracking approach (for reference)"""

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        count = 0

        def backtrack(num_digits, used, started):
            nonlocal count

            if num_digits == n:
                count += 1
                return

            for digit in range(10):
                if used & (1 << digit):
                    continue

                # Can't start with 0 for multi-digit numbers
                if not started and digit == 0 and num_digits < n - 1:
                    backtrack(num_digits + 1, used, False)
                else:
                    backtrack(num_digits + 1, used | (1 << digit), True)

        backtrack(0, 0, False)
        return count
