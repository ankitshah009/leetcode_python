#1022. Sum of Root To Leaf Binary Numbers
#Easy
#
#You are given the root of a binary tree where each node has a value 0 or 1.
#Each root-to-leaf path represents a binary number starting with the most
#significant bit.
#
#Return the sum of these numbers, which is guaranteed to fit in a 32-bit integer.
#
#Example 1:
#Input: root = [1,0,1,0,1,0,1]
#Output: 22
#Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
#
#Example 2:
#Input: root = [0]
#Output: 0
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 1000].
#    Node.val is 0 or 1.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        DFS passing current binary value down.
        At leaf, add to total sum.
        """
        def dfs(node, current_val):
            if not node:
                return 0

            current_val = (current_val << 1) | node.val

            # If leaf, return value
            if not node.left and not node.right:
                return current_val

            return dfs(node.left, current_val) + dfs(node.right, current_val)

        return dfs(root, 0)


class SolutionIterative:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """Iterative DFS with stack"""
        if not root:
            return 0

        total = 0
        stack = [(root, 0)]

        while stack:
            node, current_val = stack.pop()
            current_val = (current_val << 1) | node.val

            if not node.left and not node.right:
                total += current_val
            else:
                if node.right:
                    stack.append((node.right, current_val))
                if node.left:
                    stack.append((node.left, current_val))

        return total
