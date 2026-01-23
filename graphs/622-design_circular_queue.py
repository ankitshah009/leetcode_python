#622. Design Circular Queue
#Medium
#
#Design your implementation of the circular queue. The circular queue is a linear
#data structure in which the operations are performed based on FIFO (First In First
#Out) principle, and the last position is connected back to the first position to
#make a circle. It is also called "Ring Buffer".
#
#Implement the MyCircularQueue class:
#- MyCircularQueue(k) Initializes the object with the size of the queue to be k.
#- int Front() Gets the front item from the queue. If the queue is empty, return -1.
#- int Rear() Gets the last item from the queue. If the queue is empty, return -1.
#- boolean enQueue(int value) Inserts an element into the circular queue. Return
#  true if the operation is successful.
#- boolean deQueue() Deletes an element from the circular queue. Return true if
#  the operation is successful.
#- boolean isEmpty() Checks whether the circular queue is empty or not.
#- boolean isFull() Checks whether the circular queue is full or not.
#
#Constraints:
#    1 <= k <= 1000
#    0 <= value <= 1000
#    At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

class MyCircularQueue:
    """Array-based circular queue"""

    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        tail = (self.head + self.count) % self.capacity
        self.queue[tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        tail = (self.head + self.count - 1) % self.capacity
        return self.queue[tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


class MyCircularQueueTwoPointers:
    """Using head and tail pointers"""

    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.head = 0
        self.tail = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
