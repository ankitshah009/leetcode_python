#783. Minimum Distance Between BST Nodes
#Easy
#
#Given the root of a Binary Search Tree (BST), return the minimum difference
#between the values of any two different nodes in the tree.
#
#Example 1:
#Input: root = [4,2,6,1,3]
#Output: 1
#
#Example 2:
#Input: root = [1,0,48,null,null,12,49]
#Output: 1
#
#Constraints:
#    The number of nodes in the tree is in the range [2, 100].
#    0 <= Node.val <= 10^5

class Solution:
    def minDiffInBST(self, root) -> int:
        """
        Inorder traversal gives sorted order. Find min consecutive difference.
        """
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff


class SolutionIterative:
    """Iterative inorder traversal"""

    def minDiffInBST(self, root) -> int:
        stack = []
        prev = None
        min_diff = float('inf')
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val

            node = node.right

        return min_diff


class SolutionList:
    """Collect values and sort"""

    def minDiffInBST(self, root) -> int:
        values = []

        def inorder(node):
            if node:
                inorder(node.left)
                values.append(node.val)
                inorder(node.right)

        inorder(root)

        return min(values[i] - values[i-1] for i in range(1, len(values)))
