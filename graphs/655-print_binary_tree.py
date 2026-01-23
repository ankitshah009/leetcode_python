#655. Print Binary Tree
#Medium
#
#Given the root of a binary tree, construct a 0-indexed m x n string matrix res
#that represents a formatted layout of the tree. The formatted layout matrix
#should be constructed using the following rules:
#
#- The height of the tree is height and the number of rows m should be equal to
#  height + 1.
#- The number of columns n should be equal to 2^(height+1) - 1.
#- Place the root node in the middle of the top row (more formally, at location
#  res[0][(n-1)/2]).
#- For each node that has been placed in the matrix at position res[r][c], place
#  its left child at res[r+1][c-2^(height-r-1)] and its right child at
#  res[r+1][c+2^(height-r-1)].
#- Continue this process until all the nodes in the tree have been placed.
#- Any empty cells should contain the empty string "".
#
#Return the constructed matrix res.
#
#Example 1:
#Input: root = [1,2]
#Output: [["","1",""],["2","",""]]
#
#Example 2:
#Input: root = [1,2,3,null,4]
#Output: [["","","","1","","",""],
#         ["","2","","","","3",""],
#         ["","","4","","","",""]]
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 2^10].
#    -99 <= Node.val <= 99
#    The depth of the tree will be in the range [1, 10].

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        """
        Calculate height, then place nodes recursively.
        """
        def get_height(node):
            if not node:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))

        height = get_height(root)
        rows = height + 1
        cols = (1 << rows) - 1  # 2^(height+1) - 1

        result = [[""] * cols for _ in range(rows)]

        def fill(node, row, left, right):
            if not node:
                return

            mid = (left + right) // 2
            result[row][mid] = str(node.val)

            fill(node.left, row + 1, left, mid - 1)
            fill(node.right, row + 1, mid + 1, right)

        fill(root, 0, 0, cols - 1)
        return result


class SolutionBFS:
    """BFS approach with position tracking"""

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        from collections import deque

        # Get height
        def get_height(node):
            if not node:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))

        height = get_height(root)
        rows = height + 1
        cols = (1 << rows) - 1

        result = [[""] * cols for _ in range(rows)]

        # BFS with (node, row, left_bound, right_bound)
        queue = deque([(root, 0, 0, cols - 1)])

        while queue:
            node, row, left, right = queue.popleft()
            if not node:
                continue

            mid = (left + right) // 2
            result[row][mid] = str(node.val)

            queue.append((node.left, row + 1, left, mid - 1))
            queue.append((node.right, row + 1, mid + 1, right))

        return result
