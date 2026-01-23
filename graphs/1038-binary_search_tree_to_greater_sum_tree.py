#1038. Binary Search Tree to Greater Sum Tree
#Medium
#
#Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
#such that every key of the original BST is changed to the original key plus
#the sum of all keys greater than the original key in BST.
#
#As a reminder, a binary search tree is a tree that satisfies these constraints:
#    The left subtree of a node contains only nodes with keys less than the
#    node's key.
#    The right subtree of a node contains only nodes with keys greater than
#    the node's key.
#    Both the left and right subtrees must also be binary search trees.
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
#    The number of nodes in the tree is in the range [1, 100].
#    0 <= Node.val <= 100
#    All the values in the tree are unique.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Reverse inorder traversal (right -> root -> left).
        Keep running sum of all visited nodes.
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
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Iterative reverse inorder using stack"""
        running_sum = 0
        stack = []
        node = root

        while stack or node:
            # Go right as far as possible
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()

            running_sum += node.val
            node.val = running_sum

            node = node.left

        return root


class SolutionMorris:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Morris traversal - O(1) space"""
        running_sum = 0
        node = root

        while node:
            if not node.right:
                # No right subtree, process node
                running_sum += node.val
                node.val = running_sum
                node = node.left
            else:
                # Find inorder successor (leftmost in right subtree)
                successor = node.right
                while successor.left and successor.left != node:
                    successor = successor.left

                if not successor.left:
                    # Make temporary link
                    successor.left = node
                    node = node.right
                else:
                    # Remove temporary link, process node
                    successor.left = None
                    running_sum += node.val
                    node.val = running_sum
                    node = node.left

        return root
