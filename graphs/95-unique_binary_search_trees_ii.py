#95. Unique Binary Search Trees II
#Medium
#
#Given an integer n, return all the structurally unique BST's (binary search
#trees), which has exactly n nodes of unique values from 1 to n. Return the
#answer in any order.
#
#Example 1:
#Input: n = 3
#Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#
#Example 2:
#Input: n = 1
#Output: [[1]]
#
#Constraints:
#    1 <= n <= 8

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        Recursive generation with memoization.
        """
        if n == 0:
            return []

        def generate(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]

            trees = []
            for root_val in range(start, end + 1):
                # Generate all left subtrees
                left_trees = generate(start, root_val - 1)
                # Generate all right subtrees
                right_trees = generate(root_val + 1, end)

                # Combine all pairs
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return generate(1, n)


class SolutionMemo:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        With explicit memoization.
        """
        if n == 0:
            return []

        memo = {}

        def generate(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]

            if (start, end) in memo:
                return memo[(start, end)]

            trees = []
            for root_val in range(start, end + 1):
                left_trees = generate(start, root_val - 1)
                right_trees = generate(root_val + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)

            memo[(start, end)] = trees
            return trees

        return generate(1, n)


class SolutionDP:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        DP approach - build from smaller subtrees.
        """
        if n == 0:
            return []

        def clone(node: Optional[TreeNode], offset: int) -> Optional[TreeNode]:
            """Clone tree with offset added to all values."""
            if not node:
                return None
            new_node = TreeNode(node.val + offset)
            new_node.left = clone(node.left, offset)
            new_node.right = clone(node.right, offset)
            return new_node

        # dp[i] = all unique BSTs with i nodes (values 1 to i)
        dp = [[] for _ in range(n + 1)]
        dp[0] = [None]

        for num_nodes in range(1, n + 1):
            for root_val in range(1, num_nodes + 1):
                left_count = root_val - 1
                right_count = num_nodes - root_val

                for left_tree in dp[left_count]:
                    for right_tree in dp[right_count]:
                        root = TreeNode(root_val)
                        root.left = clone(left_tree, 0)
                        root.right = clone(right_tree, root_val)
                        dp[num_nodes].append(root)

        return dp[n]


class SolutionIterative:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        Build trees iteratively by adding nodes.
        """
        if n == 0:
            return []

        trees = [None]

        for val in range(1, n + 1):
            new_trees = []

            for tree in trees:
                # Insert val as new root
                new_root = TreeNode(val)
                new_root.left = self.clone(tree)
                new_trees.append(new_root)

                # Insert val at each position along right spine
                curr = tree
                while curr:
                    # Clone tree up to current node
                    new_tree = self.clone(tree)

                    # Navigate to current position in cloned tree
                    node = new_tree
                    temp = tree
                    while temp != curr:
                        node = node.right
                        temp = temp.right

                    # Insert new node
                    new_node = TreeNode(val)
                    new_node.left = node.right
                    node.right = new_node
                    new_trees.append(new_tree)

                    curr = curr.right

            trees = new_trees

        return trees

    def clone(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None
        new_node = TreeNode(node.val)
        new_node.left = self.clone(node.left)
        new_node.right = self.clone(node.right)
        return new_node
