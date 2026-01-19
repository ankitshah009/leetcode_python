#113. Path Sum II
#Medium
#
#Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths
#where the sum of the node values in the path equals targetSum. Each path should be returned
#as a list of the node values, not node references.
#
#Example 1:
#Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
#Output: [[5,4,11,2],[5,8,4,5]]
#
#Example 2:
#Input: root = [1,2,3], targetSum = 5
#Output: []
#
#Example 3:
#Input: root = [1,2], targetSum = 0
#Output: []
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 5000].
#    -1000 <= Node.val <= 1000
#    -1000 <= targetSum <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right and remaining == node.val:
                result.append(path[:])
            else:
                dfs(node.left, remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)

            path.pop()

        dfs(root, targetSum, [])
        return result
