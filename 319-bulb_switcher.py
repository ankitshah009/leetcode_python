#319. Bulb Switcher
#Medium
#
#There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off
#every second bulb. On the third round, you toggle every third bulb (turning on if it's off
#or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round,
#you only toggle the last bulb.
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
        # A bulb ends up ON if it's toggled an odd number of times
        # A bulb at position i is toggled once for each divisor of i
        # Only perfect squares have an odd number of divisors
        # So the answer is the count of perfect squares <= n
        return int(math.sqrt(n))
