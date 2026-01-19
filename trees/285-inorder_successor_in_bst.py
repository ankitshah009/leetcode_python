#285. Inorder Successor in BST
#Medium
#
#Given the root of a binary search tree and a node p in it, return the in-order
#successor of that node in the BST. If the given node has no in-order successor
#in the tree, return null.
#
#The successor of a node p is the node with the smallest key greater than p.val.
#
#Example 1:
#Input: root = [2,1,3], p = 1
#Output: 2
#Explanation: 1's in-order successor node is 2.
#
#Example 2:
#Input: root = [5,3,6,2,4,null,null,1], p = 6
#Output: null
#Explanation: There is no in-order successor of the current node, so the answer
#is null.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    -10^5 <= Node.val <= 10^5
#    All Nodes will have unique values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None

        while root:
            if p.val < root.val:
                # Current node could be successor
                successor = root
                root = root.left
            else:
                # Successor must be in right subtree
                root = root.right

        return successor

    # If p has a right subtree
    def inorderSuccessorWithRightSubtree(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # If p has right subtree, successor is leftmost node in right subtree
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node

        # Otherwise, find the lowest ancestor where p is in left subtree
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            elif p.val > root.val:
                root = root.right
            else:
                break

        return successor


class SolutionPredecessor:
    """Also including inorder predecessor for completeness"""

    def inorderPredecessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        predecessor = None

        while root:
            if p.val > root.val:
                # Current node could be predecessor
                predecessor = root
                root = root.right
            else:
                # Predecessor must be in left subtree
                root = root.left

        return predecessor
