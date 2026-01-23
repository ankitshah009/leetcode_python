#1057. Campus Bikes
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
#between each other and assign the bike to that worker.
#
#If there are multiple (workeri, bikej) pairs with the same shortest Manhattan
#distance, we choose the pair with the smallest worker index. If there are
#multiple ways to do that, we choose the pair with the smallest bike index.
#
#Repeat this process until there are no available workers.
#
#Return an array answer of length n, where answer[i] is the index of the
#bike that the ith worker is assigned to.
#
#Example 1:
#Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
#Output: [1,0]
#Explanation: Worker 1 is closer to bike 0, so worker 1 gets bike 0.
#Worker 0 gets bike 1.
#
#Example 2:
#Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
#Output: [0,2,1]
#
#Constraints:
#    n == workers.length
#    m == bikes.length
#    1 <= n <= m <= 1000
#    workers[i].length == bikes[j].length == 2
#    0 <= xi, yi < 1000
#    0 <= xj, yj < 1000
#    All worker and bike locations are unique.

from typing import List
from collections import defaultdict

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        """
        Bucket sort by distance.
        Process in order of distance, then worker index, then bike index.
        """
        n, m = len(workers), len(bikes)

        # Group pairs by Manhattan distance
        # Max distance is 2000 (grid is 1000x1000)
        buckets = defaultdict(list)

        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx - bx) + abs(wy - by)
                buckets[dist].append((i, j))

        result = [-1] * n
        used_bikes = set()

        # Process in order of distance
        for dist in sorted(buckets.keys()):
            for worker, bike in buckets[dist]:
                if result[worker] == -1 and bike not in used_bikes:
                    result[worker] = bike
                    used_bikes.add(bike)

        return result


class SolutionSorting:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        """Sort all pairs by (distance, worker_idx, bike_idx)"""
        pairs = []

        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx - bx) + abs(wy - by)
                pairs.append((dist, i, j))

        pairs.sort()

        result = [-1] * len(workers)
        used_bikes = set()

        for dist, worker, bike in pairs:
            if result[worker] == -1 and bike not in used_bikes:
                result[worker] = bike
                used_bikes.add(bike)

        return result


class SolutionHeap:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        """Min heap approach"""
        import heapq

        heap = []
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx - bx) + abs(wy - by)
                heapq.heappush(heap, (dist, i, j))

        result = [-1] * len(workers)
        used_bikes = set()
        assigned = 0

        while assigned < len(workers):
            dist, worker, bike = heapq.heappop(heap)
            if result[worker] == -1 and bike not in used_bikes:
                result[worker] = bike
                used_bikes.add(bike)
                assigned += 1

        return result
