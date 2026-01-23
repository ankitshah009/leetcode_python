#679. 24 Game
#Hard
#
#You are given an integer array cards of length 4. You have 4 cards, each containing
#a number in the range [1, 9]. You should arrange the numbers on these cards in a
#mathematical expression using the operators ['+', '-', '*', '/'] to get the value 24.
#
#You are allowed to use parentheses to change the priority of operations, but each
#card must be used exactly once.
#
#Return true if you can get 24, and false otherwise.
#
#Example 1:
#Input: cards = [4, 1, 8, 7]
#Output: true
#Explanation: (8-4) * (7-1) = 24
#
#Example 2:
#Input: cards = [1, 2, 1, 2]
#Output: false
#
#Constraints:
#    cards.length == 4
#    1 <= cards[i] <= 9

from typing import List
from itertools import permutations

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        """
        Backtracking: pick any two numbers, apply operation,
        replace with result, and recurse.
        """
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-9

            # Try all pairs of numbers
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue

                    # Remaining numbers
                    remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]

                    # Try all operations
                    a, b = nums[i], nums[j]
                    operations = [a + b, a - b, a * b]
                    if b != 0:
                        operations.append(a / b)

                    for result in operations:
                        if solve(remaining + [result]):
                            return True

            return False

        return solve([float(c) for c in cards])


class SolutionPermutation:
    """Try all permutations and operator combinations"""

    def judgePoint24(self, cards: List[int]) -> bool:
        def evaluate(a, b, op):
            if op == 0:
                return a + b
            elif op == 1:
                return a - b
            elif op == 2:
                return a * b
            elif op == 3:
                return a / b if b != 0 else float('inf')

        def try_ops(nums):
            a, b, c, d = nums

            # All possible ways to parenthesize and apply 3 operators
            for op1 in range(4):
                for op2 in range(4):
                    for op3 in range(4):
                        # ((a op1 b) op2 c) op3 d
                        r1 = evaluate(evaluate(evaluate(a, b, op1), c, op2), d, op3)
                        if abs(r1 - 24) < 1e-9:
                            return True

                        # (a op1 (b op2 c)) op3 d
                        r2 = evaluate(evaluate(a, evaluate(b, c, op2), op1), d, op3)
                        if abs(r2 - 24) < 1e-9:
                            return True

                        # (a op1 b) op2 (c op3 d)
                        r3 = evaluate(evaluate(a, b, op1), evaluate(c, d, op3), op2)
                        if abs(r3 - 24) < 1e-9:
                            return True

                        # a op1 ((b op2 c) op3 d)
                        r4 = evaluate(a, evaluate(evaluate(b, c, op2), d, op3), op1)
                        if abs(r4 - 24) < 1e-9:
                            return True

                        # a op1 (b op2 (c op3 d))
                        r5 = evaluate(a, evaluate(b, evaluate(c, d, op3), op2), op1)
                        if abs(r5 - 24) < 1e-9:
                            return True

            return False

        for perm in permutations([float(c) for c in cards]):
            if try_ops(perm):
                return True

        return False
