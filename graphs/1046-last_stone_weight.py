#1046. Last Stone Weight
#Easy
#
#You are given an array of integers stones where stones[i] is the weight of the
#ith stone.
#
#We are playing a game with the stones. On each turn, we choose the heaviest two
#stones and smash them together. Suppose the heaviest two stones have weights x
#and y with x <= y. The result of this smash is:
#- If x == y, both stones are destroyed, and
#- If x != y, the stone of weight x is destroyed, and the stone of weight y has
#  new weight y - x.
#
#At the end of the game, there is at most one stone left.
#
#Return the weight of the last remaining stone. If there are no stones left, return 0.
#
#Example 1:
#Input: stones = [2,7,4,1,8,1]
#Output: 1
#Explanation:
#We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
#we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
#we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
#we combine 1 and 1 to get 0 so the array converts to [1] then that's the value
#of the last stone.
#
#Example 2:
#Input: stones = [1]
#Output: 1
#
#Constraints:
#    1 <= stones.length <= 30
#    1 <= stones[i] <= 1000

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """Max heap simulation"""
        # Convert to max heap using negation
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # Largest
            x = -heapq.heappop(heap)  # Second largest

            if y != x:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0


class SolutionSorted:
    """Using sorted list"""

    def lastStoneWeight(self, stones: List[int]) -> int:
        from sortedcontainers import SortedList

        sl = SortedList(stones)

        while len(sl) > 1:
            y = sl.pop()  # Largest
            x = sl.pop()  # Second largest

            if y != x:
                sl.add(y - x)

        return sl[0] if sl else 0


class SolutionBruteForce:
    """Sort each iteration - O(n^2 log n)"""

    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()

            if y != x:
                stones.append(y - x)

        return stones[0] if stones else 0
