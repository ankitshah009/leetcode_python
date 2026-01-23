#968. Binary Tree Cameras
#Hard
#
#You are given the root of a binary tree. We install cameras on the tree nodes
#where each camera at a node can monitor its parent, itself, and its immediate
#children.
#
#Return the minimum number of cameras needed to monitor all nodes of the tree.
#
#Example 1:
#Input: root = [0,0,null,0,0]
#Output: 1
#
#Example 2:
#Input: root = [0,0,null,0,null,0,null,null,0]
#Output: 2
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 1000].
#    Node.val == 0

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        """
        Greedy DFS: place cameras at parents of leaves.
        States: 0=needs coverage, 1=has camera, 2=covered
        """
        cameras = 0

        def dfs(node):
            nonlocal cameras

            if not node:
                return 2  # Null nodes are "covered"

            left = dfs(node.left)
            right = dfs(node.right)

            # If any child needs coverage, place camera here
            if left == 0 or right == 0:
                cameras += 1
                return 1  # Has camera

            # If any child has camera, this node is covered
            if left == 1 or right == 1:
                return 2  # Covered

            # Both children covered but no camera, needs coverage
            return 0

        # Check if root still needs coverage
        if dfs(root) == 0:
            cameras += 1

        return cameras


class SolutionDP:
    """DP with 3 states per node"""

    def minCameraCover(self, root: TreeNode) -> int:
        INF = float('inf')

        def dfs(node):
            """
            Return (min cameras if node has camera,
                    min cameras if node covered but no camera,
                    min cameras if node not covered)
            """
            if not node:
                return (INF, 0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            # Node has camera: children can be any state
            d0 = 1 + min(left) + min(right)

            # Node covered but no camera: at least one child has camera
            d1 = min(
                left[0] + min(right[0], right[1]),
                right[0] + min(left[0], left[1])
            )

            # Node not covered: both children must be covered but no camera
            d2 = left[1] + right[1]

            return (d0, d1, d2)

        result = dfs(root)
        return min(result[0], result[1])


class SolutionIterative:
    """Post-order with explicit stack"""

    def minCameraCover(self, root: TreeNode) -> int:
        if not root:
            return 0

        cameras = 0
        # State: 0=needs, 1=has camera, 2=covered
        state = {None: 2}

        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if visited:
                left = state.get(node.left, 2)
                right = state.get(node.right, 2)

                if left == 0 or right == 0:
                    cameras += 1
                    state[node] = 1
                elif left == 1 or right == 1:
                    state[node] = 2
                else:
                    state[node] = 0
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        if state[root] == 0:
            cameras += 1

        return cameras
