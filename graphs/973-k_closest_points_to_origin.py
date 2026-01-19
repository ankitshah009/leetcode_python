#973. K Closest Points to Origin
#Medium
#
#Given an array of points where points[i] = [xi, yi] represents a point on the
#X-Y plane and an integer k, return the k closest points to the origin (0, 0).
#
#The distance between two points on the X-Y plane is the Euclidean distance
#(i.e., √(x1 - x2)^2 + (y1 - y2)^2).
#
#You may return the answer in any order. The answer is guaranteed to be unique
#(except for the order that it is in).
#
#Example 1:
#Input: points = [[1,3],[-2,2]], k = 1
#Output: [[-2,2]]
#Explanation: The distance between (1, 3) and the origin is sqrt(10).
#The distance between (-2, 2) and the origin is sqrt(8).
#Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
#
#Example 2:
#Input: points = [[3,3],[5,-1],[-2,4]], k = 2
#Output: [[3,3],[-2,4]]
#
#Constraints:
#    1 <= k <= points.length <= 10^4
#    -10^4 <= xi, yi <= 10^4

from typing import List
import heapq
import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Max heap of size k - O(n log k) time"""
        # Use max heap (negate distances)
        heap = []

        for x, y in points:
            dist = -(x * x + y * y)
            if len(heap) < k:
                heapq.heappush(heap, (dist, x, y))
            elif dist > heap[0][0]:
                heapq.heapreplace(heap, (dist, x, y))

        return [[x, y] for _, x, y in heap]


class SolutionSort:
    """Sort by distance - O(n log n) time"""

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0] * p[0] + p[1] * p[1])
        return points[:k]


class SolutionQuickSelect:
    """Quickselect - O(n) average time"""

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point):
            return point[0] * point[0] + point[1] * point[1]

        def partition(left, right, pivot_idx):
            pivot_dist = dist(points[pivot_idx])
            points[pivot_idx], points[right] = points[right], points[pivot_idx]
            store_idx = left

            for i in range(left, right):
                if dist(points[i]) < pivot_dist:
                    points[store_idx], points[i] = points[i], points[store_idx]
                    store_idx += 1

            points[right], points[store_idx] = points[store_idx], points[right]
            return store_idx

        left, right = 0, len(points) - 1

        while left < right:
            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)

            if pivot_idx == k:
                break
            elif pivot_idx < k:
                left = pivot_idx + 1
            else:
                right = pivot_idx - 1

        return points[:k]


class SolutionHeapify:
    """Using heapq.nsmallest"""

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda p: p[0] * p[0] + p[1] * p[1])
