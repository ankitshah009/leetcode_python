#623. Add One Row to Tree
#Medium
#
#Given the root of a binary tree and two integers val and depth, add a row of
#nodes with value val at the given depth depth.
#
#Note that the root node is at depth 1.
#
#The adding rule is:
#- Given the integer depth, for each not null tree node cur at the depth depth - 1,
#  create two tree nodes with value val as cur's left subtree root and right
#  subtree root.
#- cur's original left subtree should be the left subtree of the new left subtree root.
#- cur's original right subtree should be the right subtree of the new right subtree root.
#- If depth == 1 that means there is no depth depth - 1 at all, then create a tree
#  node with value val as the new root of the whole original tree, and the original
#  tree is the new root's left subtree.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    The depth of the tree is in the range [1, 10^4].
#    -100 <= Node.val <= 100
#    -10^5 <= val <= 10^5
#    1 <= depth <= the depth of tree + 1

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """DFS recursive approach"""
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        def dfs(node, curr_depth):
            if not node:
                return

            if curr_depth == depth - 1:
                # Insert new row
                new_left = TreeNode(val)
                new_right = TreeNode(val)
                new_left.left = node.left
                new_right.right = node.right
                node.left = new_left
                node.right = new_right
            else:
                dfs(node.left, curr_depth + 1)
                dfs(node.right, curr_depth + 1)

        dfs(root, 1)
        return root


class SolutionBFS:
    """BFS level order traversal"""

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        queue = deque([root])
        curr_depth = 1

        while queue and curr_depth < depth - 1:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            curr_depth += 1

        # Insert new row
        for node in queue:
            new_left = TreeNode(val)
            new_right = TreeNode(val)
            new_left.left = node.left
            new_right.right = node.right
            node.left = new_left
            node.right = new_right

        return root
