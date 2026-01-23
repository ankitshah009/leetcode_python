#1650. Lowest Common Ancestor of a Binary Tree III
#Medium
#
#Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
#
#Each node will have a reference to its parent node. The definition for Node is below:
#
#class Node {
#    public int val;
#    public Node left;
#    public Node right;
#    public Node parent;
#}
#
#According to the definition of LCA: "The lowest common ancestor of two nodes
#p and q in a tree T is the lowest node that has both p and q as descendants
#(where we allow a node to be a descendant of itself)."
#
#Example 1:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#Output: 3
#Explanation: The LCA of nodes 5 and 1 is 3.
#
#Example 2:
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
#Output: 5
#Explanation: The LCA of nodes 5 and 4 is 5.
#
#Example 3:
#Input: root = [1,2], p = 1, q = 2
#Output: 1
#
#Constraints:
#    The number of nodes in the tree is in the range [2, 10^5].
#    -10^9 <= Node.val <= 10^9
#    All Node.val are unique.
#    p != q
#    p and q exist in the tree.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Use two pointers like finding intersection of two linked lists.
        When one reaches root, switch to the other node.
        They will meet at LCA.
        """
        a, b = p, q

        while a != b:
            a = a.parent if a.parent else q
            b = b.parent if b.parent else p

        return a


class SolutionSet:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Track ancestors of p, find first common ancestor with q.
        """
        ancestors = set()

        # Add all ancestors of p
        node = p
        while node:
            ancestors.add(node)
            node = node.parent

        # Find first ancestor of q that's in the set
        node = q
        while node:
            if node in ancestors:
                return node
            node = node.parent

        return None


class SolutionDepth:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Find depths, bring to same level, then move up together.
        """
        def get_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.parent
            return depth

        depth_p = get_depth(p)
        depth_q = get_depth(q)

        # Bring to same level
        while depth_p > depth_q:
            p = p.parent
            depth_p -= 1

        while depth_q > depth_p:
            q = q.parent
            depth_q -= 1

        # Move up together until meeting
        while p != q:
            p = p.parent
            q = q.parent

        return p


class SolutionList:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Build path to root for both, find last common node.
        """
        def path_to_root(node):
            path = []
            while node:
                path.append(node)
                node = node.parent
            return path[::-1]  # Root to node

        path_p = path_to_root(p)
        path_q = path_to_root(q)

        lca = None
        for a, b in zip(path_p, path_q):
            if a == b:
                lca = a
            else:
                break

        return lca
