#1973. Count Nodes Equal to Sum of Descendants
#Medium
#
#Given the root of a binary tree, return the number of nodes where the value of
#the node is equal to the sum of the values of its descendants.
#
#A descendant of a node x is any node that is on the path from node x to some
#leaf node. The sum is considered to be 0 if the node has no descendants.
#
#Example 1:
#Input: root = [10,3,4,2,1]
#Output: 2
#Explanation: Node 10 = 3 + 4 + 2 + 1 = 10
#             Node 3 = 2 + 1 = 3 (not counting itself)
#
#Example 2:
#Input: root = [2,3,null,2,null]
#Output: 0
#
#Example 3:
#Input: root = [0]
#Output: 1
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^5].
#    0 <= Node.val <= 10^5

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        """
        DFS to compute sum of descendants for each node.
        """
        self.count = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            descendants_sum = left_sum + right_sum

            if node.val == descendants_sum:
                self.count += 1

            return descendants_sum + node.val

        dfs(root)
        return self.count


class SolutionTuple:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        """
        Return both count and sum in single traversal.
        """
        def dfs(node: Optional[TreeNode]) -> tuple:
            """Returns (count of matching nodes, total sum of subtree)"""
            if not node:
                return (0, 0)

            left_count, left_sum = dfs(node.left)
            right_count, right_sum = dfs(node.right)

            descendants_sum = left_sum + right_sum
            count = left_count + right_count

            if node.val == descendants_sum:
                count += 1

            return (count, descendants_sum + node.val)

        return dfs(root)[0]


class SolutionIterative:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        """
        Iterative post-order traversal.
        """
        if not root:
            return 0

        count = 0
        stack = [(root, False)]
        sums = {}  # node -> sum of subtree

        while stack:
            node, processed = stack.pop()

            if processed:
                left_sum = sums.get(node.left, 0)
                right_sum = sums.get(node.right, 0)
                descendants_sum = left_sum + right_sum

                if node.val == descendants_sum:
                    count += 1

                sums[node] = descendants_sum + node.val
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return count
