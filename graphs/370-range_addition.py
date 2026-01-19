#370. Range Addition
#Medium
#
#You are given an integer length and an array updates where
#updates[i] = [startIdxi, endIdxi, inci].
#
#You have an array arr of length length with all zeros, and you have some
#update operations to perform.
#
#In the ith update, you should add inci to each of the elements
#arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi].
#
#Return arr after performing all the updates.
#
#Example 1:
#Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
#Output: [-2,0,3,5,3]
#
#Explanation:
#Initial state: [0,0,0,0,0]
#After [1,3,2]: [0,2,2,2,0]
#After [2,4,3]: [0,2,5,5,3]
#After [0,2,-2]: [-2,0,3,5,3]
#
#Constraints:
#    1 <= length <= 10^5
#    0 <= updates.length <= 10^4
#    0 <= startIdxi <= endIdxi < length
#    -1000 <= inci <= 1000

from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        Difference array approach - O(n + k) where k is number of updates.

        Instead of updating entire range, mark the start and end+1 positions.
        Then compute prefix sum to get actual values.
        """
        diff = [0] * (length + 1)

        for start, end, inc in updates:
            diff[start] += inc
            diff[end + 1] -= inc

        # Compute prefix sum
        result = [0] * length
        running_sum = 0

        for i in range(length):
            running_sum += diff[i]
            result[i] = running_sum

        return result


class SolutionBruteForce:
    """Brute force O(n * k) - for reference"""

    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * length

        for start, end, inc in updates:
            for i in range(start, end + 1):
                arr[i] += inc

        return arr


class SolutionSweepLine:
    """Using sweep line with events"""

    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        from collections import defaultdict

        events = defaultdict(int)

        for start, end, inc in updates:
            events[start] += inc
            events[end + 1] -= inc

        result = [0] * length
        current = 0

        for i in range(length):
            current += events[i]
            result[i] = current

        return result
