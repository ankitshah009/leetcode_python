#1780. Check if Number is a Sum of Powers of Three
#Medium
#
#Given an integer n, return true if it is possible to represent n as the sum of
#distinct powers of three. Otherwise, return false.
#
#An integer y is a power of three if there exists an integer x such that y == 3^x.
#
#Example 1:
#Input: n = 12
#Output: true
#Explanation: 12 = 3^1 + 3^2
#
#Example 2:
#Input: n = 91
#Output: true
#Explanation: 91 = 3^0 + 3^2 + 3^4
#
#Example 3:
#Input: n = 21
#Output: false
#
#Constraints:
#    1 <= n <= 10^7

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Convert to base 3 - only 0s and 1s allowed (no digit can be 2+).
        """
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True


class SolutionIterative:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Greedy: try to subtract largest powers of 3.
        """
        # Find largest power of 3 <= n
        power = 1
        while power * 3 <= n:
            power *= 3

        while n > 0:
            if n >= power:
                n -= power
            power //= 3

        return n == 0


class SolutionRecursive:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Recursive approach.
        """
        if n == 0:
            return True
        if n % 3 == 2:
            return False
        return self.checkPowersOfThree(n // 3)


class SolutionSet:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Generate all subset sums of powers of 3.
        """
        # Generate powers of 3 up to n
        powers = []
        p = 1
        while p <= n:
            powers.append(p)
            p *= 3

        # Check if n can be formed
        sums = {0}
        for p in powers:
            sums = sums | {s + p for s in sums}

        return n in sums
