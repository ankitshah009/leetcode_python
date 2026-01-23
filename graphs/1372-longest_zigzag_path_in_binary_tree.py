#1372. Longest ZigZag Path in a Binary Tree
#Medium
#
#You are given the root of a binary tree.
#
#A ZigZag path for a binary tree is defined as follow:
#    Choose any node in the binary tree and a direction (right or left).
#    If the current direction is right, move to the right child of the current
#    node; otherwise, move to the left child.
#    Change the direction from right to left or from left to right.
#    Repeat the second and third steps until you can't move in the tree.
#
#Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
#
#Return the longest ZigZag path contained in that tree.
#
#Example 1:
#Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
#Output: 3
#
#Example 2:
#Input: root = [1,1,1,null,1,null,null,1,1,null,1]
#Output: 4
#
#Example 3:
#Input: root = [1]
#Output: 0
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 5 * 10^4].
#    1 <= Node.val <= 100

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        DFS tracking length going left and going right from each node.
        """
        self.max_length = 0

        def dfs(node, going_left, length):
            if not node:
                return

            self.max_length = max(self.max_length, length)

            if going_left:
                # We came from parent's left, now go right to continue zigzag
                dfs(node.right, False, length + 1)
                # Or start fresh going left
                dfs(node.left, True, 1)
            else:
                # We came from parent's right, now go left to continue zigzag
                dfs(node.left, True, length + 1)
                # Or start fresh going right
                dfs(node.right, False, 1)

        # Start from root going both directions
        dfs(root.left, True, 1) if root.left else None
        dfs(root.right, False, 1) if root.right else None

        return self.max_length


class SolutionReturnBoth:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """Return both left and right zigzag lengths"""
        self.max_len = 0

        def dfs(node):
            """Returns (left_zigzag_length, right_zigzag_length)"""
            if not node:
                return (-1, -1)

            left_l, left_r = dfs(node.left)
            right_l, right_r = dfs(node.right)

            # Length going left from current = 1 + right zigzag from left child
            go_left = left_r + 1
            # Length going right from current = 1 + left zigzag from right child
            go_right = right_l + 1

            self.max_len = max(self.max_len, go_left, go_right)

            return (go_left, go_right)

        dfs(root)
        return self.max_len
