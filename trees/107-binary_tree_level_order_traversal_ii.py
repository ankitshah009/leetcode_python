#107. Binary Tree Level Order Traversal II
#Medium
#
#Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
#(i.e., from left to right, level by level from leaf to root).
#
#Example 1:
#Input: root = [3,9,20,null,null,15,7]
#Output: [[15,7],[9,20],[3]]
#
#Example 2:
#Input: root = [1]
#Output: [[1]]
#
#Example 3:
#Input: root = []
#Output: []
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 2000].
#    -1000 <= Node.val <= 1000

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result[::-1]
