#356. Line Reflection
#Medium
#
#Given n points on a 2D plane, find if there is such a line parallel to the
#y-axis that reflects the given set of points symmetrically.
#
#In other words, answer whether or not if there exists a line that after
#reflecting all points over the given line, the original points' set is the
#same as the reflected ones.
#
#Note that there can be repeated points.
#
#Example 1:
#Input: points = [[1,1],[-1,1]]
#Output: true
#Explanation: We can choose the line x = 0.
#
#Example 2:
#Input: points = [[1,1],[-1,-1]]
#Output: false
#Explanation: We can't choose a line.
#
#Constraints:
#    n == points.length
#    1 <= n <= 10^4
#    -10^8 <= points[i][j] <= 10^8

from typing import List

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        """
        If there's a reflection line x = c, then for every point (x, y),
        there must be a point (2c - x, y).

        The line x = c where c = (min_x + max_x) / 2
        """
        if not points:
            return True

        point_set = set()
        min_x = float('inf')
        max_x = float('-inf')

        for x, y in points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            point_set.add((x, y))

        # The reflection line is at x = (min_x + max_x) / 2
        # For point (x, y), its reflection is at (min_x + max_x - x, y)
        sum_x = min_x + max_x

        for x, y in points:
            reflected_x = sum_x - x
            if (reflected_x, y) not in point_set:
                return False

        return True


class SolutionGroupByY:
    """Group points by y-coordinate"""

    def isReflected(self, points: List[List[int]]) -> bool:
        from collections import defaultdict

        if not points:
            return True

        # Group by y coordinate
        y_groups = defaultdict(set)
        for x, y in points:
            y_groups[y].add(x)

        # Find the reflection line
        all_x = [x for x, y in points]
        target_sum = min(all_x) + max(all_x)

        # Check each y-group
        for y, x_coords in y_groups.items():
            for x in x_coords:
                if target_sum - x not in x_coords:
                    return False

        return True
