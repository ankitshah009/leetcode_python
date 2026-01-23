#1028. Recover a Tree From Preorder Traversal
#Hard
#
#We run a preorder depth-first search (DFS) on the root of a binary tree.
#
#At each node in this traversal, we output D dashes (where D is the depth of
#this node), then we output the value of this node. If the depth of a node
#is D, the depth of its immediate child is D + 1. The depth of the root
#node is 0.
#
#If a node has only one child, that child is guaranteed to be the left child.
#
#Given the output traversal of this traversal, recover the tree and return
#its root.
#
#Example 1:
#Input: traversal = "1-2--3--4-5--6--7"
#Output: [1,2,5,3,4,6,7]
#
#Example 2:
#Input: traversal = "1-2--3---4-5--6---7"
#Output: [1,2,5,3,null,6,null,4,null,7]
#
#Example 3:
#Input: traversal = "1-401--349---90--88"
#Output: [1,401,null,349,88,90]
#
#Constraints:
#    The number of nodes in the original tree is in the range [1, 1000].
#    1 <= Node.val <= 10^9

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """
        Use stack to track path from root to current node.
        Stack depth indicates expected depth for next node.
        """
        stack = []
        i = 0
        n = len(traversal)

        while i < n:
            # Count dashes (depth)
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1

            # Parse number
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1

            node = TreeNode(val)

            # Pop stack until we find parent at depth-1
            while len(stack) > depth:
                stack.pop()

            # Attach to parent
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            stack.append(node)

        return stack[0] if stack else None


class SolutionRecursive:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """Recursive approach with index tracking"""
        self.i = 0

        def build(depth):
            if self.i >= len(traversal):
                return None

            # Count dashes at current position
            dashes = 0
            j = self.i
            while j < len(traversal) and traversal[j] == '-':
                dashes += 1
                j += 1

            if dashes != depth:
                return None

            # Move past dashes
            self.i = j

            # Parse number
            val = 0
            while self.i < len(traversal) and traversal[self.i].isdigit():
                val = val * 10 + int(traversal[self.i])
                self.i += 1

            node = TreeNode(val)
            node.left = build(depth + 1)
            node.right = build(depth + 1)

            return node

        return build(0)
