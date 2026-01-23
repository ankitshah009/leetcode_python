#652. Find Duplicate Subtrees
#Medium
#
#Given the root of a binary tree, return all duplicate subtrees.
#
#For each kind of duplicate subtrees, you only need to return the root node
#of any one of them.
#
#Two trees are duplicate if they have the same structure with the same node values.
#
#Example 1:
#Input: root = [1,2,3,4,null,2,4,null,null,4]
#Output: [[2,4],[4]]
#
#Example 2:
#Input: root = [2,1,1]
#Output: [[1]]
#
#Example 3:
#Input: root = [2,2,2,3,null,3,null]
#Output: [[2,3],[3]]
#
#Constraints:
#    The number of the nodes in the tree will be in the range [1, 5000]
#    -200 <= Node.val <= 200

from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        Serialize each subtree and use hash map to find duplicates.
        """
        count = defaultdict(int)
        result = []

        def serialize(node):
            if not node:
                return "#"

            # Post-order serialization
            left = serialize(node.left)
            right = serialize(node.right)

            subtree = f"{node.val},{left},{right}"

            count[subtree] += 1
            if count[subtree] == 2:
                result.append(node)

            return subtree

        serialize(root)
        return result


class SolutionTupleHash:
    """Use tuple instead of string for potentially better performance"""

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def serialize(node):
            if not node:
                return None

            subtree = (node.val, serialize(node.left), serialize(node.right))

            count[subtree] += 1
            if count[subtree] == 2:
                result.append(node)

            return subtree

        count = defaultdict(int)
        result = []
        serialize(root)
        return result


class SolutionIdMapping:
    """Map subtrees to unique IDs for O(n) complexity"""

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        trees = defaultdict()
        trees.default_factory = trees.__len__
        count = defaultdict(int)
        result = []

        def serialize(node):
            if not node:
                return -1

            uid = trees[(node.val, serialize(node.left), serialize(node.right))]
            count[uid] += 1

            if count[uid] == 2:
                result.append(node)

            return uid

        serialize(root)
        return result
