#225. Implement Stack using Queues
#Easy
#
#Implement a last-in-first-out (LIFO) stack using only two queues. The
#implemented stack should support all the functions of a normal stack
#(push, top, pop, and empty).
#
#Implement the MyStack class:
#    void push(int x) Pushes element x to the top of the stack.
#    int pop() Removes the element on the top of the stack and returns it.
#    int top() Returns the element on the top of the stack.
#    boolean empty() Returns true if the stack is empty, false otherwise.
#
#Notes:
#    You must use only standard operations of a queue -- which means that only
#    push to back, peek/pop from front, size and is empty operations are valid.
#    Depending on your language, the queue may not be supported natively.
#
#Example:
#Input
#["MyStack", "push", "push", "top", "pop", "empty"]
#[[], [1], [2], [], [], []]
#Output
#[null, null, null, 2, 2, false]
#
#Follow-up: Can you implement the stack using only one queue?

from collections import deque

class MyStack:
    """Using two queues - O(n) push"""

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)

        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Swap queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


class MyStackOneQueue:
    """Using single queue - O(n) push"""

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

        # Rotate the queue to put new element at front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


class MyStackPopHeavy:
    """O(n) pop, O(1) push"""

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        # Move all but last element to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        result = self.q1.popleft()

        # Swap queues
        self.q1, self.q2 = self.q2, self.q1

        return result

    def top(self) -> int:
        # Move all but last element to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        result = self.q1[0]
        self.q2.append(self.q1.popleft())

        # Swap queues
        self.q1, self.q2 = self.q2, self.q1

        return result

    def empty(self) -> bool:
        return not self.q1
