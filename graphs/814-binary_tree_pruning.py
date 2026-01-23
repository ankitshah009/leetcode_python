#814. Binary Tree Pruning
#Medium
#
#Given the root of a binary tree, return the same tree where every subtree
#(of the given tree) not containing a 1 has been removed.
#
#A subtree of a node node is node plus every node that is a descendant of node.
#
#Example 1:
#Input: root = [1,null,0,0,1]
#Output: [1,null,0,null,1]
#
#Example 2:
#Input: root = [1,0,1,0,0,0,1]
#Output: [1,null,1,null,1]
#
#Example 3:
#Input: root = [1,1,0,1,1,0,1,0]
#Output: [1,1,0,1,1,null,1]
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 200].
#    Node.val is either 0 or 1.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        """
        Post-order traversal: prune children first, then decide if node should be removed.
        """
        def contains_one(node):
            if not node:
                return False

            # Recursively prune left and right
            left_has_one = contains_one(node.left)
            right_has_one = contains_one(node.right)

            # Remove children that don't contain 1
            if not left_has_one:
                node.left = None
            if not right_has_one:
                node.right = None

            # This node is kept if it's 1 or has a child with 1
            return node.val == 1 or left_has_one or right_has_one

        return root if contains_one(root) else None


class SolutionReturn:
    """Return pruned subtree directly"""

    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # Remove this node if it's 0 and has no children
        if root.val == 0 and not root.left and not root.right:
            return None

        return root


class SolutionIterative:
    """Iterative post-order with parent tracking"""

    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # Use dummy node as parent of root
        dummy = TreeNode(1)
        dummy.left = root

        stack = [(root, dummy, 'left', False)]

        while stack:
            node, parent, direction, visited = stack.pop()

            if visited:
                # Check if subtree contains 1
                has_one = (node.val == 1 or
                          node.left is not None or
                          node.right is not None)
                if not has_one:
                    if direction == 'left':
                        parent.left = None
                    else:
                        parent.right = None
            else:
                stack.append((node, parent, direction, True))
                if node.right:
                    stack.append((node.right, node, 'right', False))
                if node.left:
                    stack.append((node.left, node, 'left', False))

        return dummy.left
