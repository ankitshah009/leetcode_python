#998. Maximum Binary Tree II
#Medium
#
#A maximum tree is a tree where every node has a value greater than any other
#value in its subtree.
#
#You are given the root of a maximum binary tree and an integer val.
#
#Just as in the previous problem, the given tree was constructed from a list a
#(root = Construct(a)) recursively with the following Construct(a) routine:
#- If a is empty, return null.
#- Otherwise, let a[i] be the largest element of a. Create a root node with the
#  value a[i].
#- The left child of root will be Construct([a[0], a[1], ..., a[i - 1]]).
#- The right child of root will be Construct([a[i + 1], a[i + 2], ..., a[a.length - 1]]).
#- Return root.
#
#Note that we were not given a directly, only a root node root = Construct(a).
#
#Return root of the maximum tree after inserting val into the tree.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 100].
#    1 <= Node.val <= 100
#    All values in the tree are unique.
#    1 <= val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        """
        val is appended to the end of array.
        If val > root.val, val becomes new root.
        Otherwise, insert into right subtree.
        """
        if not root or val > root.val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        root.right = self.insertIntoMaxTree(root.right, val)
        return root


class SolutionIterative:
    """Iterative approach"""

    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if val > root.val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        node = root
        while node.right and node.right.val > val:
            node = node.right

        # Insert val as right child, old right subtree becomes val's left
        new_node = TreeNode(val)
        new_node.left = node.right
        node.right = new_node

        return root


class SolutionExplicit:
    """More explicit explanation"""

    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        """
        Since val is at the rightmost position:
        - If val is maximum, it becomes root with old tree as left subtree
        - Otherwise, traverse right spine until finding node < val,
          insert val there with that subtree as left child
        """
        if root is None:
            return TreeNode(val)

        if val > root.val:
            return TreeNode(val, left=root)

        # Traverse right spine
        curr = root
        while curr.right and curr.right.val > val:
            curr = curr.right

        # Insert val
        new_node = TreeNode(val)
        new_node.left = curr.right
        curr.right = new_node

        return root
