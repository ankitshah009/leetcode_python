#1066. Campus Bikes II
#Medium
#
#On a campus represented on the X-Y plane, there are n workers and m bikes,
#with n <= m.
#
#You are given an array workers of length n where workers[i] = [xi, yi] is
#the position of the ith worker. You are also given an array bikes of length
#m where bikes[j] = [xj, yj] is the position of the jth bike. All the given
#positions are unique.
#
#Assign a bike to each worker. Among the available bikes and workers, we
#choose the (workeri, bikej) pair with the shortest Manhattan distance
#between each other, and assign the bike to that worker.
#
#Return the minimum possible sum of Manhattan distances between each worker
#and their assigned bike.
#
#Example 1:
#Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
#Output: 6
#Explanation: We assign bike 0 to worker 0, bike 1 to worker 1.
#The Manhattan distance of both assignments is 3, so the output is 6.
#
#Example 2:
#Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
#Output: 4
#
#Example 3:
#Input: workers = [[0,0],[1,0],[2,0],[3,0],[4,0]], bikes = [[0,999],[1,999],[2,999],[3,999],[4,999]]
#Output: 4995
#
#Constraints:
#    n == workers.length
#    m == bikes.length
#    1 <= n <= m <= 10
#    workers[i].length == bikes[j].length == 2
#    0 <= xi, yi < 1000
#    0 <= xj, yj < 1000
#    All worker and bike locations are unique.

from typing import List
from functools import lru_cache

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        """
        Bitmask DP: State is which bikes have been assigned.
        """
        n, m = len(workers), len(bikes)

        def dist(w, b):
            return abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])

        @lru_cache(maxsize=None)
        def dp(worker, bike_mask):
            if worker == n:
                return 0

            result = float('inf')
            for bike in range(m):
                if not (bike_mask & (1 << bike)):
                    result = min(result,
                                dist(worker, bike) + dp(worker + 1, bike_mask | (1 << bike)))

            return result

        return dp(0, 0)


class SolutionIterative:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        """Bottom-up DP with bitmask"""
        n, m = len(workers), len(bikes)

        def dist(w, b):
            return abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])

        INF = float('inf')
        # dp[mask] = min distance to assign first k workers,
        # where k = number of bits in mask
        dp = {0: 0}

        for worker in range(n):
            new_dp = {}
            for mask, cost in dp.items():
                for bike in range(m):
                    if not (mask & (1 << bike)):
                        new_mask = mask | (1 << bike)
                        new_cost = cost + dist(worker, bike)
                        new_dp[new_mask] = min(new_dp.get(new_mask, INF), new_cost)
            dp = new_dp

        return min(dp.values())


class SolutionHungarian:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        """
        This is actually assignment problem - Hungarian algorithm gives O(n^3).
        But for small n, bitmask DP is simpler.
        """
        import heapq

        n, m = len(workers), len(bikes)

        def dist(w, b):
            return abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])

        # Priority queue: (total_dist, worker_idx, bike_mask)
        heap = [(0, 0, 0)]
        visited = set()

        while heap:
            total_dist, worker, bike_mask = heapq.heappop(heap)

            if (worker, bike_mask) in visited:
                continue
            visited.add((worker, bike_mask))

            if worker == n:
                return total_dist

            for bike in range(m):
                if not (bike_mask & (1 << bike)):
                    new_mask = bike_mask | (1 << bike)
                    if (worker + 1, new_mask) not in visited:
                        heapq.heappush(heap, (total_dist + dist(worker, bike), worker + 1, new_mask))

        return -1
