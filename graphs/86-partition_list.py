#86. Partition List
#Medium
#
#Given the head of a linked list and a value x, partition it such that all nodes
#less than x come before nodes greater than or equal to x.
#
#You should preserve the original relative order of the nodes in each of the two
#partitions.
#
#Example 1:
#Input: head = [1,4,3,2,5,2], x = 3
#Output: [1,2,2,4,3,5]
#
#Example 2:
#Input: head = [2,1], x = 2
#Output: [1,2]
#
#Constraints:
#    The number of nodes in the list is in the range [0, 200].
#    -100 <= Node.val <= 100
#    -200 <= x <= 200

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Two dummy nodes - separate into two lists, then merge.
        """
        # Create two dummy heads
        before_head = ListNode(0)
        after_head = ListNode(0)

        before = before_head
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        # Connect the two lists
        after.next = None  # Important: avoid cycle
        before.next = after_head.next

        return before_head.next


class SolutionInPlace:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        In-place approach with dummy node.
        """
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        # Find last node < x
        last_smaller = None
        temp = dummy
        while temp.next:
            if temp.next.val < x:
                last_smaller = temp
            temp = temp.next

        if last_smaller is None:
            return head

        # Move nodes < x after last_smaller
        prev = dummy
        curr = head

        while curr:
            if curr.val < x and prev != last_smaller:
                # Move curr after last_smaller
                prev.next = curr.next
                curr.next = last_smaller.next
                last_smaller.next = curr
                last_smaller = curr
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return dummy.next


class SolutionSimple:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Collect values, rebuild list.
        """
        if not head:
            return head

        less = []
        greater_or_equal = []

        curr = head
        while curr:
            if curr.val < x:
                less.append(curr.val)
            else:
                greater_or_equal.append(curr.val)
            curr = curr.next

        # Rebuild list
        values = less + greater_or_equal
        dummy = ListNode(0)
        curr = dummy

        for val in values:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
