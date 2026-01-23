#1172. Dinner Plate Stacks
#Hard
#
#You have an infinite number of stacks arranged in a row and numbered (left
#to right) from 0, each of the stacks has the same maximum capacity.
#
#Implement the DinnerPlates class:
#    DinnerPlates(int capacity) Initializes the object with the maximum
#    capacity of the stacks capacity.
#    void push(int val) Pushes the given integer val into the leftmost stack
#    with a size less than capacity.
#    int pop() Returns the value at the top of the rightmost non-empty stack
#    and removes it from that stack, and returns -1 if all the stacks are empty.
#    int popAtStack(int index) Returns the value at the top of the stack with
#    the given index index and removes it from that stack or returns -1 if the
#    stack with that given index is empty.
#
#Example 1:
#Input
#["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push",
# "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
#[[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
#Output
#[null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]
#
#Constraints:
#    1 <= capacity <= 2 * 10^4
#    1 <= val <= 2 * 10^4
#    0 <= index <= 10^5
#    At most 2 * 10^5 calls will be made to push, pop, and popAtStack.

import heapq

class DinnerPlates:
    """
    Use heap to track leftmost non-full stack.
    Track rightmost non-empty stack index.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []  # List of stacks
        self.available = []  # Min-heap of indices with space

    def push(self, val: int) -> None:
        # Clean up heap - remove indices that are now full or don't exist
        while self.available and (
            self.available[0] >= len(self.stacks) or
            len(self.stacks[self.available[0]]) >= self.capacity
        ):
            heapq.heappop(self.available)

        if not self.available:
            # All stacks are full, create new one
            self.stacks.append([])
            heapq.heappush(self.available, len(self.stacks) - 1)

        idx = self.available[0]
        self.stacks[idx].append(val)

        # If stack is now full, remove from available
        if len(self.stacks[idx]) >= self.capacity:
            heapq.heappop(self.available)

    def pop(self) -> int:
        # Find rightmost non-empty stack
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        if not self.stacks:
            return -1

        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1

        # Add to available since we're creating space
        heapq.heappush(self.available, index)

        return self.stacks[index].pop()


class DinnerPlatesSortedList:
    """Alternative using sorted container for available indices"""
    def __init__(self, capacity: int):
        from sortedcontainers import SortedList
        self.capacity = capacity
        self.stacks = []
        self.available = SortedList()  # Indices with space

    def push(self, val: int) -> None:
        # Clean available
        while self.available and self.available[0] < len(self.stacks) and \
              len(self.stacks[self.available[0]]) >= self.capacity:
            self.available.pop(0)

        if not self.available or self.available[0] >= len(self.stacks):
            # Need new stack
            self.stacks.append([val])
            if len(self.stacks[-1]) < self.capacity:
                self.available.add(len(self.stacks) - 1)
        else:
            idx = self.available[0]
            self.stacks[idx].append(val)
            if len(self.stacks[idx]) >= self.capacity:
                self.available.remove(idx)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        if not self.stacks:
            return -1

        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1

        if index not in self.available:
            self.available.add(index)

        return self.stacks[index].pop()
