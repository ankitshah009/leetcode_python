#671. Second Minimum Node In a Binary Tree
#Easy
#
#Given a non-empty special binary tree consisting of nodes with the non-negative
#value, where each node in this tree has exactly two or zero sub-node. If the node
#has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
#
#Given such a binary tree, you need to output the second minimum value in the set
#made of all the nodes' value in the whole tree.
#
#If no such second minimum value exists, output -1 instead.
#
#Example 1:
#Input: root = [2,2,5,null,null,5,7]
#Output: 5
#
#Example 2:
#Input: root = [2,2,2]
#Output: -1
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 25].
#    1 <= Node.val <= 2^31 - 1
#    For each node, root.val = min(root.left.val, root.right.val)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        """
        Root is always the minimum.
        Find the smallest value greater than root.
        """
        if not root:
            return -1

        min_val = root.val
        second_min = float('inf')

        def dfs(node):
            nonlocal second_min

            if not node:
                return

            # If node value is between min and current second_min
            if min_val < node.val < second_min:
                second_min = node.val
            # Only explore subtrees if node might have smaller values
            elif node.val == min_val:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return second_min if second_min != float('inf') else -1


class SolutionBFS:
    """BFS approach"""

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return -1

        min_val = root.val
        second_min = float('inf')

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if min_val < node.val < second_min:
                second_min = node.val
            elif node.val == min_val:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return second_min if second_min != float('inf') else -1


class SolutionSet:
    """Collect all unique values, find second minimum"""

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        values = set()

        def dfs(node):
            if node:
                values.add(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        if len(values) < 2:
            return -1

        values.remove(min(values))
        return min(values)
