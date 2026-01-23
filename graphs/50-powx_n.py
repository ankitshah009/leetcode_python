#50. Pow(x, n)
#Medium
#
#Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
#
#Example 1:
#Input: x = 2.00000, n = 10
#Output: 1024.00000
#
#Example 2:
#Input: x = 2.10000, n = 3
#Output: 9.26100
#
#Example 3:
#Input: x = 2.00000, n = -2
#Output: 0.25000
#Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
#
#Constraints:
#    -100.0 < x < 100.0
#    -2^31 <= n <= 2^31 - 1
#    n is an integer.
#    Either x is not zero or n > 0.
#    -10^4 <= x^n <= 10^4

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Binary exponentiation (iterative) - O(log n).
        """
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        while n > 0:
            if n & 1:  # n is odd
                result *= x
            x *= x
            n >>= 1

        return result


class SolutionRecursive:
    def myPow(self, x: float, n: int) -> float:
        """
        Recursive binary exponentiation - O(log n).
        """
        if n == 0:
            return 1.0

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        else:
            return x * self.myPow(x, n - 1)


class SolutionTailRecursive:
    def myPow(self, x: float, n: int) -> float:
        """
        Tail recursive approach.
        """
        def helper(x: float, n: int, acc: float) -> float:
            if n == 0:
                return acc
            if n % 2 == 0:
                return helper(x * x, n // 2, acc)
            else:
                return helper(x * x, n // 2, acc * x)

        if n < 0:
            x = 1 / x
            n = -n

        return helper(x, n, 1.0)


class SolutionBuiltin:
    def myPow(self, x: float, n: int) -> float:
        """
        Using Python's built-in operator.
        """
        return x ** n


class SolutionNaive:
    def myPow(self, x: float, n: int) -> float:
        """
        Naive O(n) approach - for comparison.
        Will timeout for large n.
        """
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        for _ in range(n):
            result *= x

        return result
