#1666. Change the Root of a Binary Tree
#Medium
#
#Given the root of a binary tree and a leaf node, reroot the tree so that the
#leaf is the new root.
#
#You can reroot the tree with the following steps for each node cur on the path
#starting from the leaf up to the root excluding the root:
#1. If cur has a left child, then that child becomes cur's right child.
#2. cur's original parent becomes cur's left child. Note: In this step, the
#   original parent's pointer to cur becomes null, making it have at most one child.
#3. cur's original parent's original parent becomes cur's parent.
#
#Return the new root of the rerooted tree.
#
#Note: Ensure that your solution sets the Node.parent pointers correctly after
#rerooting or you will receive "Wrong Answer".
#
#Example 1:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 7
#Output: [7,2,null,5,4,3,6,null,null,1,null,0,8]
#
#Example 2:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 0
#Output: [0,1,null,3,8,5,null,6,2,null,null,7,4]
#
#Constraints:
#    The number of nodes in the tree is in the range [2, 100].
#    -10^9 <= Node.val <= 10^9
#    All Node.val are unique.
#    leaf exists in the tree.

class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        """
        Walk from leaf to root, flipping parent-child relationships.
        """
        current = leaf
        prev = None

        while current:
            # Save the original parent
            original_parent = current.parent

            # Update parent pointer
            current.parent = prev

            # Move left child to right
            if current.left:
                current.right = current.left

            # Original parent becomes left child
            current.left = original_parent

            # Detach from original parent
            if original_parent:
                if original_parent.left == current:
                    original_parent.left = None
                else:
                    original_parent.right = None

            # Move up
            prev = current
            current = original_parent

        return leaf


class SolutionIterative:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        """
        Iterative approach with explicit tracking.
        """
        # Build path from leaf to root
        path = []
        node = leaf
        while node:
            path.append(node)
            node = node.parent

        # Flip relationships along the path
        for i in range(len(path) - 1):
            child = path[i]
            parent = path[i + 1]

            # Child's left moves to right
            if child.left:
                child.right = child.left

            # Parent becomes child's left
            child.left = parent

            # Detach child from parent's children
            if parent.left == child:
                parent.left = None
            else:
                parent.right = None

            # Update parent pointer
            child.parent = path[i - 1] if i > 0 else None

        # Root node's parent becomes None
        path[-1].parent = path[-2] if len(path) > 1 else None

        return leaf


class SolutionRecursive:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        """
        Recursive approach.
        """
        def flip(node: 'Node', new_parent: 'Node') -> None:
            if not node:
                return

            original_parent = node.parent

            # Update current node's parent
            node.parent = new_parent

            # Move left to right
            if node.left:
                node.right = node.left

            # Make original parent the new left child
            if original_parent:
                # Detach from original parent first
                if original_parent.left == node:
                    original_parent.left = None
                else:
                    original_parent.right = None

                node.left = original_parent

                # Recursively flip the original parent
                flip(original_parent, node)
            else:
                node.left = None

        flip(leaf, None)
        return leaf


class SolutionClean:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        """
        Clean implementation following the problem's steps exactly.
        """
        cur = leaf

        while cur.parent:
            parent = cur.parent

            # Step 1: If cur has a left child, it becomes cur's right child
            if cur.left:
                cur.right = cur.left

            # Step 2: Original parent becomes cur's left child
            cur.left = parent

            # Detach cur from parent
            if parent.left == cur:
                parent.left = None
            elif parent.right == cur:
                parent.right = None

            # Step 3: Grandparent becomes cur's parent
            grandparent = parent.parent
            cur.parent = None  # Temporary

            # Update parent's pointer
            parent.parent = cur

            # Move up
            cur = parent
            cur.parent = grandparent if grandparent else None

        # Fix the final parent pointers
        self._fix_parents(leaf, None)
        return leaf

    def _fix_parents(self, node: 'Node', parent: 'Node') -> None:
        if not node:
            return
        node.parent = parent
        self._fix_parents(node.left, node)
        self._fix_parents(node.right, node)
