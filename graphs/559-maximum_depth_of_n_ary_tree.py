#559. Maximum Depth of N-ary Tree
#Easy
#
#Given a n-ary tree, find its maximum depth.
#
#The maximum depth is the number of nodes along the longest path from the root
#node down to the farthest leaf node.
#
#Example 1:
#Input: root = [1,null,3,2,4,null,5,6]
#Output: 3
#
#Example 2:
#Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
#Output: 5
#
#Constraints:
#    The total number of nodes is in the range [0, 10^4].
#    The depth of the n-ary tree is less than or equal to 1000.

from typing import List, Optional
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """DFS recursive"""
        if not root:
            return 0

        if not root.children:
            return 1

        return 1 + max(self.maxDepth(child) for child in root.children)


class SolutionBFS:
    """BFS level order traversal"""

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)

        return depth


class SolutionIterativeDFS:
    """Iterative DFS with stack"""

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            for child in node.children:
                stack.append((child, depth + 1))

        return max_depth
