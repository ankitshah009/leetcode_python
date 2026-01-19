#617. Merge Two Binary Trees
#Easy
#
#You are given two binary trees root1 and root2.
#
#Imagine that when you put one of them to cover the other, some nodes of the two
#trees are overlapped while the others are not. You need to merge the two trees
#into a new binary tree. The merge rule is that if two nodes overlap, then sum
#node values up as the new value of the merged node. Otherwise, the NOT null node
#will be used as the node of the new tree.
#
#Return the merged tree.
#
#Example 1:
#Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
#Output: [3,4,5,5,4,null,7]
#
#Example 2:
#Input: root1 = [1], root2 = [1,2]
#Output: [2,2]
#
#Constraints:
#    The number of nodes in both trees is in the range [0, 2000].
#    -10^4 <= Node.val <= 10^4

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """Recursive merge - creates new tree"""
        if not root1:
            return root2
        if not root2:
            return root1

        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)

        return merged


class SolutionInPlace:
    """Merge into root1 (modifies input)"""

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1


class SolutionIterative:
    """Iterative BFS approach"""

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        queue = deque([(root1, root2)])

        while queue:
            node1, node2 = queue.popleft()
            node1.val += node2.val

            if node1.left and node2.left:
                queue.append((node1.left, node2.left))
            elif node2.left:
                node1.left = node2.left

            if node1.right and node2.right:
                queue.append((node1.right, node2.right))
            elif node2.right:
                node1.right = node2.right

        return root1
