#1006. Clumsy Factorial
#Medium
#
#The factorial of a positive integer n is the product of all positive integers
#less than or equal to n.
#
#The clumsy factorial of a positive integer n is computed using the integers in
#decreasing order by swapping out the multiply operations for a fixed rotation
#of operations: multiply (*), divide (/), add (+), subtract (-).
#
#For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
#
#Return the clumsy factorial of n.
#
#Example 1:
#Input: n = 4
#Output: 7
#Explanation: 4 * 3 / 2 + 1 = 7
#
#Example 2:
#Input: n = 10
#Output: 12
#
#Constraints:
#    1 <= n <= 10^4

class Solution:
    def clumsy(self, n: int) -> int:
        """
        Process groups of 4 operations.
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        if n == 4:
            return 7

        # First group: * / +
        result = n * (n - 1) // (n - 2) + (n - 3)

        n -= 4
        while n >= 4:
            result -= n * (n - 1) // (n - 2) - (n - 3)
            n -= 4

        # Handle remaining
        if n == 3:
            result -= 6
        elif n == 2:
            result -= 2
        elif n == 1:
            result -= 1

        return result


class SolutionStack:
    """Stack-based evaluation"""

    def clumsy(self, n: int) -> int:
        ops = ['*', '/', '+', '-']
        op_idx = 0
        stack = [n]

        for i in range(n - 1, 0, -1):
            op = ops[op_idx]
            op_idx = (op_idx + 1) % 4

            if op == '*':
                stack.append(stack.pop() * i)
            elif op == '/':
                stack.append(int(stack.pop() / i))  # Truncate toward zero
            elif op == '+':
                stack.append(i)
            else:  # '-'
                stack.append(-i)

        return sum(stack)


class SolutionPattern:
    """Using pattern in results"""

    def clumsy(self, n: int) -> int:
        """
        For n >= 5, there's a pattern:
        clumsy(n) = n + 1 when n % 4 == 0
        clumsy(n) = n + 2 when n % 4 == 1 or 2
        clumsy(n) = n - 1 when n % 4 == 3
        """
        if n <= 4:
            return [0, 1, 2, 6, 7][n]

        if n % 4 == 0:
            return n + 1
        elif n % 4 == 1 or n % 4 == 2:
            return n + 2
        else:
            return n - 1
