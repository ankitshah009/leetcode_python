#991. Broken Calculator
#Medium
#
#There is a broken calculator that has the integer startValue on its display
#initially. In one operation, you can:
#- multiply the number on display by 2, or
#- subtract 1 from the number on display.
#
#Given two integers startValue and target, return the minimum number of
#operations needed to display target on the calculator.
#
#Example 1:
#Input: startValue = 2, target = 3
#Output: 2
#Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
#
#Example 2:
#Input: startValue = 5, target = 8
#Output: 2
#
#Example 3:
#Input: startValue = 3, target = 10
#Output: 3
#
#Constraints:
#    1 <= startValue, target <= 10^9

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        """
        Work backwards from target: divide by 2 or add 1.
        """
        ops = 0

        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            ops += 1

        # Now target <= startValue, need (startValue - target) subtractions
        return ops + (startValue - target)


class SolutionForward:
    """Forward thinking explanation"""

    def brokenCalc(self, startValue: int, target: int) -> int:
        """
        Key insight: work backwards.
        - If target > start: multiply is better than subtract
        - If target is odd, must add 1 before dividing (reverse of -1 then *2)
        - If target is even, divide by 2 (reverse of *2)
        """
        ops = 0

        while target > startValue:
            ops += 1
            if target % 2 == 1:
                target += 1
            else:
                target //= 2

        return ops + (startValue - target)


class SolutionRecursive:
    """Recursive with memoization"""

    def brokenCalc(self, startValue: int, target: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def ops(t):
            if t <= startValue:
                return startValue - t

            if t % 2 == 0:
                return 1 + ops(t // 2)
            else:
                return 1 + ops(t + 1)

        return ops(target)
