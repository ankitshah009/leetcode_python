#1171. Remove Zero Sum Consecutive Nodes from Linked List
#Medium
#
#Given the head of a linked list, we repeatedly delete consecutive sequences
#of nodes that sum to 0 until there are no such sequences.
#
#After doing so, return the head of the final linked list. You may return any
#such answer.
#
#Example 1:
#Input: head = [1,2,-3,3,1]
#Output: [3,1]
#Note: The answer [1,2,1] would also be accepted.
#
#Example 2:
#Input: head = [1,2,3,-3,4]
#Output: [1,2,4]
#
#Example 3:
#Input: head = [1,2,3,-3,-2]
#Output: [1]
#
#Constraints:
#    The given linked list will contain between 1 and 1000 nodes.
#    Each node in the linked list has -1000 <= node.val <= 1000.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Use prefix sum. If two nodes have same prefix sum,
        everything between them sums to 0.

        Two passes:
        1. First pass: Record last occurrence of each prefix sum
        2. Second pass: Skip to last occurrence when we see a repeated prefix
        """
        dummy = ListNode(0)
        dummy.next = head

        # First pass: find last occurrence of each prefix sum
        prefix_sum = 0
        last_occurrence = {}
        node = dummy

        while node:
            prefix_sum += node.val
            last_occurrence[prefix_sum] = node
            node = node.next

        # Second pass: connect nodes, skipping zero-sum sequences
        prefix_sum = 0
        node = dummy

        while node:
            prefix_sum += node.val
            # Skip to last node with same prefix sum
            node.next = last_occurrence[prefix_sum].next
            node = node.next

        return dummy.next


class SolutionIterative:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative approach: keep removing zero-sum sequences until none left.
        """
        dummy = ListNode(0)
        dummy.next = head

        changed = True
        while changed:
            changed = False
            prefix_sum = 0
            seen = {0: dummy}
            node = dummy.next

            while node:
                prefix_sum += node.val

                if prefix_sum in seen:
                    # Remove nodes between seen[prefix_sum] and node
                    seen[prefix_sum].next = node.next
                    changed = True
                    break

                seen[prefix_sum] = node
                node = node.next

        return dummy.next


class SolutionOnePass:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        One-pass solution with cleanup of prefix sums.
        """
        dummy = ListNode(0)
        dummy.next = head

        prefix_sum = 0
        prefix_to_node = {0: dummy}

        node = dummy
        while node:
            prefix_sum += node.val

            if prefix_sum in prefix_to_node:
                # Remove all nodes between and clear their prefix sums
                prev = prefix_to_node[prefix_sum]
                to_remove = prev.next
                temp_sum = prefix_sum

                while to_remove != node:
                    temp_sum += to_remove.val
                    if temp_sum != prefix_sum:
                        del prefix_to_node[temp_sum]
                    to_remove = to_remove.next

                prev.next = node.next
            else:
                prefix_to_node[prefix_sum] = node

            node = node.next

        return dummy.next
