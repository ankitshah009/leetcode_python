#971. Flip Binary Tree To Match Preorder Traversal
#Medium
#
#You are given the root of a binary tree with n nodes, where each node is
#uniquely assigned a value from 1 to n. You are also given a sequence of n
#values voyage, which is the desired pre-order traversal of the binary tree.
#
#Any node in the binary tree can be flipped by swapping its left and right
#subtrees.
#
#Return a list of the values of all flipped nodes. You may return the answer in
#any order. If it is impossible to flip the nodes in the tree to make the
#pre-order traversal of the tree match voyage, return [-1].
#
#Example 1:
#Input: root = [1,2], voyage = [2,1]
#Output: [-1]
#
#Example 2:
#Input: root = [1,2,3], voyage = [1,3,2]
#Output: [1]
#
#Constraints:
#    The number of nodes in the tree is n.
#    n == voyage.length
#    1 <= n <= 100
#    1 <= Node.val <= n
#    All the values in the tree are unique.
#    All the values in voyage are unique.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: list[int]) -> list[int]:
        """
        DFS following voyage, flip when necessary.
        """
        flipped = []
        idx = 0

        def dfs(node):
            nonlocal idx

            if not node:
                return True

            if node.val != voyage[idx]:
                return False

            idx += 1

            # Check if we need to flip
            if node.left and node.left.val != voyage[idx]:
                # Need to process right first, so flip
                flipped.append(node.val)
                return dfs(node.right) and dfs(node.left)
            else:
                return dfs(node.left) and dfs(node.right)

        if dfs(root):
            return flipped
        return [-1]


class SolutionIterative:
    """Iterative with stack"""

    def flipMatchVoyage(self, root: TreeNode, voyage: list[int]) -> list[int]:
        flipped = []
        stack = [root]
        idx = 0

        while stack:
            node = stack.pop()

            if not node:
                continue

            if node.val != voyage[idx]:
                return [-1]

            idx += 1

            # Decide order to push children
            if node.left and node.right:
                if node.left.val != voyage[idx]:
                    # Need to flip - process right first
                    flipped.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
                else:
                    stack.append(node.right)
                    stack.append(node.left)
            else:
                stack.append(node.right)
                stack.append(node.left)

        return flipped
