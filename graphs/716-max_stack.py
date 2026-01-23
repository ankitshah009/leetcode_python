#716. Max Stack
#Hard
#
#Design a max stack data structure that supports the stack operations and
#supports finding the stack's maximum element.
#
#Implement the MaxStack class:
#- MaxStack() Initializes the stack object.
#- void push(int x) Pushes element x onto the stack.
#- int pop() Removes the element on top of the stack and returns it.
#- int top() Gets the element on the top of the stack without removing it.
#- int peekMax() Retrieves the maximum element in the stack without removing it.
#- int popMax() Retrieves the maximum element in the stack and removes it. If
#  there is more than one maximum element, only remove the top-most one.
#
#You must come up with a solution that supports O(1) for each top call and
#O(log n) for each other call.
#
#Example 1:
#Input: ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax",
#        "pop", "top"]
#       [[], [5], [1], [5], [], [], [], [], [], []]
#Output: [null, null, null, null, 5, 5, 1, 5, 1, 5]
#
#Constraints:
#    -10^7 <= x <= 10^7
#    At most 10^5 calls will be made to push, pop, top, peekMax, and popMax.
#    There will be at least one element in the stack when pop, top, peekMax,
#    or popMax is called.

from sortedcontainers import SortedList

class MaxStack:
    """
    Use doubly-linked list for O(1) removal + SortedList for O(log n) max.
    """

    class Node:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = self.Node(0)  # Dummy
        self.tail = self.Node(0)  # Dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        # SortedList of (val, id, node) for max tracking
        self.sorted = SortedList(key=lambda x: (x[0], x[1]))
        self.id = 0

    def _add_node(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def push(self, x: int) -> None:
        node = self.Node(x)
        self._add_node(node)
        self.sorted.add((x, self.id, node))
        self.id += 1

    def pop(self) -> int:
        node = self.tail.prev
        self._remove_node(node)
        # Remove from sorted list
        for i in range(len(self.sorted) - 1, -1, -1):
            if self.sorted[i][2] is node:
                self.sorted.pop(i)
                break
        return node.val

    def top(self) -> int:
        return self.tail.prev.val

    def peekMax(self) -> int:
        return self.sorted[-1][0]

    def popMax(self) -> int:
        val, _, node = self.sorted.pop()
        self._remove_node(node)
        return val


class MaxStackSimple:
    """Simple two-stack solution - O(n) for popMax"""

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        max_val = self.peekMax()
        buffer = []

        while self.top() != max_val:
            buffer.append(self.pop())

        self.pop()  # Remove the max

        while buffer:
            self.push(buffer.pop())

        return max_val
