#1485. Clone Binary Tree With Random Pointer
#Medium
#
#A binary tree is given such that each node contains an additional random pointer
#which could point to any node in the tree or null.
#
#Return a deep copy of the tree.
#
#The tree is represented in the same input/output way as normal binary trees
#where each node is represented as a pair of [val, random_index] where:
#    val: an integer representing Node.val
#    random_index: the index of the node (in the input) where the random pointer
#    points to, or null if it does not point to any node.
#
#You will be given the tree in class Node and you should return the cloned tree
#in class NodeCopy. NodeCopy class is just a clone of Node class with the same
#attributes and constructors.
#
#Example 1:
#Input: root = [[1,null],null,[4,3],[7,0]]
#Output: [[1,null],null,[4,3],[7,0]]
#Explanation: The original binary tree is [1,null,4,7].
#The random pointer of node one is null, so it is represented as [1, null].
#The random pointer of node 4 is node 7, so it is represented as [4, 3] where
#3 is the index of node 7 in the array representing the tree.
#The random pointer of node 7 is node 1, so it is represented as [7, 0] where
#0 is the index of node 1 in the array representing the tree.
#
#Example 2:
#Input: root = [[1,4],null,[1,0],null,[1,5],[1,5]]
#Output: [[1,4],null,[1,0],null,[1,5],[1,5]]
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 1000].
#    1 <= Node.val <= 10^6

from typing import Optional
from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: Optional[Node]) -> Optional[NodeCopy]:
        """
        Two-pass approach:
        1. Create all nodes and build mapping from original to copy
        2. Set random pointers using the mapping
        """
        if not root:
            return None

        # Map from original node to copied node
        node_map = {}

        # First pass: create all nodes
        def create_nodes(node: Node) -> NodeCopy:
            if not node:
                return None

            copy = NodeCopy(node.val)
            node_map[node] = copy

            copy.left = create_nodes(node.left)
            copy.right = create_nodes(node.right)

            return copy

        copy_root = create_nodes(root)

        # Second pass: set random pointers
        def set_random(node: Node) -> None:
            if not node:
                return

            if node.random:
                node_map[node].random = node_map[node.random]

            set_random(node.left)
            set_random(node.right)

        set_random(root)

        return copy_root


class SolutionSinglePass:
    def copyRandomBinaryTree(self, root: Optional[Node]) -> Optional[NodeCopy]:
        """
        Single recursive pass with memoization.
        Create nodes on-demand and cache them.
        """
        if not root:
            return None

        node_map = {}

        def clone(node: Node) -> Optional[NodeCopy]:
            if not node:
                return None

            # Return cached copy if exists
            if node in node_map:
                return node_map[node]

            # Create new copy and cache it
            copy = NodeCopy(node.val)
            node_map[node] = copy

            # Recursively clone children and random
            copy.left = clone(node.left)
            copy.right = clone(node.right)
            copy.random = clone(node.random)

            return copy

        return clone(root)


class SolutionBFS:
    def copyRandomBinaryTree(self, root: Optional[Node]) -> Optional[NodeCopy]:
        """BFS approach"""
        if not root:
            return None

        node_map = {}

        # Create all copies first
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node not in node_map:
                node_map[node] = NodeCopy(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Set all pointers
        queue = deque([root])
        visited = set()

        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)

            copy = node_map[node]

            if node.left:
                copy.left = node_map[node.left]
                queue.append(node.left)

            if node.right:
                copy.right = node_map[node.right]
                queue.append(node.right)

            if node.random:
                copy.random = node_map[node.random]

        return node_map[root]


class SolutionIterative:
    def copyRandomBinaryTree(self, root: Optional[Node]) -> Optional[NodeCopy]:
        """Iterative DFS with stack"""
        if not root:
            return None

        node_map = {}

        def get_clone(node: Node) -> Optional[NodeCopy]:
            if not node:
                return None
            if node not in node_map:
                node_map[node] = NodeCopy(node.val)
            return node_map[node]

        stack = [root]
        visited = set()

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)

            copy = get_clone(node)
            copy.left = get_clone(node.left)
            copy.right = get_clone(node.right)
            copy.random = get_clone(node.random)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return node_map[root]
