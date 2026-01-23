#1896. Minimum Cost to Change the Final Value of Expression
#Hard
#
#You are given a valid boolean expression as a string expression consisting of
#the characters '1','0','&' (AND),'|' (OR),'(', and ')'.
#
#Return the minimum cost to change the final value of the expression.
#
#The cost of changing the final value of an expression is the minimum number of
#operations performed on the expression. The allowed operations are:
#- Turn a '1' into a '0'.
#- Turn a '0' into a '1'.
#- Turn a '&' into a '|'.
#- Turn a '|' into a '&'.
#
#Example 1:
#Input: expression = "1&(0|1)"
#Output: 1
#
#Example 2:
#Input: expression = "(0&0)&(0&0&0)"
#Output: 3
#
#Example 3:
#Input: expression = "(0|(1|0&1))"
#Output: 1
#
#Constraints:
#    1 <= expression.length <= 10^5
#    expression only contains '1','0','&','|','(', and ')'
#    All parentheses are properly matched.
#    There will be no empty parentheses (i.e.: "()" is not a substring of expression).

class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        """
        Stack-based evaluation tracking (value, cost_to_flip).
        """
        # Stack contains (current_value, cost_to_flip)
        stack = []
        ops = []  # Operators stack

        i = 0
        while i < len(expression):
            c = expression[i]

            if c == '0':
                stack.append((0, 1))
            elif c == '1':
                stack.append((1, 1))
            elif c in '&|':
                ops.append(c)
            elif c == '(':
                ops.append('(')
            elif c == ')':
                # Pop until '('
                while ops and ops[-1] != '(':
                    self.compute(stack, ops.pop())
                ops.pop()  # Remove '('

            # After processing, try to compute if we have pending operator
            while len(stack) >= 2 and ops and ops[-1] in '&|':
                self.compute(stack, ops.pop())

            i += 1

        return stack[-1][1]

    def compute(self, stack, op):
        """Combine top two values on stack with operator."""
        v2, c2 = stack.pop()
        v1, c1 = stack.pop()

        if op == '&':
            if v1 == 1 and v2 == 1:
                # Result is 1, to flip: change either to 0 or change & to |
                # If change to 0: min(c1, c2)
                # If change & to |: need one of them to be 0, so 1 + min(c1, c2)
                # Best: min(c1, c2)
                result = (1, min(c1, c2))
            elif v1 == 0 and v2 == 0:
                # Result is 0, to flip to 1: need both 1 OR change & to |
                # Change both: c1 + c2
                # Change & to |: still 0|0=0, need to also change one: 1 + min(c1, c2)
                result = (0, min(1 + min(c1, c2), c1 + c2))
            elif v1 == 1:  # v1=1, v2=0
                # Result is 0, to flip: change v2 to 1 (c2) or change & to | (1)
                result = (0, 1)
            else:  # v1=0, v2=1
                # Result is 0, to flip: change v1 to 1 (c1) or change & to | (1)
                result = (0, 1)
        else:  # op == '|'
            if v1 == 0 and v2 == 0:
                # Result is 0, to flip: change either to 1
                result = (0, min(c1, c2))
            elif v1 == 1 and v2 == 1:
                # Result is 1, to flip to 0: need both 0 OR change | to &
                result = (1, min(1 + min(c1, c2), c1 + c2))
            elif v1 == 0:  # v1=0, v2=1
                # Result is 1, to flip: change v2 to 0 (c2) or change | to & (1)
                result = (1, 1)
            else:  # v1=1, v2=0
                result = (1, 1)

        stack.append(result)


class SolutionRecursive:
    def minOperationsToFlip(self, expression: str) -> int:
        """
        Recursive descent parser.
        """
        self.i = 0

        def parse():
            """Parse and return (value, cost_to_flip)."""
            left = parse_term()

            while self.i < len(expression) and expression[self.i] in '&|':
                op = expression[self.i]
                self.i += 1
                right = parse_term()
                left = combine(left, right, op)

            return left

        def parse_term():
            if expression[self.i] == '(':
                self.i += 1  # Skip '('
                result = parse()
                self.i += 1  # Skip ')'
                return result
            else:
                val = int(expression[self.i])
                self.i += 1
                return (val, 1)

        def combine(l, r, op):
            v1, c1 = l
            v2, c2 = r

            if op == '&':
                val = v1 & v2
                if v1 == 1 and v2 == 1:
                    cost = min(c1, c2)
                elif v1 == 0 and v2 == 0:
                    cost = 1 + min(c1, c2)
                else:
                    cost = 1
            else:  # '|'
                val = v1 | v2
                if v1 == 0 and v2 == 0:
                    cost = min(c1, c2)
                elif v1 == 1 and v2 == 1:
                    cost = 1 + min(c1, c2)
                else:
                    cost = 1

            return (val, cost)

        return parse()[1]
