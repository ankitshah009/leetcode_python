#897. Increasing Order Search Tree
#Easy
#
#Given the root of a binary search tree, rearrange the tree in in-order so that
#the leftmost node in the tree is now the root of the tree, and every node has
#no left child and only one right child.
#
#Example 1:
#Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
#Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#Example 2:
#Input: root = [5,1,7]
#Output: [1,null,5,null,7]
#
#Constraints:
#    The number of nodes in the given tree will be in the range [1, 100].
#    0 <= Node.val <= 1000

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """
        In-order traversal, building new tree.
        """
        dummy = TreeNode(0)
        current = dummy

        def inorder(node):
            nonlocal current
            if not node:
                return

            inorder(node.left)

            node.left = None
            current.right = node
            current = node

            inorder(node.right)

        inorder(root)
        return dummy.right


class SolutionYield:
    """Using generator"""

    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node
                yield from inorder(node.right)

        dummy = TreeNode(0)
        current = dummy

        for node in inorder(root):
            node.left = None
            current.right = node
            current = node

        return dummy.right


class SolutionIterative:
    """Iterative in-order traversal"""

    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode(0)
        current = dummy
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            node.left = None
            current.right = node
            current = node

            node = node.right

        return dummy.right
