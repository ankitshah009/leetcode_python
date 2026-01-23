#1090. Largest Values From Labels
#Medium
#
#There is a set of n items. You are given two integer arrays values and
#labels where the value and the label of the ith element are values[i] and
#labels[i] respectively. You are also given two integers numWanted and
#useLimit.
#
#Choose a subset s of the n elements such that:
#    The size of the subset s is less than or equal to numWanted.
#    There are at most useLimit items with the same label in s.
#
#The score of a subset is the sum of the values in the subset.
#
#Return the maximum score of a subset s.
#
#Example 1:
#Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
#Output: 9
#Explanation: The subset chosen is the first, third, and fifth items.
#
#Example 2:
#Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
#Output: 12
#Explanation: The subset chosen is the first, second, and third items.
#
#Example 3:
#Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
#Output: 16
#Explanation: The subset chosen is the first and fourth items.
#
#Constraints:
#    n == values.length == labels.length
#    1 <= n <= 2 * 10^4
#    0 <= values[i], labels[i] <= 2 * 10^4
#    1 <= numWanted, useLimit <= n

from typing import List
from collections import Counter

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int],
                              numWanted: int, useLimit: int) -> int:
        """
        Greedy: Sort by value, pick highest values respecting label limit.
        """
        items = sorted(zip(values, labels), reverse=True)

        label_count = Counter()
        result = 0
        selected = 0

        for value, label in items:
            if selected >= numWanted:
                break
            if label_count[label] < useLimit:
                result += value
                label_count[label] += 1
                selected += 1

        return result


class SolutionHeap:
    def largestValsFromLabels(self, values: List[int], labels: List[int],
                              numWanted: int, useLimit: int) -> int:
        """Max heap approach"""
        import heapq

        # Max heap (negate values)
        items = [(-v, l) for v, l in zip(values, labels)]
        heapq.heapify(items)

        label_count = Counter()
        result = 0
        selected = 0

        while items and selected < numWanted:
            neg_val, label = heapq.heappop(items)
            if label_count[label] < useLimit:
                result -= neg_val
                label_count[label] += 1
                selected += 1

        return result
