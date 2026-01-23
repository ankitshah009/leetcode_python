#563. Binary Tree Tilt
#Easy
#
#Given the root of a binary tree, return the sum of every tree node's tilt.
#
#The tilt of a tree node is the absolute difference between the sum of all left
#subtree node values and all right subtree node values. If a node does not have
#a left child, then the sum of the left subtree node values is treated as 0.
#The rule is similar if the node does not have a right child.
#
#Example 1:
#Input: root = [1,2,3]
#Output: 1
#Explanation:
#Tilt of node 2 : |0-0| = 0 (no children)
#Tilt of node 3 : |0-0| = 0 (no children)
#Tilt of node 1 : |2-3| = 1 (left subtree is just node 2, right subtree is just node 3)
#Sum of every tilt : 0 + 0 + 1 = 1
#
#Example 2:
#Input: root = [4,2,9,3,5,null,7]
#Output: 15
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 10^4].
#    -1000 <= Node.val <= 1000

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        """DFS returning subtree sum while accumulating tilt"""
        self.total_tilt = 0

        def subtree_sum(node):
            if not node:
                return 0

            left_sum = subtree_sum(node.left)
            right_sum = subtree_sum(node.right)

            self.total_tilt += abs(left_sum - right_sum)

            return node.val + left_sum + right_sum

        subtree_sum(root)
        return self.total_tilt


class SolutionTuple:
    """Return both sum and tilt"""

    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            """Returns (subtree_sum, total_tilt)"""
            if not node:
                return 0, 0

            left_sum, left_tilt = dfs(node.left)
            right_sum, right_tilt = dfs(node.right)

            current_tilt = abs(left_sum - right_sum)
            total_sum = node.val + left_sum + right_sum
            total_tilt = current_tilt + left_tilt + right_tilt

            return total_sum, total_tilt

        return dfs(root)[1]
