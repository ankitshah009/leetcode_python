#1080. Insufficient Nodes in Root to Leaf Paths
#Medium
#
#Given the root of a binary tree and an integer limit, delete all insufficient
#nodes in the tree simultaneously, and return the root of the resulting
#binary tree.
#
#A node is insufficient if every root to leaf path intersecting this node
#has a sum strictly less than limit.
#
#A leaf is a node with no children.
#
#Example 1:
#Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
#Output: [1,2,3,4,null,null,7,8,9,null,14]
#
#Example 2:
#Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
#Output: [5,4,8,11,null,17,4,7,null,null,null,5]
#
#Example 3:
#Input: root = [1,2,-3,-5,null,4,null], limit = -1
#Output: [1,null,-3,4]
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 5000].
#    -10^5 <= Node.val <= 10^5
#    -10^9 <= limit <= 10^9

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        """
        DFS: Return max path sum from this node to any leaf.
        If max sum < limit, remove node.
        """
        def dfs(node, current_sum):
            if not node:
                return float('-inf')

            current_sum += node.val

            # Leaf node
            if not node.left and not node.right:
                return current_sum

            # Check children
            left_max = dfs(node.left, current_sum)
            right_max = dfs(node.right, current_sum)

            # Prune insufficient children
            if left_max < limit:
                node.left = None
            if right_max < limit:
                node.right = None

            return max(left_max, right_max)

        max_sum = dfs(root, 0)
        return None if max_sum < limit else root


class SolutionAlternative:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        """
        Return None if node should be deleted, else return node.
        """
        def dfs(node, prefix_sum):
            if not node:
                return None

            prefix_sum += node.val

            # Leaf node
            if not node.left and not node.right:
                return None if prefix_sum < limit else node

            # Recurse
            node.left = dfs(node.left, prefix_sum)
            node.right = dfs(node.right, prefix_sum)

            # If both children are deleted, this node is insufficient
            if not node.left and not node.right:
                return None

            return node

        return dfs(root, 0)
