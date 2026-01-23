#538. Convert BST to Greater Tree
#Medium
#
#Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such
#that every key of the original BST is changed to the original key plus the sum
#of all keys greater than the original key in BST.
#
#Example 1:
#Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
#Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
#
#Example 2:
#Input: root = [0,null,1]
#Output: [1,null,1]
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 10^4].
#    -10^4 <= Node.val <= 10^4
#    All the values in the tree are unique.
#    root is guaranteed to be a valid binary search tree.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Reverse inorder traversal (right -> node -> left).
        Accumulate sum of all visited nodes.
        """
        self.running_sum = 0

        def reverse_inorder(node):
            if not node:
                return

            reverse_inorder(node.right)

            self.running_sum += node.val
            node.val = self.running_sum

            reverse_inorder(node.left)

        reverse_inorder(root)
        return root


class SolutionIterative:
    """Iterative reverse inorder"""

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        running_sum = 0
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.right

            curr = stack.pop()
            running_sum += curr.val
            curr.val = running_sum

            curr = curr.left

        return root


class SolutionMorris:
    """Morris traversal - O(1) space"""

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        running_sum = 0
        curr = root

        while curr:
            if not curr.right:
                running_sum += curr.val
                curr.val = running_sum
                curr = curr.left
            else:
                # Find inorder successor
                succ = curr.right
                while succ.left and succ.left != curr:
                    succ = succ.left

                if not succ.left:
                    succ.left = curr
                    curr = curr.right
                else:
                    succ.left = None
                    running_sum += curr.val
                    curr.val = running_sum
                    curr = curr.left

        return root
