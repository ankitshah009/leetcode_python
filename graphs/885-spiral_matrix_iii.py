#885. Spiral Matrix III
#Medium
#
#You start at the cell (rStart, cStart) of an rows x cols grid facing east.
#The northwest corner is at the first row and column in the grid, and the
#southeast corner is at the last row and column.
#
#You will walk in a clockwise spiral shape to visit every position in this grid.
#Whenever you move outside the grid's boundary, you continue your walk outside
#the grid (but may return to the grid boundary later). Eventually, you reach all
#rows * cols spaces of the grid.
#
#Return an array of coordinates representing the positions of the grid in the
#order you visited them.
#
#Example 1:
#Input: rows = 1, cols = 4, rStart = 0, cStart = 0
#Output: [[0,0],[0,1],[0,2],[0,3]]
#
#Example 2:
#Input: rows = 5, cols = 6, rStart = 1, cStart = 4
#Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
#
#Constraints:
#    1 <= rows, cols <= 100
#    0 <= rStart < rows
#    0 <= cStart < cols

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        """
        Walk in spiral pattern: E, S, W, N with increasing lengths.
        Pattern: 1 right, 1 down, 2 left, 2 up, 3 right, 3 down, ...
        """
        # Direction vectors: East, South, West, North
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        result = []
        r, c = rStart, cStart
        direction = 0  # Start facing East
        steps = 1  # Steps to take in current direction

        while len(result) < rows * cols:
            # Take 'steps' in current direction (do this twice per step increase)
            for _ in range(2):
                for _ in range(steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    r += dr[direction]
                    c += dc[direction]

                direction = (direction + 1) % 4  # Turn right

            steps += 1

        return result


class SolutionSimplified:
    """Simplified spiral walk"""

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        result = [[rStart, cStart]]
        r, c = rStart, cStart

        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        step = 1

        while len(result) < rows * cols:
            for _ in range(2):
                dr, dc = directions[d]
                for _ in range(step):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                d = (d + 1) % 4

            step += 1

        return result


class SolutionGenerator:
    """Using generator"""

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        def spiral():
            r, c = rStart, cStart
            yield r, c

            k = 1
            while True:
                for _ in range(k):
                    c += 1
                    yield r, c
                for _ in range(k):
                    r += 1
                    yield r, c
                k += 1
                for _ in range(k):
                    c -= 1
                    yield r, c
                for _ in range(k):
                    r -= 1
                    yield r, c
                k += 1

        result = []
        for r, c in spiral():
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
                if len(result) == rows * cols:
                    break

        return result
