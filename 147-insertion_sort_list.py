#147. Insertion Sort List
#Medium
#
#Given the head of a singly linked list, sort the list using insertion sort, and return the
#sorted list's head.
#
#Example 1:
#Input: head = [4,2,1,3]
#Output: [1,2,3,4]
#
#Example 2:
#Input: head = [-1,5,3,4,0]
#Output: [-1,0,3,4,5]
#
#Constraints:
#    The number of nodes in the list is in the range [1, 5000].
#    -5000 <= Node.val <= 5000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = head

        while current:
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            next_node = current.next
            current.next = prev.next
            prev.next = current
            current = next_node

        return dummy.next
