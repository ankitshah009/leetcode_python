#1656. Design an Ordered Stream
#Easy
#
#There is a stream of n (idKey, value) pairs arriving in an arbitrary order,
#where idKey is an integer between 1 and n and value is a string. No two pairs
#have the same id.
#
#Design a stream that returns the values in increasing order of their IDs by
#returning a chunk (list) of values after each insertion. The concatenation of
#all the chunks should result in a list of the sorted values.
#
#Implement the OrderedStream class:
#- OrderedStream(int n) Constructs the stream to take n values.
#- String[] insert(int idKey, String value) Inserts the pair (idKey, value)
#  into the stream, then returns the largest possible chunk of currently
#  inserted values that appear next in the order.
#
#Example 1:
#Input: ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
#       [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
#Output: [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
#
#Constraints:
#    1 <= n <= 1000
#    1 <= id <= n
#    value.length == 5
#    value consists only of lowercase letters.
#    Each call to insert will have a unique id.
#    Exactly n calls will be made to insert.

from typing import List

class OrderedStream:
    """
    Simple array-based implementation with pointer.
    """

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)  # 1-indexed
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        result = []

        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])
            self.ptr += 1

        return result


class OrderedStreamDict:
    """
    Dictionary-based implementation.
    """

    def __init__(self, n: int):
        self.n = n
        self.data = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey] = value
        result = []

        while self.ptr in self.data:
            result.append(self.data[self.ptr])
            self.ptr += 1

        return result


class OrderedStreamCompact:
    """
    Compact implementation.
    """

    def __init__(self, n: int):
        self.stream = [''] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        result = []

        while self.ptr < len(self.stream) and self.stream[self.ptr]:
            result.append(self.stream[self.ptr])
            self.ptr += 1

        return result


class OrderedStreamGenerator:
    """
    Implementation with deferred processing.
    """

    def __init__(self, n: int):
        self.stream = {}
        self.ptr = 1
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value

        # Collect consecutive values starting from ptr
        start = self.ptr
        while self.ptr <= self.n and self.ptr in self.stream:
            self.ptr += 1

        return [self.stream[i] for i in range(start, self.ptr)]
