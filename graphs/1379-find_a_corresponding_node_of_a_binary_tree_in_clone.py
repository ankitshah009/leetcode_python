#1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#Easy
#
#Given two binary trees original and cloned and given a reference to a node
#target in the original tree.
#
#The cloned tree is a copy of the original tree.
#
#Return a reference to the same node in the cloned tree.
#
#Note that you are not allowed to change any of the two trees or the target node
#and the answer must be a reference to a node in the cloned tree.
#
#Example 1:
#Input: tree = [7,4,3,null,null,6,19], target = 3
#Output: 3
#Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
#
#Example 2:
#Input: tree = [7], target = 7
#Output: 7
#
#Example 3:
#Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
#Output: 4
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^4].
#    The values of the nodes of the tree are unique.
#    target node is a node from the original tree and is not null.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """
        Traverse both trees simultaneously.
        When we find target in original, return corresponding node in cloned.
        """
        def dfs(orig_node, clone_node):
            if not orig_node:
                return None

            if orig_node is target:
                return clone_node

            # Search in left subtree
            result = dfs(orig_node.left, clone_node.left)
            if result:
                return result

            # Search in right subtree
            return dfs(orig_node.right, clone_node.right)

        return dfs(original, cloned)


class SolutionBFS:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """BFS approach"""
        from collections import deque

        queue = deque([(original, cloned)])

        while queue:
            orig, clone = queue.popleft()

            if orig is target:
                return clone

            if orig.left:
                queue.append((orig.left, clone.left))
            if orig.right:
                queue.append((orig.right, clone.right))

        return None


class SolutionIterative:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """Iterative DFS using stack"""
        stack = [(original, cloned)]

        while stack:
            orig, clone = stack.pop()

            if orig is target:
                return clone

            if orig.right:
                stack.append((orig.right, clone.right))
            if orig.left:
                stack.append((orig.left, clone.left))

        return None
