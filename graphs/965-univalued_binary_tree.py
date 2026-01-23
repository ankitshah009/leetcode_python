#965. Univalued Binary Tree
#Easy
#
#A binary tree is uni-valued if every node in the tree has the same value.
#
#Given the root of a binary tree, return true if the given tree is uni-valued,
#or false otherwise.
#
#Example 1:
#Input: root = [1,1,1,1,1,null,1]
#Output: true
#
#Example 2:
#Input: root = [2,2,2,5,2]
#Output: false
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 100].
#    0 <= Node.val < 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        """
        Check all nodes have same value as root.
        """
        if not root:
            return True

        val = root.val

        def dfs(node):
            if not node:
                return True
            if node.val != val:
                return False
            return dfs(node.left) and dfs(node.right)

        return dfs(root)


class SolutionIterative:
    """BFS approach"""

    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        from collections import deque

        val = root.val
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.val != val:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return True


class SolutionSet:
    """Collect all values"""

    def isUnivalTree(self, root: TreeNode) -> bool:
        values = set()

        def dfs(node):
            if node:
                values.add(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(values) == 1
