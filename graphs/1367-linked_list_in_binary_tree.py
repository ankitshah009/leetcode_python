#1367. Linked List in Binary Tree
#Medium
#
#Given a binary tree root and a linked list with head as the first node.
#
#Return True if all the elements in the linked list starting from the head
#correspond to some downward path connected in the binary tree otherwise
#return False.
#
#In this context downward path means a path that starts at some node and goes
#downwards.
#
#Example 1:
#Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
#Output: true
#Explanation: Nodes in blue form a subpath in the binary tree.
#
#Example 2:
#Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
#Output: true
#
#Example 3:
#Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
#Output: false
#Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
#
#Constraints:
#    The number of nodes in the tree will be in the range [1, 2500].
#    The number of nodes in the list will be in the range [1, 100].
#    1 <= Node.val <= 100 for each node in the linked list and binary tree.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        For each tree node, check if linked list matches starting from there.
        """
        def matches(list_node, tree_node):
            """Check if list starting at list_node matches path from tree_node"""
            if not list_node:
                return True
            if not tree_node:
                return False
            if list_node.val != tree_node.val:
                return False
            return matches(list_node.next, tree_node.left) or matches(list_node.next, tree_node.right)

        def dfs(tree_node):
            """Try starting match from each tree node"""
            if not tree_node:
                return False
            if matches(head, tree_node):
                return True
            return dfs(tree_node.left) or dfs(tree_node.right)

        return dfs(root)


class SolutionKMP:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        KMP-style approach for efficiency with long lists.
        Build failure function for linked list pattern.
        """
        # Build pattern array and failure function
        pattern = []
        node = head
        while node:
            pattern.append(node.val)
            node = node.next

        m = len(pattern)
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = fail[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            fail[i] = j

        # DFS with pattern matching
        def dfs(tree_node, j):
            if not tree_node:
                return False

            while j > 0 and tree_node.val != pattern[j]:
                j = fail[j - 1]

            if tree_node.val == pattern[j]:
                j += 1

            if j == m:
                return True

            return dfs(tree_node.left, j) or dfs(tree_node.right, j)

        return dfs(root, 0)
