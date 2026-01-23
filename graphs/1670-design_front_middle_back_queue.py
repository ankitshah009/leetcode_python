#1670. Design Front Middle Back Queue
#Medium
#
#Design a queue that supports push and pop operations in the front, middle,
#and back.
#
#Implement the FrontMiddleBackQueue class:
#- FrontMiddleBackQueue() Initializes the queue.
#- void pushFront(int val) Adds val to the front of the queue.
#- void pushMiddle(int val) Adds val to the middle of the queue.
#- void pushBack(int val) Adds val to the back of the queue.
#- int popFront() Removes the front element and returns it. If queue is empty,
#  return -1.
#- int popMiddle() Removes the middle element and returns it. If queue is empty,
#  return -1.
#- int popBack() Removes the back element and returns it. If queue is empty,
#  return -1.
#
#Note: The middle element is the element at index floor((n-1)/2) for size n.
#
#Example 1:
#Input:
#["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle",
# "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
#[[], [1], [2], [3], [4], [], [], [], [], []]
#Output:
#[null, null, null, null, null, 1, 3, 4, 2, -1]
#
#Constraints:
#    1 <= val <= 10^9
#    At most 1000 calls will be made to pushFront, pushMiddle, pushBack,
#    popFront, popMiddle, and popBack.

from collections import deque

class FrontMiddleBackQueue:
    """
    Use two deques to maintain front and back halves.
    Keep front half <= back half in size.
    """

    def __init__(self):
        self.front = deque()  # First half
        self.back = deque()   # Second half

    def _balance(self):
        """Ensure len(front) <= len(back) <= len(front) + 1"""
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        elif len(self.back) > len(self.front) + 1:
            self.front.append(self.back.popleft())

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) < len(self.back):
            self.front.append(val)
        else:
            self.back.appendleft(val)

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.front and not self.back:
            return -1
        if self.front:
            val = self.front.popleft()
        else:
            val = self.back.popleft()
        self._balance()
        return val

    def popMiddle(self) -> int:
        if not self.front and not self.back:
            return -1
        if len(self.front) < len(self.back):
            val = self.back.popleft()
        else:
            val = self.front.pop()
        return val

    def popBack(self) -> int:
        if not self.back:
            return -1
        val = self.back.pop()
        self._balance()
        return val


class FrontMiddleBackQueueList:
    """
    Simple list-based implementation (less efficient for large n).
    """

    def __init__(self):
        self.data = []

    def pushFront(self, val: int) -> None:
        self.data.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        mid = len(self.data) // 2
        self.data.insert(mid, val)

    def pushBack(self, val: int) -> None:
        self.data.append(val)

    def popFront(self) -> int:
        if not self.data:
            return -1
        return self.data.pop(0)

    def popMiddle(self) -> int:
        if not self.data:
            return -1
        mid = (len(self.data) - 1) // 2
        return self.data.pop(mid)

    def popBack(self) -> int:
        if not self.data:
            return -1
        return self.data.pop()


class FrontMiddleBackQueueDeque:
    """
    Single deque implementation for clarity.
    """

    def __init__(self):
        self.q = deque()

    def pushFront(self, val: int) -> None:
        self.q.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        mid = len(self.q) // 2
        self.q.rotate(-mid)
        self.q.appendleft(val)
        self.q.rotate(mid)

    def pushBack(self, val: int) -> None:
        self.q.append(val)

    def popFront(self) -> int:
        return self.q.popleft() if self.q else -1

    def popMiddle(self) -> int:
        if not self.q:
            return -1
        mid = (len(self.q) - 1) // 2
        self.q.rotate(-mid)
        val = self.q.popleft()
        self.q.rotate(mid)
        return val

    def popBack(self) -> int:
        return self.q.pop() if self.q else -1
