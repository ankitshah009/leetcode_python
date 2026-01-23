#871. Minimum Number of Refueling Stops
#Hard
#
#A car travels from a starting position to a destination which is target miles
#east of the starting position.
#
#There are gas stations along the way. The gas stations are represented as an
#array stations where stations[i] = [positioni, fueli] indicates that the ith
#gas station is positioni miles east of the starting position and has fueli
#liters of gas.
#
#The car starts with an infinite tank of gas, which initially has startFuel
#liters of fuel in it. It uses one liter of gas per one mile that it drives.
#When the car reaches a gas station, it may stop and refuel, transferring all
#the gas from the station into the car.
#
#Return the minimum number of refueling stops the car must make in order to
#reach its destination. If it cannot reach the destination, return -1.
#
#Example 1:
#Input: target = 1, startFuel = 1, stations = []
#Output: 0
#
#Example 2:
#Input: target = 100, startFuel = 1, stations = [[10,100]]
#Output: -1
#
#Example 3:
#Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
#Output: 2
#
#Constraints:
#    1 <= target, startFuel <= 10^9
#    0 <= stations.length <= 500
#    1 <= positioni < positioni+1 < target
#    1 <= fueli < 10^9

import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        """
        Greedy with max-heap: at each station, save fuel.
        When stuck, use largest saved fuel.
        """
        # Max-heap of fuel amounts (negative for max-heap)
        heap = []
        fuel = startFuel
        stops = 0
        prev_pos = 0

        stations.append([target, 0])  # Add target as final "station"

        for pos, station_fuel in stations:
            fuel -= (pos - prev_pos)

            # While we can't reach this station, use saved fuel
            while heap and fuel < 0:
                fuel += -heapq.heappop(heap)
                stops += 1

            if fuel < 0:
                return -1

            heapq.heappush(heap, -station_fuel)
            prev_pos = pos

        return stops


class SolutionDP:
    """DP approach: dp[i] = max distance with i stops"""

    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        n = len(stations)
        # dp[i] = max distance reachable with i refueling stops
        dp = [startFuel] + [0] * n

        for i, (pos, fuel) in enumerate(stations):
            # Process in reverse to avoid using station twice
            for j in range(i, -1, -1):
                if dp[j] >= pos:
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)

        for i in range(n + 1):
            if dp[i] >= target:
                return i

        return -1


class SolutionSimulation:
    """Direct simulation with heap"""

    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        max_heap = []
        fuel = startFuel
        idx = 0
        stops = 0

        while fuel < target:
            # Add all reachable stations to heap
            while idx < len(stations) and stations[idx][0] <= fuel:
                heapq.heappush(max_heap, -stations[idx][1])
                idx += 1

            if not max_heap:
                return -1

            fuel += -heapq.heappop(max_heap)
            stops += 1

        return stops
