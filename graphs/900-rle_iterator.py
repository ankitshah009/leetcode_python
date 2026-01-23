#900. RLE Iterator
#Medium
#
#We can use run-length encoding (i.e., RLE) to encode a sequence of integers.
#In a run-length encoded array of even length encoding (0-indexed), for all
#even i, encoding[i] tells us the number of times that the non-negative integer
#value encoding[i + 1] is repeated in the sequence.
#
#Given a run-length encoded array, design an iterator that iterates through it.
#
#Implement the RLEIterator class:
#- RLEIterator(int[] encoding) Initializes the object with the encoded array.
#- int next(int n) Exhausts the next n elements and returns the last element
#  exhausted in this way. If there is no element left to exhaust, return -1.
#
#Example 1:
#Input: ["RLEIterator","next","next","next","next"]
#       [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
#Output: [null,8,8,5,-1]
#
#Constraints:
#    2 <= encoding.length <= 1000
#    encoding.length is even.
#    0 <= encoding[i] <= 10^9
#    1 <= n <= 10^9
#    At most 1000 calls will be made to next.

class RLEIterator:
    def __init__(self, encoding: list[int]):
        self.encoding = encoding
        self.index = 0  # Current position in encoding (always even)
        self.remaining = 0  # Remaining count at current position

        # Initialize first element
        if encoding:
            self.remaining = encoding[0]

    def next(self, n: int) -> int:
        while n > 0:
            if self.index >= len(self.encoding):
                return -1

            if self.remaining == 0:
                # Move to next pair
                self.index += 2
                if self.index >= len(self.encoding):
                    return -1
                self.remaining = self.encoding[self.index]
                continue

            if self.remaining >= n:
                self.remaining -= n
                return self.encoding[self.index + 1]
            else:
                n -= self.remaining
                self.remaining = 0

        return -1


class RLEIteratorSimple:
    """Simpler implementation"""

    def __init__(self, encoding: list[int]):
        self.encoding = encoding
        self.i = 0

    def next(self, n: int) -> int:
        while self.i < len(self.encoding):
            if n <= self.encoding[self.i]:
                self.encoding[self.i] -= n
                return self.encoding[self.i + 1]
            n -= self.encoding[self.i]
            self.i += 2

        return -1


class RLEIteratorDeque:
    """Using deque"""

    def __init__(self, encoding: list[int]):
        from collections import deque
        self.pairs = deque()
        for i in range(0, len(encoding), 2):
            if encoding[i] > 0:
                self.pairs.append([encoding[i], encoding[i + 1]])

    def next(self, n: int) -> int:
        while self.pairs and n > 0:
            if self.pairs[0][0] >= n:
                self.pairs[0][0] -= n
                return self.pairs[0][1]
            n -= self.pairs[0][0]
            self.pairs.popleft()

        return -1
