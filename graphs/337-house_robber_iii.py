#337. House Robber III
#Medium
#
#The thief has found himself a new place for his thievery again. There is only
#one entrance to this area, called root.
#
#Besides the root, each house has one and only one parent house. After a tour,
#the smart thief realized that all houses in this place form a binary tree. It
#will automatically contact the police if two directly-linked houses were
#broken into on the same night.
#
#Given the root of the binary tree, return the maximum amount of money the
#thief can rob without alerting the police.
#
#Example 1:
#Input: root = [3,2,3,null,3,null,1]
#Output: 7
#Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#
#Example 2:
#Input: root = [3,4,5,1,3,null,1]
#Output: 9
#Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    0 <= Node.val <= 10^4

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        DP on tree.
        For each node, return (rob_this, skip_this).
        """
        def dfs(node):
            if not node:
                return 0, 0

            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            # If we rob this node, we must skip children
            rob_this = node.val + left_skip + right_skip

            # If we skip this node, we take max of each child
            skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)

            return rob_this, skip_this

        return max(dfs(root))


class SolutionMemo:
    """Memoization approach"""

    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(node, can_rob):
            if not node:
                return 0

            if (node, can_rob) in memo:
                return memo[(node, can_rob)]

            # Option 1: Skip this node
            result = dfs(node.left, True) + dfs(node.right, True)

            # Option 2: Rob this node (if allowed)
            if can_rob:
                rob_result = node.val + dfs(node.left, False) + dfs(node.right, False)
                result = max(result, rob_result)

            memo[(node, can_rob)] = result
            return result

        return dfs(root, True)


class SolutionSimpleMemo:
    """Simpler memoization - just track max for each node"""

    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(node):
            if not node:
                return 0

            if node in memo:
                return memo[node]

            # Option 1: Rob this node, skip children
            rob_this = node.val
            if node.left:
                rob_this += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                rob_this += dfs(node.right.left) + dfs(node.right.right)

            # Option 2: Skip this node, take max from children
            skip_this = dfs(node.left) + dfs(node.right)

            memo[node] = max(rob_this, skip_this)
            return memo[node]

        return dfs(root)
