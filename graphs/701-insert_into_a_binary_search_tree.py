#701. Insert into a Binary Search Tree
#Medium
#
#You are given the root node of a binary search tree (BST) and a value to
#insert into the tree. Return the root node of the BST after the insertion.
#It is guaranteed that the new value does not exist in the original BST.
#
#Notice that there may exist multiple valid ways for the insertion, as long as
#the tree remains a BST after insertion. You can return any of them.
#
#Example 1:
#Input: root = [4,2,7,1,3], val = 5
#Output: [4,2,7,1,3,5]
#
#Example 2:
#Input: root = [40,20,60,10,30,50,70], val = 25
#Output: [40,20,60,10,30,50,70,null,null,25]
#
#Constraints:
#    The number of nodes in the tree will be in the range [0, 10^4].
#    -10^8 <= Node.val <= 10^8
#    All the values Node.val are unique.
#    -10^8 <= val <= 10^8
#    It's guaranteed that val does not exist in the original BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root, val: int):
        """
        Recursive: find correct position and insert.
        """
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


class SolutionIterative:
    """Iterative approach"""

    def insertIntoBST(self, root, val: int):
        new_node = TreeNode(val)

        if not root:
            return new_node

        curr = root
        while True:
            if val < curr.val:
                if not curr.left:
                    curr.left = new_node
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right

        return root


class SolutionParent:
    """Track parent during traversal"""

    def insertIntoBST(self, root, val: int):
        if not root:
            return TreeNode(val)

        parent = None
        curr = root

        while curr:
            parent = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)

        return root
