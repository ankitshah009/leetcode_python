#1302. Deepest Leaves Sum
#Medium
#
#Given the root of a binary tree, return the sum of values of its deepest leaves.
#
#Example 1:
#Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
#Output: 15
#
#Example 2:
#Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
#Output: 19
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    1 <= Node.val <= 100

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        BFS level order traversal.
        Return sum of last level.
        """
        if not root:
            return 0

        queue = deque([root])
        level_sum = 0

        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return level_sum


class SolutionDFS:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """DFS tracking depth"""
        self.max_depth = 0
        self.total = 0

        def dfs(node, depth):
            if not node:
                return

            if depth > self.max_depth:
                self.max_depth = depth
                self.total = node.val
            elif depth == self.max_depth:
                self.total += node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return self.total


class SolutionTwoPass:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """Two pass: find max depth, then sum leaves at that depth"""
        def get_depth(node):
            if not node:
                return 0
            return 1 + max(get_depth(node.left), get_depth(node.right))

        def sum_at_depth(node, current, target):
            if not node:
                return 0
            if current == target:
                return node.val
            return sum_at_depth(node.left, current + 1, target) + \
                   sum_at_depth(node.right, current + 1, target)

        max_depth = get_depth(root)
        return sum_at_depth(root, 1, max_depth)
