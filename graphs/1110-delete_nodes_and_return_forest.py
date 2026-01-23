#1110. Delete Nodes And Return Forest
#Medium
#
#Given the root of a binary tree, each node in the tree has a distinct value.
#
#After deleting all nodes with a value in to_delete, we are left with a
#forest (a disjoint union of trees).
#
#Return the roots of the trees in the remaining forest. You may return the
#result in any order.
#
#Example 1:
#Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
#Output: [[1,2,null,4],[6],[7]]
#
#Example 2:
#Input: root = [1,2,4,null,3], to_delete = [3]
#Output: [[1,2,4]]
#
#Constraints:
#    The number of nodes in the given tree is at most 1000.
#    Each node has a distinct value between 1 and 1000.
#    to_delete.length <= 1000
#    to_delete contains distinct values between 1 and 1000.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
        DFS: Return None if node should be deleted.
        If parent deleted, children become roots.
        """
        to_delete_set = set(to_delete)
        result = []

        def dfs(node, is_root):
            if not node:
                return None

            deleted = node.val in to_delete_set

            # If this is a root and not deleted, add to result
            if is_root and not deleted:
                result.append(node)

            # Process children - they become roots if current node is deleted
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)

            return None if deleted else node

        dfs(root, True)
        return result


class SolutionBFS:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """BFS approach"""
        from collections import deque

        to_delete_set = set(to_delete)
        result = []

        if root.val not in to_delete_set:
            result.append(root)

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                if node.left.val in to_delete_set:
                    node.left = None
                elif node.val in to_delete_set:
                    result.append(node.left)

            if node.right:
                queue.append(node.right)
                if node.right.val in to_delete_set:
                    node.right = None
                elif node.val in to_delete_set:
                    result.append(node.right)

        return result
