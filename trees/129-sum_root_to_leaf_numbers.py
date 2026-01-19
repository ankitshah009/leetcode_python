#129. Sum Root to Leaf Numbers
#Medium
#
#You are given the root of a binary tree containing digits from 0 to 9 only.
#
#Each root-to-leaf path in the tree represents a number.
#
#Return the total sum of all root-to-leaf numbers.
#
#Example 1:
#Input: root = [1,2,3]
#Output: 25
#Explanation:
#The root-to-leaf path 1->2 represents the number 12.
#The root-to-leaf path 1->3 represents the number 13.
#Therefore, sum = 12 + 13 = 25.
#
#Example 2:
#Input: root = [4,9,0,5,1]
#Output: 1026
#Explanation:
#The root-to-leaf path 4->9->5 represents the number 495.
#The root-to-leaf path 4->9->1 represents the number 491.
#The root-to-leaf path 4->0 represents the number 40.
#Therefore, sum = 495 + 491 + 40 = 1026.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 1000].
#    0 <= Node.val <= 9
#    The depth of the tree will not exceed 10.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum = current_sum * 10 + node.val

            if not node.left and not node.right:
                return current_sum

            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)
