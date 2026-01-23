#1828. Queries on Number of Points Inside a Circle
#Medium
#
#You are given an array points where points[i] = [xi, yi] is the coordinates of
#the ith point on a 2D plane. Multiple points can have the same coordinates.
#
#You are also given an array queries where queries[j] = [xj, yj, rj] describes
#a circle centered at (xj, yj) with a radius of rj.
#
#For each query, compute the number of points inside the jth circle. Points on
#the border of the circle are considered inside.
#
#Return an array answer, where answer[j] is the answer to the jth query.
#
#Example 1:
#Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
#Output: [3,2,2]
#
#Example 2:
#Input: points = [[1,1],[2,2],[3,3],[4,4],[5,5]],
#       queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
#Output: [2,3,2,4]
#
#Constraints:
#    1 <= points.length <= 500
#    points[i].length == 2
#    0 <= xi, yi <= 500
#    1 <= queries.length <= 500
#    queries[j].length == 3
#    0 <= xj, yj <= 500
#    1 <= rj <= 500
#    All coordinates are integers.

from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        For each query, count points within distance r.
        """
        result = []

        for xc, yc, r in queries:
            r_sq = r * r
            count = sum(1 for x, y in points
                       if (x - xc) ** 2 + (y - yc) ** 2 <= r_sq)
            result.append(count)

        return result


class SolutionExplicit:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        Explicit loop version.
        """
        answer = []

        for cx, cy, r in queries:
            count = 0
            for px, py in points:
                # Check if point is inside or on circle
                dx = px - cx
                dy = py - cy
                if dx * dx + dy * dy <= r * r:
                    count += 1
            answer.append(count)

        return answer


class SolutionNumpy:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        Using numpy for vectorized computation (if available).
        """
        import numpy as np

        pts = np.array(points)
        result = []

        for cx, cy, r in queries:
            dists_sq = (pts[:, 0] - cx) ** 2 + (pts[:, 1] - cy) ** 2
            count = np.sum(dists_sq <= r * r)
            result.append(int(count))

        return result
