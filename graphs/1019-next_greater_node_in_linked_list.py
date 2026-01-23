#1019. Next Greater Node In Linked List
#Medium
#
#You are given the head of a linked list with n nodes.
#
#For each node in the list, find the value of the next greater node. That is,
#for each node, find the value of the first node that is next to it and has a
#strictly larger value than it.
#
#Return an integer array answer where answer[i] is the value of the next greater
#node of the ith node (1-indexed). If the ith node does not have a next greater
#node, set answer[i] = 0.
#
#Example 1:
#Input: head = [2,1,5]
#Output: [5,5,0]
#
#Example 2:
#Input: head = [2,7,4,3,5]
#Output: [7,0,5,5,0]
#
#Constraints:
#    The number of nodes in the list is n.
#    1 <= n <= 10^4
#    1 <= Node.val <= 10^9

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> list[int]:
        """
        Monotonic stack with indices.
        """
        # Convert to array
        values = []
        while head:
            values.append(head.val)
            head = head.next

        n = len(values)
        result = [0] * n
        stack = []  # Stack of indices

        for i in range(n):
            while stack and values[stack[-1]] < values[i]:
                idx = stack.pop()
                result[idx] = values[i]
            stack.append(i)

        return result


class SolutionReverse:
    """Process in reverse"""

    def nextLargerNodes(self, head: ListNode) -> list[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        n = len(values)
        result = [0] * n
        stack = []  # Stack of values (decreasing)

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= values[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1]

            stack.append(values[i])

        return result


class SolutionOnePass:
    """One pass with stack of (index, value)"""

    def nextLargerNodes(self, head: ListNode) -> list[int]:
        result = []
        stack = []  # (index, value)
        idx = 0

        while head:
            while stack and stack[-1][1] < head.val:
                prev_idx, _ = stack.pop()
                result[prev_idx] = head.val

            stack.append((idx, head.val))
            result.append(0)
            idx += 1
            head = head.next

        return result
