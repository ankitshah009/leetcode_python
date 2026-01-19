#141. Linked List Cycle
#Easy
#
#Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
#There is a cycle in a linked list if there is some node in the list that can be reached
#again by continuously following the next pointer.
#
#Return true if there is a cycle in the linked list. Otherwise, return false.
#
#Example 1:
#Input: head = [3,2,0,-4], pos = 1
#Output: true
#Explanation: There is a cycle in the linked list, where the tail connects to the 1st node.
#
#Example 2:
#Input: head = [1,2], pos = 0
#Output: true
#
#Example 3:
#Input: head = [1], pos = -1
#Output: false
#
#Constraints:
#    The number of the nodes in the list is in the range [0, 10^4].
#    -10^5 <= Node.val <= 10^5
#    pos is -1 or a valid index in the linked-list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
