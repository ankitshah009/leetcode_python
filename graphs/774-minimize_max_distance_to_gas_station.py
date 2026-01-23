#774. Minimize Max Distance to Gas Station
#Hard
#
#You are given an integer array stations that represents the positions of the
#gas stations on the x-axis. You are also given an integer k.
#
#You should add k new gas stations. You can add the stations anywhere on the
#x-axis, and not necessarily on an integer position.
#
#Let penalty() be the maximum distance between adjacent gas stations after
#adding the k new stations.
#
#Return the smallest possible value of penalty(). Answers within 10^-6 of the
#actual answer will be accepted.
#
#Example 1:
#Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
#Output: 0.50000
#
#Example 2:
#Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1
#Output: 14.00000
#
#Constraints:
#    10 <= stations.length <= 2000
#    0 <= stations[i] <= 10^8
#    stations is sorted in a strictly increasing order.
#    1 <= k <= 10^6

class Solution:
    def minmaxGasDist(self, stations: list[int], k: int) -> float:
        """
        Binary search on the answer (max distance).
        """
        # Calculate gaps between stations
        gaps = [stations[i + 1] - stations[i] for i in range(len(stations) - 1)]

        def stations_needed(max_dist):
            """Count stations needed to make all gaps <= max_dist."""
            count = 0
            for gap in gaps:
                count += int(gap / max_dist)
            return count

        # Binary search
        left, right = 0, max(gaps)

        while right - left > 1e-6:
            mid = (left + right) / 2
            if stations_needed(mid) <= k:
                right = mid
            else:
                left = mid

        return left


class SolutionHeap:
    """Greedy with max-heap (TLE for large k but conceptually correct)"""

    def minmaxGasDist(self, stations: list[int], k: int) -> float:
        import heapq

        # Heap: (-average_gap, original_gap, num_segments)
        heap = []
        for i in range(len(stations) - 1):
            gap = stations[i + 1] - stations[i]
            heapq.heappush(heap, (-gap, gap, 1))

        for _ in range(k):
            neg_avg, original, segments = heapq.heappop(heap)
            segments += 1
            new_avg = original / segments
            heapq.heappush(heap, (-new_avg, original, segments))

        return -heap[0][0]


class SolutionBinarySearchOptimized:
    """Optimized binary search"""

    def minmaxGasDist(self, stations: list[int], k: int) -> float:
        n = len(stations)
        gaps = [stations[i + 1] - stations[i] for i in range(n - 1)]

        left, right = 0, 10**8

        while right - left > 1e-6:
            mid = (left + right) / 2

            count = sum(int(gap / mid) for gap in gaps)

            if count <= k:
                right = mid
            else:
                left = mid

        return left
