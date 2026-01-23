#993. Cousins in Binary Tree
#Easy
#
#Given the root of a binary tree with unique values and the values of two
#different nodes x and y, return true if the nodes with values x and y are
#cousins, or false otherwise.
#
#Two nodes of a binary tree are cousins if they have the same depth but have
#different parents.
#
#Example 1:
#Input: root = [1,2,3,4], x = 4, y = 3
#Output: false
#
#Example 2:
#Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
#Output: true
#
#Example 3:
#Input: root = [1,2,3,null,4], x = 2, y = 3
#Output: false
#
#Constraints:
#    The number of nodes in the tree is in the range [2, 100].
#    1 <= Node.val <= 100
#    Each node has a unique value.
#    x != y
#    x and y exist in the tree.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        BFS to find depth and parent of x and y.
        """
        x_info = None  # (depth, parent)
        y_info = None

        def dfs(node, parent, depth):
            nonlocal x_info, y_info

            if not node:
                return

            if node.val == x:
                x_info = (depth, parent)
            if node.val == y:
                y_info = (depth, parent)

            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)

        dfs(root, None, 0)

        # Cousins: same depth, different parents
        return x_info[0] == y_info[0] and x_info[1] != y_info[1]


class SolutionBFS:
    """BFS level by level"""

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque([(root, None)])  # (node, parent)

        while queue:
            x_parent = y_parent = None

            for _ in range(len(queue)):
                node, parent = queue.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            # Check if both found at this level
            if x_parent and y_parent:
                return x_parent != y_parent
            if x_parent or y_parent:
                return False  # Only one found at this level

        return False


class SolutionDict:
    """Store info in dict"""

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        info = {}  # val -> (depth, parent_val)

        def dfs(node, parent_val, depth):
            if not node:
                return
            info[node.val] = (depth, parent_val)
            dfs(node.left, node.val, depth + 1)
            dfs(node.right, node.val, depth + 1)

        dfs(root, None, 0)

        return info[x][0] == info[y][0] and info[x][1] != info[y][1]
