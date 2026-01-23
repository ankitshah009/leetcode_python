#590. N-ary Tree Postorder Traversal
#Easy
#
#Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
#
#Example 1:
#Input: root = [1,null,3,2,4,null,5,6]
#Output: [5,6,3,2,4,1]
#
#Example 2:
#Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
#Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 10^4].
#    0 <= Node.val <= 10^4
#    The height of the n-ary tree is less than or equal to 1000.

from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """Recursive postorder"""
        result = []

        def dfs(node):
            if not node:
                return
            for child in node.children:
                dfs(child)
            result.append(node.val)

        dfs(root)
        return result


class SolutionIterative:
    """Iterative using stack - reverse preorder"""

    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            # Add children left to right
            stack.extend(node.children)

        return result[::-1]  # Reverse for postorder


class SolutionIterativeProper:
    """True iterative postorder with visited tracking"""

    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if visited:
                result.append(node.val)
            else:
                stack.append((node, True))
                for child in reversed(node.children):
                    stack.append((child, False))

        return result
