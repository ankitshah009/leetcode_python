#1721. Swapping Nodes in a Linked List
#Medium
#
#You are given the head of a linked list, and an integer k.
#
#Return the head of the linked list after swapping the values of the kth node
#from the beginning and the kth node from the end (the list is 1-indexed).
#
#Example 1:
#Input: head = [1,2,3,4,5], k = 2
#Output: [1,4,3,2,5]
#
#Example 2:
#Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
#Output: [7,9,6,6,8,7,3,0,9,5]
#
#Constraints:
#    The number of nodes in the list is n.
#    1 <= k <= n <= 10^5
#    0 <= Node.val <= 100

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Two pointers - find kth from start and kth from end.
        """
        # Find kth node from start
        first = head
        for _ in range(k - 1):
            first = first.next

        # Find kth node from end using two pointers
        slow = head
        fast = first

        while fast.next:
            slow = slow.next
            fast = fast.next

        second = slow

        # Swap values
        first.val, second.val = second.val, first.val

        return head


class SolutionTwoPass:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Two pass approach - find length first.
        """
        # First pass: find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Find kth from start
        first = head
        for _ in range(k - 1):
            first = first.next

        # Find kth from end (which is (length - k + 1)th from start)
        second = head
        for _ in range(length - k):
            second = second.next

        # Swap values
        first.val, second.val = second.val, first.val

        return head


class SolutionList:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Convert to list, swap, convert back (uses O(n) space).
        """
        # Collect all nodes
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        n = len(nodes)

        # Swap values of kth from start and kth from end
        nodes[k - 1].val, nodes[n - k].val = nodes[n - k].val, nodes[k - 1].val

        return head
