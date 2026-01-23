#19. Remove Nth Node From End of List
#Medium
#
#Given the head of a linked list, remove the nth node from the end of the list
#and return its head.
#
#Example 1:
#Input: head = [1,2,3,4,5], n = 2
#Output: [1,2,3,5]
#
#Example 2:
#Input: head = [1], n = 1
#Output: []
#
#Example 3:
#Input: head = [1,2], n = 1
#Output: [1]
#
#Constraints:
#    The number of nodes in the list is sz.
#    1 <= sz <= 30
#    0 <= Node.val <= 100
#    1 <= n <= sz
#
#Follow up: Could you do this in one pass?

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Two pointers - one pass solution.
        Fast pointer is n steps ahead of slow pointer.
        """
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the nth node
        slow.next = slow.next.next

        return dummy.next


class SolutionTwoPass:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Two pass solution - count length first.
        """
        dummy = ListNode(0, head)

        # First pass: count length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Find node before the one to remove
        steps = length - n
        curr = dummy

        for _ in range(steps):
            curr = curr.next

        # Remove node
        curr.next = curr.next.next

        return dummy.next


class SolutionRecursive:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Recursive solution with counter.
        """
        def helper(node: Optional[ListNode]) -> int:
            if not node:
                return 0

            count = helper(node.next) + 1

            if count == n + 1:
                node.next = node.next.next

            return count

        dummy = ListNode(0, head)
        helper(dummy)

        return dummy.next


class SolutionStack:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Using stack to track nodes.
        """
        dummy = ListNode(0, head)
        stack = []
        curr = dummy

        while curr:
            stack.append(curr)
            curr = curr.next

        # Pop n nodes to get to the predecessor
        for _ in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next

        return dummy.next
