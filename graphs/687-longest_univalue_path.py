#687. Longest Univalue Path
#Medium
#
#Given the root of a binary tree, return the length of the longest path, where
#each node in the path has the same value. This path may or may not pass through
#the root.
#
#The length of the path between two nodes is represented by the number of edges
#between them.
#
#Example 1:
#Input: root = [5,4,5,1,1,null,5]
#Output: 2
#Explanation: The longest path with same value is [5,5,5].
#
#Example 2:
#Input: root = [1,4,5,4,4,null,5]
#Output: 2
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 10^4].
#    -1000 <= Node.val <= 1000
#    The depth of the tree will not exceed 1000.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestUnivaluePath(self, root) -> int:
        """
        DFS: for each node, compute longest univalue path going down.
        Update global max with path through current node.
        """
        self.max_length = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # Extend left path if values match
            left_path = left + 1 if node.left and node.left.val == node.val else 0
            # Extend right path if values match
            right_path = right + 1 if node.right and node.right.val == node.val else 0

            # Update max with path through this node
            self.max_length = max(self.max_length, left_path + right_path)

            # Return longest path going down (can't go both ways)
            return max(left_path, right_path)

        dfs(root)
        return self.max_length


class SolutionTuple:
    """Return tuple instead of using instance variable"""

    def longestUnivaluePath(self, root) -> int:
        def dfs(node):
            # Returns (max_length_in_subtree, longest_arm_from_node)
            if not node:
                return 0, 0

            left_max, left_arm = dfs(node.left)
            right_max, right_arm = dfs(node.right)

            # Compute arms from current node
            curr_left = left_arm + 1 if node.left and node.left.val == node.val else 0
            curr_right = right_arm + 1 if node.right and node.right.val == node.val else 0

            # Max in this subtree
            curr_max = max(left_max, right_max, curr_left + curr_right)

            return curr_max, max(curr_left, curr_right)

        return dfs(root)[0] if root else 0
