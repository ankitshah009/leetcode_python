#251. Flatten 2D Vector
#Medium
#
#Design an iterator to flatten a 2D vector. It should support the next and hasNext
#operations.
#
#Implement the Vector2D class:
#    Vector2D(int[][] vec) Initializes the object with the 2D vector vec.
#    next() Returns the next element from the 2D vector and moves the pointer
#    one step forward. You may assume that all the calls to next are valid.
#    hasNext() Returns true if there are still some elements in the vector, and
#    false otherwise.
#
#Example 1:
#Input
#["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
#[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
#Output
#[null, 1, 2, 3, true, true, 4, false]
#
#Explanation
#Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
#vector2D.next();    // return 1
#vector2D.next();    // return 2
#vector2D.next();    // return 3
#vector2D.hasNext(); // return True
#vector2D.hasNext(); // return True
#vector2D.next();    // return 4
#vector2D.hasNext(); // return False
#
#Constraints:
#    0 <= vec.length <= 200
#    0 <= vec[i].length <= 500
#    -500 <= vec[i][j] <= 500
#    At most 10^5 calls will be made to next and hasNext.

class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.outer = 0  # Current row index
        self.inner = 0  # Current column index

    def _advance_to_next(self):
        # Move pointers to next valid element
        while self.outer < len(self.vec) and self.inner >= len(self.vec[self.outer]):
            self.outer += 1
            self.inner = 0

    def next(self) -> int:
        self._advance_to_next()
        result = self.vec[self.outer][self.inner]
        self.inner += 1
        return result

    def hasNext(self) -> bool:
        self._advance_to_next()
        return self.outer < len(self.vec)


class Vector2DFlattened:
    """Alternative: Flatten during initialization"""

    def __init__(self, vec: List[List[int]]):
        self.flattened = []
        for row in vec:
            self.flattened.extend(row)
        self.index = 0

    def next(self) -> int:
        result = self.flattened[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.flattened)


class Vector2DGenerator:
    """Using Python generator"""

    def __init__(self, vec: List[List[int]]):
        def flatten():
            for row in vec:
                for val in row:
                    yield val

        self.gen = flatten()
        self.next_val = None
        self._load_next()

    def _load_next(self):
        try:
            self.next_val = next(self.gen)
        except StopIteration:
            self.next_val = None

    def next(self) -> int:
        result = self.next_val
        self._load_next()
        return result

    def hasNext(self) -> bool:
        return self.next_val is not None
