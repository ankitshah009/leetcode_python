#1474. Delete N Nodes After M Nodes of a Linked List
#Easy
#
#You are given the head of a linked list and two integers m and n.
#
#Traverse the linked list and remove some nodes in the following way:
#    Start with the head as the current node.
#    Keep the first m nodes starting with the current node.
#    Remove the next n nodes
#    Keep repeating steps 2 and 3 until you reach the end of the list.
#
#Return the head of the modified list after removing the mentioned nodes.
#
#Example 1:
#Input: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
#Output: [1,2,6,7,11,12]
#Explanation: Keep the first (m = 2) nodes starting from the head (1 ->2) shown
#in black nodes. Delete the next (n = 3) nodes (3 -> 4 -> 5) shown in red.
#Continue with the same procedure until reaching the tail.
#
#Example 2:
#Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
#Output: [1,5,9]
#
#Example 3:
#Input: head = [1,2,3,4,5,6,7,8], m = 3, n = 1
#Output: [1,2,3,5,6,7]
#
#Constraints:
#    The number of nodes in the list is in the range [1, 10^4].
#    1 <= Node.val <= 10^6
#    1 <= m, n <= 1000

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        """
        Traverse: keep m nodes, skip n nodes, repeat.
        """
        current = head

        while current:
            # Keep m nodes
            for _ in range(m - 1):
                if not current:
                    return head
                current = current.next

            if not current:
                return head

            # Skip n nodes
            to_delete = current.next
            for _ in range(n):
                if not to_delete:
                    break
                to_delete = to_delete.next

            # Connect
            current.next = to_delete
            current = to_delete

        return head


class SolutionAlternative:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        """Alternative with cleaner loop structure"""
        current = head

        while current:
            # Keep m - 1 more nodes (m total including current)
            keep_count = m - 1
            while keep_count > 0 and current.next:
                current = current.next
                keep_count -= 1

            # Now current is the last node to keep
            # Skip n nodes
            node_to_skip = current.next
            skip_count = n
            while skip_count > 0 and node_to_skip:
                node_to_skip = node_to_skip.next
                skip_count -= 1

            # Connect last kept node to node after skipped section
            current.next = node_to_skip
            current = node_to_skip

        return head


class SolutionRecursive:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        """Recursive approach"""
        def process(node: ListNode, keep: int, skip: int) -> Optional[ListNode]:
            if not node:
                return None

            # Find the m-th node (last to keep)
            current = node
            for _ in range(keep - 1):
                if not current.next:
                    return node
                current = current.next

            # Skip n nodes after current
            to_skip = current.next
            for _ in range(skip):
                if not to_skip:
                    break
                to_skip = to_skip.next

            # Recursively process rest
            current.next = process(to_skip, keep, skip)

            return node

        return process(head, m, n)


class SolutionCounter:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        """Using position counter"""
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        position = 0  # 0-indexed position in current group

        while current:
            group_pos = position % (m + n)

            if group_pos < m:
                # Keep this node
                prev = current
                current = current.next
            else:
                # Delete this node
                prev.next = current.next
                current = current.next

            position += 1

        return dummy.next
