#951. Flip Equivalent Binary Trees
#Medium
#
#For a binary tree T, we can define a flip operation as follows: choose any node,
#and swap the left and right child subtrees.
#
#A binary tree X is flip equivalent to a binary tree Y if and only if we can
#make X equal to Y after some number of flip operations.
#
#Given the roots of two binary trees root1 and root2, return true if the two
#trees are flip equivalent or false otherwise.
#
#Example 1:
#Input: root1 = [1,2,3,4,5,6,null,null,null,7,8],
#       root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
#Output: true
#
#Constraints:
#    The number of nodes in each tree is in the range [0, 100].
#    Each tree will have unique node values in the range [0, 99].

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        Recursively check: either children match or flipped children match.
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        # Either no flip or flip
        no_flip = (self.flipEquiv(root1.left, root2.left) and
                   self.flipEquiv(root1.right, root2.right))
        flip = (self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))

        return no_flip or flip


class SolutionIterative:
    """Iterative with canonical form"""

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def canonical(node):
            """Return canonical representation."""
            if not node:
                return None

            # Recursively get canonical forms of children
            left = canonical(node.left)
            right = canonical(node.right)

            # Order by value (smaller first)
            if left and right:
                if left[0] > right[0]:
                    left, right = right, left
            elif right:
                left, right = right, None

            return (node.val, left, right)

        return canonical(root1) == canonical(root2)


class SolutionExplicit:
    """More explicit comparison"""

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            if n1.val != n2.val:
                return False

            # Get children values
            def get_val(node):
                return node.val if node else -1

            # Check if children can be matched
            if get_val(n1.left) == get_val(n2.left):
                return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)
            else:
                return dfs(n1.left, n2.right) and dfs(n1.right, n2.left)

        return dfs(root1, root2)
