#1676. Lowest Common Ancestor of a Binary Tree IV
#Medium
#
#Given the root of a binary tree and an array of TreeNode objects nodes, return
#the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will
#exist in the tree, and all values of the tree's nodes are unique.
#
#Example 1:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
#Output: 2
#Explanation: The LCA of nodes 4 and 7 is node 2.
#
#Example 2:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
#Output: 1
#Explanation: The LCA of a single node is the node itself.
#
#Example 3:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
#Output: 5
#Explanation: The LCA of nodes 7, 6, 2, and 4 is node 5.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    -10^9 <= Node.val <= 10^9
#    All Node.val are unique.
#    All nodes[i] will exist in the tree.
#    All nodes[i] are distinct.

from typing import List, Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode',
                            nodes: 'List[TreeNode]') -> 'TreeNode':
        """
        Recursive approach: find LCA where at least one node exists in subtree.
        """
        target_set = set(nodes)

        def dfs(node: TreeNode) -> TreeNode:
            if not node:
                return None
            if node in target_set:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            return left or right

        return dfs(root)


class SolutionIterative:
    def lowestCommonAncestor(self, root: 'TreeNode',
                            nodes: 'List[TreeNode]') -> 'TreeNode':
        """
        Iterative approach using parent pointers.
        """
        if not root:
            return None

        # Build parent map
        parent = {root: None}
        stack = [root]

        while stack:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Find ancestors of first node
        ancestors = set()
        node = nodes[0]
        while node:
            ancestors.add(node)
            node = parent[node]

        # For each subsequent node, reduce ancestors to common ones
        for target in nodes[1:]:
            current_ancestors = set()
            node = target
            while node:
                current_ancestors.add(node)
                node = parent[node]
            ancestors &= current_ancestors

        # Find lowest (deepest) common ancestor
        # Traverse from any node upward, first ancestor in set is LCA
        node = nodes[0]
        while node not in ancestors:
            node = parent[node]

        return node


class SolutionPairwise:
    def lowestCommonAncestor(self, root: 'TreeNode',
                            nodes: 'List[TreeNode]') -> 'TreeNode':
        """
        Find LCA pairwise, then find LCA of all results.
        """
        def lca_two(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            if not root or root == p or root == q:
                return root
            left = lca_two(root.left, p, q)
            right = lca_two(root.right, p, q)
            if left and right:
                return root
            return left or right

        result = nodes[0]
        for i in range(1, len(nodes)):
            result = lca_two(root, result, nodes[i])

        return result


class SolutionEulerTour:
    def lowestCommonAncestor(self, root: 'TreeNode',
                            nodes: 'List[TreeNode]') -> 'TreeNode':
        """
        Using Euler tour and sparse table (for multiple queries).
        Simplified version for single query.
        """
        # Build parent and depth maps
        parent = {root: None}
        depth = {root: 0}
        stack = [root]

        while stack:
            node = stack.pop()
            for child in [node.left, node.right]:
                if child:
                    parent[child] = node
                    depth[child] = depth[node] + 1
                    stack.append(child)

        # Find deepest node among targets
        target_set = set(nodes)
        deepest = max(nodes, key=lambda x: depth[x])

        # Collect all ancestors
        ancestors = {}
        node = deepest
        while node:
            ancestors[node] = depth[node]
            node = parent[node]

        # Find first common ancestor for all nodes
        for target in nodes:
            node = target
            while node not in ancestors:
                ancestors[node] = depth[node]
                node = parent[node]

        # LCA is the node in ancestors with maximum depth that's ancestor of all
        # Use recursive approach which is simpler
        def dfs(node: TreeNode) -> TreeNode:
            if not node:
                return None
            if node in target_set:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left or right

        return dfs(root)
