#25. Reverse Nodes in k-Group
#Hard
#
#Given the head of a linked list, reverse the nodes of the list k at a time, and return
#the modified list.
#
#k is a positive integer and is less than or equal to the length of the linked list. If the
#number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
#You may not alter the values in the list's nodes, only nodes themselves may be changed.
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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head, k):
            prev = None
            curr = head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev

        # Count total nodes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while count >= k:
            group_start = prev_group_end.next
            group_end = group_start

            # Find end of group
            for _ in range(k - 1):
                group_end = group_end.next

            next_group_start = group_end.next

            # Reverse group
            reverse(group_start, k)

            # Connect reversed group
            prev_group_end.next = group_end
            group_start.next = next_group_start

            # Move to next group
            prev_group_end = group_start
            count -= k

        return dummy.next
