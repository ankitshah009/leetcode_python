#339. Nested List Weight Sum
#Medium
#
#You are given a nested list of integers nestedList. Each element is either an
#integer or a list whose elements may also be integers or other lists.
#
#The depth of an integer is the number of lists that it is inside of. For
#example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to
#its depth.
#
#Return the sum of each integer in nestedList multiplied by its depth.
#
#Example 1:
#Input: nestedList = [[1,1],2,[1,1]]
#Output: 10
#Explanation: Four 1's at depth 2, one 2 at depth 1.
#4*2 + 2*1 = 10.
#
#Example 2:
#Input: nestedList = [1,[4,[6]]]
#Output: 27
#Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3.
#1*1 + 4*2 + 6*3 = 27.
#
#Example 3:
#Input: nestedList = [0]
#Output: 0
#
#Constraints:
#    1 <= nestedList.length <= 50
#    The values of the integers in the nested list is in the range [-100, 100].
#    The maximum depth of any integer is less than or equal to 50.

from typing import List

# This is the interface that allows for creating nested lists.
class NestedInteger:
    def __init__(self, value=None):
        pass

    def isInteger(self) -> bool:
        """Return True if this NestedInteger holds a single integer."""
        pass

    def getInteger(self) -> int:
        """Return the single integer that this NestedInteger holds, if it holds a single integer."""
        pass

    def getList(self) -> List['NestedInteger']:
        """Return the nested list that this NestedInteger holds, if it holds a nested list."""
        pass

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """DFS approach"""
        def dfs(nested_list, depth):
            total = 0
            for item in nested_list:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    total += dfs(item.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)


class SolutionBFS:
    """BFS approach with level tracking"""

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        from collections import deque

        queue = deque([(item, 1) for item in nestedList])
        total = 0

        while queue:
            item, depth = queue.popleft()

            if item.isInteger():
                total += item.getInteger() * depth
            else:
                for nested_item in item.getList():
                    queue.append((nested_item, depth + 1))

        return total


class SolutionIterative:
    """Iterative DFS using stack"""

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        stack = [(item, 1) for item in nestedList]
        total = 0

        while stack:
            item, depth = stack.pop()

            if item.isInteger():
                total += item.getInteger() * depth
            else:
                for nested_item in item.getList():
                    stack.append((nested_item, depth + 1))

        return total
