#1008. Construct Binary Search Tree from Preorder Traversal
#Medium
#
#Given an array of integers preorder, which represents the preorder traversal
#of a BST, construct the tree and return its root.
#
#It is guaranteed that there is always possible to find a binary search tree
#with the given requirements for the given test cases.
#
#Example 1:
#Input: preorder = [8,5,1,7,10,12]
#Output: [8,5,10,1,7,null,12]
#
#Example 2:
#Input: preorder = [1,3]
#Output: [1,null,3]
#
#Constraints:
#    1 <= preorder.length <= 100
#    1 <= preorder[i] <= 1000
#    All the values of preorder are unique.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode:
        """
        Recursive with bounds.
        """
        idx = [0]

        def build(lower=float('-inf'), upper=float('inf')):
            if idx[0] == len(preorder):
                return None

            val = preorder[idx[0]]
            if val < lower or val > upper:
                return None

            idx[0] += 1
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)
            return node

        return build()


class SolutionBinarySearch:
    """Binary search for split point"""

    def bstFromPreorder(self, preorder: list[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        # Find split: first element > root
        split = 1
        while split < len(preorder) and preorder[split] < preorder[0]:
            split += 1

        root.left = self.bstFromPreorder(preorder[1:split])
        root.right = self.bstFromPreorder(preorder[split:])

        return root


class SolutionIterative:
    """Iterative with stack"""

    def bstFromPreorder(self, preorder: list[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]

        for i in range(1, len(preorder)):
            val = preorder[i]
            node = TreeNode(val)

            if val < stack[-1].val:
                stack[-1].left = node
            else:
                parent = None
                while stack and stack[-1].val < val:
                    parent = stack.pop()
                parent.right = node

            stack.append(node)

        return root
