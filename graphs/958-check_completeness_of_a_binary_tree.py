#958. Check Completeness of a Binary Tree
#Medium
#
#Given the root of a binary tree, determine if it is a complete binary tree.
#
#In a complete binary tree, every level except possibly the last is completely
#filled, and all nodes in the last level are as far left as possible.
#
#Example 1:
#Input: root = [1,2,3,4,5,6]
#Output: true
#
#Example 2:
#Input: root = [1,2,3,4,5,null,7]
#Output: false
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 100].
#    1 <= Node.val <= 1000

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        """
        BFS: after seeing a null, should see no more nodes.
        """
        queue = deque([root])
        seen_null = False

        while queue:
            node = queue.popleft()

            if node is None:
                seen_null = True
            else:
                if seen_null:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True


class SolutionIndex:
    """Using index property of complete tree"""

    def isCompleteTree(self, root: TreeNode) -> bool:
        # In complete tree, if we number nodes 1, 2, 3, ...
        # then max index should equal count of nodes
        nodes = []

        def dfs(node, idx):
            if node:
                nodes.append(idx)
                dfs(node.left, 2 * idx)
                dfs(node.right, 2 * idx + 1)

        dfs(root, 1)
        return len(nodes) == max(nodes)


class SolutionLevelOrder:
    """Level order with gap detection"""

    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = deque([root])
        gap = False

        while queue:
            node = queue.popleft()

            if node.left:
                if gap:
                    return False
                queue.append(node.left)
            else:
                gap = True

            if node.right:
                if gap:
                    return False
                queue.append(node.right)
            else:
                gap = True

        return True
