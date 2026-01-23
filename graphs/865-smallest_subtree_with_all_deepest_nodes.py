#865. Smallest Subtree with all the Deepest Nodes
#Medium
#
#Given the root of a binary tree, the depth of each node is the shortest
#distance to the root.
#
#Return the smallest subtree such that it contains all the deepest nodes in the
#original tree.
#
#A node is called the deepest if it has the largest depth possible among any
#node in the entire tree.
#
#The subtree of a node is a tree consisting of that node, plus the set of all
#descendants of that node.
#
#Example 1:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4]
#Output: [2,7,4]
#
#Example 2:
#Input: root = [1]
#Output: [1]
#
#Example 3:
#Input: root = [0,1,3,null,2]
#Output: [2]
#
#Constraints:
#    The number of nodes in the tree will be in the range [1, 500].
#    0 <= Node.val <= 500
#    The values of the nodes in the tree are unique.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """
        Return (node, depth) where node is the LCA of all deepest nodes.
        """
        def dfs(node):
            if not node:
                return (None, 0)

            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)

            if left_depth > right_depth:
                return (left_node, left_depth + 1)
            elif right_depth > left_depth:
                return (right_node, right_depth + 1)
            else:
                # Equal depths: current node is the LCA
                return (node, left_depth + 1)

        return dfs(root)[0]


class SolutionTwoPass:
    """Two passes: find depth, then find LCA"""

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # First pass: compute depths
        depth = {None: -1}

        def compute_depth(node, d):
            if node:
                depth[node] = d
                compute_depth(node.left, d + 1)
                compute_depth(node.right, d + 1)

        compute_depth(root, 0)
        max_depth = max(depth.values())

        # Second pass: find LCA of deepest nodes
        def find_lca(node):
            if not node or depth[node] == max_depth:
                return node

            left = find_lca(node.left)
            right = find_lca(node.right)

            if left and right:
                return node
            return left or right

        return find_lca(root)


class SolutionIterative:
    """Iterative with parent pointers"""

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        from collections import deque

        if not root:
            return None

        parent = {root: None}
        queue = deque([root])
        deepest = []

        while queue:
            deepest = list(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    parent[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parent[node.right] = node
                    queue.append(node.right)

        # Find LCA of all deepest nodes
        while len(set(deepest)) > 1:
            deepest = list(set(parent[n] for n in deepest))

        return deepest[0]
