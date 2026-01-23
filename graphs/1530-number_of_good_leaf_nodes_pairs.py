#1530. Number of Good Leaf Nodes Pairs
#Medium
#
#You are given the root of a binary tree and an integer distance. A pair of two
#different leaf nodes of a binary tree is said to be good if the length of the
#shortest path between them is less than or equal to distance.
#
#Return the number of good leaf node pairs in the tree.
#
#Example 1:
#Input: root = [1,2,3,null,4], distance = 3
#Output: 1
#Explanation: The leaf nodes of the tree are 3 and 4 and the length of the
#shortest path between them is 3. This is the only good pair.
#
#Example 2:
#Input: root = [1,2,3,4,5,6,7], distance = 3
#Output: 2
#Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2.
#
#Example 3:
#Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
#Output: 1
#Explanation: The only good pair is [2,7] with shortest path = 3.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 2^10].
#    1 <= Node.val <= 100
#    1 <= distance <= 10

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        DFS returning distances of all leaf nodes from current node.
        At each node, count pairs between left and right subtrees.
        """
        self.result = 0

        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []

            # Leaf node
            if not node.left and not node.right:
                return [1]

            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            # Count good pairs between left and right subtrees
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        self.result += 1

            # Return incremented distances (prune those > distance)
            return [d + 1 for d in left_distances + right_distances if d + 1 < distance]

        dfs(root)
        return self.result


class SolutionOptimized:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        Optimized: use count arrays instead of lists.
        distances[i] = number of leaves at distance i from this node.
        """
        self.result = 0

        def dfs(node: Optional[TreeNode]) -> List[int]:
            # distances[i] = count of leaves at distance i
            distances = [0] * (distance + 1)

            if not node:
                return distances

            if not node.left and not node.right:
                distances[0] = 1
                return distances

            left = dfs(node.left)
            right = dfs(node.right)

            # Count pairs
            for i in range(distance + 1):
                for j in range(distance + 1):
                    if i + j + 2 <= distance:
                        self.result += left[i] * right[j]

            # Shift distances by 1
            for i in range(distance - 1, -1, -1):
                distances[i + 1] = left[i] + right[i]

            return distances

        dfs(root)
        return self.result


class SolutionLCA:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        Alternative: Find all leaves, compute LCA distances.
        Less efficient but conceptually clearer.
        """
        # Find all leaves with their paths from root
        leaves = []

        def find_leaves(node, path):
            if not node:
                return
            path = path + [node]
            if not node.left and not node.right:
                leaves.append(path)
            else:
                find_leaves(node.left, path)
                find_leaves(node.right, path)

        find_leaves(root, [])

        # Count pairs
        count = 0
        n = len(leaves)

        for i in range(n):
            for j in range(i + 1, n):
                # Find LCA depth
                path1, path2 = leaves[i], leaves[j]
                lca_depth = 0
                for k in range(min(len(path1), len(path2))):
                    if path1[k] == path2[k]:
                        lca_depth = k + 1
                    else:
                        break

                # Distance = (depth1 - lca) + (depth2 - lca)
                dist = (len(path1) - lca_depth) + (len(path2) - lca_depth)
                if dist <= distance:
                    count += 1

        return count
