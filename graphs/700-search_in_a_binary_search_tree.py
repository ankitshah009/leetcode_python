#700. Search in a Binary Search Tree
#Easy
#
#You are given the root of a binary search tree (BST) and an integer val.
#
#Find the node in the BST that the node's value equals val and return the
#subtree rooted with that node. If such a node does not exist, return null.
#
#Example 1:
#Input: root = [4,2,7,1,3], val = 2
#Output: [2,1,3]
#
#Example 2:
#Input: root = [4,2,7,1,3], val = 5
#Output: []
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 5000].
#    1 <= Node.val <= 10^7
#    root is a binary search tree.
#    1 <= val <= 10^7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root, val: int):
        """
        Recursive BST search - O(h) time where h is height.
        """
        if not root:
            return None

        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


class SolutionIterative:
    """Iterative approach"""

    def searchBST(self, root, val: int):
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right

        return None


class SolutionWalrus:
    """Using walrus operator for concise iteration"""

    def searchBST(self, root, val: int):
        node = root
        while node and node.val != val:
            node = node.left if val < node.val else node.right
        return node
