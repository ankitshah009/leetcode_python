#1448. Count Good Nodes in Binary Tree
#Medium
#
#Given a binary tree root, a node X in the tree is named good if in the path from
#root to X there are no nodes with a value greater than X.
#
#Return the number of good nodes in the binary tree.
#
#Example 1:
#Input: root = [3,1,4,3,null,1,5]
#Output: 4
#Explanation: Nodes in blue are good.
#Root Node (3) is always a good node.
#Node 4 -> (3,4) is the maximum value in the path starting from the root.
#Node 5 -> (3,4,5) is the maximum value in the path
#Node 3 -> (3,1,3) is the maximum value in the path.
#
#Example 2:
#Input: root = [3,3,null,4,2]
#Output: 3
#
#Example 3:
#Input: root = [1]
#Output: 1
#
#Constraints:
#    The number of nodes in the binary tree is in the range [1, 10^5].
#    Each node's value is between [-10^4, 10^4].

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """DFS with max value tracking"""

        def dfs(node, max_val):
            if not node:
                return 0

            good = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)

            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)

            return good

        return dfs(root, float('-inf'))


class SolutionIterative:
    """Iterative DFS using stack"""

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        stack = [(root, float('-inf'))]

        while stack:
            node, max_val = stack.pop()

            if node.val >= max_val:
                count += 1
                max_val = node.val

            if node.right:
                stack.append((node.right, max_val))
            if node.left:
                stack.append((node.left, max_val))

        return count


class SolutionBFS:
    """BFS approach"""

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        queue = deque([(root, float('-inf'))])

        while queue:
            node, max_val = queue.popleft()

            if node.val >= max_val:
                count += 1
                max_val = node.val

            if node.left:
                queue.append((node.left, max_val))
            if node.right:
                queue.append((node.right, max_val))

        return count
