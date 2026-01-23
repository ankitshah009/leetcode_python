#939. Minimum Area Rectangle
#Medium
#
#You are given an array of points in the X-Y plane points where points[i] =
#[xi, yi].
#
#Return the minimum area of a rectangle formed from these points, with sides
#parallel to the X and Y axes. If there is not any such rectangle, return 0.
#
#Example 1:
#Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
#Output: 4
#
#Example 2:
#Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
#Output: 2
#
#Constraints:
#    1 <= points.length <= 500
#    points[i].length == 2
#    0 <= xi, yi <= 4 * 10^4
#    All the given points are unique.

class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        """
        For each pair of diagonal points, check if the other two corners exist.
        """
        point_set = set(map(tuple, points))
        min_area = float('inf')
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                # Must be diagonal (different x and y)
                if x1 != x2 and y1 != y2:
                    # Check if other two corners exist
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        min_area = min(min_area, area)

        return min_area if min_area != float('inf') else 0


class SolutionByColumns:
    """Group points by x-coordinate"""

    def minAreaRect(self, points: list[list[int]]) -> int:
        from collections import defaultdict

        # Group y values by x
        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)

        # For efficiency, only consider columns with 2+ points
        columns = {x: sorted(ys) for x, ys in columns.items() if len(ys) >= 2}

        # Track previously seen (y1, y2) pairs and their x-coordinate
        last_x = {}
        min_area = float('inf')

        for x in sorted(columns.keys()):
            ys = columns[x]
            for i in range(len(ys)):
                for j in range(i + 1, len(ys)):
                    y1, y2 = ys[i], ys[j]

                    if (y1, y2) in last_x:
                        area = (x - last_x[(y1, y2)]) * (y2 - y1)
                        min_area = min(min_area, area)

                    last_x[(y1, y2)] = x

        return min_area if min_area != float('inf') else 0


class SolutionHash:
    """Using hash for diagonal pairs"""

    def minAreaRect(self, points: list[list[int]]) -> int:
        point_set = {(x, y) for x, y in points}
        min_area = float('inf')

        points.sort()

        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                if x1 == x2 or y1 == y2:
                    continue

                if (x1, y2) in point_set and (x2, y1) in point_set:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    min_area = min(min_area, area)

        return min_area if min_area != float('inf') else 0
