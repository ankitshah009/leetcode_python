#298. Binary Tree Longest Consecutive Sequence
#Medium
#
#Given the root of a binary tree, return the length of the longest consecutive
#sequence path.
#
#A consecutive sequence path is a path where the values increase by one along
#the path.
#
#Note that the path can start at any node in the tree, and you cannot go from a
#node to its parent in the path.
#
#Example 1:
#Input: root = [1,null,3,2,4,null,null,null,5]
#Output: 3
#Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
#
#Example 2:
#Input: root = [2,null,3,2,null,1]
#Output: 2
#Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 3 * 10^4].
#    -3 * 10^4 <= Node.val <= 3 * 10^4

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0

        def dfs(node, parent_val, length):
            if not node:
                return

            # Check if current continues the sequence
            if node.val == parent_val + 1:
                length += 1
            else:
                length = 1

            self.max_length = max(self.max_length, length)

            dfs(node.left, node.val, length)
            dfs(node.right, node.val, length)

        dfs(root, root.val - 1, 0)
        return self.max_length

    # Alternative without class variable
    def longestConsecutiveAlt(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent_val, length):
            if not node:
                return length

            if node.val == parent_val + 1:
                curr_length = length + 1
            else:
                curr_length = 1

            left_max = dfs(node.left, node.val, curr_length)
            right_max = dfs(node.right, node.val, curr_length)

            return max(curr_length, left_max, right_max)

        if not root:
            return 0
        return dfs(root, root.val - 1, 0)

    # BFS approach
    def longestConsecutiveBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        from collections import deque

        max_length = 1
        queue = deque([(root, 1)])  # (node, current_length)

        while queue:
            node, length = queue.popleft()
            max_length = max(max_length, length)

            for child in [node.left, node.right]:
                if child:
                    if child.val == node.val + 1:
                        queue.append((child, length + 1))
                    else:
                        queue.append((child, 1))

        return max_length
