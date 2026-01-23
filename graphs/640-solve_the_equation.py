#640. Solve the Equation
#Medium
#
#Solve a given equation and return the value of 'x' in the form of a string
#"x=#value". The equation contains only '+', '-' operation, the variable 'x'
#and its coefficient.
#
#If there is no solution for the equation, return "No solution".
#If there are infinite solutions for the equation, return "Infinite solutions".
#If there is exactly one solution for the equation, the value of 'x' is guaranteed
#to be an integer.
#
#Example 1:
#Input: equation = "x+5-3+x=6+x-2"
#Output: "x=2"
#
#Example 2:
#Input: equation = "x=x"
#Output: "Infinite solutions"
#
#Example 3:
#Input: equation = "2x=x"
#Output: "x=0"
#
#Constraints:
#    3 <= equation.length <= 1000
#    equation has exactly one '='.
#    equation consists of integers with absolute value in range [0, 100].

import re

class Solution:
    def solveEquation(self, equation: str) -> str:
        """Parse and solve linear equation"""

        def parse(expr):
            """Parse expression, return (coefficient of x, constant)"""
            coef = 0
            const = 0

            # Add '+' at start if needed for consistent parsing
            if expr[0] not in '+-':
                expr = '+' + expr

            # Find all terms
            terms = re.findall(r'[+-]?\d*x?', expr)

            for term in terms:
                if not term or term in '+-':
                    continue

                if 'x' in term:
                    # Coefficient term
                    term = term.replace('x', '')
                    if term == '' or term == '+':
                        coef += 1
                    elif term == '-':
                        coef -= 1
                    else:
                        coef += int(term)
                else:
                    # Constant term
                    const += int(term)

            return coef, const

        left, right = equation.split('=')
        left_coef, left_const = parse(left)
        right_coef, right_const = parse(right)

        # Move everything to left side: (left_coef - right_coef)x = right_const - left_const
        coef = left_coef - right_coef
        const = right_const - left_const

        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"

        return f"x={const // coef}"


class SolutionManualParse:
    """Manual parsing without regex"""

    def solveEquation(self, equation: str) -> str:
        def parse(expr):
            coef = 0
            const = 0
            i = 0
            sign = 1

            while i < len(expr):
                if expr[i] == '+':
                    sign = 1
                    i += 1
                elif expr[i] == '-':
                    sign = -1
                    i += 1
                elif expr[i] == 'x':
                    coef += sign
                    i += 1
                else:
                    # Parse number
                    j = i
                    while j < len(expr) and expr[j].isdigit():
                        j += 1

                    num = int(expr[i:j])

                    if j < len(expr) and expr[j] == 'x':
                        coef += sign * num
                        j += 1
                    else:
                        const += sign * num

                    i = j

            return coef, const

        left, right = equation.split('=')
        lc, ln = parse(left)
        rc, rn = parse(right)

        coef = lc - rc
        const = rn - ln

        if coef == 0:
            return "Infinite solutions" if const == 0 else "No solution"

        return f"x={const // coef}"
