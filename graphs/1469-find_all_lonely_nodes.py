#1469. Find All The Lonely Nodes
#Easy
#
#In a binary tree, a lonely node is a node that is the only child of its parent
#node. The root of the tree is not lonely because it does not have a parent node.
#
#Given the root of a binary tree, return an array containing the values of all
#lonely nodes in the tree. Return the list in any order.
#
#Example 1:
#Input: root = [1,2,3,null,4]
#Output: [4]
#Explanation: Light blue node is the only lonely node.
#Node 1 is the root and is not lonely.
#Nodes 2 and 3 have the same parent and are not lonely.
#
#Example 2:
#Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
#Output: [6,2]
#Explanation: Light blue nodes are lonely nodes.
#
#Example 3:
#Input: root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]
#Output: [77,55,33,66,44,22]
#Explanation: Nodes 99 and 88 share the same parent. Node 77 is the only child
#of node 99. Node 55 is the only child of node 77 and so on.
#Node 66 is the only child of node 88. Node 44 is the only child of node 66
#and so on.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 1000].
#    1 <= Node.val <= 10^6

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        """
        DFS: if a node has exactly one child, that child is lonely.
        """
        lonely = []

        def dfs(node: TreeNode) -> None:
            if not node:
                return

            # Check if exactly one child exists
            if node.left and not node.right:
                lonely.append(node.left.val)
            elif node.right and not node.left:
                lonely.append(node.right.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return lonely


class SolutionBFS:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        """BFS approach"""
        if not root:
            return []

        lonely = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            # Check children
            if node.left and not node.right:
                lonely.append(node.left.val)
            elif node.right and not node.left:
                lonely.append(node.right.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return lonely


class SolutionIterative:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        """Iterative DFS with stack"""
        if not root:
            return []

        lonely = []
        stack = [root]

        while stack:
            node = stack.pop()

            # Process children
            if node.left:
                if not node.right:
                    lonely.append(node.left.val)
                stack.append(node.left)

            if node.right:
                if not node.left:
                    lonely.append(node.right.val)
                stack.append(node.right)

        return lonely


class SolutionFunctional:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        """Functional style with list comprehension"""
        def collect(node: TreeNode) -> List[int]:
            if not node:
                return []

            result = []

            # Check if either child is lonely
            if node.left and not node.right:
                result.append(node.left.val)
            elif node.right and not node.left:
                result.append(node.right.val)

            return result + collect(node.left) + collect(node.right)

        return collect(root)
