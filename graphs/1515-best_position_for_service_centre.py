#1515. Best Position for a Service Centre
#Hard
#
#A delivery company wants to build a new service center in a new city. The
#company knows the positions of all the customers in this city on a 2D-Map and
#wants to build the new center in a position such that the sum of the euclidean
#distances to all customers is minimum.
#
#Given an array positions where positions[i] = [xi, yi] is the position of the
#ith customer on the map, return the minimum sum of the euclidean distances to
#all customers.
#
#In other words, you need to choose the position of the service center [xcentre,
#ycentre] such that the following formula is minimized:
#
#Answers within 10^-5 of the actual value will be accepted.
#
#Example 1:
#Input: positions = [[0,1],[1,0],[1,2],[2,1]]
#Output: 4.00000
#Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1]
#will make the distance to each customer = 1, the sum of all distances is 4
#which is the minimum possible we can achieve.
#
#Example 2:
#Input: positions = [[1,1],[3,3]]
#Output: 2.82843
#Explanation: The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843
#
#Constraints:
#    1 <= positions.length <= 50
#    positions[i].length == 2
#    0 <= xi, yi <= 100

from typing import List
import math

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        """
        Geometric median problem.
        Use Weiszfeld's algorithm (iteratively weighted least squares).
        """
        n = len(positions)

        if n == 1:
            return 0.0

        def total_distance(cx: float, cy: float) -> float:
            return sum(math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
                       for x, y in positions)

        # Initialize with centroid
        cx = sum(x for x, y in positions) / n
        cy = sum(y for x, y in positions) / n

        eps = 1e-7

        for _ in range(1000):  # Max iterations
            numerator_x = 0.0
            numerator_y = 0.0
            denominator = 0.0

            for x, y in positions:
                dist = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
                if dist < eps:
                    dist = eps  # Avoid division by zero

                weight = 1.0 / dist
                numerator_x += x * weight
                numerator_y += y * weight
                denominator += weight

            new_cx = numerator_x / denominator
            new_cy = numerator_y / denominator

            # Check convergence
            if abs(new_cx - cx) < eps and abs(new_cy - cy) < eps:
                break

            cx, cy = new_cx, new_cy

        return total_distance(cx, cy)


class SolutionGradientDescent:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        """
        Gradient descent approach.
        """
        n = len(positions)

        if n == 1:
            return 0.0

        def total_distance(cx: float, cy: float) -> float:
            return sum(math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
                       for x, y in positions)

        # Start with centroid
        cx = sum(x for x, y in positions) / n
        cy = sum(y for x, y in positions) / n

        # Decreasing step sizes
        step = 50.0

        while step > 1e-7:
            best_dist = total_distance(cx, cy)
            best_cx, best_cy = cx, cy

            # Try all 4 directions
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx * step, cy + dy * step
                dist = total_distance(nx, ny)
                if dist < best_dist:
                    best_dist = dist
                    best_cx, best_cy = nx, ny

            if best_cx == cx and best_cy == cy:
                # No improvement, reduce step
                step *= 0.5
            else:
                cx, cy = best_cx, best_cy

        return total_distance(cx, cy)


class SolutionTernarySearch:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        """
        Ternary search in both dimensions.
        The function is convex, so ternary search works.
        """
        def total_distance(cx: float, cy: float) -> float:
            return sum(math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
                       for x, y in positions)

        def ternary_search_y(cx: float, lo: float, hi: float) -> float:
            eps = 1e-7
            while hi - lo > eps:
                m1 = lo + (hi - lo) / 3
                m2 = hi - (hi - lo) / 3
                if total_distance(cx, m1) < total_distance(cx, m2):
                    hi = m2
                else:
                    lo = m1
            return (lo + hi) / 2

        def ternary_search_x(lo: float, hi: float) -> tuple:
            eps = 1e-7
            while hi - lo > eps:
                m1 = lo + (hi - lo) / 3
                m2 = hi - (hi - lo) / 3

                y1 = ternary_search_y(m1, 0, 100)
                y2 = ternary_search_y(m2, 0, 100)

                if total_distance(m1, y1) < total_distance(m2, y2):
                    hi = m2
                else:
                    lo = m1

            cx = (lo + hi) / 2
            cy = ternary_search_y(cx, 0, 100)
            return cx, cy

        cx, cy = ternary_search_x(0, 100)
        return total_distance(cx, cy)
