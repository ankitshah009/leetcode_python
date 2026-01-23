#1628. Design an Expression Tree With Evaluate Function
#Medium
#
#Given the postfix tokens of an arithmetic expression, build and return the
#binary expression tree that represents this expression.
#
#Postfix notation is a notation for writing arithmetic expressions in which
#the operands (numbers) appear before their operators. For example, the postfix
#tokens of the expression 4*(5-(7+2)) are [4,5,7,2,+,-,*].
#
#The class Node is an interface you should use to implement the binary expression
#tree. The returned tree will be tested using the evaluate function, which is
#supposed to evaluate the tree's value. You should not remove the Node class;
#however, you can modify it as you wish, and you can define other classes to
#implement it if needed.
#
#A binary expression tree is a kind of binary tree used to represent arithmetic
#expressions. Each node of a binary expression tree has either zero or two
#children. Leaf nodes (nodes with 0 children) correspond to operands (numbers),
#and internal nodes (nodes with two children) correspond to the operators
#'+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).
#
#It's guaranteed that no subtree will yield a value that exceeds 10^9 in absolute
#value, and all the operations are valid (i.e., no division by zero).
#
#Example 1:
#Input: s = ["3","4","+","2","*","7","/"]
#Output: 2
#Explanation: The expression tree is:
#        /
#       / \
#      *   7
#     / \
#    +   2
#   / \
#  3   4
#
#Example 2:
#Input: s = ["4","5","2","7","+","-","*"]
#Output: -16
#Explanation: The expression tree is:
#        *
#       / \
#      4   -
#         / \
#        5   +
#           / \
#          2   7
#
#Constraints:
#    1 <= s.length < 100
#    s.length is odd.
#    s consists of numbers and the characters '+', '-', '*', and '/'.
#    If s[i] is a number, its integer representation is no more than 10^5.
#    The tree is guaranteed to be valid.
#    The absolute value of the result and intermediate values will not exceed 10^9.
#    It is guaranteed that no expression will include division by zero.

from typing import List
import abc
from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class NumNode(Node):
    """Leaf node representing a number."""
    def __init__(self, val: int):
        self.val = val

    def evaluate(self) -> int:
        return self.val


class OpNode(Node):
    """Internal node representing an operator."""
    def __init__(self, op: str, left: Node, right: Node):
        self.op = op
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()

        if self.op == '+':
            return left_val + right_val
        elif self.op == '-':
            return left_val - right_val
        elif self.op == '*':
            return left_val * right_val
        else:  # '/'
            return int(left_val / right_val)  # Truncate toward zero


class TreeBuilder:
    def buildTree(self, postfix: List[str]) -> 'Node':
        """
        Build expression tree from postfix tokens.
        Use a stack: push numbers, pop two operands for operators.
        """
        stack = []

        for token in postfix:
            if token in '+-*/':
                # Operator: pop two operands
                right = stack.pop()
                left = stack.pop()
                node = OpNode(token, left, right)
                stack.append(node)
            else:
                # Number: create leaf node
                stack.append(NumNode(int(token)))

        return stack[0]


# Alternative implementation using single Node class
class NodeSingle:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        if self.left is None:
            # Leaf: val is a number
            return int(self.val)

        # Internal node: val is operator
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()

        if self.val == '+':
            return left_val + right_val
        elif self.val == '-':
            return left_val - right_val
        elif self.val == '*':
            return left_val * right_val
        else:
            return int(left_val / right_val)


class TreeBuilderSingle:
    def buildTree(self, postfix: List[str]) -> 'NodeSingle':
        stack = []

        for token in postfix:
            if token in '+-*/':
                right = stack.pop()
                left = stack.pop()
                stack.append(NodeSingle(token, left, right))
            else:
                stack.append(NodeSingle(token))

        return stack[0]
