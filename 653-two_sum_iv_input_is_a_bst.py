#653. Two Sum IV - Input is a BST
#Easy
#
#Given the root of a binary search tree and an integer k, return true if there exist two
#elements in the BST such that their sum is equal to k, or false otherwise.
#
#Example 1:
#Input: root = [5,3,6,2,4,null,7], k = 9
#Output: true
#
#Example 2:
#Input: root = [5,3,6,2,4,null,7], k = 28
#Output: false
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    -10^4 <= Node.val <= 10^4
#    root is guaranteed to be a valid binary search tree.
#    -10^5 <= k <= 10^5

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return False

            complement = k - node.val
            if complement in seen:
                return True

            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
