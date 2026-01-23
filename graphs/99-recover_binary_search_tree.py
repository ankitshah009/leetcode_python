#99. Recover Binary Search Tree
#Medium
#
#You are given the root of a binary search tree (BST), where the values of
#exactly two nodes of the tree were swapped by mistake. Recover the tree without
#changing its structure.
#
#Example 1:
#Input: root = [1,3,null,null,2]
#Output: [3,1,null,null,2]
#Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3
#makes the BST valid.
#
#Example 2:
#Input: root = [3,1,4,null,null,2]
#Output: [2,1,4,null,null,3]
#Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2
#and 3 makes the BST valid.
#
#Constraints:
#    The number of nodes in the tree is in the range [2, 1000].
#    -2^31 <= Node.val <= 2^31 - 1

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Morris traversal - O(1) space.
        Find two swapped nodes during inorder traversal.
        """
        first = second = prev = None

        curr = root
        while curr:
            if not curr.left:
                # Process current node
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                # Find predecessor
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right

                if not predecessor.right:
                    # First visit - create thread
                    predecessor.right = curr
                    curr = curr.left
                else:
                    # Second visit - remove thread, process node
                    predecessor.right = None
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right

        # Swap values
        if first and second:
            first.val, second.val = second.val, first.val


class SolutionInorder:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Recursive inorder traversal.
        """
        self.first = self.second = self.prev = None

        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            inorder(node.left)

            # Check for violation
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        # Swap values
        self.first.val, self.second.val = self.second.val, self.first.val


class SolutionIterative:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Iterative inorder with stack.
        """
        stack = []
        first = second = prev = None
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Check for violation
            if prev and prev.val > curr.val:
                if not first:
                    first = prev
                second = curr

            prev = curr
            curr = curr.right

        # Swap values
        first.val, second.val = second.val, first.val


class SolutionSort:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Collect values, sort, reassign (uses O(n) space).
        """
        nodes = []
        values = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        values.sort()

        for i, node in enumerate(nodes):
            node.val = values[i]
