#1612. Check If Two Expression Trees are Equivalent
#Medium
#
#A binary expression tree is a kind of binary tree used to represent arithmetic
#expressions. Each node of a binary expression tree has either zero or two
#children. Leaf nodes (nodes with 0 children) correspond to operands (variables),
#and internal nodes (nodes with two children) correspond to the operators.
#In this problem, we consider the '+' operator only (i.e., we only consider
#addition).
#
#You are given the roots of two binary expression trees, root1 and root2.
#Return true if the two binary expression trees are equivalent. Otherwise,
#return false.
#
#Two binary expression trees are equivalent if they evaluate to the same value
#regardless of what the variables are set to.
#
#Example 1:
#Input: root1 = [x], root2 = [x]
#Output: true
#
#Example 2:
#Input: root1 = [+,a,+,null,null,b,c], root2 = [+,+,a,b,c]
#Output: true
#Explanation: a + (b + c) == (b + c) + a
#
#Example 3:
#Input: root1 = [+,a,+,null,null,b,c], root2 = [+,+,a,b,d]
#Output: false
#Explanation: a + (b + c) != (b + c) + a + d
#
#Constraints:
#    The number of nodes in both trees are equal, which is at most 10.
#    The leaves are lowercase English letters.
#    The interior nodes are '+'.

from typing import Optional
from collections import Counter

class Node:
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        """
        Since we only have addition, the expression value depends only on
        the multiset of variables. Count variables in each tree and compare.
        """
        def count_vars(node: Node) -> Counter:
            if not node:
                return Counter()

            if not node.left and not node.right:
                # Leaf node - variable
                return Counter({node.val: 1})

            # Internal node - combine children
            return count_vars(node.left) + count_vars(node.right)

        return count_vars(root1) == count_vars(root2)


class SolutionIterative:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        """
        Iterative approach using stack.
        """
        def get_vars(root: Node) -> Counter:
            if not root:
                return Counter()

            counter = Counter()
            stack = [root]

            while stack:
                node = stack.pop()

                if node.val != '+':
                    # Leaf variable
                    counter[node.val] += 1
                else:
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)

            return counter

        return get_vars(root1) == get_vars(root2)


class SolutionCollect:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        """
        Collect all variables and sort them.
        """
        def collect(node: Node, result: list):
            if not node:
                return

            if not node.left and not node.right:
                result.append(node.val)
            else:
                collect(node.left, result)
                collect(node.right, result)

        vars1 = []
        vars2 = []
        collect(root1, vars1)
        collect(root2, vars2)

        return sorted(vars1) == sorted(vars2)
