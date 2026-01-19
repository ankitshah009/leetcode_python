#572. Subtree of Another Tree
#Easy
#
#Given the roots of two binary trees root and subRoot, return true if there is a
#subtree of root with the same structure and node values of subRoot and false otherwise.
#
#A subtree of a binary tree tree is a tree that consists of a node in tree and all
#of this node's descendants.
#
#Example 1:
#Input: root = [3,4,5,1,2], subRoot = [4,1,2]
#Output: true
#
#Example 2:
#Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
#Output: false
#
#Constraints:
#    The number of nodes in the root tree is in the range [1, 2000].
#    The number of nodes in the subRoot tree is in the range [1, 1000].
#    -10^4 <= root.val <= 10^4
#    -10^4 <= subRoot.val <= 10^4

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Check if subRoot is a subtree of root"""
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class SolutionSerialization:
    """Using tree serialization and string matching"""

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "#"
            return f"^{node.val}^{serialize(node.left)}^{serialize(node.right)}"

        return serialize(subRoot) in serialize(root)


class SolutionMerkle:
    """Using Merkle hashing for O(n+m) comparison"""

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def get_hash(node):
            if not node:
                return hash(None)
            return hash((node.val, get_hash(node.left), get_hash(node.right)))

        def check(node, target_hash, subRoot):
            if not node:
                return False
            if get_hash(node) == target_hash:
                if self.isSameTree(node, subRoot):
                    return True
            return check(node.left, target_hash, subRoot) or check(node.right, target_hash, subRoot)

        return check(root, get_hash(subRoot), subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
