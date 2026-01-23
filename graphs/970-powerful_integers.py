#970. Powerful Integers
#Medium
#
#Given three integers x, y, and bound, return a list of all the powerful
#integers that have a value less than or equal to bound.
#
#An integer is powerful if it can be represented as x^i + y^j for some integers
#i >= 0 and j >= 0.
#
#You may return the answer in any order. The answer is guaranteed to be unique.
#
#Example 1:
#Input: x = 2, y = 3, bound = 10
#Output: [2,3,4,5,7,9,10]
#
#Example 2:
#Input: x = 3, y = 5, bound = 15
#Output: [2,4,6,8,10,14]
#
#Constraints:
#    1 <= x, y <= 100
#    0 <= bound <= 10^6

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        """
        Enumerate all x^i + y^j <= bound.
        """
        result = set()

        # Generate powers of x
        powers_x = [1]
        if x > 1:
            val = x
            while val < bound:
                powers_x.append(val)
                val *= x

        # Generate powers of y
        powers_y = [1]
        if y > 1:
            val = y
            while val < bound:
                powers_y.append(val)
                val *= y

        # Combine
        for px in powers_x:
            for py in powers_y:
                total = px + py
                if total <= bound:
                    result.add(total)

        return list(result)


class SolutionDirect:
    """Direct enumeration"""

    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        result = set()

        i = 0
        while x ** i <= bound:
            j = 0
            while x ** i + y ** j <= bound:
                result.add(x ** i + y ** j)
                j += 1
                if y == 1:
                    break

            i += 1
            if x == 1:
                break

        return list(result)


class SolutionLog:
    """Using logarithms for bounds"""

    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        import math

        result = set()

        # Max power for x
        max_i = 0 if x == 1 else int(math.log(bound) / math.log(x)) + 1
        max_j = 0 if y == 1 else int(math.log(bound) / math.log(y)) + 1

        for i in range(max_i + 1):
            for j in range(max_j + 1):
                val = x ** i + y ** j
                if val <= bound:
                    result.add(val)

        return list(result)
