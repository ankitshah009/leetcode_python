#21. Merge Two Sorted Lists
#Easy
#
#You are given the heads of two sorted linked lists list1 and list2.
#
#Merge the two lists into one sorted list. The list should be made by splicing
#together the nodes of the first two lists.
#
#Return the head of the merged linked list.
#
#Example 1:
#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]
#
#Example 2:
#Input: list1 = [], list2 = []
#Output: []
#
#Example 3:
#Input: list1 = [], list2 = [0]
#Output: [0]
#
#Constraints:
#    The number of nodes in both lists is in the range [0, 50].
#    -100 <= Node.val <= 100
#    Both list1 and list2 are sorted in non-decreasing order.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative approach with dummy head.
        """
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach remaining nodes
        current.next = list1 if list1 else list2

        return dummy.next


class SolutionRecursive:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach.
        """
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


class SolutionInPlace:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        In-place merge without creating new nodes.
        """
        if not list1:
            return list2
        if not list2:
            return list1

        # Ensure list1 starts with smaller value
        if list1.val > list2.val:
            list1, list2 = list2, list1

        head = list1

        while list1.next and list2:
            if list1.next.val <= list2.val:
                list1 = list1.next
            else:
                # Insert list2 node after list1
                temp = list1.next
                list1.next = list2
                list2 = list2.next
                list1.next.next = temp
                list1 = list1.next

        # Attach remaining list2
        if list2:
            list1.next = list2

        return head
