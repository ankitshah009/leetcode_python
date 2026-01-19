#404. Sum of Left Leaves
#Easy
#
#Given the root of a binary tree, return the sum of all left leaves.
#
#A leaf is a node with no children. A left leaf is a leaf that is the left
#child of another node.
#
#Example 1:
#Input: root = [3,9,20,null,null,15,7]
#Output: 24
#Explanation: There are two left leaves in the binary tree, with values 9 and
#15 respectively. Their sum is 24.
#
#Example 2:
#Input: root = [1]
#Output: 0
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 1000].
#    -1000 <= Node.val <= 1000

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """Recursive DFS with flag for left child"""
        def dfs(node, is_left):
            if not node:
                return 0

            # Check if it's a leaf
            if not node.left and not node.right:
                return node.val if is_left else 0

            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)


class SolutionIterative:
    """Iterative BFS"""

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        from collections import deque
        queue = deque([(root, False)])
        total = 0

        while queue:
            node, is_left = queue.popleft()

            if not node.left and not node.right:
                if is_left:
                    total += node.val
            else:
                if node.left:
                    queue.append((node.left, True))
                if node.right:
                    queue.append((node.right, False))

        return total


class SolutionStack:
    """Iterative DFS with stack"""

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, False)]
        total = 0

        while stack:
            node, is_left = stack.pop()

            if not node.left and not node.right:
                if is_left:
                    total += node.val
            else:
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, True))

        return total


class SolutionSimple:
    """Simple recursive without flag parameter"""

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = 0

        # Check if left child is a leaf
        if root.left:
            if not root.left.left and not root.left.right:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)

        total += self.sumOfLeftLeaves(root.right)

        return total
