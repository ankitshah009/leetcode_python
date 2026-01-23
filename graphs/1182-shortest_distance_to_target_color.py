#1182. Shortest Distance to Target Color
#Medium
#
#You are given an array colors, in which there are three colors: 1, 2, and 3.
#
#You are also given some queries. Each query consists of two integers i and c,
#return the shortest distance between the given index i and the target color c.
#If there is no solution return -1.
#
#Example 1:
#Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
#Output: [3,0,3]
#Explanation:
#The nearest 3 from index 1 is at index 4 (3 steps away).
#The nearest 2 from index 2 is at index 2 itself (0 steps away).
#The nearest 1 from index 6 is at index 3 (3 steps away).
#
#Example 2:
#Input: colors = [1,2], queries = [[0,3]]
#Output: [-1]
#Explanation: There is no 3 in the array.
#
#Constraints:
#    1 <= colors.length <= 5 * 10^4
#    1 <= colors[i] <= 3
#    1 <= queries.length <= 5 * 10^4
#    queries[i].length == 2
#    0 <= queries[i][0] < colors.length
#    1 <= queries[i][1] <= 3

from typing import List
import bisect

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        """
        Precompute positions of each color.
        For each query, binary search to find closest position.
        """
        # Store positions for each color
        positions = {1: [], 2: [], 3: []}

        for i, c in enumerate(colors):
            positions[c].append(i)

        result = []

        for i, c in queries:
            pos_list = positions[c]

            if not pos_list:
                result.append(-1)
                continue

            # Binary search for closest position
            idx = bisect.bisect_left(pos_list, i)

            min_dist = float('inf')

            # Check position at idx
            if idx < len(pos_list):
                min_dist = min(min_dist, pos_list[idx] - i)

            # Check position at idx - 1
            if idx > 0:
                min_dist = min(min_dist, i - pos_list[idx - 1])

            result.append(min_dist)

        return result


class SolutionDP:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        """
        Precompute distance to each color for every index.
        Two passes: left to right and right to left.
        """
        n = len(colors)
        INF = float('inf')

        # dist[i][c] = distance from index i to nearest color c+1
        dist = [[INF] * 3 for _ in range(n)]

        # Left to right pass
        last_seen = [-INF, -INF, -INF]  # Last seen index of each color

        for i in range(n):
            last_seen[colors[i] - 1] = i
            for c in range(3):
                if last_seen[c] != -INF:
                    dist[i][c] = i - last_seen[c]

        # Right to left pass
        last_seen = [INF, INF, INF]

        for i in range(n - 1, -1, -1):
            last_seen[colors[i] - 1] = i
            for c in range(3):
                if last_seen[c] != INF:
                    dist[i][c] = min(dist[i][c], last_seen[c] - i)

        result = []
        for i, c in queries:
            d = dist[i][c - 1]
            result.append(d if d != INF else -1)

        return result
