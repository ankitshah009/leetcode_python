#328. Odd Even Linked List
#Medium
#
#Given the head of a singly linked list, group all the nodes with odd indices
#together followed by the nodes with even indices, and return the reordered
#list.
#
#The first node is considered odd, and the second node is even, and so on.
#
#Note that the relative order inside both the even and odd groups should remain
#as it was in the input.
#
#You must solve the problem in O(1) extra space complexity and O(n) time
#complexity.
#
#Example 1:
#Input: head = [1,2,3,4,5]
#Output: [1,3,5,2,4]
#
#Example 2:
#Input: head = [2,1,3,5,6,4,7]
#Output: [2,3,6,7,1,5,4]
#
#Constraints:
#    The number of nodes in the linked list is in the range [0, 10^4].
#    -10^6 <= Node.val <= 10^6

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Two pointers for odd and even lists"""
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even  # Save start of even list

        while even and even.next:
            odd.next = even.next  # Connect odd to next odd
            odd = odd.next

            even.next = odd.next  # Connect even to next even
            even = even.next

        odd.next = even_head  # Connect odd list to even list

        return head


class SolutionDummy:
    """Using dummy nodes"""

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd_dummy = ListNode(0)
        even_dummy = ListNode(0)
        odd_tail = odd_dummy
        even_tail = even_dummy

        current = head
        is_odd = True

        while current:
            if is_odd:
                odd_tail.next = current
                odd_tail = odd_tail.next
            else:
                even_tail.next = current
                even_tail = even_tail.next

            current = current.next
            is_odd = not is_odd

        even_tail.next = None  # Important: terminate even list
        odd_tail.next = even_dummy.next  # Connect odd to even

        return odd_dummy.next


class SolutionIndex:
    """Using index counter"""

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even
        index = 3
        current = even.next

        while current:
            if index % 2 == 1:  # Odd position
                odd.next = current
                odd = odd.next
            else:  # Even position
                even.next = current
                even = even.next

            current = current.next
            index += 1

        even.next = None
        odd.next = even_head

        return head
