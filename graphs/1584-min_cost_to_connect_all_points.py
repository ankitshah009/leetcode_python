#1584. Min Cost to Connect All Points
#Medium
#
#You are given an array points representing integer coordinates of some points on a 2D-plane,
#where points[i] = [xi, yi].
#
#The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between
#them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
#
#Return the minimum cost to make all points connected. All points are connected if there is
#exactly one simple path between any two points.
#
#Example 1:
#Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
#Output: 20
#Explanation: We can connect the points as shown above to get the minimum cost of 20.
#Notice that there is a unique path between every pair of points.
#
#Example 2:
#Input: points = [[3,12],[-2,5],[-4,1]]
#Output: 18
#
#Constraints:
#    1 <= points.length <= 1000
#    -10^6 <= xi, yi <= 10^6
#    All pairs (xi, yi) are distinct.

import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0

        # Prim's algorithm
        visited = [False] * n
        min_cost = 0
        edges_used = 0

        # Min heap: (cost, point_index)
        heap = [(0, 0)]

        while edges_used < n:
            cost, curr = heapq.heappop(heap)

            if visited[curr]:
                continue

            visited[curr] = True
            min_cost += cost
            edges_used += 1

            # Add edges to all unvisited points
            for next_point in range(n):
                if not visited[next_point]:
                    dist = abs(points[curr][0] - points[next_point][0]) + \
                           abs(points[curr][1] - points[next_point][1])
                    heapq.heappush(heap, (dist, next_point))

        return min_cost
