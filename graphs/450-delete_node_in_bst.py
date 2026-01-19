#450. Delete Node in a BST
#Medium
#
#Given a root node reference of a BST and a key, delete the node with the given
#key in the BST. Return the root node reference (possibly updated) of the BST.
#
#Basically, the deletion can be divided into two stages:
#1. Search for a node to remove.
#2. If the node is found, delete the node.
#
#Example 1:
#Input: root = [5,3,6,2,4,null,7], key = 3
#Output: [5,4,6,2,null,null,7]
#Explanation: Given key to delete is 3. So we find the node with value 3 and
#delete it.
#One valid answer is [5,4,6,2,null,null,7].
#Another valid answer is [5,2,6,null,4,null,7].
#
#Example 2:
#Input: root = [5,3,6,2,4,null,7], key = 0
#Output: [5,3,6,2,4,null,7]
#Explanation: The tree does not contain a node with value = 0.
#
#Example 3:
#Input: root = [], key = 0
#Output: []
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 10^4].
#    -10^5 <= Node.val <= 10^5
#    Each node has a unique value.
#    root is a valid binary search tree.
#    -10^5 <= key <= 10^5

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """Recursive deletion"""
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to delete found
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Node has two children
            # Find inorder successor (smallest in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left

            # Replace value with successor
            root.val = successor.val
            # Delete successor
            root.right = self.deleteNode(root.right, successor.val)

        return root


class SolutionPredecessor:
    """Using inorder predecessor instead of successor"""

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Find inorder predecessor (largest in left subtree)
            predecessor = root.left
            while predecessor.right:
                predecessor = predecessor.right

            root.val = predecessor.val
            root.left = self.deleteNode(root.left, predecessor.val)

        return root


class SolutionIterative:
    """Iterative approach"""

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Find the node and its parent
        parent = None
        current = root

        while current and current.val != key:
            parent = current
            if key < current.val:
                current = current.left
            else:
                current = current.right

        if not current:
            return root

        # Case: Node has at most one child
        if not current.left or not current.right:
            child = current.left if current.left else current.right

            if not parent:
                return child
            if parent.left == current:
                parent.left = child
            else:
                parent.right = child
        else:
            # Case: Node has two children
            successor_parent = current
            successor = current.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            current.val = successor.val

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return root
