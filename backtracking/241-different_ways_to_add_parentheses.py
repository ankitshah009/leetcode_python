#241. Different Ways to Add Parentheses
#Medium
#
#Given a string expression of numbers and operators, return all possible results
#from computing all the different possible ways to group numbers and operators.
#You may return the answer in any order.
#
#The test cases are generated such that the output values fit in a 32-bit integer
#and the number of different results does not exceed 10^4.
#
#Example 1:
#Input: expression = "2-1-1"
#Output: [0,2]
#Explanation:
#((2-1)-1) = 0
#(2-(1-1)) = 2
#
#Example 2:
#Input: expression = "2*3-4*5"
#Output: [-34,-14,-10,-10,10]
#Explanation:
#(2*(3-(4*5))) = -34
#((2*3)-(4*5)) = -14
#((2*(3-4))*5) = -10
#(2*((3-4)*5)) = -10
#(((2*3)-4)*5) = 10
#
#Constraints:
#    1 <= expression.length <= 20
#    expression consists of digits and the operator '+', '-', and '*'.
#    All the integer values in the input expression are in the range [0, 99].
#    The integer values in the input expression do not have a leading '-' or '+'
#    denoting the sign.

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def compute(expr):
            if expr in memo:
                return memo[expr]

            # If expression is just a number
            if expr.isdigit():
                return [int(expr)]

            results = []

            for i, char in enumerate(expr):
                if char in '+-*':
                    # Split at operator and compute left and right
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])

                    # Combine results
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            else:  # char == '*'
                                results.append(left * right)

            memo[expr] = results
            return results

        return compute(expression)

    # Alternative without memoization (for small inputs)
    def diffWaysToComputeSimple(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        results = []

        for i, char in enumerate(expression):
            if char in '+-*':
                left_results = self.diffWaysToComputeSimple(expression[:i])
                right_results = self.diffWaysToComputeSimple(expression[i+1:])

                for left in left_results:
                    for right in right_results:
                        if char == '+':
                            results.append(left + right)
                        elif char == '-':
                            results.append(left - right)
                        else:
                            results.append(left * right)

        return results
