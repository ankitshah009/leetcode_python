#742. Closest Leaf in a Binary Tree
#Medium
#
#Given the root of a binary tree where every node has a unique value and a
#target integer k, return the value of the nearest leaf node to the target k
#in the tree.
#
#Nearest to a leaf means the least number of edges traveled on the binary tree
#to reach any leaf of the tree. Also, a node is called a leaf if it has no
#children.
#
#Example 1:
#Input: root = [1,3,2], k = 1
#Output: 2
#Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
#
#Example 2:
#Input: root = [1], k = 1
#Output: 1
#Explanation: The nearest leaf node is the root node itself.
#
#Example 3:
#Input: root = [1,2,3,4,null,null,null,5,null,6], k = 2
#Output: 3
#Explanation: The leaf node with value 3 is nearest to the node with value 2.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 1000].
#    1 <= Node.val <= 1000
#    All the values of the tree are unique.
#    There exist some node in the tree where Node.val == k.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def findClosestLeaf(self, root, k: int) -> int:
        """
        Convert tree to undirected graph, BFS from target node.
        """
        # Build graph
        graph = defaultdict(list)
        leaves = set()

        def build_graph(node, parent):
            if not node:
                return

            if not node.left and not node.right:
                leaves.add(node.val)

            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)

            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root, None)

        # BFS from target
        queue = deque([k])
        visited = {k}

        while queue:
            node = queue.popleft()

            if node in leaves:
                return node

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return -1


class SolutionDFS:
    """DFS to find target, then BFS for nearest leaf"""

    def findClosestLeaf(self, root, k: int) -> int:
        # Find path from root to target
        def find_path(node, target, path):
            if not node:
                return False
            path.append(node)
            if node.val == target:
                return True
            if find_path(node.left, target, path) or find_path(node.right, target, path):
                return True
            path.pop()
            return False

        path = []
        find_path(root, k, path)

        # Find closest leaf from each node in path
        def closest_leaf_down(node, dist):
            if not node:
                return (float('inf'), -1)
            if not node.left and not node.right:
                return (dist, node.val)

            left = closest_leaf_down(node.left, dist + 1)
            right = closest_leaf_down(node.right, dist + 1)

            return left if left[0] <= right[0] else right

        result = (float('inf'), -1)

        for i, node in enumerate(path):
            # Distance from target to this node in path
            dist_to_target = len(path) - 1 - i

            # Find closest leaf going down from this node
            # but not through the path to target
            if i == len(path) - 1:
                leaf_dist, leaf_val = closest_leaf_down(node, dist_to_target)
            else:
                # Block the child that's in the path
                next_in_path = path[i + 1]
                temp_left, temp_right = node.left, node.right

                if node.left == next_in_path:
                    node.left = None
                else:
                    node.right = None

                leaf_dist, leaf_val = closest_leaf_down(node, dist_to_target)

                node.left, node.right = temp_left, temp_right

            if leaf_dist < result[0]:
                result = (leaf_dist, leaf_val)

        return result[1]
