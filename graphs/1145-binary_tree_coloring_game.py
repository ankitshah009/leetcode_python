#1145. Binary Tree Coloring Game
#Medium
#
#Two players play a turn based game on a binary tree. We are given the root
#of this binary tree, and the number of nodes n in the tree. n is odd, and
#each node has a distinct value from 1 to n.
#
#Initially, the first player names a value x with 1 <= x <= n, and the second
#player names a value y with 1 <= y <= n and y != x. The first player colors
#the node with value x red, and the second player colors the node with value y blue.
#
#Then, the players take turns starting with the first player. In each turn,
#that player chooses a node of their color (red if player 1, blue if player 2)
#and colors an uncolored neighbor of the chosen node (either the left child,
#right child, or parent of the chosen node.)
#
#If (and only if) a player cannot choose such a node in this way, they must
#pass their turn. If both players pass their turn, the game ends, and the
#winner is the player that colored more nodes.
#
#You are the second player. If it is possible to choose such a y to ensure
#you win the game, return true. If it is not possible, return false.
#
#Example 1:
#Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
#Output: true
#Explanation: The second player can choose the node with value 2.
#
#Example 2:
#Input: root = [1,2,3], n = 3, x = 1
#Output: false
#
#Constraints:
#    The number of nodes in the tree is n.
#    1 <= x <= n <= 100
#    n is odd.
#    1 <= Node.val <= n
#    All the values of the tree are unique.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        """
        Second player can block one of three regions:
        1. Left subtree of x
        2. Right subtree of x
        3. Parent direction of x

        Win if any region has > n/2 nodes.
        """
        left_count = right_count = 0

        def count_nodes(node):
            nonlocal left_count, right_count

            if not node:
                return 0

            left = count_nodes(node.left)
            right = count_nodes(node.right)

            if node.val == x:
                left_count = left
                right_count = right

            return left + right + 1

        count_nodes(root)

        # Parent region has remaining nodes
        parent_count = n - left_count - right_count - 1

        # Second player wins if any region > half
        half = n // 2
        return left_count > half or right_count > half or parent_count > half


class SolutionFindNode:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        """First find x, then count subtrees"""
        def find(node, val):
            if not node:
                return None
            if node.val == val:
                return node
            return find(node.left, val) or find(node.right, val)

        def count(node):
            if not node:
                return 0
            return 1 + count(node.left) + count(node.right)

        x_node = find(root, x)
        left = count(x_node.left)
        right = count(x_node.right)
        parent = n - left - right - 1

        return max(left, right, parent) > n // 2
