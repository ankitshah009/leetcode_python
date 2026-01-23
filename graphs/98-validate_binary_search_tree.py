#98. Validate Binary Search Tree
#Medium
#
#Given the root of a binary tree, determine if it is a valid binary search tree
#(BST).
#
#A valid BST is defined as follows:
#- The left subtree of a node contains only nodes with keys less than the node's
#  key.
#- The right subtree of a node contains only nodes with keys greater than the
#  node's key.
#- Both the left and right subtrees must also be binary search trees.
#
#Example 1:
#Input: root = [2,1,3]
#Output: true
#
#Example 2:
#Input: root = [5,1,4,null,null,3,6]
#Output: false
#Explanation: The root node's value is 5 but its right child's value is 4.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    -2^31 <= Node.val <= 2^31 - 1

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Recursive with min/max bounds.
        """
        def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        return validate(root, float('-inf'), float('inf'))


class SolutionInorder:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Inorder traversal - should produce sorted sequence.
        """
        prev = float('-inf')

        def inorder(node: Optional[TreeNode]) -> bool:
            nonlocal prev

            if not node:
                return True

            if not inorder(node.left):
                return False

            if node.val <= prev:
                return False

            prev = node.val

            return inorder(node.right)

        return inorder(root)


class SolutionIterative:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative inorder traversal.
        """
        stack = []
        prev = float('-inf')
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if current.val <= prev:
                return False

            prev = current.val
            current = current.right

        return True


class SolutionBFS:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        BFS with bounds tracking.
        """
        if not root:
            return True

        queue = [(root, float('-inf'), float('inf'))]

        while queue:
            node, min_val, max_val = queue.pop(0)

            if node.val <= min_val or node.val >= max_val:
                return False

            if node.left:
                queue.append((node.left, min_val, node.val))

            if node.right:
                queue.append((node.right, node.val, max_val))

        return True
