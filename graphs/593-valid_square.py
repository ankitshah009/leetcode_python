#593. Valid Square
#Medium
#
#Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true
#if the four points construct a square.
#
#The coordinate of a point pi is represented as [xi, yi]. The input is not given
#in any order.
#
#A valid square has four equal sides with positive length and four equal angles
#(90-degree angles).
#
#Example 1:
#Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
#Output: true
#
#Example 2:
#Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
#Output: false
#
#Example 3:
#Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
#Output: true
#
#Constraints:
#    p1.length == p2.length == p3.length == p4.length == 2
#    -10^4 <= xi, yi <= 10^4

from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        A square has 4 equal sides and 2 equal diagonals.
        Calculate all 6 distances, should have exactly 2 unique values
        with count 4 (sides) and 2 (diagonals), and diagonals > sides.
        """
        def dist_sq(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2

        points = [p1, p2, p3, p4]
        distances = []

        for i in range(4):
            for j in range(i + 1, 4):
                distances.append(dist_sq(points[i], points[j]))

        distances.sort()

        # Should have 4 equal sides (smaller) and 2 equal diagonals (larger)
        # All distances should be positive (no overlapping points)
        return (distances[0] > 0 and
                distances[0] == distances[1] == distances[2] == distances[3] and
                distances[4] == distances[5] and
                distances[0] * 2 == distances[4])  # diagonal = side * sqrt(2)


class SolutionSet:
    """Using set to check unique distances"""

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist_sq(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2

        points = [p1, p2, p3, p4]
        distances = set()

        for i in range(4):
            for j in range(i + 1, 4):
                d = dist_sq(points[i], points[j])
                if d == 0:
                    return False
                distances.add(d)

        return len(distances) == 2
