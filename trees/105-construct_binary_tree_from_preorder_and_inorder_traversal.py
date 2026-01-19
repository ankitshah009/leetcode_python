#105. Construct Binary Tree from Preorder and Inorder Traversal
#Medium
#
#Given two integer arrays preorder and inorder where preorder is the preorder traversal of
#a binary tree and inorder is the inorder traversal of the same tree, construct and return
#the binary tree.
#
#Example 1:
#Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#Output: [3,9,20,null,null,15,7]
#
#Example 2:
#Input: preorder = [-1], inorder = [-1]
#Output: [-1]
#
#Constraints:
#    1 <= preorder.length <= 3000
#    inorder.length == preorder.length
#    -3000 <= preorder[i], inorder[i] <= 3000
#    preorder and inorder consist of unique values.
#    Each value of inorder also appears in preorder.
#    preorder is guaranteed to be the preorder traversal of the tree.
#    inorder is guaranteed to be the inorder traversal of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.preorder_idx = 0

        def build(left, right):
            if left > right:
                return None

            root_val = preorder[self.preorder_idx]
            self.preorder_idx += 1

            root = TreeNode(root_val)
            inorder_idx = inorder_map[root_val]

            root.left = build(left, inorder_idx - 1)
            root.right = build(inorder_idx + 1, right)

            return root

        return build(0, len(inorder) - 1)
