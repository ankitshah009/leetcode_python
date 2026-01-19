#382. Linked List Random Node
#Medium
#
#Given a singly linked list, return a random node's value from the linked list.
#Each node must have the same probability of being chosen.
#
#Implement the Solution class:
#- Solution(ListNode head) Initializes the object with the head of the singly
#  linked list head.
#- int getRandom() Chooses a node randomly from the list and returns its value.
#  All the nodes of the list should be equally likely to be chosen.
#
#Example 1:
#Input: ["Solution", "getRandom", "getRandom", "getRandom", "getRandom",
#        "getRandom"]
#       [[[1, 2, 3]], [], [], [], [], []]
#Output: [null, 1, 3, 2, 2, 3]
#
#Constraints:
#    The number of nodes in the linked list will be in the range [1, 10^4].
#    -10^4 <= Node.val <= 10^4
#    At most 10^4 calls will be made to getRandom.

import random
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Reservoir Sampling - O(1) space, O(n) per getRandom.
    Works even if list length is unknown or changes.
    """

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = self.head.val
        node = self.head.next
        count = 2

        while node:
            # With probability 1/count, replace result
            if random.randint(1, count) == 1:
                result = node.val
            node = node.next
            count += 1

        return result


class SolutionArray:
    """Store all values in array - O(n) space, O(1) per getRandom"""

    def __init__(self, head: Optional[ListNode]):
        self.values = []
        while head:
            self.values.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.values)


class SolutionLength:
    """Calculate length first, then random index"""

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        node = head
        while node:
            self.length += 1
            node = node.next

    def getRandom(self) -> int:
        idx = random.randint(0, self.length - 1)
        node = self.head
        for _ in range(idx):
            node = node.next
        return node.val
