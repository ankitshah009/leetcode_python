#979. Distribute Coins in Binary Tree
#Medium
#
#You are given the root of a binary tree with n nodes where each node in the
#tree has node.val coins. There are n coins in total throughout the whole tree.
#
#In one move, we may choose two adjacent nodes and move one coin from one node
#to another. A move may be from parent to child, or from child to parent.
#
#Return the minimum number of moves required to make every node have exactly
#one coin.
#
#Example 1:
#Input: root = [3,0,0]
#Output: 2
#
#Example 2:
#Input: root = [0,3,0]
#Output: 3
#
#Constraints:
#    The number of nodes in the tree is n.
#    1 <= n <= 100
#    0 <= Node.val <= n
#    The sum of all Node.val is n.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        """
        DFS: each node returns excess coins (positive) or deficit (negative).
        Moves = sum of |flow| across all edges.
        """
        moves = 0

        def dfs(node):
            nonlocal moves

            if not node:
                return 0

            left_flow = dfs(node.left)
            right_flow = dfs(node.right)

            # Moves needed = |coins flowing through each edge|
            moves += abs(left_flow) + abs(right_flow)

            # Return flow from this subtree: (coins - 1) + left + right
            return node.val - 1 + left_flow + right_flow

        dfs(root)
        return moves


class SolutionExplicit:
    """More explicit calculation"""

    def distributeCoins(self, root: TreeNode) -> int:
        moves = 0

        def dfs(node):
            """Return (excess coins, nodes in subtree)."""
            nonlocal moves

            if not node:
                return 0

            # Get excess from children
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)

            # Moves needed to balance children
            moves += abs(left_excess) + abs(right_excess)

            # This node's excess: coins - 1 (what it needs) + children's excess
            return node.val - 1 + left_excess + right_excess

        dfs(root)
        return moves


class SolutionIterative:
    """Post-order iterative"""

    def distributeCoins(self, root: TreeNode) -> int:
        moves = 0
        excess = {None: 0}

        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if visited:
                left_excess = excess.get(node.left, 0)
                right_excess = excess.get(node.right, 0)

                moves += abs(left_excess) + abs(right_excess)
                excess[node] = node.val - 1 + left_excess + right_excess
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return moves
