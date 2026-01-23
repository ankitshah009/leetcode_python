#1123. Lowest Common Ancestor of Deepest Leaves
#Medium
#
#Given the root of a binary tree, return the lowest common ancestor of its
#deepest leaves.
#
#Recall that:
#    The node of a binary tree is a leaf if and only if it has no children
#    The depth of the root of the tree is 0. If the depth of a node is d,
#    the depth of each of its children is d + 1.
#    The lowest common ancestor of a set S of nodes is the node A with the
#    largest depth such that every node in S is in the subtree with root A.
#
#Example 1:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4]
#Output: [2,7,4]
#Explanation: The deepest leaves are nodes 7 and 4.
#Their LCA is 2.
#
#Example 2:
#Input: root = [1]
#Output: [1]
#Explanation: The deepest leaf is node 1.
#
#Example 3:
#Input: root = [0,1,3,null,2]
#Output: [2]
#Explanation: The deepest leaf is node 2.
#
#Constraints:
#    The number of nodes in the tree will be in the range [1, 1000].
#    0 <= Node.val <= 1000
#    The values of the nodes in the tree are unique.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        DFS returning (node, depth).
        If left and right depths equal, current node is LCA.
        Otherwise, return the deeper subtree's result.
        """
        def dfs(node):
            if not node:
                return None, 0

            left_lca, left_depth = dfs(node.left)
            right_lca, right_depth = dfs(node.right)

            if left_depth == right_depth:
                return node, left_depth + 1
            elif left_depth > right_depth:
                return left_lca, left_depth + 1
            else:
                return right_lca, right_depth + 1

        return dfs(root)[0]


class SolutionTwoPass:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        First find max depth, then find LCA of all nodes at max depth.
        """
        def max_depth(node):
            if not node:
                return 0
            return 1 + max(max_depth(node.left), max_depth(node.right))

        target_depth = max_depth(root)

        def find_lca(node, depth):
            if not node:
                return None
            if depth == target_depth:
                return node

            left = find_lca(node.left, depth + 1)
            right = find_lca(node.right, depth + 1)

            if left and right:
                return node
            return left or right

        return find_lca(root, 1)
