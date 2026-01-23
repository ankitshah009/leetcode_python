#1290. Convert Binary Number in a Linked List to Integer
#Easy
#
#Given head which is a reference node to a singly-linked list. The value of
#each node in the linked list is either 0 or 1. The linked list holds the
#binary representation of a number.
#
#Return the decimal value of the number in the linked list.
#
#The most significant bit is at the head of the linked list.
#
#Example 1:
#Input: head = [1,0,1]
#Output: 5
#Explanation: (101) in base 2 = (5) in base 10
#
#Example 2:
#Input: head = [0]
#Output: 0
#
#Constraints:
#    The Linked List is not empty.
#    Number of nodes will not exceed 30.
#    Each node's value is either 0 or 1.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
        Traverse and build number bit by bit.
        result = result * 2 + current_bit
        """
        result = 0
        while head:
            result = result * 2 + head.val
            head = head.next
        return result


class SolutionBitwise:
    def getDecimalValue(self, head: ListNode) -> int:
        """Using bit operations"""
        result = 0
        while head:
            result = (result << 1) | head.val
            head = head.next
        return result


class SolutionString:
    def getDecimalValue(self, head: ListNode) -> int:
        """Collect bits as string, then convert"""
        bits = []
        while head:
            bits.append(str(head.val))
            head = head.next
        return int(''.join(bits), 2)
