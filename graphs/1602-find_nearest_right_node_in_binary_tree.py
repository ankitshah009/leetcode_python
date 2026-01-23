#1602. Find Nearest Right Node in Binary Tree
#Medium
#
#Given the root of a binary tree and a node u in the tree, return the nearest
#node on the same level that is to the right of u, or return null if u is the
#rightmost node in its level.
#
#Example 1:
#Input: root = [1,2,3,null,4,5,6], u = 4
#Output: 5
#Explanation: The nearest node on the same level to the right of node 4 is node 5.
#
#Example 2:
#Input: root = [3,null,4,2], u = 2
#Output: null
#Explanation: There are no nodes to the right of 2.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^5].
#    1 <= Node.val <= 10^5
#    All values in the tree are distinct.
#    u is a node in the binary tree rooted at root.

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        """
        BFS level-order traversal.
        Find u, then return the next node in the same level.
        """
        if not root:
            return None

        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if node == u:
                    # Check if there's a next node in this level
                    if i < level_size - 1:
                        return queue.popleft()
                    return None

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return None


class SolutionDFS:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        """
        DFS approach: track target depth and find next node at same depth.
        """
        self.target_depth = -1
        self.result = None

        def dfs(node: TreeNode, depth: int) -> bool:
            if not node or self.result:
                return False

            if self.target_depth == depth:
                # Found the next node at target depth
                self.result = node
                return True

            if node == u:
                # Found target, record its depth
                self.target_depth = depth
                return False

            # Traverse left to right (pre-order)
            return dfs(node.left, depth + 1) or dfs(node.right, depth + 1)

        dfs(root, 0)
        return self.result


class SolutionBFSSimple:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        """
        Simplified BFS with None as level separator.
        """
        queue = deque([root, None])

        while queue:
            node = queue.popleft()

            if node == u:
                return queue.popleft()  # Next node or None (level end)

            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            elif queue:
                # End of level, add separator for next level
                queue.append(None)

        return None


class SolutionRecursive:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        """
        Recursive approach using level tracking.
        """
        levels = []

        def build_levels(node: TreeNode, depth: int):
            if not node:
                return

            if depth >= len(levels):
                levels.append([])

            levels[depth].append(node)
            build_levels(node.left, depth + 1)
            build_levels(node.right, depth + 1)

        build_levels(root, 0)

        # Find u and return next node
        for level in levels:
            for i, node in enumerate(level):
                if node == u:
                    if i + 1 < len(level):
                        return level[i + 1]
                    return None

        return None
