#366. Find Leaves of Binary Tree
#Medium
#
#Given the root of a binary tree, collect a tree's nodes as if you were doing
#this:
#- Collect all the leaf nodes.
#- Remove all the leaf nodes.
#- Repeat until the tree is empty.
#
#Example 1:
#Input: root = [1,2,3,4,5]
#Output: [[4,5,3],[2],[1]]
#Explanation:
#[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers
#since per each level it does not matter the order on which elements are
#returned.
#
#Example 2:
#Input: root = [1]
#Output: [[1]]
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 100].
#    -100 <= Node.val <= 100

from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Group by height from bottom (leaf level = 0).
        Height of node = max(height of children) + 1
        """
        result = defaultdict(list)

        def get_height(node):
            if not node:
                return -1

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            height = max(left_height, right_height) + 1
            result[height].append(node.val)

            return height

        get_height(root)
        return [result[i] for i in range(len(result))]


class SolutionRemoval:
    """Actually remove leaves in each iteration"""

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def remove_leaves(node):
            if not node:
                return None

            if not node.left and not node.right:
                result[-1].append(node.val)
                return None

            node.left = remove_leaves(node.left)
            node.right = remove_leaves(node.right)
            return node

        while root:
            result.append([])
            root = remove_leaves(root)

        return result


class SolutionBFS:
    """BFS approach with parent tracking"""

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        if not root:
            return []

        # Build parent map and find initial leaves
        parent = {root: None}
        children_count = defaultdict(int)
        leaves = []

        queue = deque([root])
        while queue:
            node = queue.popleft()

            if node.left:
                parent[node.left] = node
                children_count[node] += 1
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                children_count[node] += 1
                queue.append(node.right)

            if not node.left and not node.right:
                leaves.append(node)

        result = []

        while leaves:
            result.append([node.val for node in leaves])
            new_leaves = []

            for node in leaves:
                p = parent[node]
                if p:
                    children_count[p] -= 1
                    if children_count[p] == 0:
                        new_leaves.append(p)

            leaves = new_leaves

        return result
