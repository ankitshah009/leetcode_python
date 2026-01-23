#1161. Maximum Level Sum of a Binary Tree
#Medium
#
#Given the root of a binary tree, the level of its root is 1, the level of
#its children is 2, and so on.
#
#Return the smallest level x such that the sum of all the values of nodes at
#level x is maximal.
#
#Example 1:
#Input: root = [1,7,0,7,-8,null,null]
#Output: 2
#Explanation:
#Level 1 sum = 1.
#Level 2 sum = 7 + 0 = 7.
#Level 3 sum = 7 + -8 = -1.
#So we return the level with the maximum sum which is level 2.
#
#Example 2:
#Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
#Output: 2
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    -10^5 <= Node.val <= 10^5

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """BFS level by level, track maximum sum"""
        if not root:
            return 0

        queue = deque([root])
        max_sum = float('-inf')
        max_level = 1
        level = 0

        while queue:
            level += 1
            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

        return max_level


class SolutionDFS:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """DFS collecting sums by level"""
        level_sums = []

        def dfs(node, level):
            if not node:
                return

            if level >= len(level_sums):
                level_sums.append(0)

            level_sums[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        # Find level with max sum (1-indexed)
        max_sum = max(level_sums)
        return level_sums.index(max_sum) + 1
