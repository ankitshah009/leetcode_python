#319. Bulb Switcher
#Medium
#
#There are n bulbs that are initially off. You first turn on all the bulbs,
#then you turn off every second bulb.
#
#On the third round, you toggle every third bulb (turning on if it's off or
#turning off if it's on). For the ith round, you toggle every i bulb. For the
#nth round, you only toggle the last bulb.
#
#Return the number of bulbs that are on after n rounds.
#
#Example 1:
#Input: n = 3
#Output: 1
#Explanation: At first, the three bulbs are [off, off, off].
#After the first round, the three bulbs are [on, on, on].
#After the second round, the three bulbs are [on, off, on].
#After the third round, the three bulbs are [on, off, off].
#So you should return 1 because there is only one bulb is on.
#
#Example 2:
#Input: n = 0
#Output: 0
#
#Example 3:
#Input: n = 1
#Output: 1
#
#Constraints:
#    0 <= n <= 10^9

import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        Mathematical insight:
        - Bulb i is toggled once for each of its divisors
        - A bulb ends up ON if toggled odd number of times
        - Only perfect squares have odd number of divisors
        - Answer is count of perfect squares <= n = floor(sqrt(n))
        """
        return int(math.sqrt(n))


class SolutionBruteForce:
    """Brute force simulation (for small n only)"""

    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0

        bulbs = [False] * (n + 1)  # 1-indexed

        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                bulbs[j] = not bulbs[j]

        return sum(bulbs)


class SolutionDivisors:
    """Count numbers with odd divisors"""

    def bulbSwitch(self, n: int) -> int:
        count = 0
        i = 1
        while i * i <= n:
            count += 1
            i += 1
        return count
