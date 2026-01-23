#24. Swap Nodes in Pairs
#Medium
#
#Given a linked list, swap every two adjacent nodes and return its head. You must
#solve the problem without modifying the values in the list's nodes (i.e., only
#nodes themselves may be changed.)
#
#Example 1:
#Input: head = [1,2,3,4]
#Output: [2,1,4,3]
#
#Example 2:
#Input: head = []
#Output: []
#
#Example 3:
#Input: head = [1]
#Output: [1]
#
#Example 4:
#Input: head = [1,2,3]
#Output: [2,1,3]
#
#Constraints:
#    The number of nodes in the list is in the range [0, 100].
#    0 <= Node.val <= 100

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative approach with dummy head.
        """
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            # Nodes to swap
            first = prev.next
            second = first.next

            # Perform swap
            prev.next = second
            first.next = second.next
            second.next = first

            # Move to next pair
            prev = first

        return dummy.next


class SolutionRecursive:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach.
        """
        if not head or not head.next:
            return head

        # Nodes to swap
        first = head
        second = head.next

        # Swap and recursively handle remaining
        first.next = self.swapPairs(second.next)
        second.next = first

        return second


class SolutionPointers:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Alternative pointer manipulation.
        """
        if not head or not head.next:
            return head

        # New head will be the second node
        new_head = head.next
        prev = None

        while head and head.next:
            first = head
            second = head.next
            third = second.next

            # Swap
            second.next = first
            first.next = third

            # Connect with previous pair
            if prev:
                prev.next = second

            # Move forward
            prev = first
            head = third

        return new_head
