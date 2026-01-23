#637. Average of Levels in Binary Tree
#Easy
#
#Given the root of a binary tree, return the average value of the nodes on each
#level in the form of an array. Answers within 10^-5 of the actual answer will
#be accepted.
#
#Example 1:
#Input: root = [3,9,20,null,null,15,7]
#Output: [3.00000,14.50000,11.00000]
#
#Example 2:
#Input: root = [3,9,20,15,7]
#Output: [3.00000,14.50000,11.00000]
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    -2^31 <= Node.val <= 2^31 - 1

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """BFS level order traversal"""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_size)

        return result


class SolutionDFS:
    """DFS with level tracking"""

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_sums = []  # (sum, count) for each level

        def dfs(node, level):
            if not node:
                return

            if level == len(level_sums):
                level_sums.append([0, 0])

            level_sums[level][0] += node.val
            level_sums[level][1] += 1

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return [s / c for s, c in level_sums]
