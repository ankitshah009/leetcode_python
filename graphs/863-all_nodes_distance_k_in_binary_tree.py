#863. All Nodes Distance K in Binary Tree
#Medium
#
#Given the root of a binary tree, the value of a target node target, and an
#integer k, return an array of the values of all nodes that have a distance k
#from the target node.
#
#You can return the answer in any order.
#
#Example 1:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
#Output: [7,4,1]
#
#Example 2:
#Input: root = [1], target = 1, k = 3
#Output: []
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 500].
#    0 <= Node.val <= 500
#    All the values Node.val are unique.
#    target is the value of one of the nodes in the tree.
#    0 <= k <= 1000

from collections import deque, defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        """
        Build parent map, then BFS from target.
        """
        # Build parent map
        parent = {}

        def build_parent(node, par):
            if node:
                parent[node] = par
                build_parent(node.left, node)
                build_parent(node.right, node)

        build_parent(root, None)

        # BFS from target
        queue = deque([(target, 0)])
        visited = {target}
        result = []

        while queue:
            node, dist = queue.popleft()

            if dist == k:
                result.append(node.val)
                continue

            # Explore neighbors: left, right, parent
            for neighbor in [node.left, node.right, parent.get(node)]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

        return result


class SolutionDFS:
    """DFS approach"""

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        result = []

        def dfs(node, dist):
            """DFS to find nodes at distance k from target in subtree"""
            if not node:
                return
            if dist == k:
                result.append(node.val)
                return
            dfs(node.left, dist + 1)
            dfs(node.right, dist + 1)

        def find_target(node):
            """
            Returns distance from node to target (-1 if not in subtree)
            Also finds nodes at distance k going up through ancestors
            """
            if not node:
                return -1

            if node == target:
                dfs(node, 0)
                return 0

            left_dist = find_target(node.left)
            if left_dist != -1:
                if left_dist + 1 == k:
                    result.append(node.val)
                else:
                    # Search in right subtree at remaining distance
                    dfs(node.right, left_dist + 2)
                return left_dist + 1

            right_dist = find_target(node.right)
            if right_dist != -1:
                if right_dist + 1 == k:
                    result.append(node.val)
                else:
                    dfs(node.left, right_dist + 2)
                return right_dist + 1

            return -1

        find_target(root)
        return result
