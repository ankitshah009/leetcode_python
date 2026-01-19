#232. Implement Queue using Stacks
#Easy
#
#Implement a first in first out (FIFO) queue using only two stacks. The
#implemented queue should support all the functions of a normal queue
#(push, peek, pop, and empty).
#
#Implement the MyQueue class:
#    void push(int x) Pushes element x to the back of the queue.
#    int pop() Removes the element from the front of the queue and returns it.
#    int peek() Returns the element at the front of the queue.
#    boolean empty() Returns true if the queue is empty, false otherwise.
#
#Notes:
#    You must use only standard operations of a stack -- only push to top,
#    peek/pop from top, size, and is empty operations are valid.
#
#Example:
#Input
#["MyQueue", "push", "push", "peek", "pop", "empty"]
#[[], [1], [2], [], [], []]
#Output
#[null, null, null, 1, 1, false]
#
#Follow-up: Can you implement the queue such that each operation is amortized
#O(1) time complexity?

class MyQueue:
    """
    Two stacks: input and output.
    Amortized O(1) for all operations.
    """

    def __init__(self):
        self.input_stack = []   # For push
        self.output_stack = []  # For pop/peek

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self.peek()  # Ensure output_stack has elements
        return self.output_stack.pop()

    def peek(self) -> int:
        if not self.output_stack:
            # Transfer all elements from input to output
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack


class MyQueueSingleStack:
    """Using recursion to simulate second stack"""

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self._push_bottom(x)

    def _push_bottom(self, x: int):
        if not self.stack:
            self.stack.append(x)
        else:
            top = self.stack.pop()
            self._push_bottom(x)
            self.stack.append(top)

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack


class MyQueueCostlyPush:
    """O(n) push, O(1) pop/peek"""

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # Move all to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # Push new element to s1
        self.s1.append(x)

        # Move all back to s1
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1
