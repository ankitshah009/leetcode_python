#333. Largest BST Subtree
#Medium
#
#Given the root of a binary tree, find the largest subtree, which is also a
#Binary Search Tree (BST), where the largest means subtree has the largest number
#of nodes.
#
#A Binary Search Tree (BST) is a tree in which all the nodes follow the below-
#mentioned properties:
#    The left subtree values are less than the value of their parent (root) node.
#    The right subtree values are greater than the value of their parent (root) node.
#
#Note: A subtree must include all of its descendants.
#
#Example 1:
#Input: root = [10,5,15,1,8,null,7]
#Output: 3
#Explanation: The Largest BST Subtree is [5,1,8].
#
#Example 2:
#Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
#Output: 2
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 10^4].
#    -10^4 <= Node.val <= 10^4
#
#Follow up: Can you figure out ways to solve it with O(n) time complexity?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        # Returns (is_bst, size, min_val, max_val)
        self.max_size = 0

        def dfs(node):
            if not node:
                return True, 0, float('inf'), float('-inf')

            left_is_bst, left_size, left_min, left_max = dfs(node.left)
            right_is_bst, right_size, right_min, right_max = dfs(node.right)

            # Current subtree is BST if:
            # 1. Both subtrees are BST
            # 2. node.val > left_max and node.val < right_min
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                size = left_size + right_size + 1
                self.max_size = max(self.max_size, size)
                return True, size, min(left_min, node.val), max(right_max, node.val)

            return False, 0, 0, 0

        dfs(root)
        return self.max_size

    # Alternative without class variable
    def largestBSTSubtreeAlt(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Returns (is_bst, size, min_val, max_val, max_bst_size)
            if not node:
                return True, 0, float('inf'), float('-inf'), 0

            left = dfs(node.left)
            right = dfs(node.right)

            left_is_bst, left_size, left_min, left_max, left_max_bst = left
            right_is_bst, right_size, right_min, right_max, right_max_bst = right

            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                size = left_size + right_size + 1
                return (True, size, min(left_min, node.val),
                       max(right_max, node.val), size)

            return False, 0, 0, 0, max(left_max_bst, right_max_bst)

        return dfs(root)[4]
