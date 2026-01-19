#281. Zigzag Iterator
#Medium
#
#Given two vectors of integers v1 and v2, implement an iterator to return their
#elements alternately.
#
#Implement the ZigzagIterator class:
#    ZigzagIterator(List<int> v1, List<int> v2) Initializes the object with the
#    two vectors v1 and v2.
#    next() Returns the current element from the iterator and moves the iterator
#    to the next element.
#    hasNext() Returns true if the iterator still has elements, and false otherwise.
#
#Example 1:
#Input: v1 = [1,2], v2 = [3,4,5,6]
#Output: [1,3,2,4,5,6]
#Explanation: By calling next repeatedly until hasNext returns false, the order
#of elements returned by next should be: [1,3,2,4,5,6].
#
#Example 2:
#Input: v1 = [1], v2 = []
#Output: [1]
#
#Example 3:
#Input: v1 = [], v2 = [1]
#Output: [1]
#
#Constraints:
#    0 <= v1.length, v2.length <= 1000
#    1 <= v1.length + v2.length <= 2000
#    -2^31 <= v1[i], v2[i] <= 2^31 - 1
#
#Follow up: What if you are given k 1d vectors? How well can your code be extended
#to such cases?

from collections import deque

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = deque()
        if v1:
            self.queue.append((v1, 0))
        if v2:
            self.queue.append((v2, 0))

    def next(self) -> int:
        vec, idx = self.queue.popleft()
        result = vec[idx]

        # If more elements in this vector, add back to queue
        if idx + 1 < len(vec):
            self.queue.append((vec, idx + 1))

        return result

    def hasNext(self) -> bool:
        return len(self.queue) > 0


class ZigzagIteratorKVectors:
    """Extended for k vectors"""

    def __init__(self, vectors: List[List[int]]):
        self.queue = deque()
        for vec in vectors:
            if vec:
                self.queue.append(iter(vec))

    def next(self) -> int:
        iterator = self.queue.popleft()
        result = next(iterator)

        # Try to get next element to see if iterator has more
        try:
            peek = next(iterator)
            # Put back the peeked value and iterator
            self.queue.append(self._prepend_iterator(peek, iterator))
        except StopIteration:
            pass  # Iterator exhausted, don't add back

        return result

    def _prepend_iterator(self, first_val, rest_iter):
        yield first_val
        yield from rest_iter

    def hasNext(self) -> bool:
        return len(self.queue) > 0


class ZigzagIteratorSimple:
    """Simple two-pointer approach for two vectors"""

    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.i1 = 0
        self.i2 = 0
        self.turn = 0  # 0 for v1, 1 for v2

    def next(self) -> int:
        # Find next valid vector
        while True:
            if self.turn == 0 and self.i1 < len(self.v1):
                result = self.v1[self.i1]
                self.i1 += 1
                self.turn = 1
                return result
            elif self.turn == 1 and self.i2 < len(self.v2):
                result = self.v2[self.i2]
                self.i2 += 1
                self.turn = 0
                return result
            else:
                # Current turn's vector is exhausted, try other
                self.turn = 1 - self.turn

    def hasNext(self) -> bool:
        return self.i1 < len(self.v1) or self.i2 < len(self.v2)
