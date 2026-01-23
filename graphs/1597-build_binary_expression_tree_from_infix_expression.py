#1597. Build Binary Expression Tree from Infix Expression
#Hard
#
#A binary expression tree is a kind of binary tree used to represent arithmetic
#expressions. Each node of a binary expression tree has either zero or two
#children. Leaf nodes (nodes with 0 children) correspond to operands (numbers),
#and internal nodes (nodes with 2 children) correspond to the operators
#'+', '-', '*', and '/'.
#
#For each internal node with operator o, the infix expression it represents is
#(A o B), where A is the expression the left subtree represents and B is the
#expression the right subtree represents.
#
#You are given a string s, an infix expression containing operands, operators
#('+', '-', '*', '/'), and parentheses ('(' and ')').
#
#Return any valid binary expression tree, which its in-order traversal reproduces s.
#
#Note: You must use parentheses to preserve the correct order of operations.
#
#Example 1:
#Input: s = "3*4-2*5"
#Output: [-,*,*,3,4,2,5]
#Explanation: The tree is:
#        -
#       / \
#      *   *
#     / \ / \
#    3  4 2  5
#
#Example 2:
#Input: s = "2-3/(5*2)+1"
#Output: [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]
#
#Example 3:
#Input: s = "1+2+3+4+5"
#Output: [+,+,5,+,4,null,null,+,3,null,null,1,2]
#
#Constraints:
#    1 <= s.length <= 100
#    s consists of digits and the characters '+', '-', '*', and '/'.
#    Operands in s are exactly 1 digit.
#    It is guaranteed that s is a valid expression.

from typing import Optional

class Node:
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def expTree(self, s: str) -> 'Node':
        """
        Parse infix expression using recursive descent parser.

        Grammar:
        expr   -> term (('+' | '-') term)*
        term   -> factor (('*' | '/') factor)*
        factor -> '(' expr ')' | number

        Build tree during parsing.
        """
        self.s = s
        self.pos = 0

        return self.parse_expr()

    def parse_expr(self) -> Node:
        """Parse expression (handles + and -)"""
        left = self.parse_term()

        while self.pos < len(self.s) and self.s[self.pos] in '+-':
            op = self.s[self.pos]
            self.pos += 1
            right = self.parse_term()
            left = Node(op, left, right)

        return left

    def parse_term(self) -> Node:
        """Parse term (handles * and /)"""
        left = self.parse_factor()

        while self.pos < len(self.s) and self.s[self.pos] in '*/':
            op = self.s[self.pos]
            self.pos += 1
            right = self.parse_factor()
            left = Node(op, left, right)

        return left

    def parse_factor(self) -> Node:
        """Parse factor (number or parenthesized expression)"""
        if self.s[self.pos] == '(':
            self.pos += 1  # Skip '('
            node = self.parse_expr()
            self.pos += 1  # Skip ')'
            return node
        else:
            # Number (single digit)
            num = self.s[self.pos]
            self.pos += 1
            return Node(num)


class SolutionStack:
    def expTree(self, s: str) -> 'Node':
        """
        Stack-based approach using operator precedence.

        Use two stacks: one for operands (nodes) and one for operators.
        Process based on operator precedence.
        """
        def precedence(op: str) -> int:
            if op in '+-':
                return 1
            if op in '*/':
                return 2
            return 0

        def apply_op(operands: list, operators: list):
            right = operands.pop()
            left = operands.pop()
            op = operators.pop()
            operands.append(Node(op, left, right))

        operands = []
        operators = []

        i = 0
        while i < len(s):
            c = s[i]

            if c.isdigit():
                operands.append(Node(c))

            elif c == '(':
                operators.append(c)

            elif c == ')':
                while operators and operators[-1] != '(':
                    apply_op(operands, operators)
                operators.pop()  # Remove '('

            elif c in '+-*/':
                while operators and operators[-1] != '(' and precedence(operators[-1]) >= precedence(c):
                    apply_op(operands, operators)
                operators.append(c)

            i += 1

        while operators:
            apply_op(operands, operators)

        return operands[0]


class SolutionIterative:
    def expTree(self, s: str) -> 'Node':
        """
        Iterative shunting-yard algorithm variant.
        """
        prec = {'+': 1, '-': 1, '*': 2, '/': 2}

        nodes = []  # Stack of expression nodes
        ops = []    # Stack of operators

        def build():
            op = ops.pop()
            right = nodes.pop()
            left = nodes.pop()
            nodes.append(Node(op, left, right))

        for c in s:
            if c.isdigit():
                nodes.append(Node(c))
            elif c == '(':
                ops.append(c)
            elif c == ')':
                while ops[-1] != '(':
                    build()
                ops.pop()  # pop '('
            else:  # operator
                while ops and ops[-1] != '(' and prec.get(ops[-1], 0) >= prec[c]:
                    build()
                ops.append(c)

        while ops:
            build()

        return nodes[0]
