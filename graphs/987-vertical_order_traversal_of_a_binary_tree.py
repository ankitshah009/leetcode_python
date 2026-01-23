#987. Vertical Order Traversal of a Binary Tree
#Hard
#
#Given the root of a binary tree, calculate the vertical order traversal.
#
#For each node at position (row, col), its left and right children will be at
#positions (row + 1, col - 1) and (row + 1, col + 1) respectively.
#
#The vertical order traversal of a binary tree is a list of top-to-bottom
#orderings for each column index. If two nodes are in the same row and column,
#they should be sorted by their values.
#
#Return the vertical order traversal of the binary tree.
#
#Example 1:
#Input: root = [3,9,20,null,null,15,7]
#Output: [[9],[3,15],[20],[7]]
#
#Example 2:
#Input: root = [1,2,3,4,5,6,7]
#Output: [[4],[2],[1,5,6],[3],[7]]
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 1000].
#    0 <= Node.val <= 1000

from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        """
        DFS with (row, col) tracking, then sort.
        """
        nodes = []  # (col, row, val)

        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        # Sort by col, then row, then val
        nodes.sort()

        # Group by column
        result = []
        prev_col = None

        for col, row, val in nodes:
            if col != prev_col:
                result.append([])
                prev_col = col
            result[-1].append(val)

        return result


class SolutionDict:
    """Using nested dictionary"""

    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        columns = defaultdict(lambda: defaultdict(list))

        def dfs(node, row, col):
            if not node:
                return
            columns[col][row].append(node.val)
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        result = []
        for col in sorted(columns.keys()):
            col_vals = []
            for row in sorted(columns[col].keys()):
                col_vals.extend(sorted(columns[col][row]))
            result.append(col_vals)

        return result


class SolutionBFS:
    """BFS approach"""

    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        from collections import deque

        nodes = []
        queue = deque([(root, 0, 0)])  # (node, row, col)

        while queue:
            node, row, col = queue.popleft()
            nodes.append((col, row, node.val))

            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))

        nodes.sort()

        result = []
        prev_col = None

        for col, row, val in nodes:
            if col != prev_col:
                result.append([])
                prev_col = col
            result[-1].append(val)

        return result
