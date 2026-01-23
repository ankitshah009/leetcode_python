#1706. Where Will the Ball Fall
#Medium
#
#You have a 2-D grid of size m x n representing a box, and you have n balls. The
#box is open on the top and bottom sides.
#
#Each cell in the box has a diagonal board spanning two corners of the cell that
#can redirect a ball to the right or to the left.
#
#- A board that redirects the ball to the right spans the top-left corner to the
#  bottom-right corner and is represented in the grid as 1.
#- A board that redirects the ball to the left spans the top-right corner to the
#  bottom-left corner and is represented in the grid as -1.
#
#Return an array answer of size n where answer[i] is the column that the ball
#falls out of at the bottom after dropping the ball from the ith column at the
#top, or -1 if the ball gets stuck in the box.
#
#Example 1:
#Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
#Output: [1,-1,-1,-1,-1]
#
#Example 2:
#Input: grid = [[-1]]
#Output: [-1]
#
#Example 3:
#Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
#Output: [0,1,2,3,4,-1]
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 100
#    grid[i][j] is 1 or -1.

from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        """
        Simulate each ball's path through the grid.
        Ball gets stuck if it forms a V shape with adjacent cell.
        """
        m, n = len(grid), len(grid[0])
        result = []

        for ball in range(n):
            col = ball

            for row in range(m):
                direction = grid[row][col]
                next_col = col + direction

                # Check if ball gets stuck
                # Stuck if: hits wall or forms V with neighbor
                if next_col < 0 or next_col >= n:
                    col = -1
                    break
                if grid[row][next_col] != direction:
                    col = -1
                    break

                col = next_col

            result.append(col)

        return result


class SolutionDFS:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        """
        DFS approach for each ball.
        """
        m, n = len(grid), len(grid[0])

        def drop(row: int, col: int) -> int:
            if row == m:
                return col

            direction = grid[row][col]
            next_col = col + direction

            # Check boundaries
            if next_col < 0 or next_col >= n:
                return -1

            # Check V shape (stuck)
            if grid[row][next_col] != direction:
                return -1

            return drop(row + 1, next_col)

        return [drop(0, col) for col in range(n)]


class SolutionMemo:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        """
        Memoized approach - reuse computations.
        """
        m, n = len(grid), len(grid[0])
        memo = {}

        def drop(row: int, col: int) -> int:
            if row == m:
                return col

            if (row, col) in memo:
                return memo[(row, col)]

            direction = grid[row][col]
            next_col = col + direction

            if next_col < 0 or next_col >= n or grid[row][next_col] != direction:
                memo[(row, col)] = -1
            else:
                memo[(row, col)] = drop(row + 1, next_col)

            return memo[(row, col)]

        return [drop(0, col) for col in range(n)]
