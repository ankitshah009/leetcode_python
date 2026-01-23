#894. All Possible Full Binary Trees
#Medium
#
#Given an integer n, return a list of all possible full binary trees with n nodes.
#Each node of each tree in the answer must have Node.val == 0.
#
#Each element of the answer is the root node of one possible tree. You may return
#the final list of trees in any order.
#
#A full binary tree is a binary tree where each node has exactly 0 or 2 children.
#
#Example 1:
#Input: n = 7
#Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
#
#Example 2:
#Input: n = 3
#Output: [[0,0,0]]
#
#Constraints:
#    1 <= n <= 20

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        """
        Full binary tree requires odd number of nodes.
        Recursively build: root + left subtree + right subtree.
        """
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]

        result = []

        # Distribute remaining n-1 nodes between left and right (both must be odd)
        for left_nodes in range(1, n, 2):
            right_nodes = n - 1 - left_nodes

            for left_tree in self.allPossibleFBT(left_nodes):
                for right_tree in self.allPossibleFBT(right_nodes):
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    result.append(root)

        return result


class SolutionMemo:
    """With memoization"""

    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def build(n):
            if n % 2 == 0:
                return []
            if n == 1:
                return [TreeNode(0)]

            result = []
            for i in range(1, n, 2):
                for left in build(i):
                    for right in build(n - 1 - i):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)

            return result

        return build(n)


class SolutionDP:
    """Bottom-up DP"""

    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        if n % 2 == 0:
            return []

        dp = {1: [TreeNode(0)]}

        for nodes in range(3, n + 1, 2):
            dp[nodes] = []
            for left_nodes in range(1, nodes, 2):
                right_nodes = nodes - 1 - left_nodes

                for left in dp.get(left_nodes, []):
                    for right in dp.get(right_nodes, []):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        dp[nodes].append(root)

        return dp.get(n, [])
