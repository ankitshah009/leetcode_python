#2816. Double a Number Represented as a Linked List
#Medium
#
#You are given the head of a non-empty linked list representing a non-negative integer
#without leading zeroes.
#
#Return the head of the linked list after doubling it.
#
#Example 1:
#Input: head = [1,8,9]
#Output: [3,7,8]
#Explanation: The figure above corresponds to the given linked list which represents the
#number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
#
#Example 2:
#Input: head = [9,9,9]
#Output: [1,9,9,8]
#Explanation: The figure above corresponds to the given linked list which represents the
#number 999. Hence, the returned linked list represents the number 999 * 2 = 1998.
#
#Constraints:
#    The number of nodes in the list is in the range [1, 10^4]
#    0 <= Node.val <= 9
#    The input is generated such that the list represents a number that does not have
#        leading zeros, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the list
        def reverse(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        # Reverse to process from least significant digit
        head = reverse(head)

        carry = 0
        current = head

        while current:
            doubled = current.val * 2 + carry
            current.val = doubled % 10
            carry = doubled // 10

            if not current.next and carry:
                current.next = ListNode(carry)
                carry = 0

            current = current.next

        # Reverse back
        return reverse(head)
