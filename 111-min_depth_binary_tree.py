#111. Minimum Depth of Binary Tree
#Easy
#
#Given a binary tree, find its minimum depth.
#
#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
#Note: A leaf is a node with no children.
#
# 
#
#Example 1:
#
#Input: root = [3,9,20,null,null,15,7]
#Output: 2
#
#Example 2:
#
#Input: root = [2,null,3,null,4,null,5,null,6]
#Output: 5
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left:
            return 1+self.minDepth(root.right)
        elif not root.right:
            return 1+self.minDepth(root.left)
        else:
            return 1+min(self.minDepth(root.right), self.minDepth(root.left))
