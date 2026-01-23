#83. Remove Duplicates from Sorted List
#Easy
#
#Given the head of a sorted linked list, delete all duplicates such that each
#element appears only once. Return the linked list sorted as well.
#
#Example 1:
#Input: head = [1,1,2]
#Output: [1,2]
#
#Example 2:
#Input: head = [1,1,2,3,3]
#Output: [1,2,3]
#
#Constraints:
#    The number of nodes in the list is in the range [0, 300].
#    -100 <= Node.val <= 100
#    The list is guaranteed to be sorted in ascending order.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Simple iteration - skip duplicate nodes.
        """
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


class SolutionRecursive:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach.
        """
        if not head or not head.next:
            return head

        head.next = self.deleteDuplicates(head.next)

        return head.next if head.val == head.next.val else head


class SolutionTwoPointers:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Two pointers - slow for result, fast for scanning.
        """
        if not head:
            return head

        slow = head
        fast = head.next

        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next

        slow.next = None
        return head
