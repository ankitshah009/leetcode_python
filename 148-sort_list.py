#148. Sort List
#Medium
#
#Given the head of a linked list, return the list after sorting it in ascending order.
#
#Example 1:
#Input: head = [4,2,1,3]
#Output: [1,2,3,4]
#
#Example 2:
#Input: head = [-1,5,3,4,0]
#Output: [-1,0,3,4,5]
#
#Example 3:
#Input: head = []
#Output: []
#
#Constraints:
#    The number of nodes in the list is in the range [0, 5 * 10^4].
#    -10^5 <= Node.val <= 10^5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0)
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
