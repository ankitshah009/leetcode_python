#1325. Delete Leaves With a Given Value
#Medium
#
#Given a binary tree root and an integer target, delete all the leaf nodes with
#value target.
#
#Note that once you delete a leaf node with value target, if its parent node
#becomes a leaf node and has the value target, it should also be deleted (you
#need to continue doing that until you cannot).
#
#Example 1:
#Input: root = [1,2,3,2,null,2,4], target = 2
#Output: [1,null,3,null,4]
#Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).
#After removing, new leaves with value 2 are created (Picture in center).
#
#Example 2:
#Input: root = [1,3,3,3,2], target = 3
#Output: [1,3,null,null,2]
#
#Example 3:
#Input: root = [1,2,null,2,null,2], target = 2
#Output: [1]
#Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 3000].
#    1 <= Node.val <= 1000
#    1 <= target <= 1000

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        Post-order DFS: process children first, then check if current node
        should be removed.
        """
        if not root:
            return None

        # Process children first
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # After processing children, check if this node is now a leaf with target value
        if root.left is None and root.right is None and root.val == target:
            return None

        return root


class SolutionIterative:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """Iterative post-order traversal using stack"""
        if not root:
            return None

        dummy = TreeNode(0)
        dummy.left = root

        stack = [(dummy, False)]
        parent_map = {root: (dummy, 'left')}

        while stack:
            node, visited = stack.pop()

            if visited:
                # Post-order: check if it's a target leaf
                if node.left is None and node.right is None and node.val == target:
                    parent, direction = parent_map[node]
                    if direction == 'left':
                        parent.left = None
                    else:
                        parent.right = None
            else:
                stack.append((node, True))

                if node.right:
                    stack.append((node.right, False))
                    parent_map[node.right] = (node, 'right')

                if node.left:
                    stack.append((node.left, False))
                    parent_map[node.left] = (node, 'left')

        return dummy.left


class SolutionWhileLoop:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """Keep removing until no changes"""
        def remove_once(node):
            if not node:
                return None, False

            left, left_removed = remove_once(node.left)
            right, right_removed = remove_once(node.right)

            node.left = left
            node.right = right

            if left is None and right is None and node.val == target:
                return None, True

            return node, left_removed or right_removed

        # Keep removing until stable
        changed = True
        while changed:
            root, changed = remove_once(root)

        return root
