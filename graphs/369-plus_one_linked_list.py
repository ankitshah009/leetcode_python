#369. Plus One Linked List
#Medium
#
#Given a non-negative integer represented as a linked list of digits, plus one
#to the integer.
#
#The digits are stored such that the most significant digit is at the head of
#the list.
#
#Example 1:
#Input: head = [1,2,3]
#Output: [1,2,4]
#
#Example 2:
#Input: head = [0]
#Output: [1]
#
#Constraints:
#    The number of nodes in the linked list is in the range [1, 100].
#    0 <= Node.val <= 9
#    The number represented by the linked list does not contain leading zeros
#    except for the zero itself.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """
        Find the rightmost non-9 digit, increment it, and set all following
        digits to 0.
        """
        # Sentinel node in case we need to add a new head
        sentinel = ListNode(0)
        sentinel.next = head

        # Find rightmost non-9 digit
        not_nine = sentinel
        node = head

        while node:
            if node.val != 9:
                not_nine = node
            node = node.next

        # Increment the rightmost non-9
        not_nine.val += 1

        # Set all following digits to 0
        node = not_nine.next
        while node:
            node.val = 0
            node = node.next

        return sentinel if sentinel.val == 1 else sentinel.next


class SolutionRecursive:
    """Recursive approach"""

    def plusOne(self, head: ListNode) -> ListNode:
        def add_one(node):
            """Returns carry after adding one"""
            if not node:
                return 1

            carry = add_one(node.next)
            total = node.val + carry
            node.val = total % 10
            return total // 10

        carry = add_one(head)

        if carry:
            new_head = ListNode(1)
            new_head.next = head
            return new_head

        return head


class SolutionReverse:
    """Reverse, add one, reverse back"""

    def plusOne(self, head: ListNode) -> ListNode:
        def reverse(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        # Reverse the list
        head = reverse(head)

        # Add one
        carry = 1
        node = head
        prev = None

        while node and carry:
            total = node.val + carry
            node.val = total % 10
            carry = total // 10
            prev = node
            node = node.next

        if carry:
            prev.next = ListNode(1)

        # Reverse back
        return reverse(head)


class SolutionStack:
    """Using stack to process from right to left"""

    def plusOne(self, head: ListNode) -> ListNode:
        stack = []
        node = head

        while node:
            stack.append(node)
            node = node.next

        carry = 1
        while stack and carry:
            node = stack.pop()
            total = node.val + carry
            node.val = total % 10
            carry = total // 10

        if carry:
            new_head = ListNode(1)
            new_head.next = head
            return new_head

        return head
