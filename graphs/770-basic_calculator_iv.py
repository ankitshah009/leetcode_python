#770. Basic Calculator IV
#Hard
#
#Given an expression such as expression = "e + 8 - a + 5" and an evaluation map
#such as {"e": 1} (given in terms of evalvars = ["e"] and evalints = [1]),
#return a list of tokens representing the simplified expression, such as
#["-1*a","14"]
#
#An expression alternates chunks and symbols, with a space separating each chunk
#and symbol.
#A chunk is either an expression in parentheses, a variable, or a non-negative
#integer.
#A variable is a string of lowercase letters (not including digits.)
#
#Return the simplified expression as a list of tokens. The tokens should be in
#order of decreasing degree where the degree of a token is:
#- If it's a constant, the degree is 0.
#- If it's a single variable, the degree is 1.
#- If it's an expression of multiplication, the degree is the sum of degrees.
#
#Example 1:
#Input: expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
#Output: ["-1*a","14"]
#
#Example 2:
#Input: expression = "e - 8 + temperature - pressure",
#       evalvars = ["e", "temperature"], evalints = [1, 12]
#Output: ["-1*pressure","5"]
#
#Constraints:
#    1 <= expression.length <= 250
#    expression consists of lowercase English letters, digits, '+', '-', '*',
#    '(', ')', ' '.

from collections import Counter

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: list[str],
                          evalints: list[int]) -> list[str]:
        """
        Parse expression, evaluate with polynomial arithmetic.
        """
        class Poly(Counter):
            def __add__(self, other):
                result = Poly(self)
                for k, v in other.items():
                    result[k] += v
                return result

            def __sub__(self, other):
                result = Poly(self)
                for k, v in other.items():
                    result[k] -= v
                return result

            def __mul__(self, other):
                result = Poly()
                for k1, v1 in self.items():
                    for k2, v2 in other.items():
                        key = tuple(sorted(k1 + k2))
                        result[key] += v1 * v2
                return result

            def evaluate(self, env):
                result = Poly()
                for vars, coef in self.items():
                    new_vars = []
                    for v in vars:
                        if v in env:
                            coef *= env[v]
                        else:
                            new_vars.append(v)
                    result[tuple(new_vars)] += coef
                return result

            def to_list(self):
                terms = [(k, v) for k, v in self.items() if v != 0]
                terms.sort(key=lambda x: (-len(x[0]), x[0]))
                result = []
                for vars, coef in terms:
                    if vars:
                        result.append('*'.join([str(coef)] + list(vars)))
                    else:
                        result.append(str(coef))
                return result

        env = dict(zip(evalvars, evalints))

        def make_poly(token):
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                return Poly({(): int(token)})
            else:
                return Poly({(token,): 1})

        def parse(tokens):
            # Recursive descent parser
            def parse_expr():
                result = parse_term()
                while tokens and tokens[-1] in '+-':
                    op = tokens.pop()
                    term = parse_term()
                    if op == '+':
                        result = result + term
                    else:
                        result = result - term
                return result

            def parse_term():
                result = parse_factor()
                while tokens and tokens[-1] == '*':
                    tokens.pop()
                    result = result * parse_factor()
                return result

            def parse_factor():
                if tokens[-1] == ')':
                    tokens.pop()  # ')'
                    result = parse_expr()
                    tokens.pop()  # '('
                else:
                    result = make_poly(tokens.pop())
                return result

            return parse_expr()

        # Tokenize (reverse for stack-like popping)
        tokens = expression.replace('(', '( ').replace(')', ' )').split()[::-1]
        poly = parse(tokens).evaluate(env)

        return poly.to_list()
