#92. Reverse Linked List II
#Medium
#
#Given the head of a singly linked list and two integers left and right where
#left <= right, reverse the nodes of the list from position left to position
#right, and return the reversed list.
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

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        One pass with pointer manipulation.
        """
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # Move to node before left position
        for _ in range(left - 1):
            prev = prev.next

        # Start of reversal section
        curr = prev.next

        # Reverse from left to right
        for _ in range(right - left):
            # Move next node to front of reversed section
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next


class SolutionIterative:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Standard reversal with explicit start/end tracking.
        """
        if not head or left == right:
            return head

        dummy = ListNode(0, head)

        # Find position before left
        pre_left = dummy
        for _ in range(left - 1):
            pre_left = pre_left.next

        # Standard reversal
        prev = None
        curr = pre_left.next

        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Connect reversed section
        pre_left.next.next = curr  # Connect end of reversed to rest
        pre_left.next = prev  # Connect pre_left to new head

        return dummy.next


class SolutionRecursive:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Recursive approach.
        """
        if left == 1:
            return self.reverseN(head, right)

        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Reverse first n nodes."""
        if n == 1:
            return head

        new_head = self.reverseN(head.next, n - 1)
        successor = head.next.next
        head.next.next = head
        head.next = successor
        return new_head


class SolutionStack:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Using stack (more space, clearer logic).
        """
        dummy = ListNode(0, head)
        stack = []

        # Find position before left
        pre_left = dummy
        for _ in range(left - 1):
            pre_left = pre_left.next

        # Push nodes to stack
        curr = pre_left.next
        for _ in range(right - left + 1):
            stack.append(curr)
            curr = curr.next

        # Rebuild reversed section
        post_right = curr
        while stack:
            pre_left.next = stack.pop()
            pre_left = pre_left.next

        pre_left.next = post_right
        return dummy.next
