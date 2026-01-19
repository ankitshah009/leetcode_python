#143. Reorder List
#Medium
#
#You are given the head of a singly linked-list. The list can be represented as:
#L0 → L1 → … → Ln - 1 → Ln
#
#Reorder the list to be on the following form:
#L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
#You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#
#Example 1:
#Input: head = [1,2,3,4]
#Output: [1,4,2,3]
#
#Example 2:
#Input: head = [1,2,3,4,5]
#Output: [1,5,2,4,3]
#
#Constraints:
#    The number of nodes in the list is in the range [1, 5 * 10^4].
#    1 <= Node.val <= 1000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        current = slow.next
        slow.next = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Merge two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
