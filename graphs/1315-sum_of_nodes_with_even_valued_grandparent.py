#1315. Sum of Nodes with Even-Valued Grandparent
#Medium
#
#Given the root of a binary tree, return the sum of values of nodes with an
#even-valued grandparent. If there are no nodes with an even-valued grandparent,
#return 0.
#
#A grandparent of a node is the parent of its parent if it exists.
#
#Example 1:
#Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
#Output: 18
#Explanation: The red nodes are the nodes with even-value grandparent while the
#blue nodes are the even-value grandparents.
#
#Example 2:
#Input: root = [1]
#Output: 0
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    1 <= Node.val <= 100

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        DFS passing parent and grandparent values.
        """
        def dfs(node, parent_val, grandparent_val):
            if not node:
                return 0

            total = 0
            if grandparent_val % 2 == 0:
                total += node.val

            total += dfs(node.left, node.val, parent_val)
            total += dfs(node.right, node.val, parent_val)

            return total

        return dfs(root, 1, 1)  # Use odd values as dummy


class SolutionAlt:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """Alternative: when we see even node, add grandchildren"""
        self.total = 0

        def dfs(node):
            if not node:
                return

            # If this node has even value, add grandchildren
            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        self.total += node.left.left.val
                    if node.left.right:
                        self.total += node.left.right.val
                if node.right:
                    if node.right.left:
                        self.total += node.right.left.val
                    if node.right.right:
                        self.total += node.right.right.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.total


class SolutionBFS:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """BFS approach"""
        from collections import deque

        if not root:
            return 0

        total = 0
        queue = deque([root])

        while queue:
            node = queue.popleft()

            # Check if this node is an even-valued grandparent
            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        total += node.left.left.val
                    if node.left.right:
                        total += node.left.right.val
                if node.right:
                    if node.right.left:
                        total += node.right.left.val
                    if node.right.right:
                        total += node.right.right.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return total
