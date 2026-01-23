#94. Binary Tree Inorder Traversal
#Easy
#
#Given the root of a binary tree, return the inorder traversal of its nodes'
#values.
#
#Example 1:
#Input: root = [1,null,2,3]
#Output: [1,3,2]
#
#Example 2:
#Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
#Output: [4,2,6,5,7,1,3,9,8]
#
#Example 3:
#Input: root = []
#Output: []
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 100].
#    -100 <= Node.val <= 100

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Recursive approach.
        """
        result = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result


class SolutionIterative:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative with stack.
        """
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result


class SolutionMorris:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Morris traversal - O(1) space.
        """
        result = []
        current = root

        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                # Find inorder predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if not predecessor.right:
                    # Make current the right child of predecessor
                    predecessor.right = current
                    current = current.left
                else:
                    # Revert the modification
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right

        return result


class SolutionGenerator:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Using generator.
        """
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        return list(inorder(root))
