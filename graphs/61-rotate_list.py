#61. Rotate List
#Medium
#
#Given the head of a linked list, rotate the list to the right by k places.
#
#Example 1:
#Input: head = [1,2,3,4,5], k = 2
#Output: [4,5,1,2,3]
#
#Example 2:
#Input: head = [0,1,2], k = 4
#Output: [2,0,1]
#
#Constraints:
#    The number of nodes in the list is in the range [0, 500].
#    -100 <= Node.val <= 100
#    0 <= k <= 2 * 10^9

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Connect tail to head, then break at appropriate position.
        """
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Normalize k
        k = k % length
        if k == 0:
            return head

        # Make circular
        tail.next = head

        # Find new tail (length - k - 1 steps from head)
        steps = length - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next

        # Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head


class SolutionTwoPass:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Two pass approach - find length first.
        """
        if not head or not head.next:
            return head

        # First pass: count length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        k = k % length
        if k == 0:
            return head

        # Second pass: find new tail
        slow = fast = head

        # Move fast k steps ahead
        for _ in range(k):
            fast = fast.next

        # Move both until fast reaches end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Rotate
        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head
