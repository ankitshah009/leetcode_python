#772. Basic Calculator III
#Hard
#
#Implement a basic calculator to evaluate a simple expression string.
#
#The expression string contains only non-negative integers, '+', '-', '*', '/'
#operators, and open '(' and closing ')' parentheses. The integer division
#should truncate toward zero.
#
#You may assume that the given expression is always valid.
#
#Example 1:
#Input: s = "1+1"
#Output: 2
#
#Example 2:
#Input: s = "6-4/2"
#Output: 4
#
#Example 3:
#Input: s = "2*(5+5*2)/3+(6/2+8)"
#Output: 21
#
#Constraints:
#    1 <= s.length <= 10^4
#    s consists of digits, '+', '-', '*', '/', '(', and ')'.
#    s is a valid expression.

class Solution:
    def calculate(self, s: str) -> int:
        """
        Recursive descent parser for expression with + - * / and parentheses.
        """
        self.i = 0

        def parse_expr():
            terms = [parse_term()]
            while self.i < len(s) and s[self.i] in '+-':
                op = s[self.i]
                self.i += 1
                if op == '+':
                    terms.append(parse_term())
                else:
                    terms.append(-parse_term())
            return sum(terms)

        def parse_term():
            result = parse_factor()
            while self.i < len(s) and s[self.i] in '*/':
                op = s[self.i]
                self.i += 1
                if op == '*':
                    result *= parse_factor()
                else:
                    result = int(result / parse_factor())
            return result

        def parse_factor():
            # Skip spaces
            while self.i < len(s) and s[self.i] == ' ':
                self.i += 1

            if s[self.i] == '(':
                self.i += 1
                result = parse_expr()
                self.i += 1  # Skip ')'
                return result
            else:
                # Parse number
                start = self.i
                while self.i < len(s) and s[self.i].isdigit():
                    self.i += 1
                return int(s[start:self.i])

        return parse_expr()


class SolutionStack:
    """Stack-based approach"""

    def calculate(self, s: str) -> int:
        def calc(s):
            stack = []
            num = 0
            op = '+'
            i = 0

            while i < len(s):
                c = s[i]

                if c.isdigit():
                    num = num * 10 + int(c)

                if c == '(':
                    # Find matching ')'
                    depth = 1
                    j = i + 1
                    while depth > 0:
                        if s[j] == '(':
                            depth += 1
                        elif s[j] == ')':
                            depth -= 1
                        j += 1
                    num = calc(s[i + 1:j - 1])
                    i = j - 1

                if c in '+-*/' or i == len(s) - 1:
                    if op == '+':
                        stack.append(num)
                    elif op == '-':
                        stack.append(-num)
                    elif op == '*':
                        stack.append(stack.pop() * num)
                    elif op == '/':
                        stack.append(int(stack.pop() / num))
                    op = c
                    num = 0

                i += 1

            return sum(stack)

        return calc(s)
