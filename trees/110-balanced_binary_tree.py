#110. Balanced Binary Tree
#Easy
#
#Given a binary tree, determine if it is height-balanced.
#
#A height-balanced binary tree is a binary tree in which the depth of the two subtrees of
#every node never differs by more than one.
#
#Example 1:
#Input: root = [3,9,20,null,null,15,7]
#Output: true
#
#Example 2:
#Input: root = [1,2,2,3,3,null,null,4,4]
#Output: false
#
#Example 3:
#Input: root = []
#Output: true
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 5000].
#    -10^4 <= Node.val <= 10^4

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_height(node):
            if not node:
                return 0

            left_height = check_height(node.left)
            if left_height == -1:
                return -1

            right_height = check_height(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return check_height(root) != -1
