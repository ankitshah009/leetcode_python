#1516. Move Sub-Tree of N-Ary Tree
#Hard
#
#Given the root of an N-ary tree of unique values, and two nodes of the tree p
#and q.
#
#You should move the subtree of the node p to become a direct child of node q.
#If p is already a direct child of q, do not change anything. Node q must be
#inside the subtree of node p. Also, keep the original order of children of
#each node. If the node p is the root and has no sibling, q becomes the new
#root of the tree.
#
#Return the root of the tree after adjusting it to the mentioned conditions.
#
#There are 3 cases for nodes p and q:
#    Node q is in the sub-tree of node p.
#    Node p is in the sub-tree of node q.
#    Neither node p is in the sub-tree of node q nor node q is in the sub-tree
#    of node p.
#
#Notice that in all cases, the initial tree is valid (nodes have unique values
#and each node has at most one parent).
#
#Example 1:
#Input: root = [1,null,2,3,null,4,5,null,6,null,7,8], p = 4, q = 1
#Output: [1,null,2,3,4,null,5,null,6,null,7,8]
#
#Example 2:
#Input: root = [1,null,2,3,null,4,5,null,6,null,7,8], p = 7, q = 4
#Output: [1,null,2,3,null,4,5,null,6,7,null,8]
#
#Example 3:
#Input: root = [1,null,2,3,null,4,5,null,6,null,7,8], p = 3, q = 8
#Output: [1,null,2,null,4,5,null,6,null,7,8,null,null,null,3]
#
#Constraints:
#    The total number of nodes is between [2, 1000].
#    Each node has a unique value.
#    p != null
#    q != null
#    p and q are two different nodes (i.e. p != q).

from typing import Optional, List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        """
        Cases:
        1. p is already a direct child of q -> do nothing
        2. q is in p's subtree -> move q's parent to be p's parent, then p under q
        3. q is not in p's subtree -> simply move p under q
        """
        # Find parents of p and q
        parent_p = None
        parent_q = None

        def find_parents(node: 'Node', parent: 'Node') -> None:
            nonlocal parent_p, parent_q
            if node == p:
                parent_p = parent
            if node == q:
                parent_q = parent
            for child in node.children:
                find_parents(child, node)

        find_parents(root, None)

        # Case 1: p is already direct child of q
        if parent_p == q:
            return root

        # Check if q is in p's subtree
        def is_in_subtree(ancestor: 'Node', target: 'Node') -> bool:
            if ancestor == target:
                return True
            for child in ancestor.children:
                if is_in_subtree(child, target):
                    return True
            return False

        q_in_p_subtree = is_in_subtree(p, q)

        if q_in_p_subtree:
            # Case 2: q is in p's subtree
            # First, remove q from its parent's children
            parent_q.children.remove(q)

            # Replace q with p's children (q was in p's subtree)
            # Actually, we need to move p under q, so:
            # 1. Remove p from its parent
            # 2. Make p a child of q
            # 3. If q was under p, q's original children stay, p moves to be q's child

            if parent_p is None:
                # p is root
                # q becomes new root
                q.children.append(p)
                return q
            else:
                parent_p.children.remove(p)
                q.children.append(p)
                return root
        else:
            # Case 3: q is not in p's subtree
            # Simply remove p from parent and add to q
            if parent_p is None:
                # p is root, q becomes new root with p as child
                q.children.append(p)
                return q
            else:
                parent_p.children.remove(p)
                q.children.append(p)
                return root


class SolutionCleaner:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        """
        Cleaner implementation with helper functions.
        """
        # Build parent map
        parent = {root: None}

        def build_parent_map(node: 'Node') -> None:
            for child in node.children:
                parent[child] = node
                build_parent_map(child)

        build_parent_map(root)

        # Check if p is already child of q
        if parent[p] == q:
            return root

        # Check if q is descendant of p
        def is_descendant(ancestor: 'Node', node: 'Node') -> bool:
            current = node
            while current:
                if current == ancestor:
                    return True
                current = parent.get(current)
            return False

        q_under_p = is_descendant(p, q)

        # Remove p from its parent
        if parent[p]:
            parent[p].children.remove(p)

        if q_under_p:
            # Remove q from its parent and place p's position
            parent[q].children.remove(q)

            if parent[p]:
                # p had a parent, q takes p's old spot relative to tree structure
                pass  # q is already removed from its position

        # Add p as child of q
        q.children.append(p)

        # Determine new root
        if parent[p] is None:
            # p was root
            if q_under_p:
                return q
            else:
                return q  # q becomes new root since we moved root under it
        else:
            return root
