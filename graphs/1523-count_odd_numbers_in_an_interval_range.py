#1523. Count Odd Numbers in an Interval Range
#Easy
#
#Given two non-negative integers low and high. Return the count of odd numbers
#between low and high (inclusive).
#
#Example 1:
#Input: low = 3, high = 7
#Output: 3
#Explanation: The odd numbers between 3 and 7 are [3,5,7].
#
#Example 2:
#Input: low = 8, high = 10
#Output: 1
#Explanation: The odd numbers between 8 and 10 are [9].
#
#Constraints:
#    0 <= low <= high <= 10^9

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Count odds from 0 to n is (n + 1) // 2.
        Count from low to high = count(0 to high) - count(0 to low-1).
        """
        # Odds in [0, n] = (n + 1) // 2
        # Odds in [low, high] = odds_to(high) - odds_to(low - 1)
        return (high + 1) // 2 - low // 2


class SolutionCases:
    def countOdds(self, low: int, high: int) -> int:
        """
        Case analysis based on parity of endpoints.
        """
        count = (high - low) // 2

        # If either endpoint is odd, add 1
        if low % 2 == 1 or high % 2 == 1:
            count += 1

        return count


class SolutionFormula:
    def countOdds(self, low: int, high: int) -> int:
        """
        Direct formula.
        In range [a, b], number of odds = (b - a) // 2 + (1 if a or b is odd else 0)
        Or equivalently: (b - a + 1 + (a % 2)) // 2
        """
        return (high - low + 1 + (low % 2)) // 2


class SolutionBruteForce:
    def countOdds(self, low: int, high: int) -> int:
        """
        Brute force (for small ranges only).
        """
        count = 0
        for num in range(low, high + 1):
            if num % 2 == 1:
                count += 1
        return count


class SolutionBitwise:
    def countOdds(self, low: int, high: int) -> int:
        """
        Bitwise operations.
        """
        # low & 1 is 1 if low is odd, 0 if even
        # high & 1 is 1 if high is odd, 0 if even

        # Base count
        count = (high - low) >> 1

        # Add 1 if either endpoint is odd
        if (low & 1) | (high & 1):
            count += 1

        return count
