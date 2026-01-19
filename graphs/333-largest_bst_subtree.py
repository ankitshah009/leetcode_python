#333. Largest BST Subtree
#Medium
#
#Given the root of a binary tree, find the largest subtree, which is also a
#Binary Search Tree (BST), where the largest means subtree has the largest
#number of nodes.
#
#A Binary Search Tree (BST) is a tree in which all the nodes follow the
#below-mentioned properties:
#- The left subtree values are less than the value of their parent (root) node.
#- The right subtree values are greater than the value of their parent node.
#
#Example 1:
#Input: root = [10,5,15,1,8,null,7]
#Output: 3
#Explanation: The largest BST subtree is [5,1,8]. The return value is the
#subtree's size, which is 3.
#
#Example 2:
#Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
#Output: 2
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 10^4].
#    -10^4 <= Node.val <= 10^4

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        """
        Post-order traversal.
        For each subtree, track: (is_bst, size, min_val, max_val)
        """
        self.max_size = 0

        def dfs(node):
            if not node:
                # Empty tree is BST with size 0
                return True, 0, float('inf'), float('-inf')

            left_is_bst, left_size, left_min, left_max = dfs(node.left)
            right_is_bst, right_size, right_min, right_max = dfs(node.right)

            # Check if current subtree is BST
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                size = left_size + right_size + 1
                self.max_size = max(self.max_size, size)
                return True, size, min(left_min, node.val), max(right_max, node.val)

            # Not a BST
            return False, 0, 0, 0

        dfs(root)
        return self.max_size


class SolutionTuple:
    """Cleaner tuple-based approach"""

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Returns: (size of largest BST in subtree, min, max, is_bst)
            if not node:
                return 0, float('inf'), float('-inf'), True

            left_size, left_min, left_max, left_bst = dfs(node.left)
            right_size, right_min, right_max, right_bst = dfs(node.right)

            if left_bst and right_bst and left_max < node.val < right_min:
                # This subtree is a BST
                size = left_size + right_size + 1
                return size, min(left_min, node.val), max(right_max, node.val), True

            # Not BST, return max of children
            return max(left_size, right_size), 0, 0, False

        return dfs(root)[0]


class SolutionNaive:
    """O(n^2) naive approach - check each subtree"""

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def is_bst(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return is_bst(node.left, min_val, node.val) and is_bst(node.right, node.val, max_val)

        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        def dfs(node):
            if not node:
                return 0

            if is_bst(node, float('-inf'), float('inf')):
                return count_nodes(node)

            return max(dfs(node.left), dfs(node.right))

        return dfs(root)
