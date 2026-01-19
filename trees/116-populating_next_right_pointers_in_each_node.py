#116. Populating Next Right Pointers in Each Node
#Medium
#
#You are given a perfect binary tree where all leaves are on the same level, and every parent
#has two children. Populate each next pointer to point to its next right node. If there is
#no next right node, the next pointer should be set to NULL.
#
#Example 1:
#Input: root = [1,2,3,4,5,6,7]
#Output: [1,#,2,3,#,4,5,6,7,#]
#Explanation: Given the above perfect binary tree, your function should populate each next
#pointer to point to its next right node.
#
#Example 2:
#Input: root = []
#Output: []
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 2^12 - 1].
#    -1000 <= Node.val <= 1000

# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:
                # Connection 1: left child to right child
                head.left.next = head.right

                # Connection 2: right child to next's left child
                if head.next:
                    head.right.next = head.next.left

                head = head.next

            leftmost = leftmost.left

        return root
