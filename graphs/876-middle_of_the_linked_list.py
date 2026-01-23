#876. Middle of the Linked List
#Easy
#
#Given the head of a singly linked list, return the middle node of the linked list.
#
#If there are two middle nodes, return the second middle node.
#
#Example 1:
#Input: head = [1,2,3,4,5]
#Output: [3,4,5]
#Explanation: The middle node is node 3.
#
#Example 2:
#Input: head = [1,2,3,4,5,6]
#Output: [4,5,6]
#Explanation: With two middle nodes 3 and 4, we return the second one.
#
#Constraints:
#    The number of nodes in the list is in the range [1, 100].
#    1 <= Node.val <= 100

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        Fast and slow pointer approach.
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


class SolutionCount:
    """Count nodes first, then traverse to middle"""

    def middleNode(self, head: ListNode) -> ListNode:
        # Count nodes
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        # Go to middle
        middle = count // 2
        current = head
        for _ in range(middle):
            current = current.next

        return current


class SolutionArray:
    """Store all nodes in array"""

    def middleNode(self, head: ListNode) -> ListNode:
        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next

        return nodes[len(nodes) // 2]


class SolutionTwoPass:
    """Two-pass approach"""

    def middleNode(self, head: ListNode) -> ListNode:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        node = head
        for _ in range(n // 2):
            node = node.next

        return node
