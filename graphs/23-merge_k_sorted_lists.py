#23. Merge k Sorted Lists
#Hard
#
#You are given an array of k linked-lists lists, each linked-list is sorted in
#ascending order.
#
#Merge all the linked-lists into one sorted linked-list and return it.
#
#Example 1:
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#merging them into one sorted list:
#1->1->2->3->4->4->5->6
#
#Example 2:
#Input: lists = []
#Output: []
#
#Example 3:
#Input: lists = [[]]
#Output: []
#
#Constraints:
#    k == lists.length
#    0 <= k <= 10^4
#    0 <= lists[i].length <= 500
#    -10^4 <= lists[i][j] <= 10^4
#    lists[i] is sorted in ascending order.
#    The sum of lists[i].length will not exceed 10^4.

from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Min heap approach - O(N log k) time.
        """
        dummy = ListNode()
        current = dummy

        # Min heap with (value, index, node)
        # Index is used to break ties for nodes with same values
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


class SolutionDivideConquer:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Divide and conquer - O(N log k) time.
        """
        def merge_two(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            current = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

            current.next = l1 if l1 else l2
            return dummy.next

        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(merge_two(l1, l2))
            lists = merged

        return lists[0]


class SolutionMergeOne:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge one by one - O(kN) time.
        """
        def merge_two(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            current = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

            current.next = l1 if l1 else l2
            return dummy.next

        if not lists:
            return None

        result = lists[0]
        for i in range(1, len(lists)):
            result = merge_two(result, lists[i])

        return result


class SolutionSort:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Collect all values, sort, and build new list - O(N log N) time.
        """
        values = []

        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        values.sort()

        dummy = ListNode()
        current = dummy

        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next
