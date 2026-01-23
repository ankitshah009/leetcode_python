#1429. First Unique Number
#Medium
#
#You have a queue of integers, you need to retrieve the first unique integer
#in the queue.
#
#Implement the FirstUnique class:
#    FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
#    int showFirstUnique() returns the value of the first unique integer of the
#    queue, and returns -1 if there is no such integer.
#    void add(int value) insert value to the queue.
#
#Example 1:
#Input:
#["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
#[[[2,3,5]],[],[5],[],[2],[],[3],[]]
#Output: [null,2,null,2,null,3,null,-1]
#Explanation:
#FirstUnique firstUnique = new FirstUnique([2,3,5]);
#firstUnique.showFirstUnique(); // return 2
#firstUnique.add(5);            // the queue is now [2,3,5,5]
#firstUnique.showFirstUnique(); // return 2
#firstUnique.add(2);            // the queue is now [2,3,5,5,2]
#firstUnique.showFirstUnique(); // return 3
#firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
#firstUnique.showFirstUnique(); // return -1
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^8
#    1 <= value <= 10^8
#    At most 50000 calls will be made to showFirstUnique and add.

from typing import List
from collections import OrderedDict

class FirstUnique:
    """
    Use OrderedDict to maintain insertion order and O(1) operations.
    Keep unique numbers in OrderedDict, remove when duplicate found.
    """

    def __init__(self, nums: List[int]):
        self.unique = OrderedDict()  # Stores unique values
        self.seen = set()            # All values ever seen

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.unique:
            return next(iter(self.unique))
        return -1

    def add(self, value: int) -> None:
        if value in self.seen:
            # Already seen, remove from unique if present
            if value in self.unique:
                del self.unique[value]
        else:
            # First time seeing this value
            self.seen.add(value)
            self.unique[value] = True


class FirstUniqueDoublyLinkedList:
    """Using doubly linked list for O(1) removal"""

    class Node:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, nums: List[int]):
        self.head = self.Node(0)  # Dummy head
        self.tail = self.Node(0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

        self.val_to_node = {}  # value -> node (only for unique values)
        self.seen = set()

        for num in nums:
            self.add(num)

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def showFirstUnique(self) -> int:
        if self.head.next != self.tail:
            return self.head.next.val
        return -1

    def add(self, value: int) -> None:
        if value in self.seen:
            if value in self.val_to_node:
                self._remove_node(self.val_to_node[value])
                del self.val_to_node[value]
        else:
            self.seen.add(value)
            node = self.Node(value)
            self.val_to_node[value] = node
            self._add_to_tail(node)


class FirstUniqueSimple:
    """Simpler but less efficient for showFirstUnique"""

    def __init__(self, nums: List[int]):
        from collections import Counter
        self.queue = list(nums)
        self.count = Counter(nums)

    def showFirstUnique(self) -> int:
        # Clean up front of queue
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.pop(0)

        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        self.count[value] += 1
