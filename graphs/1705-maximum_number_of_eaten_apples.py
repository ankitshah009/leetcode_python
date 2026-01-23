#1705. Maximum Number of Eaten Apples
#Medium
#
#There is a special kind of apple tree that grows apples every day for n days.
#On the ith day, the tree grows apples[i] apples that will rot after days[i]
#days, that is on day i + days[i] the apples will be rotten and cannot be eaten.
#On some days, the apple tree does not grow any apples.
#
#You can eat at most one apple a day (to stay healthy). Note that you can keep
#eating after the first n days.
#
#Return the maximum number of apples you can eat.
#
#Example 1:
#Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
#Output: 7
#
#Example 2:
#Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
#Output: 5
#
#Constraints:
#    n == apples.length == days.length
#    1 <= n <= 2 * 10^4
#    0 <= apples[i], days[i] <= 2 * 10^4

from typing import List
import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        """
        Greedy with min heap - always eat apple expiring soonest.
        Heap stores (expiry_day, count).
        """
        n = len(apples)
        heap = []  # (expiry_day, apple_count)
        eaten = 0
        day = 0

        while day < n or heap:
            # Add new apples
            if day < n and apples[day] > 0:
                expiry = day + days[day]
                heapq.heappush(heap, (expiry, apples[day]))

            # Remove rotten apples
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)

            # Eat one apple (earliest expiring)
            if heap:
                expiry, count = heapq.heappop(heap)
                eaten += 1
                if count > 1:
                    heapq.heappush(heap, (expiry, count - 1))

            day += 1

        return eaten


class SolutionDetailed:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        """
        Same approach with more detailed comments.
        """
        n = len(apples)
        min_heap = []
        total_eaten = 0
        current_day = 0

        while current_day < n or min_heap:
            # Day current_day: new apples grow
            if current_day < n:
                if apples[current_day] > 0:
                    # These apples expire on day (current_day + days[current_day])
                    expiry_day = current_day + days[current_day]
                    heapq.heappush(min_heap, (expiry_day, apples[current_day]))

            # Remove all batches that have expired
            while min_heap and min_heap[0][0] <= current_day:
                heapq.heappop(min_heap)

            # Eat one apple from the batch expiring soonest
            if min_heap:
                expiry, count = heapq.heappop(min_heap)
                total_eaten += 1

                # If batch has more apples, put it back
                if count > 1:
                    heapq.heappush(min_heap, (expiry, count - 1))

            current_day += 1

        return total_eaten
