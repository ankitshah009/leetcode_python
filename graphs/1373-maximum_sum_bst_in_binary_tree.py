#1373. Maximum Sum BST in Binary Tree
#Hard
#
#Given a binary tree root, return the maximum sum of all keys of any sub-tree
#which is also a Binary Search Tree (BST).
#
#Assume a BST is defined as follows:
#    The left subtree of a node contains only nodes with keys less than the node's key.
#    The right subtree of a node contains only nodes with keys greater than the node's key.
#    Both the left and right subtrees must also be binary search trees.
#
#Example 1:
#Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
#Output: 20
#Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
#
#Example 2:
#Input: root = [4,3,null,1,2]
#Output: 2
#Explanation: Maximum sum in a valid Binary search tree is obtained in a single node with key equal to 2.
#
#Example 3:
#Input: root = [-4,-2,-5]
#Output: 0
#Explanation: All values are negatives. Return an empty BST.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 4 * 10^4].
#    -4 * 10^4 <= Node.val <= 4 * 10^4

from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        """
        Post-order DFS returning (is_bst, min_val, max_val, sum).
        """
        self.max_sum = 0

        def dfs(node) -> Tuple[bool, int, int, int]:
            """Returns (is_bst, min_val, max_val, subtree_sum)"""
            if not node:
                return (True, float('inf'), float('-inf'), 0)

            left_bst, left_min, left_max, left_sum = dfs(node.left)
            right_bst, right_min, right_max, right_sum = dfs(node.right)

            # Check if current subtree is BST
            if left_bst and right_bst and left_max < node.val < right_min:
                current_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, current_sum)

                return (True,
                        min(left_min, node.val),
                        max(right_max, node.val),
                        current_sum)

            # Not a BST
            return (False, 0, 0, 0)

        dfs(root)
        return self.max_sum


class SolutionExplicit:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        """More explicit implementation"""
        INF = float('inf')
        max_sum = [0]  # Use list for mutable closure

        def helper(node):
            # Returns (is_valid_bst, min_val, max_val, sum)
            if not node:
                return True, INF, -INF, 0

            # Get info from children
            l_valid, l_min, l_max, l_sum = helper(node.left)
            r_valid, r_min, r_max, r_sum = helper(node.right)

            # Current subtree is BST if:
            # 1. Both children are BSTs
            # 2. Current node > max of left subtree
            # 3. Current node < min of right subtree
            if l_valid and r_valid and l_max < node.val < r_min:
                curr_sum = l_sum + r_sum + node.val
                max_sum[0] = max(max_sum[0], curr_sum)

                curr_min = l_min if node.left else node.val
                curr_max = r_max if node.right else node.val

                return True, min(curr_min, node.val), max(curr_max, node.val), curr_sum

            return False, 0, 0, 0

        helper(root)
        return max_sum[0]
