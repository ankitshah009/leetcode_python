#199. Binary Tree Right Side View
#Medium
#
#Given the root of a binary tree, imagine yourself standing on the right side
#of it, return the values of the nodes you can see ordered from top to bottom.
#
#Example 1:
#Input: root = [1,2,3,null,5,null,4]
#Output: [1,3,4]
#
#Example 2:
#Input: root = [1,null,3]
#Output: [1,3]
#
#Example 3:
#Input: root = []
#Output: []
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 100].
#    -100 <= Node.val <= 100

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """BFS level-by-level, take last node of each level"""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # Last node in this level
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


class SolutionDFS:
    """DFS approach - visit right child first"""

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth):
            if not node:
                return

            # First node we see at this depth is the rightmost
            if depth == len(result):
                result.append(node.val)

            # Visit right first, then left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result


class SolutionDFSDict:
    """DFS with dictionary to track rightmost at each level"""

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightmost = {}
        max_depth = -1

        def dfs(node, depth):
            nonlocal max_depth
            if not node:
                return

            max_depth = max(max_depth, depth)

            # Always update - last update at each depth will be from left subtree
            # but we visit right last, so it will be rightmost
            if depth not in rightmost:
                rightmost[depth] = node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            rightmost[depth] = node.val  # Right overwrites left

        dfs(root, 0)
        return [rightmost[i] for i in range(max_depth + 1)] if root else []
