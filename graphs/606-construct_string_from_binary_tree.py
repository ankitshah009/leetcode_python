#606. Construct String from Binary Tree
#Easy
#
#Given the root of a binary tree, construct a string consisting of parenthesis and
#integers from a binary tree with the preorder traversal way, and return it.
#
#Omit all the empty parenthesis pairs that do not affect the one-to-one mapping
#relationship between the string and the original binary tree.
#
#Example 1:
#Input: root = [1,2,3,4]
#Output: "1(2(4))(3)"
#
#Example 2:
#Input: root = [1,2,3,null,4]
#Output: "1(2()(4))(3)"
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    -1000 <= Node.val <= 1000

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """Recursive preorder traversal"""
        if not root:
            return ""

        result = str(root.val)

        if root.left or root.right:
            result += f"({self.tree2str(root.left)})"

        if root.right:
            result += f"({self.tree2str(root.right)})"

        return result


class SolutionIterative:
    """Iterative with stack"""

    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        result = []
        stack = [root]
        visited = set()

        while stack:
            node = stack[-1]

            if node in visited:
                stack.pop()
                result.append(")")
            else:
                visited.add(node)
                result.append(f"({node.val}")

                if not node.left and node.right:
                    result.append("()")

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return "".join(result)[1:-1]  # Remove outer parentheses
