#234. Palindrome Linked List
#Easy
#
#Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
#
#Example 1:
#Input: head = [1,2,2,1]
#Output: true
#
#Example 2:
#Input: head = [1,2]
#Output: false
#
#Constraints:
#    The number of nodes in the list is in the range [1, 10^5].
#    0 <= Node.val <= 9

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # Find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        current = slow.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Compare halves
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
