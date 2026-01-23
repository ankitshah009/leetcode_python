#543. Diameter of Binary Tree
#Easy
#
#Given the root of a binary tree, return the length of the diameter of the tree.
#
#The diameter of a binary tree is the length of the longest path between any two
#nodes in a tree. This path may or may not pass through the root.
#
#The length of a path between two nodes is represented by the number of edges
#between them.
#
#Example 1:
#Input: root = [1,2,3,4,5]
#Output: 3
#Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
#
#Example 2:
#Input: root = [1,2]
#Output: 1
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    -100 <= Node.val <= 100

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        DFS returning height, tracking max diameter.
        Diameter through a node = left_height + right_height
        """
        self.diameter = 0

        def height(node):
            if not node:
                return 0

            left_h = height(node.left)
            right_h = height(node.right)

            # Update diameter (path through this node)
            self.diameter = max(self.diameter, left_h + right_h)

            return 1 + max(left_h, right_h)

        height(root)
        return self.diameter


class SolutionTuple:
    """Return both height and diameter from recursion"""

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            """Returns (height, max_diameter)"""
            if not node:
                return 0, 0

            left_h, left_d = dfs(node.left)
            right_h, right_d = dfs(node.right)

            height = 1 + max(left_h, right_h)
            diameter = max(left_d, right_d, left_h + right_h)

            return height, diameter

        return dfs(root)[1]


class SolutionIterative:
    """Iterative postorder traversal"""

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, False)]
        heights = {}
        diameter = 0

        while stack:
            node, visited = stack.pop()

            if visited:
                left_h = heights.get(node.left, 0)
                right_h = heights.get(node.right, 0)
                heights[node] = 1 + max(left_h, right_h)
                diameter = max(diameter, left_h + right_h)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return diameter
