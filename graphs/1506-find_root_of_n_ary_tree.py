#1506. Find Root of N-Ary Tree
#Medium
#
#You are given all the nodes of an N-ary tree as an array of Node objects,
#where each node has a unique value.
#
#Return the root of the N-ary tree.
#
#Custom testing:
#    An N-ary tree can be serialized as represented in its level order traversal
#    where each group of children is separated by the null value.
#
#For example, the above tree is serialized as
#[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].
#
#The testing will be done in the following way:
#    The input data should be provided as a serialization of the tree.
#    The driver code will construct the tree from the serialized input data and
#    put each Node object into an array in an arbitrary order.
#    The driver code will pass the array to findRoot, and your function should
#    find and return the root Node object in the array.
#    The driver code will take the returned Node object and serialize it. If the
#    serialized value and the input data are the same, the test passes.
#
#Example 1:
#Input: tree = [1,null,3,2,4,null,5,6]
#Output: [1,null,3,2,4,null,5,6]
#Explanation: The tree from the input data is shown above.
#
#Example 2:
#Input: tree = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
#Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
#
#Constraints:
#    The total number of nodes is between [1, 5 * 10^4].
#    Each node has a unique value.
#
#Follow up: Could you solve this problem in constant space complexity with a
#linear time algorithm?

from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        """
        XOR approach: root appears once, all others appear twice
        (once as node, once as child).
        XOR of all values XOR values of all children = root's value.
        """
        xor_sum = 0

        for node in tree:
            xor_sum ^= node.val
            for child in node.children:
                xor_sum ^= child.val

        # Find node with this value
        for node in tree:
            if node.val == xor_sum:
                return node

        return None


class SolutionSet:
    def findRoot(self, tree: List['Node']) -> 'Node':
        """
        Use set: collect all children, root is the only node not in children set.
        O(n) time, O(n) space.
        """
        children = set()

        for node in tree:
            for child in node.children:
                children.add(child)

        for node in tree:
            if node not in children:
                return node

        return None


class SolutionSum:
    def findRoot(self, tree: List['Node']) -> 'Node':
        """
        Sum approach: sum of all node values - sum of all child values = root value.
        """
        total_sum = 0
        child_sum = 0

        for node in tree:
            total_sum += node.val
            for child in node.children:
                child_sum += child.val

        root_val = total_sum - child_sum

        for node in tree:
            if node.val == root_val:
                return node

        return None


class SolutionInDegree:
    def findRoot(self, tree: List['Node']) -> 'Node':
        """
        Root has in-degree 0 (no parent pointing to it).
        """
        from collections import defaultdict

        # Count in-degrees
        in_degree = defaultdict(int)

        for node in tree:
            if node not in in_degree:
                in_degree[node] = 0
            for child in node.children:
                in_degree[child] += 1

        # Find node with in-degree 0
        for node in tree:
            if in_degree[node] == 0:
                return node

        return None


class SolutionConstantSpace:
    def findRoot(self, tree: List['Node']) -> 'Node':
        """
        Follow-up: O(1) space using XOR.
        Every node except root appears exactly twice when considering:
        1. As a node in the tree list
        2. As a child of some parent
        XOR all these, only root's value remains.
        """
        xor_result = 0

        for node in tree:
            # XOR this node's value
            xor_result ^= node.val
            # XOR all children's values
            for child in node.children:
                xor_result ^= child.val

        # Now xor_result = root's value
        for node in tree:
            if node.val == xor_result:
                return node

        return None
