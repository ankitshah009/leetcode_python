#250. Count Univalue Subtrees
#Medium
#
#Given the root of a binary tree, return the number of uni-value subtrees.
#
#A uni-value subtree means all nodes of the subtree have the same value.
#
#Example 1:
#Input: root = [5,1,5,5,5,null,5]
#Output: 4
#
#Example 2:
#Input: root = []
#Output: 0
#
#Example 3:
#Input: root = [5,5,5,5,5,null,5]
#Output: 6
#
#Constraints:
#    The number of the node in the tree will be in the range [0, 1000].
#    -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def is_uni(node):
            if not node:
                return True

            left_uni = is_uni(node.left)
            right_uni = is_uni(node.right)

            # Check if current subtree is uni-value
            if left_uni and right_uni:
                if node.left and node.left.val != node.val:
                    return False
                if node.right and node.right.val != node.val:
                    return False
                self.count += 1
                return True

            return False

        is_uni(root)
        return self.count

    # Alternative without class variable
    def countUnivalSubtreesAlt(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Returns (is_uni, count)
            if not node:
                return True, 0

            left_uni, left_count = dfs(node.left)
            right_uni, right_count = dfs(node.right)

            total = left_count + right_count

            if not left_uni or not right_uni:
                return False, total

            if node.left and node.left.val != node.val:
                return False, total

            if node.right and node.right.val != node.val:
                return False, total

            return True, total + 1

        _, count = dfs(root)
        return count
