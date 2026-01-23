#25. Reverse Nodes in k-Group
#Hard
#
#Given the head of a linked list, reverse the nodes of the list k at a time, and
#return the modified list.
#
#k is a positive integer and is less than or equal to the length of the linked
#list. If the number of nodes is not a multiple of k then left-out nodes, in the
#end, should remain as it is.
#
#You may not alter the values in the list's nodes, only nodes themselves may be
#changed.
#
#Example 1:
#Input: head = [1,2,3,4,5], k = 2
#Output: [2,1,4,3,5]
#
#Example 2:
#Input: head = [1,2,3,4,5], k = 3
#Output: [3,2,1,4,5]
#
#Constraints:
#    The number of nodes in the list is n.
#    1 <= k <= n <= 5000
#    0 <= Node.val <= 1000
#
#Follow-up: Can you solve the problem in O(1) extra memory space?

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Iterative approach - reverse k nodes at a time.
        """
        def reverse_linked_list(head: ListNode, k: int) -> ListNode:
            prev = None
            curr = head

            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1

            return prev

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # Save the start of next group
            group_next = kth.next

            # Reverse the group
            prev, curr = kth.next, group_prev.next

            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Connect with previous part
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next


class SolutionRecursive:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Recursive approach.
        """
        # Check if we have k nodes
        count = 0
        curr = head

        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head

        # Reverse k nodes
        prev = self.reverseKGroup(curr, k)
        curr = head

        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev


class SolutionStack:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Using stack for reversal.
        """
        dummy = ListNode(0, head)
        prev = dummy
        stack = []

        while head:
            # Fill stack with k nodes
            count = 0
            while head and count < k:
                stack.append(head)
                head = head.next
                count += 1

            if count == k:
                # Reverse by popping from stack
                while stack:
                    prev.next = stack.pop()
                    prev = prev.next
                prev.next = head
            else:
                # Not enough nodes, keep original order
                prev.next = stack[0]

        return dummy.next
