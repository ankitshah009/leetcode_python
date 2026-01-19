#61. Rotate List
#Medium
#
#Given the head of a linked list, rotate the list to the right by k places.
#
#Example 1:
#Input: head = [1,2,3,4,5], k = 2
#Output: [4,5,1,2,3]
#
#Example 2:
#Input: head = [0,1,2], k = 4
#Output: [2,0,1]
#
#Constraints:
#    The number of nodes in the list is in the range [0, 500].
#    -100 <= Node.val <= 100
#    0 <= k <= 2 * 10^9

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Normalize k
        k = k % length
        if k == 0:
            return head

        # Find new tail (length - k - 1 steps from head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Rotate
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head
