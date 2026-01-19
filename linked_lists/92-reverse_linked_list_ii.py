#92. Reverse Linked List II
#Medium
#
#Given the head of a singly linked list and two integers left and right where left <= right,
#reverse the nodes of the list from position left to position right, and return the reversed list.
#
#Example 1:
#Input: head = [1,2,3,4,5], left = 2, right = 4
#Output: [1,4,3,2,5]
#
#Example 2:
#Input: head = [5], left = 1, right = 1
#Output: [5]
#
#Constraints:
#    The number of nodes in the list is n.
#    1 <= n <= 500
#    -500 <= Node.val <= 500
#    1 <= left <= right <= n

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move to position before left
        for _ in range(left - 1):
            prev = prev.next

        # Reverse from left to right
        current = prev.next
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
