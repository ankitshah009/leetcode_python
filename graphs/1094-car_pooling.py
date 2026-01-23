#1094. Car Pooling
#Medium
#
#There is a car with capacity empty seats. The vehicle only drives east
#(i.e., it cannot turn around and drive west).
#
#You are given the integer capacity and an array trips where trips[i] =
#[numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi
#passengers and the locations to pick them up and drop them off are fromi
#and toi respectively. The locations are given as the number of kilometers
#due east from the car's initial location.
#
#Return true if it is possible to pick up and drop off all passengers for
#all the given trips, or false otherwise.
#
#Example 1:
#Input: trips = [[2,1,5],[3,3,7]], capacity = 4
#Output: false
#
#Example 2:
#Input: trips = [[2,1,5],[3,3,7]], capacity = 5
#Output: true
#
#Constraints:
#    1 <= trips.length <= 1000
#    trips[i].length == 3
#    1 <= numPassengersi <= 100
#    0 <= fromi < toi <= 1000
#    1 <= capacity <= 10^5

from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Difference array / sweep line algorithm.
        Track passenger changes at each location.
        """
        changes = [0] * 1001

        for num, start, end in trips:
            changes[start] += num
            changes[end] -= num

        current = 0
        for change in changes:
            current += change
            if current > capacity:
                return False

        return True


class SolutionSortedEvents:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """Event-based approach with sorting"""
        events = []
        for num, start, end in trips:
            events.append((start, num))   # Pick up
            events.append((end, -num))    # Drop off

        events.sort()

        current = 0
        for _, change in events:
            current += change
            if current > capacity:
                return False

        return True


class SolutionHeap:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """Min heap for ongoing trips"""
        import heapq

        trips = sorted(trips, key=lambda x: x[1])
        heap = []  # (end_time, num_passengers)
        current = 0

        for num, start, end in trips:
            # Drop off passengers whose trip ended
            while heap and heap[0][0] <= start:
                _, passengers = heapq.heappop(heap)
                current -= passengers

            # Pick up new passengers
            current += num
            if current > capacity:
                return False

            heapq.heappush(heap, (end, num))

        return True
