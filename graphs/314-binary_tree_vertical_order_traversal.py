#314. Binary Tree Vertical Order Traversal
#Medium
#
#Given the root of a binary tree, return the vertical order traversal of its
#nodes' values. (i.e., from top to bottom, column by column).
#
#If two nodes are in the same row and column, the order should be from left to
#right.
#
#Example 1:
#Input: root = [3,9,20,null,null,15,7]
#Output: [[9],[3,15],[20],[7]]
#
#Example 2:
#Input: root = [3,9,8,4,0,1,7]
#Output: [[4],[9],[3,0,1],[8],[7]]
#
#Example 3:
#Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
#Output: [[4],[9,5],[3,0,1],[8,2],[7]]
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 100].
#    -100 <= Node.val <= 100

from collections import defaultdict, deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """BFS with column tracking"""
        if not root:
            return []

        columns = defaultdict(list)
        queue = deque([(root, 0)])  # (node, column)

        min_col = max_col = 0

        while queue:
            node, col = queue.popleft()
            columns[col].append(node.val)

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        return [columns[col] for col in range(min_col, max_col + 1)]


class SolutionDFS:
    """DFS with sorting by row"""

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        columns = defaultdict(list)

        def dfs(node, row, col):
            if not node:
                return

            columns[col].append((row, node.val))

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        result = []
        for col in sorted(columns.keys()):
            # Sort by row, then by order of insertion (for same row)
            column_vals = sorted(columns[col], key=lambda x: x[0])
            result.append([val for _, val in column_vals])

        return result


class SolutionSorted:
    """Using sorted dictionary"""

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from sortedcontainers import SortedDict

        if not root:
            return []

        columns = SortedDict()
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            if col not in columns:
                columns[col] = []
            columns[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        return list(columns.values())
