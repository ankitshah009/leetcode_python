#404. Sum of Left Leaves
#Easy
#
#Given the root of a binary tree, return the sum of all left leaves.
#
#A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
#
#Example 1:
#Input: root = [3,9,20,null,null,15,7]
#Output: 24
#Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
#
#Example 2:
#Input: root = [1]
#Output: 0
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 1000].
#    -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = 0

        # Check if left child is a leaf
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        else:
            total += self.sumOfLeftLeaves(root.left)

        total += self.sumOfLeftLeaves(root.right)

        return total
