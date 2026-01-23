#1644. Lowest Common Ancestor of a Binary Tree II
#Medium
#
#Given the root of a binary tree, return the lowest common ancestor (LCA) of
#two given nodes, p and q. If either node p or q does not exist in the tree,
#return null. All values of the nodes in the tree are unique.
#
#According to the definition of LCA on Wikipedia: "The lowest common ancestor
#of two nodes p and q in a binary tree T is the lowest node that has both p and
#q as descendants (where we allow a node to be a descendant of itself)".
#
#Example 1:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#Output: 3
#Explanation: The LCA of nodes 5 and 1 is 3.
#
#Example 2:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
#Output: 5
#Explanation: The LCA of nodes 5 and 4 is 5.
#
#Example 3:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
#Output: null
#Explanation: Node 10 does not exist in the tree.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    -10^9 <= Node.val <= 10^9
#    All Node.val are unique.
#    p != q

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Similar to LCA but must verify both nodes exist.
        Post-order traversal ensures we check entire tree.
        """
        self.found_p = False
        self.found_q = False

        def dfs(node: TreeNode) -> TreeNode:
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p:
                self.found_p = True
                return node
            if node == q:
                self.found_q = True
                return node

            if left and right:
                return node
            return left or right

        result = dfs(root)

        # Only return result if both nodes were found
        return result if self.found_p and self.found_q else None


class SolutionTwoPass:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Two-pass approach:
        1. First check if both nodes exist
        2. Then find LCA
        """
        def exists(node: TreeNode, target: TreeNode) -> bool:
            if not node:
                return False
            if node == target:
                return True
            return exists(node.left, target) or exists(node.right, target)

        if not exists(root, p) or not exists(root, q):
            return None

        def lca(node: TreeNode) -> TreeNode:
            if not node or node == p or node == q:
                return node

            left = lca(node.left)
            right = lca(node.right)

            if left and right:
                return node
            return left or right

        return lca(root)


class SolutionCounter:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Count found nodes during traversal.
        """
        self.count = 0
        self.result = None

        def dfs(node: TreeNode) -> bool:
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            mid = node == p or node == q
            if mid:
                self.count += 1

            if mid + left + right >= 2:
                self.result = node

            return mid or left or right

        dfs(root)

        return self.result if self.count == 2 else None
