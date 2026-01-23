#1716. Calculate Money in Leetcode Bank
#Easy
#
#Hercy wants to save money for his first car. He puts money in the Leetcode bank
#every day.
#
#He starts by putting in $1 on Monday, the first day. Every day from Tuesday to
#Sunday, he will put in $1 more than the day before. On every subsequent Monday,
#he will put in $1 more than the previous Monday.
#
#Given n, return the total amount of money he will have in the Leetcode bank at
#the end of the nth day.
#
#Example 1:
#Input: n = 4
#Output: 10
#
#Example 2:
#Input: n = 10
#Output: 37
#
#Example 3:
#Input: n = 20
#Output: 96
#
#Constraints:
#    1 <= n <= 1000

class Solution:
    def totalMoney(self, n: int) -> int:
        """
        Math formula approach.
        Full weeks: each week starts with (week_num) and adds 1 each day
        Week k contributes: k + (k+1) + ... + (k+6) = 7k + 21
        """
        full_weeks = n // 7
        remaining_days = n % 7

        # Sum of full weeks: sum of (7k + 21) for k = 1 to full_weeks
        # = 7 * (1 + 2 + ... + full_weeks) + 21 * full_weeks
        # = 7 * full_weeks * (full_weeks + 1) / 2 + 21 * full_weeks
        full_week_sum = (7 * full_weeks * (full_weeks + 1) // 2) + (21 * full_weeks)

        # Remaining days in partial week (week full_weeks + 1)
        # Start value is (full_weeks + 1)
        start = full_weeks + 1
        partial_sum = sum(start + i for i in range(remaining_days))

        return full_week_sum + partial_sum


class SolutionSimple:
    def totalMoney(self, n: int) -> int:
        """
        Direct simulation.
        """
        total = 0
        week = 0
        day_of_week = 0

        for _ in range(n):
            if day_of_week == 0:
                week += 1
            total += week + day_of_week
            day_of_week = (day_of_week + 1) % 7

        return total


class SolutionArithmetic:
    def totalMoney(self, n: int) -> int:
        """
        Using arithmetic series formulas.
        """
        weeks = n // 7
        days = n % 7

        # Each complete week k (1-indexed) contributes:
        # k + (k+1) + (k+2) + ... + (k+6) = 7k + 21

        # Sum of complete weeks = sum of (7k + 21) for k = 1 to weeks
        complete = 7 * weeks * (weeks + 1) // 2 + 21 * weeks

        # Partial week: starts at (weeks + 1), adds (weeks + 1 + i) for i = 0 to days-1
        # = days * (weeks + 1) + (0 + 1 + ... + (days - 1))
        # = days * (weeks + 1) + days * (days - 1) / 2
        partial = days * (weeks + 1) + days * (days - 1) // 2

        return complete + partial
