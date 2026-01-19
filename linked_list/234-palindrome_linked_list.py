#234. Palindrome Linked List
#Easy
#
#Given the head of a singly linked list, return true if it is a palindrome or
#false otherwise.
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
#
#Follow up: Could you do it in O(n) time and O(1) space?

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        O(n) time, O(1) space.
        1. Find middle using slow/fast pointers
        2. Reverse second half
        3. Compare both halves
        4. (Optional) Restore the list
        """
        if not head or not head.next:
            return True

        # Find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second_half = self.reverse(slow.next)

        # Compare
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


class SolutionStack:
    """O(n) time and space using stack"""

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        current = head

        while current:
            values.append(current.val)
            current = current.next

        return values == values[::-1]


class SolutionRecursive:
    """Recursive comparison"""

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front = head

        def check(node):
            if not node:
                return True

            if not check(node.next):
                return False

            if self.front.val != node.val:
                return False

            self.front = self.front.next
            return True

        return check(head)


class SolutionHalfStack:
    """Stack only first half"""

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Find length
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Push first half to stack
        stack = []
        current = head
        for _ in range(length // 2):
            stack.append(current.val)
            current = current.next

        # Skip middle for odd length
        if length % 2 == 1:
            current = current.next

        # Compare with second half
        while current:
            if stack.pop() != current.val:
                return False
            current = current.next

        return True
