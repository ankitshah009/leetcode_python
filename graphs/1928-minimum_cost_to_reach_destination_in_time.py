#1928. Minimum Cost to Reach Destination in Time
#Hard
#
#There is a country of n cities numbered from 0 to n - 1 where all the cities
#are connected by bi-directional roads. The roads are represented as a 2D
#integer array edges where edges[i] = [x_i, y_i, time_i] denotes a road between
#cities x_i and y_i that takes time_i minutes to travel. There may be multiple
#roads of differing travel times connecting the same two cities, but no road
#connects a city to itself.
#
#Each time you pass through a city, you must pay a passing fee. This is
#represented as a 0-indexed integer array passingFees of length n where
#passingFees[j] is the amount of dollars you must pay when you pass through
#city j.
#
#In the beginning, you are at city 0 and want to reach city n - 1 in maxTime
#minutes or less. The cost of your journey is the sum of passing fees for each
#city that you passed through at some point of your journey (including the
#source and destination cities).
#
#Given maxTime, edges, and passingFees, return the minimum cost to complete
#your journey, or -1 if you cannot complete it within maxTime minutes.
#
#Example 1:
#Input: maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],
#       [4,5,15]], passingFees = [5,1,2,20,20,3]
#Output: 11
#
#Example 2:
#Input: maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],
#       [4,5,15]], passingFees = [5,1,2,20,20,3]
#Output: 48
#
#Constraints:
#    1 <= maxTime <= 1000
#    n == passingFees.length
#    2 <= n <= 1000
#    n - 1 <= edges.length <= 1000
#    0 <= x_i, y_i <= n - 1
#    1 <= time_i <= 1000
#    1 <= passingFees[j] <= 1000

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        """
        Dijkstra with state (city, time).
        """
        n = len(passingFees)

        # Build graph
        graph = defaultdict(list)
        for x, y, t in edges:
            graph[x].append((y, t))
            graph[y].append((x, t))

        # min_cost[city][time] = min cost to reach city in exactly 'time' minutes
        # Too much memory, use min_time[city] = min time to reach with current cost
        INF = float('inf')

        # (cost, time, city)
        heap = [(passingFees[0], 0, 0)]
        # min_time[city] = minimum time to reach this city (for pruning)
        min_time = [INF] * n
        min_time[0] = 0

        while heap:
            cost, time, city = heapq.heappop(heap)

            if city == n - 1:
                return cost

            if time > min_time[city]:
                continue

            for neighbor, travel_time in graph[city]:
                new_time = time + travel_time

                if new_time <= maxTime and new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    new_cost = cost + passingFees[neighbor]
                    heapq.heappush(heap, (new_cost, new_time, neighbor))

        return -1


class SolutionDP:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        """
        DP: dp[t][city] = min cost to reach city in exactly t minutes.
        """
        n = len(passingFees)
        INF = float('inf')

        # dp[t][city] = min cost
        dp = [[INF] * n for _ in range(maxTime + 1)]
        dp[0][0] = passingFees[0]

        # Build edge list per city
        graph = defaultdict(list)
        for x, y, t in edges:
            graph[x].append((y, t))
            graph[y].append((x, t))

        for t in range(maxTime + 1):
            for city in range(n):
                if dp[t][city] == INF:
                    continue

                for neighbor, travel_time in graph[city]:
                    new_time = t + travel_time
                    if new_time <= maxTime:
                        new_cost = dp[t][city] + passingFees[neighbor]
                        dp[new_time][neighbor] = min(dp[new_time][neighbor], new_cost)

        result = min(dp[t][n - 1] for t in range(maxTime + 1))
        return result if result != INF else -1
