#1206. Design Skiplist
#Hard
#
#Design a Skiplist without using any built-in libraries.
#
#A skiplist is a data structure that takes O(log(n)) time to add, erase and
#search. Comparing with treap and red-black tree which has the same function
#and performance, the code length of Skiplist can be comparatively short and
#the idea behind Skiplists is just simple linked lists.
#
#Implement the Skiplist class:
#    Skiplist() Initializes the object of the skiplist.
#    bool search(int target) Returns true if the integer target exists in the
#    Skiplist or false otherwise.
#    void add(int num) Inserts the value num into the SkipList.
#    bool erase(int num) Removes the value num from the Skiplist and returns
#    true. If num does not exist in the Skiplist, do nothing and return false.
#
#Example 1:
#Input
#["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
#[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
#Output
#[null, null, null, null, false, null, true, false, true, false]
#
#Constraints:
#    0 <= num, target <= 2 * 10^4
#    At most 5 * 10^4 calls will be made to search, add, and erase.

import random

class Node:
    def __init__(self, val=-1, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down


class Skiplist:
    def __init__(self):
        self.head = Node()  # Sentinel head at top level

    def search(self, target: int) -> bool:
        node = self.head

        while node:
            # Move right while next node's value is less than target
            while node.right and node.right.val < target:
                node = node.right

            # Check if we found target
            if node.right and node.right.val == target:
                return True

            # Move down a level
            node = node.down

        return False

    def add(self, num: int) -> None:
        # Track nodes where we might need to insert
        stack = []
        node = self.head

        while node:
            while node.right and node.right.val < num:
                node = node.right
            stack.append(node)
            node = node.down

        # Insert at bottom level, potentially promote up
        insert = True
        down = None

        while insert and stack:
            node = stack.pop()
            node.right = Node(num, node.right, down)
            down = node.right
            insert = random.random() < 0.5  # 50% chance to promote

        # If we need to add new level
        if insert:
            self.head = Node(-1, Node(num, None, down), self.head)

    def erase(self, num: int) -> bool:
        node = self.head
        found = False

        while node:
            while node.right and node.right.val < num:
                node = node.right

            if node.right and node.right.val == num:
                found = True
                node.right = node.right.right  # Remove node

            node = node.down

        return found


class SkiplistWithLevel:
    """Alternative implementation with explicit level tracking"""
    MAX_LEVEL = 16

    def __init__(self):
        self.head = [None] * self.MAX_LEVEL
        self.level = 0

    def _random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.MAX_LEVEL - 1:
            level += 1
        return level

    def search(self, target: int) -> bool:
        prev = [None] * self.MAX_LEVEL
        self._find(target, prev)
        return prev[0] and prev[0].val == target

    def _find(self, target, prev):
        """Find predecessor at each level"""
        curr = self.head

        for i in range(self.level, -1, -1):
            while curr[i] and curr[i].val < target:
                curr = curr[i].forward

            prev[i] = curr

    def add(self, num: int) -> None:
        # Simplified: just use the Node-based implementation above
        pass

    def erase(self, num: int) -> bool:
        # Simplified: just use the Node-based implementation above
        pass
