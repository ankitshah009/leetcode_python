#341. Flatten Nested List Iterator
#Medium
#
#You are given a nested list of integers nestedList. Each element is either an
#integer or a list whose elements may also be integers or other lists.
#Implement an iterator to flatten it.
#
#Implement the NestedIterator class:
#- NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with
#  the nested list nestedList.
#- int next() Returns the next integer in the nested list.
#- boolean hasNext() Returns true if there are still some integers in the
#  nested list and false otherwise.
#
#Example 1:
#Input: nestedList = [[1,1],2,[1,1]]
#Output: [1,1,2,1,1]
#
#Example 2:
#Input: nestedList = [1,[4,[6]]]
#Output: [1,4,6]
#
#Constraints:
#    1 <= nestedList.length <= 500
#    The values of the integers in the nested list is in the range [-10^6, 10^6].

from typing import List

class NestedInteger:
    def isInteger(self) -> bool:
        pass

    def getInteger(self) -> int:
        pass

    def getList(self) -> List['NestedInteger']:
        pass

class NestedIterator:
    """Stack-based lazy flattening"""

    def __init__(self, nestedList: List[NestedInteger]):
        # Stack stores items in reverse order
        self.stack = nestedList[::-1]

    def next(self) -> int:
        # hasNext ensures top of stack is an integer
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        # Flatten until we have an integer at the top
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            # Pop the list and push its elements in reverse
            self.stack.pop()
            self.stack.extend(top.getList()[::-1])
        return False


class NestedIteratorEager:
    """Eager flattening - flatten everything upfront"""

    def __init__(self, nestedList: List[NestedInteger]):
        self.flattened = []
        self._flatten(nestedList)
        self.index = 0

    def _flatten(self, nested_list):
        for item in nested_list:
            if item.isInteger():
                self.flattened.append(item.getInteger())
            else:
                self._flatten(item.getList())

    def next(self) -> int:
        result = self.flattened[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.flattened)


class NestedIteratorGenerator:
    """Using generator for lazy evaluation"""

    def __init__(self, nestedList: List[NestedInteger]):
        def flatten(nested):
            for item in nested:
                if item.isInteger():
                    yield item.getInteger()
                else:
                    yield from flatten(item.getList())

        self.gen = flatten(nestedList)
        self.next_val = None
        self.has_next = False
        self._advance()

    def _advance(self):
        try:
            self.next_val = next(self.gen)
            self.has_next = True
        except StopIteration:
            self.has_next = False

    def next(self) -> int:
        result = self.next_val
        self._advance()
        return result

    def hasNext(self) -> bool:
        return self.has_next
