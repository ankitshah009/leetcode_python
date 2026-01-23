#776. Split BST
#Medium
#
#Given the root of a binary search tree (BST) and an integer target, split the
#tree into two subtrees where one subtree has nodes that are all smaller or
#equal to the target value, while the other subtree has all nodes that are
#greater than the target value. It Is not necessarily the case that the tree
#contains a node with the value target.
#
#Additionally, most of the structure of the original tree should remain. Formally,
#for any child c with parent p in the original tree, if they are both in the
#same subtree after the split, then node c should still have the parent p.
#
#Return an array of the two roots of the two subtrees.
#
#Example 1:
#Input: root = [4,2,6,1,3,5,7], target = 2
#Output: [[2,1],[4,3,6,null,null,5,7]]
#
#Example 2:
#Input: root = [1], target = 1
#Output: [[1],[]]
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 50].
#    0 <= Node.val, target <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def splitBST(self, root, target: int):
        """
        Recursively split: return [tree <= target, tree > target].
        """
        if not root:
            return [None, None]

        if root.val <= target:
            # Root goes to left tree
            # Split right subtree
            left_of_right, right_of_right = self.splitBST(root.right, target)
            root.right = left_of_right
            return [root, right_of_right]
        else:
            # Root goes to right tree
            # Split left subtree
            left_of_left, right_of_left = self.splitBST(root.left, target)
            root.left = right_of_left
            return [left_of_left, root]


class SolutionIterative:
    """Iterative approach"""

    def splitBST(self, root, target: int):
        # Dummy heads for the two trees
        small_dummy = TreeNode(0)
        large_dummy = TreeNode(0)

        small_curr = small_dummy
        large_curr = large_dummy

        while root:
            if root.val <= target:
                # Add to small tree
                small_curr.right = root
                small_curr = root
                root = root.right
            else:
                # Add to large tree
                large_curr.left = root
                large_curr = root
                root = root.left

        # Clean up connections
        small_curr.right = None
        large_curr.left = None

        return [small_dummy.right, large_dummy.left]
