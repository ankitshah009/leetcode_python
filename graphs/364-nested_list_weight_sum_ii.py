#364. Nested List Weight Sum II
#Medium
#
#You are given a nested list of integers nestedList. Each element is either an
#integer or a list whose elements may also be integers or other lists.
#
#The depth of an integer is the number of lists that it is inside of. For
#example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to
#its depth. Let maxDepth be the maximum depth of any integer.
#
#The weight of an integer is maxDepth - (the depth of the integer) + 1.
#
#Return the sum of each integer in nestedList multiplied by its weight.
#
#Example 1:
#Input: nestedList = [[1,1],2,[1,1]]
#Output: 8
#Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
#1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
#
#Example 2:
#Input: nestedList = [1,[4,[6]]]
#Output: 17
#Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
#1*3 + 4*2 + 6*1 = 17
#
#Constraints:
#    1 <= nestedList.length <= 50
#    The values of the integers in the nested list is in the range [-100, 100].
#    The maximum depth of any integer is less than or equal to 50.

from typing import List

class NestedInteger:
    def __init__(self, value=None):
        pass

    def isInteger(self) -> bool:
        pass

    def getInteger(self) -> int:
        pass

    def getList(self) -> List['NestedInteger']:
        pass

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        """
        Two-pass: find max depth, then calculate weighted sum.
        """
        def get_max_depth(nested_list, depth):
            max_d = depth
            for item in nested_list:
                if not item.isInteger():
                    max_d = max(max_d, get_max_depth(item.getList(), depth + 1))
            return max_d

        def weighted_sum(nested_list, depth, max_depth):
            total = 0
            for item in nested_list:
                if item.isInteger():
                    total += item.getInteger() * (max_depth - depth + 1)
                else:
                    total += weighted_sum(item.getList(), depth + 1, max_depth)
            return total

        max_depth = get_max_depth(nestedList, 1)
        return weighted_sum(nestedList, 1, max_depth)


class SolutionBFS:
    """BFS level by level - accumulate sum multiple times"""

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        """
        Key insight: Instead of weight = maxDepth - depth + 1,
        we add each level's sum for each subsequent level.
        Level 1 integers are added maxDepth times,
        Level 2 integers are added maxDepth-1 times, etc.
        """
        from collections import deque

        level_sum = 0
        total = 0
        queue = nestedList[:]

        while queue:
            next_level = []
            for item in queue:
                if item.isInteger():
                    level_sum += item.getInteger()
                else:
                    next_level.extend(item.getList())

            total += level_sum  # Add accumulated sum
            queue = next_level

        return total


class SolutionOnePass:
    """Single pass with accumulated sum"""

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        weighted_sum = 0
        unweighted_sum = 0

        while nestedList:
            next_level = []
            for item in nestedList:
                if item.isInteger():
                    unweighted_sum += item.getInteger()
                else:
                    next_level.extend(item.getList())

            weighted_sum += unweighted_sum
            nestedList = next_level

        return weighted_sum
