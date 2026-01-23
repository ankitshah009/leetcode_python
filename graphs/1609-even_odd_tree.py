#1609. Even Odd Tree
#Medium
#
#A binary tree is named Even-Odd if it meets the following conditions:
#- The root of the binary tree is at level index 0, its children are at level
#  index 1, their children are at level index 2, etc.
#- For every even-indexed level, all nodes at the level have odd integer values
#  in strictly increasing order (from left to right).
#- For every odd-indexed level, all nodes at the level have even integer values
#  in strictly decreasing order (from left to right).
#
#Given the root of a binary tree, return true if the binary tree is Even-Odd,
#otherwise return false.
#
#Example 1:
#Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
#Output: true
#Explanation: The node values on each level are:
#Level 0: [1]
#Level 1: [10,4]
#Level 2: [3,7,9]
#Level 3: [12,8,6,2]
#
#Example 2:
#Input: root = [5,4,2,3,3,7]
#Output: false
#
#Example 3:
#Input: root = [5,9,1,3,5,7]
#Output: false
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^5].
#    1 <= Node.val <= 10^6

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """
        BFS level-order traversal.
        Check conditions for each level.
        """
        if not root:
            return True

        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            prev_val = None

            for _ in range(level_size):
                node = queue.popleft()
                val = node.val

                if level % 2 == 0:
                    # Even level: odd values, strictly increasing
                    if val % 2 == 0:  # Must be odd
                        return False
                    if prev_val is not None and val <= prev_val:
                        return False
                else:
                    # Odd level: even values, strictly decreasing
                    if val % 2 == 1:  # Must be even
                        return False
                    if prev_val is not None and val >= prev_val:
                        return False

                prev_val = val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return True


class SolutionDFS:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """
        DFS approach: track the last seen value at each level.
        """
        # last_val[level] = last value seen at this level
        last_val = {}

        def dfs(node: TreeNode, level: int) -> bool:
            if not node:
                return True

            val = node.val

            # Check parity
            if level % 2 == 0:
                # Even level: need odd value
                if val % 2 == 0:
                    return False
            else:
                # Odd level: need even value
                if val % 2 == 1:
                    return False

            # Check ordering
            if level in last_val:
                if level % 2 == 0:
                    # Strictly increasing
                    if val <= last_val[level]:
                        return False
                else:
                    # Strictly decreasing
                    if val >= last_val[level]:
                        return False

            last_val[level] = val

            # Process children left to right
            return dfs(node.left, level + 1) and dfs(node.right, level + 1)

        return dfs(root, 0)


class SolutionCompact:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """
        Compact BFS implementation.
        """
        queue = deque([(root, 0)])

        prev = {}  # level -> previous value

        while queue:
            node, level = queue.popleft()

            # Parity check
            if (level % 2) == (node.val % 2):
                return False

            # Ordering check
            if level in prev:
                if level % 2 == 0 and node.val <= prev[level]:
                    return False
                if level % 2 == 1 and node.val >= prev[level]:
                    return False

            prev[level] = node.val

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return True
