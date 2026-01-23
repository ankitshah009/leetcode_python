#82. Remove Duplicates from Sorted List II
#Medium
#
#Given the head of a sorted linked list, delete all nodes that have duplicate
#numbers, leaving only distinct numbers from the original list. Return the linked
#list sorted as well.
#
#Example 1:
#Input: head = [1,2,3,3,4,4,5]
#Output: [1,2,5]
#
#Example 2:
#Input: head = [1,1,1,2,3]
#Output: [2,3]
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
        Sentinel node approach - handles edge cases cleanly.
        """
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            # Check if current node is start of duplicates
            if head.next and head.val == head.next.val:
                # Skip all nodes with same value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip the last duplicate
                prev.next = head.next
            else:
                prev = prev.next

            head = head.next

        return dummy.next


class SolutionRecursive:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach.
        """
        if not head or not head.next:
            return head

        if head.val == head.next.val:
            # Skip all nodes with same value
            while head.next and head.val == head.next.val:
                head = head.next
            # Recurse from next distinct value
            return self.deleteDuplicates(head.next)
        else:
            # Keep current node, recurse on rest
            head.next = self.deleteDuplicates(head.next)
            return head


class SolutionTwoPointers:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Two pointers without dummy node.
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head

        while fast:
            # Check if fast is a duplicate
            if fast.next and fast.val == fast.next.val:
                # Find end of duplicates
                dup_val = fast.val
                while fast and fast.val == dup_val:
                    fast = fast.next
                slow.next = fast
            else:
                slow = slow.next
                fast = fast.next

        return dummy.next
