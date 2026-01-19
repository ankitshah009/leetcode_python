#23. Merge k Sorted Lists
#Hard
#
#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
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

import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        heap = []

        # Initialize heap with first node from each list
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
