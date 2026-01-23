#872. Leaf-Similar Trees
#Easy
#
#Consider all the leaves of a binary tree, from left to right order, the values
#of those leaves form a leaf value sequence.
#
#Two binary trees are considered leaf-similar if their leaf value sequence is
#the same.
#
#Return true if and only if the two given trees with head nodes root1 and root2
#are leaf-similar.
#
#Example 1:
#Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
#Output: true
#
#Example 2:
#Input: root1 = [1,2,3], root2 = [1,3,2]
#Output: false
#
#Constraints:
#    The number of nodes in each tree will be in the range [1, 200].
#    Both trees will have values in the range [0, 200].

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        Get leaf sequences and compare.
        """
        def get_leaves(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return get_leaves(node.left) + get_leaves(node.right)

        return get_leaves(root1) == get_leaves(root2)


class SolutionGenerator:
    """Using generator for memory efficiency"""

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leaves(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from leaves(node.left)
                yield from leaves(node.right)

        return list(leaves(root1)) == list(leaves(root2))


class SolutionIterative:
    """Iterative DFS"""

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leaves(root):
            leaves = []
            stack = [root]

            while stack:
                node = stack.pop()
                if node:
                    if not node.left and not node.right:
                        leaves.append(node.val)
                    else:
                        stack.append(node.right)
                        stack.append(node.left)

            return leaves

        return get_leaves(root1) == get_leaves(root2)


class SolutionLazy:
    """Lazy comparison using iterators"""

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        from itertools import zip_longest

        def leaves(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                else:
                    yield from leaves(node.left)
                    yield from leaves(node.right)

        return all(a == b for a, b in zip_longest(leaves(root1), leaves(root2)))
