#138. Copy List with Random Pointer
#Medium
#
#A linked list of length n is given such that each node contains an additional random pointer,
#which could point to any node in the list, or null.
#
#Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
#where each new node has its value set to the value of its corresponding original node.
#
#Example 1:
#Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
#Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#Example 2:
#Input: head = [[1,1],[2,1]]
#Output: [[1,1],[2,1]]
#
#Example 3:
#Input: head = [[3,null],[3,0],[3,null]]
#Output: [[3,null],[3,0],[3,null]]
#
#Constraints:
#    0 <= n <= 1000
#    -10^4 <= Node.val <= 10^4
#    Node.random is null or is pointing to some node in the linked list.

# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Create copy nodes interleaved with original
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Set random pointers for copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Separate the two lists
        dummy = Node(0)
        copy_current = dummy
        current = head

        while current:
            copy_current.next = current.next
            current.next = current.next.next
            copy_current = copy_current.next
            current = current.next

        return dummy.next
