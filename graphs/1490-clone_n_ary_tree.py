#1490. Clone N-ary Tree
#Medium
#
#Given a root of an N-ary tree, return a deep copy (clone) of the tree.
#
#Each node in the n-ary tree contains a val (int) and a list (List[Node]) of
#its children.
#
#class Node {
#    public int val;
#    public List<Node> children;
#}
#
#Nary-Tree input serialization is represented in their level order traversal,
#each group of children is separated by the null value.
#
#Example 1:
#Input: root = [1,null,3,2,4,null,5,6]
#Output: [1,null,3,2,4,null,5,6]
#
#Example 2:
#Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
#Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
#
#Constraints:
#    The depth of the n-ary tree is less than or equal to 1000.
#    The total number of nodes is between [0, 10^4].

from typing import Optional, List
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: Optional[Node]) -> Optional[Node]:
        """
        Recursive DFS clone.
        """
        if not root:
            return None

        # Create new node with same value
        clone = Node(root.val)

        # Recursively clone all children
        clone.children = [self.cloneTree(child) for child in root.children]

        return clone


class SolutionBFS:
    def cloneTree(self, root: Optional[Node]) -> Optional[Node]:
        """
        BFS clone with queue.
        """
        if not root:
            return None

        # Map from original to clone
        node_map = {}

        # BFS
        queue = deque([root])
        node_map[root] = Node(root.val)

        while queue:
            original = queue.popleft()
            clone = node_map[original]

            for child in original.children:
                if child not in node_map:
                    node_map[child] = Node(child.val)
                    queue.append(child)
                clone.children.append(node_map[child])

        return node_map[root]


class SolutionIterative:
    def cloneTree(self, root: Optional[Node]) -> Optional[Node]:
        """
        Iterative DFS with stack.
        """
        if not root:
            return None

        # Stack stores (original, clone) pairs
        clone_root = Node(root.val)
        stack = [(root, clone_root)]

        while stack:
            original, clone = stack.pop()

            for child in original.children:
                child_clone = Node(child.val)
                clone.children.append(child_clone)
                stack.append((child, child_clone))

        return clone_root


class SolutionMemo:
    def cloneTree(self, root: Optional[Node]) -> Optional[Node]:
        """
        With memoization (useful if tree has shared references).
        """
        if not root:
            return None

        memo = {}

        def clone(node: Node) -> Node:
            if not node:
                return None

            if node in memo:
                return memo[node]

            new_node = Node(node.val)
            memo[node] = new_node

            new_node.children = [clone(child) for child in node.children]

            return new_node

        return clone(root)
