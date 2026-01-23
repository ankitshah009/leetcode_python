#1660. Correct a Binary Tree
#Medium
#
#You have a binary tree with a small defect. There is exactly one invalid node
#where its right child incorrectly points to another node at the same depth but
#to the invalid node's right.
#
#Given the root of the binary tree with this defect, root, return the root of
#the binary tree after removing this invalid node and every node underneath it
#(and their subtrees).
#
#Example 1:
#Input: root = [1,2,3], fromNode = 2, toNode = 3
#Output: [1,null,3]
#Explanation: The node with value 2 is invalid, so remove it.
#
#Example 2:
#Input: root = [8,3,1,7,null,9,4,2,null,null,null,5,6], fromNode = 7, toNode = 4
#Output: [8,3,1,null,null,9,4,null,null,5,6]
#
#Constraints:
#    The number of nodes in the tree is in the range [3, 10^4].
#    -10^9 <= Node.val <= 10^9
#    All node values are unique.
#    fromNode != toNode
#    fromNode and toNode will exist and are at the same depth.
#    toNode is to the right of fromNode.
#    fromNode.right is toNode.

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        """
        BFS from right to left. When we see a node whose right child
        was already visited at this level, we found the invalid node.
        """
        if not root:
            return root

        queue = deque([(root, None, False)])  # (node, parent, is_left_child)
        visited = set()

        while queue:
            size = len(queue)
            level_nodes = []

            for _ in range(size):
                node, parent, is_left = queue.popleft()
                level_nodes.append((node, parent, is_left))

            # Process right to left to detect invalid edge
            visited_this_level = set()

            for node, parent, is_left in reversed(level_nodes):
                # Check if right child points to already visited node
                if node.right and id(node.right) in visited_this_level:
                    # Found invalid node, remove it
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None
                    return root

                visited_this_level.add(id(node))

                # Add children for next level (left first, then right)
                if node.left:
                    queue.append((node.left, node, True))
                if node.right:
                    queue.append((node.right, node, False))

            visited.update(visited_this_level)

        return root


class SolutionBFSSimple:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        """
        BFS right to left, using set to track visited.
        """
        queue = deque([root])
        seen = set()

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                # Check right child first
                if node.right:
                    if id(node.right) in seen:
                        # This node is invalid
                        pass  # Will be removed by parent
                    else:
                        seen.add(id(node.right))

                # Remove invalid child from parent
                if node.left and node.left.right and id(node.left.right) in seen:
                    node.left = None
                    continue
                if node.right and node.right.right and id(node.right.right) in seen:
                    node.right = None
                    continue

                # Add children right to left
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return root


class SolutionDFS:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        """
        DFS with visited set, processing right before left.
        """
        visited = set()

        def dfs(node: TreeNode) -> TreeNode:
            if not node:
                return None

            # Check if this node's right child was already visited
            if node.right and id(node.right) in visited:
                return None

            visited.add(id(node))

            # Process right first (to detect the invalid link)
            node.right = dfs(node.right)
            node.left = dfs(node.left)

            return node

        return dfs(root)


class SolutionClean:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        """
        Clean BFS implementation processing right to left.
        """
        queue = deque([root])
        seen = {id(root)}

        while queue:
            node = queue.popleft()

            # Check right child
            if node.right:
                if node.right.right and id(node.right.right) in seen:
                    node.right = None
                    return root
                seen.add(id(node.right))
                queue.append(node.right)

            # Check left child
            if node.left:
                if node.left.right and id(node.left.right) in seen:
                    node.left = None
                    return root
                seen.add(id(node.left))
                queue.append(node.left)

        return root
