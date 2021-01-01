#104. Maximum Depth of Binary Tree
#Easy
#
#Given the root of a binary tree, return its maximum depth.
#
#A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# 
#
#Example 1:
#
#Input: root = [3,9,20,null,null,15,7]
#Output: 3
#
#Example 2:
#
#Input: root = [1,null,2]
#Output: 2
#
#Example 3:
#
#Input: root = []
#Output: 0
#
#Example 4:
#
#Input: root = [0]
#Output: 1
#
# 
#
#Constraints:
#
#    The number of nodes in the tree is in the range [0, 104].
#    -100 <= Node.val <= 100
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    height = 0
    def maxDepth(self, root: TreeNode) -> int:
        def setHeight(root, height):
            if root:
                if self.height < height:
                    self.height = height
                setHeight(root.left, height+1) 
                setHeight(root.right, height+1)
        
        setHeight(root, self.height+1)
        return self.height
