#156. Binary Tree Upside Down
#Medium
#
#Given the root of a binary tree, turn the tree upside down and return the new root.
#
#You can turn a binary tree upside down with the following steps:
#- The original left child becomes the new root.
#- The original root becomes the new right child.
#- The original right child becomes the new left child.
#
#The mentioned steps are done level by level. It is guaranteed that every right
#node has a sibling (a left node with the same parent) and has no children.
#
#Example 1:
#Input: root = [1,2,3,4,5]
#Output: [4,5,2,null,null,3,1]
#
#Example 2:
#Input: root = []
#Output: []
#
#Example 3:
#Input: root = [1]
#Output: [1]
#
#Constraints:
#    The number of nodes in the tree will be in the range [0, 10].
#    1 <= Node.val <= 10
#    Every right node in the tree has a sibling (a left node that shares the same
#    parent).
#    Every right node in the tree has no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive approach
        if not root or not root.left:
            return root

        # Get the new root from the leftmost path
        new_root = self.upsideDownBinaryTree(root.left)

        # Rearrange pointers
        root.left.left = root.right  # Original right becomes new left
        root.left.right = root       # Original root becomes new right
        root.left = None
        root.right = None

        return new_root

    def upsideDownBinaryTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iterative approach
        if not root:
            return None

        curr = root
        prev = None
        prev_right = None

        while curr:
            # Store next node
            next_node = curr.left

            # Rewire current node
            curr.left = prev_right  # Previous right becomes current left
            prev_right = curr.right # Store current right for next iteration
            curr.right = prev       # Previous node becomes current right

            # Move to next
            prev = curr
            curr = next_node

        return prev
