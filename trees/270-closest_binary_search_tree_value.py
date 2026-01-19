#270. Closest Binary Search Tree Value
#Easy
#
#Given the root of a binary search tree and a target value, return the value in
#the BST that is closest to the target. If there are multiple answers, print the
#smallest.
#
#Example 1:
#Input: root = [4,2,5,1,3], target = 3.714286
#Output: 4
#
#Example 2:
#Input: root = [1], target = 4.428571
#Output: 1
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    0 <= Node.val <= 10^9
#    -10^9 <= target <= 10^9

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val

        while root:
            # Update closest if current is closer
            # If same distance, prefer smaller value
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            elif abs(root.val - target) == abs(closest - target):
                closest = min(closest, root.val)

            # Move to appropriate subtree
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closest

    # Recursive approach
    def closestValueRecursive(self, root: Optional[TreeNode], target: float) -> int:
        def helper(node, closest):
            if not node:
                return closest

            # Update closest
            if abs(node.val - target) < abs(closest - target):
                closest = node.val
            elif abs(node.val - target) == abs(closest - target):
                closest = min(closest, node.val)

            # Search in appropriate subtree
            if target < node.val:
                return helper(node.left, closest)
            else:
                return helper(node.right, closest)

        return helper(root, root.val)
