#653. Two Sum IV - Input is a BST
#Easy
#
#Given the root of a binary search tree and an integer k, return true if there
#exist two elements in the BST such that their sum is equal to k, or false otherwise.
#
#Example 1:
#Input: root = [5,3,6,2,4,null,7], k = 9
#Output: true
#
#Example 2:
#Input: root = [5,3,6,2,4,null,7], k = 28
#Output: false
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    -10^4 <= Node.val <= 10^4
#    root is guaranteed to be a valid binary search tree.
#    -10^5 <= k <= 10^5

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Use set to store seen values.
        """
        seen = set()

        def dfs(node):
            if not node:
                return False

            if k - node.val in seen:
                return True

            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)


class SolutionTwoPointers:
    """
    Use BST property - inorder gives sorted array.
    Then use two pointers.
    """

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Get sorted array via inorder traversal
        nums = []

        def inorder(node):
            if node:
                inorder(node.left)
                nums.append(node.val)
                inorder(node.right)

        inorder(root)

        # Two pointers
        left, right = 0, len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1

        return False


class SolutionBFS:
    """BFS with hash set"""

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        from collections import deque

        if not root:
            return False

        seen = set()
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if k - node.val in seen:
                return True

            seen.add(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False
