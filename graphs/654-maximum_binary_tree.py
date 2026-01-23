#654. Maximum Binary Tree
#Medium
#
#You are given an integer array nums with no duplicates. A maximum binary tree
#can be built recursively from nums using the following algorithm:
#
#1. Create a root node whose value is the maximum value in nums.
#2. Recursively build the left subtree on the subarray prefix to the left of
#   the maximum value.
#3. Recursively build the right subtree on the subarray suffix to the right of
#   the maximum value.
#
#Return the maximum binary tree built from nums.
#
#Example 1:
#Input: nums = [3,2,1,6,0,5]
#Output: [6,3,5,null,2,0,null,null,1]
#
#Example 2:
#Input: nums = [3,2,1]
#Output: [3,null,2,null,1]
#
#Constraints:
#    1 <= nums.length <= 1000
#    0 <= nums[i] <= 1000
#    All integers in nums are unique.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Recursive approach - find max, split, and recurse.
        """
        if not nums:
            return None

        max_val = max(nums)
        max_idx = nums.index(max_val)

        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx + 1:])

        return root


class SolutionOptimized:
    """Optimized with index passing instead of slicing"""

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left > right:
                return None

            # Find max in range
            max_idx = left
            for i in range(left + 1, right + 1):
                if nums[i] > nums[max_idx]:
                    max_idx = i

            root = TreeNode(nums[max_idx])
            root.left = build(left, max_idx - 1)
            root.right = build(max_idx + 1, right)

            return root

        return build(0, len(nums) - 1)


class SolutionStack:
    """
    Monotonic stack approach - O(n) time.
    Use decreasing stack to build tree in one pass.
    """

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []

        for num in nums:
            node = TreeNode(num)

            # Pop smaller elements - they become left children
            while stack and stack[-1].val < num:
                node.left = stack.pop()

            # Current node becomes right child of stack top
            if stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0] if stack else None
