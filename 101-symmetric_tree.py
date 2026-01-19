#101. Symmetric Tree
#Easy
#
#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric
#around its center).
#
#Example 1:
#Input: root = [1,2,2,3,4,4,3]
#Output: true
#
#Example 2:
#Input: root = [1,2,2,null,3,null,3]
#Output: false
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 1000].
#    -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right) if root else True
