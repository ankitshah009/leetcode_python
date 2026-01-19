#117. Populating Next Right Pointers in Each Node II
#Medium
#
#Given a binary tree, populate each next pointer to point to its next right node. If there
#is no next right node, the next pointer should be set to NULL.
#
#Example 1:
#Input: root = [1,2,3,4,5,null,7]
#Output: [1,#,2,3,#,4,5,7,#]
#
#Example 2:
#Input: root = []
#Output: []
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 6000].
#    -100 <= Node.val <= 100

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

        current = root
        dummy = Node(0)

        while current:
            tail = dummy
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                current = current.next

            current = dummy.next
            dummy.next = None

        return root
