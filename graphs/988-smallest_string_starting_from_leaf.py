#988. Smallest String Starting From Leaf
#Medium
#
#You are given the root of a binary tree where each node has a value in the
#range [0, 25] representing the letters 'a' to 'z'.
#
#Return the lexicographically smallest string that starts at a leaf of this
#tree and ends at the root.
#
#Example 1:
#Input: root = [0,1,2,3,4,3,4]
#Output: "dba"
#
#Example 2:
#Input: root = [25,1,3,1,3,0,2]
#Output: "adz"
#
#Example 3:
#Input: root = [2,2,1,null,1,0,null,0]
#Output: "abc"
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 8500].
#    0 <= Node.val <= 25

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        """
        DFS collecting path, compare at leaves.
        """
        smallest = None

        def dfs(node, path):
            nonlocal smallest

            if not node:
                return

            path.append(chr(ord('a') + node.val))

            if not node.left and not node.right:
                # Leaf: reverse path to get string
                s = ''.join(reversed(path))
                if smallest is None or s < smallest:
                    smallest = s
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            path.pop()

        dfs(root, [])
        return smallest


class SolutionString:
    """Build string directly"""

    def smallestFromLeaf(self, root: TreeNode) -> str:
        smallest = [None]

        def dfs(node, suffix):
            if not node:
                return

            current = chr(ord('a') + node.val) + suffix

            if not node.left and not node.right:
                if smallest[0] is None or current < smallest[0]:
                    smallest[0] = current
            else:
                dfs(node.left, current)
                dfs(node.right, current)

        dfs(root, "")
        return smallest[0]


class SolutionIterative:
    """Iterative DFS"""

    def smallestFromLeaf(self, root: TreeNode) -> str:
        smallest = None
        stack = [(root, "")]

        while stack:
            node, path = stack.pop()
            current = chr(ord('a') + node.val) + path

            if not node.left and not node.right:
                if smallest is None or current < smallest:
                    smallest = current
            else:
                if node.left:
                    stack.append((node.left, current))
                if node.right:
                    stack.append((node.right, current))

        return smallest
