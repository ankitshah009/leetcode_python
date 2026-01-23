#1286. Iterator for Combination
#Medium
#
#Design the CombinationIterator class:
#    CombinationIterator(string characters, int combinationLength) Initializes
#    the object with a string characters of sorted distinct lowercase English
#    letters and a number combinationLength as arguments.
#    next() Returns the next combination of length combinationLength in
#    lexicographical order.
#    hasNext() Returns true if and only if there exists a next combination.
#
#Example 1:
#Input:
#["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
#[["abc", 2], [], [], [], [], [], []]
#Output: [null, "ab", true, "ac", true, "bc", false]
#Explanation:
#CombinationIterator itr = new CombinationIterator("abc", 2);
#itr.next();    // return "ab"
#itr.hasNext(); // return True
#itr.next();    // return "ac"
#itr.hasNext(); // return True
#itr.next();    // return "bc"
#itr.hasNext(); // return False
#
#Constraints:
#    1 <= combinationLength <= characters.length <= 15
#    All the characters of characters are unique.
#    At most 10^4 calls will be made to next and hasNext.
#    It is guaranteed that all calls of the function next are valid.

from itertools import combinations

class CombinationIterator:
    """Pre-generate all combinations using itertools."""

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = list(combinations(characters, combinationLength))
        self.index = 0

    def next(self) -> str:
        result = ''.join(self.combinations[self.index])
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)


class CombinationIteratorBitmask:
    """Use bitmask to iterate through combinations."""

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.length = combinationLength
        self.n = len(characters)
        # Start with all 1s in positions for lexicographically smallest
        self.mask = (1 << self.n) - 1  # Will find first valid

    def next(self) -> str:
        # Find next valid mask (with exactly combinationLength bits set)
        while self.mask >= 0:
            if bin(self.mask).count('1') == self.length:
                result = []
                for i in range(self.n):
                    if self.mask & (1 << (self.n - 1 - i)):
                        result.append(self.chars[i])
                self.mask -= 1
                return ''.join(result)
            self.mask -= 1
        return ""

    def hasNext(self) -> bool:
        temp = self.mask
        while temp >= 0:
            if bin(temp).count('1') == self.length:
                return True
            temp -= 1
        return False


class CombinationIteratorGenerator:
    """Generate combinations on the fly."""

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.length = combinationLength
        self.n = len(characters)
        # Store current indices
        self.indices = list(range(combinationLength))
        self.finished = False

    def next(self) -> str:
        result = ''.join(self.chars[i] for i in self.indices)

        # Find rightmost index that can be incremented
        i = self.length - 1
        while i >= 0 and self.indices[i] == self.n - self.length + i:
            i -= 1

        if i < 0:
            self.finished = True
        else:
            self.indices[i] += 1
            for j in range(i + 1, self.length):
                self.indices[j] = self.indices[j - 1] + 1

        return result

    def hasNext(self) -> bool:
        return not self.finished
