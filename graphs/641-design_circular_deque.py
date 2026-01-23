#641. Design Circular Deque
#Medium
#
#Design your implementation of the circular double-ended queue (deque).
#
#Implement the MyCircularDeque class:
#- MyCircularDeque(int k) Initializes the deque with a maximum size of k.
#- boolean insertFront(int value) Adds an item at the front of Deque. Returns true
#  if the operation is successful, or false otherwise.
#- boolean insertLast(int value) Adds an item at the rear of Deque. Returns true
#  if the operation is successful, or false otherwise.
#- boolean deleteFront() Deletes an item from the front of Deque. Returns true if
#  the operation is successful, or false otherwise.
#- boolean deleteLast() Deletes an item from the rear of Deque. Returns true if
#  the operation is successful, or false otherwise.
#- int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
#- int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
#- boolean isEmpty() Returns true if the deque is empty, or false otherwise.
#- boolean isFull() Returns true if the deque is full, or false otherwise.
#
#Constraints:
#    1 <= k <= 1000
#    0 <= value <= 1000
#    At most 2000 calls will be made to insertFront, insertLast, deleteFront,
#    deleteLast, getFront, getRear, isEmpty, isFull.

class MyCircularDeque:
    """Array-based circular deque"""

    def __init__(self, k: int):
        self.capacity = k
        self.data = [0] * k
        self.front = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        rear = (self.front + self.size) % self.capacity
        self.data[rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        rear = (self.front + self.size - 1) % self.capacity
        return self.data[rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


class MyCircularDequeLinkedList:
    """Doubly linked list implementation"""

    class Node:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = self.Node(-1)  # Dummy head
        self.tail = self.Node(-1)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        node = self.Node(value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        node = self.Node(value)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.next.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
