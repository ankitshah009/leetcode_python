#1214. Two Sum BSTs
#Medium
#
#Given the roots of two binary search trees, root1 and root2, return true if
#and only if there is a node in the first tree and a node in the second tree
#whose values sum up to a given integer target.
#
#Example 1:
#Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
#Output: true
#Explanation: 2 and 3 sum up to 5.
#
#Example 2:
#Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
#Output: false
#
#Constraints:
#    The number of nodes in each tree is in the range [1, 5000].
#    -10^9 <= Node.val, target <= 10^9

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        """
        Collect values from tree1 into set.
        Search tree2 for complement.
        """
        # Collect all values from tree1
        values = set()

        def collect(node):
            if not node:
                return
            values.add(node.val)
            collect(node.left)
            collect(node.right)

        collect(root1)

        # Search tree2 for complement
        def search(node):
            if not node:
                return False
            complement = target - node.val
            if complement in values:
                return True
            return search(node.left) or search(node.right)

        return search(root2)


class SolutionBSTSearch:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        """
        For each node in tree1, BST search for complement in tree2.
        """
        def bst_search(node, val):
            if not node:
                return False
            if node.val == val:
                return True
            if val < node.val:
                return bst_search(node.left, val)
            return bst_search(node.right, val)

        def traverse(node):
            if not node:
                return False
            complement = target - node.val
            if bst_search(root2, complement):
                return True
            return traverse(node.left) or traverse(node.right)

        return traverse(root1)


class SolutionTwoPointers:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        """
        Use BST iterators for O(n+m) solution.
        One iterator goes forward (increasing), other backward (decreasing).
        """
        # Inorder traversal of tree1 (increasing)
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        # Reverse inorder of tree2 (decreasing)
        def reverse_inorder(node):
            if not node:
                return []
            return reverse_inorder(node.right) + [node.val] + reverse_inorder(node.left)

        arr1 = inorder(root1)
        arr2 = reverse_inorder(root2)

        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            current_sum = arr1[i] + arr2[j]
            if current_sum == target:
                return True
            elif current_sum < target:
                i += 1
            else:
                j += 1

        return False
