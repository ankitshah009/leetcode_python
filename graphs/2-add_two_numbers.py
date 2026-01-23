#2. Add Two Numbers
#Medium
#
#You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in reverse order, and each of their nodes contains a
#single digit. Add the two numbers and return the sum as a linked list.
#
#You may assume the two numbers do not contain any leading zero, except the
#number 0 itself.
#
#Example 1:
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.
#
#Example 2:
#Input: l1 = [0], l2 = [0]
#Output: [0]
#
#Example 3:
#Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]
#
#Constraints:
#    The number of nodes in each linked list is in the range [1, 100].
#    0 <= Node.val <= 9
#    It is guaranteed that the list represents a number that does not have
#    leading zeros.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Simulate addition with carry.
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


class SolutionRecursive:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach.
        """
        def add(n1, n2, carry):
            if not n1 and not n2 and not carry:
                return None

            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0
            total = val1 + val2 + carry

            node = ListNode(total % 10)
            node.next = add(
                n1.next if n1 else None,
                n2.next if n2 else None,
                total // 10
            )
            return node

        return add(l1, l2, 0)


class SolutionConvert:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Convert to numbers, add, convert back (for understanding).
        Note: May overflow for very large numbers.
        """
        def to_number(node):
            num = 0
            multiplier = 1
            while node:
                num += node.val * multiplier
                multiplier *= 10
                node = node.next
            return num

        def to_list(num):
            if num == 0:
                return ListNode(0)
            dummy = ListNode(0)
            current = dummy
            while num:
                current.next = ListNode(num % 10)
                current = current.next
                num //= 10
            return dummy.next

        return to_list(to_number(l1) + to_number(l2))
