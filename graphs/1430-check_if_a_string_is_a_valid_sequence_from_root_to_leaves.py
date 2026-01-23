#1430. Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
#Medium
#
#Given a binary tree where each path going from the root to any leaf form a
#valid sequence, check if a given string is a valid sequence in such binary tree.
#
#We get the given string from the concatenation of an array of integers arr and
#the concatenation of all values of the nodes along a path results in a sequence
#in the given binary tree.
#
#Example 1:
#Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
#Output: true
#Explanation:
#The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
#Other valid sequences are:
#0 -> 1 -> 1 -> 0
#0 -> 0 -> 0
#
#Example 2:
#Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
#Output: false
#Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
#
#Example 3:
#Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
#Output: false
#Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.
#
#Constraints:
#    1 <= arr.length <= 5000
#    0 <= arr[i] <= 9
#    Each node's value is between [0 - 9].

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        """
        DFS to check if there's a root-to-leaf path matching arr.
        Path must end at a leaf (not just match the array).
        """
        def dfs(node: Optional[TreeNode], idx: int) -> bool:
            if not node:
                return False

            # Current value must match
            if idx >= len(arr) or node.val != arr[idx]:
                return False

            # If this is the last element, must be at a leaf
            if idx == len(arr) - 1:
                return node.left is None and node.right is None

            # Continue to children
            return dfs(node.left, idx + 1) or dfs(node.right, idx + 1)

        return dfs(root, 0)


class SolutionBFS:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        """BFS approach"""
        from collections import deque

        if not root or root.val != arr[0]:
            return False

        if len(arr) == 1:
            return root.left is None and root.right is None

        queue = deque([(root, 0)])

        while queue:
            node, idx = queue.popleft()

            if idx == len(arr) - 1:
                # Check if it's a leaf
                if node.left is None and node.right is None:
                    return True
                continue

            # Add children if they match next value
            if node.left and node.left.val == arr[idx + 1]:
                queue.append((node.left, idx + 1))
            if node.right and node.right.val == arr[idx + 1]:
                queue.append((node.right, idx + 1))

        return False


class SolutionIterative:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        """Iterative DFS with stack"""
        if not root:
            return False

        stack = [(root, 0)]

        while stack:
            node, idx = stack.pop()

            # Value mismatch
            if node.val != arr[idx]:
                continue

            # Check if at end of array
            if idx == len(arr) - 1:
                # Must be a leaf
                if not node.left and not node.right:
                    return True
                continue

            # Add children to stack
            if node.right:
                stack.append((node.right, idx + 1))
            if node.left:
                stack.append((node.left, idx + 1))

        return False
