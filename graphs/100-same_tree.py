#100. Same Tree
#Easy
#
#Given the roots of two binary trees p and q, write a function to check if they
#are the same or not.
#
#Two binary trees are considered the same if they are structurally identical, and
#the nodes have the same value.
#
#Example 1:
#Input: p = [1,2,3], q = [1,2,3]
#Output: true
#
#Example 2:
#Input: p = [1,2], q = [1,null,2]
#Output: false
#
#Example 3:
#Input: p = [1,2,1], q = [1,1,2]
#Output: false
#
#Constraints:
#    The number of nodes in both trees is in the range [0, 100].
#    -10^4 <= Node.val <= 10^4

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Recursive comparison.
        """
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class SolutionIterative:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Iterative BFS comparison.
        """
        from collections import deque

        queue = deque([(p, q)])

        while queue:
            node1, node2 = queue.popleft()

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))

        return True


class SolutionDFS:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Iterative DFS with stack.
        """
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True


class SolutionSerialization:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Serialize and compare (for educational purpose).
        """
        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return "null"
            return f"{node.val},{serialize(node.left)},{serialize(node.right)}"

        return serialize(p) == serialize(q)
