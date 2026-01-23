#554. Brick Wall
#Medium
#
#There is a rectangular brick wall in front of you with n rows of bricks. The ith
#row has some number of bricks each of the same height (i.e., one unit) but they
#can be of different widths. The total width of each row is the same.
#
#Draw a vertical line from the top to the bottom and cross the least bricks. If
#your line goes through the edge of a brick, then the brick is not considered as
#crossed. You cannot draw a line just along one of the two vertical edges of the
#wall, in which case the line will obviously cross no bricks.
#
#Given the 2D array wall that contains the information about the wall, return the
#minimum number of crossed bricks after drawing such a vertical line.
#
#Example 1:
#Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
#Output: 2
#
#Example 2:
#Input: wall = [[1],[1],[1]]
#Output: 3
#
#Constraints:
#    n == wall.length
#    1 <= n <= 10^4
#    1 <= wall[i].length <= 10^4
#    1 <= sum(wall[i].length) <= 2 * 10^4
#    sum(wall[i]) is the same for each row i.
#    1 <= wall[i][j] <= 2^31 - 1

from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        Count edges at each position.
        Line crossing max edges crosses min bricks.
        """
        edge_count = defaultdict(int)

        for row in wall:
            pos = 0
            for i in range(len(row) - 1):  # Don't count last edge
                pos += row[i]
                edge_count[pos] += 1

        max_edges = max(edge_count.values(), default=0)
        return len(wall) - max_edges


class SolutionExplicit:
    """More explicit approach"""

    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import Counter

        # Find all edge positions (excluding wall edges)
        edges = Counter()

        for row in wall:
            position = 0
            for brick in row[:-1]:  # Skip last brick
                position += brick
                edges[position] += 1

        if not edges:
            return len(wall)

        # Line at position with most edges crosses fewest bricks
        most_common_edge = max(edges.values())
        return len(wall) - most_common_edge
