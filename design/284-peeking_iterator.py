#284. Peeking Iterator
#Medium
#
#Design an iterator that supports the peek operation on an existing iterator in
#addition to the hasNext and the next operations.
#
#Implement the PeekingIterator class:
#    PeekingIterator(Iterator<int> nums) Initializes the object with the given
#    integer iterator iterator.
#    int peek() Returns the next element in the array without moving the pointer.
#    int next() Returns the next element in the array and moves the pointer to
#    the next element.
#    boolean hasNext() Returns true if there are still elements in the array.
#
#Example 1:
#Input
#["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
#[[[1, 2, 3]], [], [], [], [], []]
#Output
#[null, 1, 2, 2, 3, false]
#
#Explanation
#PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
#peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
#peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
#peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
#peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
#peekingIterator.hasNext(); // return False
#
#Constraints:
#    1 <= nums.length <= 1000
#    1 <= nums[i] <= 1000
#    All the calls to next and peek are valid.
#    At most 1000 calls will be made to next, hasNext, and peek.
#
#Follow up: How would you extend your design to be generic and work with all types,
#not just integer?

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator: 'Iterator'):
        self.iterator = iterator
        self.peeked_value = None
        self.has_peeked = False

    def peek(self) -> int:
        if not self.has_peeked:
            self.peeked_value = self.iterator.next()
            self.has_peeked = True
        return self.peeked_value

    def next(self) -> int:
        if self.has_peeked:
            self.has_peeked = False
            return self.peeked_value
        return self.iterator.next()

    def hasNext(self) -> bool:
        return self.has_peeked or self.iterator.hasNext()


class PeekingIteratorAlwaysCache:
    """Alternative: Always keep next value cached"""

    def __init__(self, iterator: 'Iterator'):
        self.iterator = iterator
        self._load_next()

    def _load_next(self):
        if self.iterator.hasNext():
            self.next_val = self.iterator.next()
            self.has_next = True
        else:
            self.next_val = None
            self.has_next = False

    def peek(self) -> int:
        return self.next_val

    def next(self) -> int:
        result = self.next_val
        self._load_next()
        return result

    def hasNext(self) -> bool:
        return self.has_next
