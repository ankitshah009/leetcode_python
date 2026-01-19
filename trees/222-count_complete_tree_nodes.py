#222. Count Complete Tree Nodes
#Medium
#
#Given the root of a complete binary tree, return the number of the nodes in the tree.
#
#According to Wikipedia, every level, except possibly the last, is completely filled
#in a complete binary tree, and all nodes in the last level are as far left as possible.
#It can have between 1 and 2h nodes inclusive at the last level h.
#
#Design an algorithm that runs in less than O(n) time complexity.
#
#Example 1:
#Input: root = [1,2,3,4,5,6]
#Output: 6
#
#Example 2:
#Input: root = []
#Output: 0
#
#Example 3:
#Input: root = [1]
#Output: 1
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 5 * 10^4].
#    0 <= Node.val <= 5 * 10^4
#    The tree is guaranteed to be complete.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def get_height(node, go_left=True):
            height = 0
            while node:
                height += 1
                node = node.left if go_left else node.right
            return height

        left_height = get_height(root, True)
        right_height = get_height(root, False)

        if left_height == right_height:
            # Perfect binary tree: 2^h - 1 nodes
            return (1 << left_height) - 1

        # Not perfect: recursively count left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # Binary search approach: O(log^2 n)
    def countNodesBinarySearch(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Get the height of the tree
        height = 0
        node = root
        while node.left:
            height += 1
            node = node.left

        if height == 0:
            return 1

        # Binary search on the last level
        # Check if node at index idx (0 to 2^height - 1) exists
        def exists(idx, height, node):
            left, right = 0, (1 << height) - 1
            for _ in range(height):
                mid = (left + right) // 2
                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None

        left, right = 0, (1 << height) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if exists(mid, height, root):
                left = mid
            else:
                right = mid - 1

        # Total nodes = nodes in first (height) levels + nodes in last level
        return (1 << height) - 1 + left + 1
