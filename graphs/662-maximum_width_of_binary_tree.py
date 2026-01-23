#662. Maximum Width of Binary Tree
#Medium
#
#Given the root of a binary tree, return the maximum width of the given tree.
#
#The maximum width of a tree is the maximum width among all levels.
#
#The width of one level is defined as the length between the end-nodes (the
#leftmost and rightmost non-null nodes), where the null nodes between the
#end-nodes that would be present in a complete binary tree extending down to
#that level are also counted into the length calculation.
#
#Example 1:
#Input: root = [1,3,2,5,3,null,9]
#Output: 4
#
#Example 2:
#Input: root = [1,3,2,5,null,null,9,6,null,7]
#Output: 7
#
#Example 3:
#Input: root = [1,3,2,5]
#Output: 2
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 3000].
#    -100 <= Node.val <= 100

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        BFS with position indexing.
        Left child = 2*pos, Right child = 2*pos + 1
        """
        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 0)])  # (node, position)

        while queue:
            level_size = len(queue)
            _, first_pos = queue[0]

            for _ in range(level_size):
                node, pos = queue.popleft()

                # Normalize position to avoid overflow
                pos -= first_pos

                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))

            # Width is difference between last and first position + 1
            last_pos = pos
            max_width = max(max_width, last_pos + 1)

        return max_width


class SolutionDFS:
    """DFS with leftmost position tracking"""

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        leftmost = {}  # level -> leftmost position at that level
        self.max_width = 0

        def dfs(node, level, pos):
            if not node:
                return

            if level not in leftmost:
                leftmost[level] = pos

            self.max_width = max(self.max_width, pos - leftmost[level] + 1)

            dfs(node.left, level + 1, 2 * pos)
            dfs(node.right, level + 1, 2 * pos + 1)

        dfs(root, 0, 0)
        return self.max_width


class SolutionBFSOptimized:
    """BFS with offset normalization per level"""

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 1
        level = [(root, 0)]

        while level:
            next_level = []
            for node, pos in level:
                if node.left:
                    next_level.append((node.left, pos * 2))
                if node.right:
                    next_level.append((node.right, pos * 2 + 1))

            if next_level:
                # Normalize positions
                min_pos = next_level[0][1]
                next_level = [(node, pos - min_pos) for node, pos in next_level]
                max_width = max(max_width, next_level[-1][1] + 1)

            level = next_level

        return max_width
