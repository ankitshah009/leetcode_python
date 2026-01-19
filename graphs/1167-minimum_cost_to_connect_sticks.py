#1167. Minimum Cost to Connect Sticks
#Medium
#
#You have some number of sticks with positive integer lengths. These lengths are
#given as an array sticks, where sticks[i] is the length of the ith stick.
#
#You can connect any two sticks of lengths x and y into one stick by paying a
#cost of x + y. You must connect all the sticks until there is only one stick
#remaining.
#
#Return the minimum cost of connecting all the given sticks into one stick in
#this way.
#
#Example 1:
#Input: sticks = [2,4,3]
#Output: 14
#Explanation: You start with sticks = [2,4,3].
#1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
#2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
#There is only one stick left, so you are done. The total cost is 5 + 9 = 14.
#
#Example 2:
#Input: sticks = [1,8,3,5]
#Output: 30
#Explanation: You start with sticks = [1,8,3,5].
#1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
#2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
#3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
#The total cost is 4 + 9 + 17 = 30.
#
#Example 3:
#Input: sticks = [5]
#Output: 0
#
#Constraints:
#    1 <= sticks.length <= 10^4
#    1 <= sticks[i] <= 10^4

from typing import List
import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """
        Min heap - always combine two smallest sticks.
        Similar to Huffman encoding.
        """
        if len(sticks) <= 1:
            return 0

        heapq.heapify(sticks)
        total_cost = 0

        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)

            cost = first + second
            total_cost += cost
            heapq.heappush(sticks, cost)

        return total_cost


class SolutionSorted:
    """Using sorted list (less efficient but educational)"""

    def connectSticks(self, sticks: List[int]) -> int:
        from sortedcontainers import SortedList

        if len(sticks) <= 1:
            return 0

        sl = SortedList(sticks)
        total_cost = 0

        while len(sl) > 1:
            first = sl.pop(0)
            second = sl.pop(0)

            cost = first + second
            total_cost += cost
            sl.add(cost)

        return total_cost


class SolutionTwoQueues:
    """Using two queues for O(n log n) time due to initial sort"""

    def connectSticks(self, sticks: List[int]) -> int:
        from collections import deque

        if len(sticks) <= 1:
            return 0

        sticks.sort()
        q1 = deque(sticks)
        q2 = deque()
        total_cost = 0

        def get_min():
            if not q1:
                return q2.popleft()
            if not q2:
                return q1.popleft()
            return q1.popleft() if q1[0] <= q2[0] else q2.popleft()

        while len(q1) + len(q2) > 1:
            first = get_min()
            second = get_min()

            cost = first + second
            total_cost += cost
            q2.append(cost)

        return total_cost
