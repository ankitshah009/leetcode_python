#1339. Maximum Product of Splitted Binary Tree
#Medium
#
#Given the root of a binary tree, split the binary tree into two subtrees by
#removing one edge such that the product of the sums of the subtrees is maximized.
#
#Return the maximum product of the sums of the two subtrees. Since the answer
#may be too large, return it modulo 10^9 + 7.
#
#Note that you need to maximize the answer before taking the mod and not after
#taking it.
#
#Example 1:
#Input: root = [1,2,3,4,5,6]
#Output: 110
#Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
#
#Example 2:
#Input: root = [1,null,2,3,4,null,null,5,6]
#Output: 90
#Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6. Their product is 90 (15*6)
#
#Constraints:
#    The number of nodes in the tree is in the range [2, 5 * 10^4].
#    1 <= Node.val <= 10^4

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        First pass: compute total sum.
        Second pass: for each subtree sum S, product = S * (total - S).
        """
        MOD = 10**9 + 7

        # First pass: compute total sum
        def tree_sum(node):
            if not node:
                return 0
            return node.val + tree_sum(node.left) + tree_sum(node.right)

        total = tree_sum(root)

        # Second pass: find all subtree sums and compute max product
        self.max_product = 0

        def find_subtree_sums(node):
            if not node:
                return 0

            subtree_sum = node.val + find_subtree_sums(node.left) + find_subtree_sums(node.right)
            product = subtree_sum * (total - subtree_sum)
            self.max_product = max(self.max_product, product)

            return subtree_sum

        find_subtree_sums(root)

        return self.max_product % MOD


class SolutionOnePass:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """Store all subtree sums, then find max product"""
        MOD = 10**9 + 7
        subtree_sums = []

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            subtree_sums.append(s)
            return s

        total = dfs(root)

        max_product = 0
        for s in subtree_sums:
            max_product = max(max_product, s * (total - s))

        return max_product % MOD
