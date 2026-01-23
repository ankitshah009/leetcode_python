#1026. Maximum Difference Between Node and Ancestor
#Medium
#
#Given the root of a binary tree, find the maximum value v for which there
#exist different nodes a and b where v = |a.val - b.val| and a is an
#ancestor of b.
#
#A node a is an ancestor of b if either: any child of a is equal to b or
#any child of a is an ancestor of b.
#
#Example 1:
#Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
#Output: 7
#Explanation: We have various ancestor-node differences, some of which are given below:
#|8 - 3| = 5
#|3 - 7| = 4
#|8 - 1| = 7
#|10 - 13| = 3
#Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
#
#Example 2:
#Input: root = [1,null,2,null,0,3]
#Output: 3
#
#Constraints:
#    The number of nodes in the tree is in the range [2, 5000].
#    0 <= Node.val <= 10^5

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Pass min and max values down the path.
        At each node, max diff is max(|val - min|, |val - max|)
        """
        def dfs(node, min_val, max_val):
            if not node:
                return max_val - min_val

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            left = dfs(node.left, min_val, max_val)
            right = dfs(node.right, min_val, max_val)

            return max(left, right)

        return dfs(root, root.val, root.val)


class SolutionBottomUp:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Return (min, max) from subtree, compute diff at each node.
        """
        self.result = 0

        def dfs(node):
            if not node:
                return float('inf'), float('-inf')

            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)

            subtree_min = min(left_min, right_min)
            subtree_max = max(left_max, right_max)

            # Compute diff with descendants
            if subtree_min != float('inf'):
                self.result = max(self.result, abs(node.val - subtree_min))
            if subtree_max != float('-inf'):
                self.result = max(self.result, abs(node.val - subtree_max))

            return min(node.val, subtree_min), max(node.val, subtree_max)

        dfs(root)
        return self.result
