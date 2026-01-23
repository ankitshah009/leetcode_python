#1669. Merge In Between Linked Lists
#Medium
#
#You are given two linked lists: list1 and list2 of sizes n and m respectively.
#
#Remove list1's nodes from the ath node to the bth node, and put list2 in their
#place.
#
#Example 1:
#Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
#Output: [10,1,13,1000000,1000001,1000002,5]
#Explanation: We remove nodes 3 and 4 and put list2 in their place.
#
#Example 2:
#Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
#Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
#
#Constraints:
#    3 <= list1.length <= 10^4
#    1 <= a <= b < list1.length - 1
#    1 <= list2.length <= 10^4

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int,
                       list2: ListNode) -> ListNode:
        """
        Find node before position a and node after position b.
        Connect them with list2.
        """
        # Find node at position a-1
        pre_a = list1
        for _ in range(a - 1):
            pre_a = pre_a.next

        # Find node at position b+1
        post_b = pre_a
        for _ in range(b - a + 2):
            post_b = post_b.next

        # Find tail of list2
        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next

        # Connect
        pre_a.next = list2
        list2_tail.next = post_b

        return list1


class SolutionTwoPointers:
    def mergeInBetween(self, list1: ListNode, a: int, b: int,
                       list2: ListNode) -> ListNode:
        """
        Use two pointers to find both positions.
        """
        # Find position a-1 and b
        ptr1 = list1
        ptr2 = list1

        for i in range(b):
            if i < a - 1:
                ptr1 = ptr1.next
            ptr2 = ptr2.next

        # ptr1 is at position a-1
        # ptr2 is at position b, so ptr2.next is position b+1

        # Find list2 tail
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next

        # Merge
        ptr1.next = list2
        tail2.next = ptr2.next

        return list1


class SolutionWithCount:
    def mergeInBetween(self, list1: ListNode, a: int, b: int,
                       list2: ListNode) -> ListNode:
        """
        Count positions while traversing.
        """
        dummy = ListNode(0, list1)
        prev = dummy
        current = list1
        position = 0

        pre_a = None
        post_b = None

        while current:
            if position == a - 1:
                pre_a = current
            if position == b:
                post_b = current.next
                break

            prev = current
            current = current.next
            position += 1

        # Get list2 tail
        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next

        # Merge
        if pre_a:
            pre_a.next = list2
        list2_tail.next = post_b

        return dummy.next


class SolutionCompact:
    def mergeInBetween(self, list1: ListNode, a: int, b: int,
                       list2: ListNode) -> ListNode:
        """
        Compact implementation.
        """
        # Navigate to (a-1)th node
        node = list1
        for _ in range(a - 1):
            node = node.next

        # Save connection point and navigate to (b+1)th node
        connect_start = node
        for _ in range(b - a + 2):
            node = node.next
        connect_end = node

        # Get list2 tail
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next

        # Make connections
        connect_start.next = list2
        tail2.next = connect_end

        return list1
