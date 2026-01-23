#736. Parse Lisp Expression
#Hard
#
#You are given a string expression representing a Lisp-like expression to
#return the integer value of.
#
#The syntax for these expressions is given as follows:
#- An expression is either an integer, let expression, add expression, mult
#  expression, or an assigned variable. Expressions always evaluate to a
#  single integer.
#- An integer could be positive or negative.
#- A let expression takes the form "(let v1 e1 v2 e2 ... vn en expr)", where
#  let is always the string "let", then there are one or more pairs of
#  alternating variables and expressions, and finally an expression to evaluate.
#- An add expression takes the form "(add e1 e2)" where add is always the
#  string "add", there are always two expressions e1, e2, and the result is
#  the addition of the evaluation of e1 and e2.
#- A mult expression takes the form "(mult e1 e2)" similarly, the result is
#  the multiplication of the evaluation of e1 and e2.
#- A variable starts with a lowercase letter, then zero or more lowercase
#  letters or digits.
#
#Example 1:
#Input: expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
#Output: 14
#Explanation: In the expression (add x y), when checking for the value of the
#variable x, we check from the innermost scope to the outermost in the context
#of the variable we are trying to evaluate.
#
#Example 2:
#Input: expression = "(let x 3 x 2 x)"
#Output: 2
#
#Example 3:
#Input: expression = "(let x 1 y 2 x (add x y) (add x y))"
#Output: 5
#
#Constraints:
#    1 <= expression.length <= 2000
#    The answer and all intermediate calculations fit in a 32-bit integer.

class Solution:
    def evaluate(self, expression: str) -> int:
        """
        Recursive descent parser with scope handling.
        """
        def parse(expr, scope):
            if expr[0] != '(':
                # Variable or integer
                if expr[0].isdigit() or expr[0] == '-':
                    return int(expr)
                return scope[expr]

            # Remove outer parentheses
            expr = expr[1:-1]

            # Parse command
            tokens = tokenize(expr)
            cmd = tokens[0]

            if cmd == 'let':
                # Create new scope
                new_scope = scope.copy()
                i = 1
                while i < len(tokens) - 1:
                    var = tokens[i]
                    val = parse(tokens[i + 1], new_scope)
                    new_scope[var] = val
                    i += 2
                return parse(tokens[-1], new_scope)

            elif cmd == 'add':
                return parse(tokens[1], scope) + parse(tokens[2], scope)

            elif cmd == 'mult':
                return parse(tokens[1], scope) * parse(tokens[2], scope)

        def tokenize(expr):
            """Split expression into tokens, respecting parentheses."""
            tokens = []
            i = 0
            while i < len(expr):
                if expr[i] == ' ':
                    i += 1
                    continue

                if expr[i] == '(':
                    # Find matching closing paren
                    depth = 1
                    j = i + 1
                    while depth > 0:
                        if expr[j] == '(':
                            depth += 1
                        elif expr[j] == ')':
                            depth -= 1
                        j += 1
                    tokens.append(expr[i:j])
                    i = j
                else:
                    # Find end of token
                    j = i
                    while j < len(expr) and expr[j] != ' ' and expr[j] != ')':
                        j += 1
                    tokens.append(expr[i:j])
                    i = j

            return tokens

        return parse(expression, {})


class SolutionIterator:
    """Using iterator for parsing"""

    def evaluate(self, expression: str) -> int:
        def parse(tokens, scope):
            token = next(tokens)

            if token != '(':
                if token.lstrip('-').isdigit():
                    return int(token)
                return scope[token]

            cmd = next(tokens)

            if cmd == 'let':
                new_scope = scope.copy()
                while True:
                    var = next(tokens)
                    if var == ')':
                        break
                    peek = next(tokens)
                    if peek == ')':
                        return parse(iter([var]), new_scope)
                    val = parse(iter([peek]) if peek != '(' else iter(['(' + get_paren(tokens)]), new_scope)
                    new_scope[var] = val
                # Return value of last expression
                return new_scope.get(var, int(var) if var.lstrip('-').isdigit() else None)

            elif cmd == 'add':
                a = parse(tokens, scope)
                b = parse(tokens, scope)
                next(tokens)  # closing )
                return a + b

            elif cmd == 'mult':
                a = parse(tokens, scope)
                b = parse(tokens, scope)
                next(tokens)  # closing )
                return a * b

        def get_paren(tokens):
            result = []
            depth = 1
            while depth > 0:
                t = next(tokens)
                if t == '(':
                    depth += 1
                elif t == ')':
                    depth -= 1
                result.append(t)
            return ' '.join(result)

        # Tokenize
        import re
        tokens = iter(re.findall(r'[()]|[^\s()]+', expression))
        return parse(tokens, {})
