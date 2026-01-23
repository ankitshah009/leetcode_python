#1120. Maximum Average Subtree
#Medium
#
#Given the root of a binary tree, return the maximum average value of a
#subtree of that tree. Answers within 10^-5 of the actual answer will be
#accepted.
#
#A subtree of a tree is any node of that tree plus all its descendants.
#
#The average value of a tree is the sum of its values, divided by the
#number of nodes.
#
#Example 1:
#Input: root = [5,6,1]
#Output: 6.00000
#Explanation:
#For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
#For the node with value = 6 we have an average of 6 / 1 = 6.
#For the node with value = 1 we have an average of 1 / 1 = 1.
#So the answer is 6 which is the maximum.
#
#Example 2:
#Input: root = [0,null,1]
#Output: 1.00000
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    0 <= Node.val <= 10^5

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        """
        DFS returning (sum, count) for each subtree.
        Track maximum average.
        """
        self.max_avg = 0

        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            avg = total_sum / total_count
            self.max_avg = max(self.max_avg, avg)

            return total_sum, total_count

        dfs(root)
        return self.max_avg


class SolutionTuple:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        """Return (sum, count, max_avg) from DFS"""
        def dfs(node):
            if not node:
                return 0, 0, 0

            l_sum, l_cnt, l_max = dfs(node.left)
            r_sum, r_cnt, r_max = dfs(node.right)

            total_sum = l_sum + r_sum + node.val
            total_cnt = l_cnt + r_cnt + 1
            curr_avg = total_sum / total_cnt

            max_avg = max(l_max, r_max, curr_avg)

            return total_sum, total_cnt, max_avg

        return dfs(root)[2]
