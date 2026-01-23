#1620. Coordinate With Maximum Network Quality
#Medium
#
#You are given an array of network towers towers, where towers[i] = [xi, yi, qi]
#denotes the ith network tower with location (xi, yi) and quality factor qi.
#All the coordinates are integral coordinates on the X-Y plane, and the distance
#between two coordinates is the Euclidean distance.
#
#You are also given an integer radius where a tower is reachable if the distance
#is less than or equal to radius. Outside that distance, the signal becomes
#garbled, and the tower is not reachable.
#
#The signal quality of the ith tower at a coordinate (x, y) is calculated with
#the formula ⌊qi / (1 + d)⌋, where d is the distance between the tower and the
#coordinate. The network quality at a coordinate is the sum of the signal
#qualities from all the reachable towers.
#
#Return the array [cx, cy] representing the integral coordinate (cx, cy) where
#the network quality is maximum. If there are multiple coordinates with the
#same network quality, return the lexicographically minimum non-negative coordinate.
#
#Note:
#- A coordinate (x1, y1) is lexicographically smaller than (x2, y2) if either:
#  x1 < x2, or x1 == x2 and y1 < y2.
#- ⌊val⌋ is the greatest integer less than or equal to val (the floor function).
#
#Example 1:
#Input: towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
#Output: [2,1]
#Explanation: At coordinate (2, 1) the total quality is 13.
#
#Example 2:
#Input: towers = [[23,11,21]], radius = 9
#Output: [23,11]
#
#Example 3:
#Input: towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
#Output: [1,2]
#
#Constraints:
#    1 <= towers.length <= 50
#    towers[i].length == 3
#    0 <= xi, yi, qi <= 50
#    1 <= radius <= 50

from typing import List
import math

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        """
        Brute force: Check all coordinates in the bounding box.
        Since coordinates are 0-50, we check all (51 x 51) points.
        """
        max_quality = 0
        best = [0, 0]

        # Determine search range
        max_x = max(t[0] for t in towers)
        max_y = max(t[1] for t in towers)

        for x in range(max_x + radius + 1):
            for y in range(max_y + radius + 1):
                quality = 0

                for tx, ty, q in towers:
                    d = math.sqrt((x - tx) ** 2 + (y - ty) ** 2)
                    if d <= radius:
                        quality += int(q / (1 + d))

                if quality > max_quality:
                    max_quality = quality
                    best = [x, y]

        return best


class SolutionOptimized:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        """
        Slightly optimized with early termination.
        """
        def compute_quality(x: int, y: int) -> int:
            total = 0
            for tx, ty, q in towers:
                dist = math.sqrt((x - tx) ** 2 + (y - ty) ** 2)
                if dist <= radius:
                    total += int(q / (1 + dist))
            return total

        # Search in reasonable bounds
        max_coord = 50

        best_quality = -1
        best_coord = [0, 0]

        for x in range(max_coord + 1):
            for y in range(max_coord + 1):
                q = compute_quality(x, y)
                if q > best_quality:
                    best_quality = q
                    best_coord = [x, y]

        return best_coord


class SolutionBoundedSearch:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        """
        Search only within the bounding box of towers.
        """
        if not towers:
            return [0, 0]

        min_x = max(0, min(t[0] for t in towers) - radius)
        max_x = max(t[0] for t in towers) + radius
        min_y = max(0, min(t[1] for t in towers) - radius)
        max_y = max(t[1] for t in towers) + radius

        # Cap at 50 based on constraints
        max_x = min(max_x, 50)
        max_y = min(max_y, 50)

        best_quality = 0
        best = [0, 0]

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                quality = 0
                for tx, ty, q in towers:
                    d = math.sqrt((x - tx) ** 2 + (y - ty) ** 2)
                    if d <= radius:
                        quality += int(q / (1 + d))

                if quality > best_quality or (quality == best_quality and [x, y] < best):
                    best_quality = quality
                    best = [x, y]

        return best
