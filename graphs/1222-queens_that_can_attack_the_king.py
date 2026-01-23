#1222. Queens That Can Attack the King
#Medium
#
#On a 0-indexed 8 x 8 chessboard, there can be multiple black queens and one
#white king.
#
#You are given a 2D integer array queens where queens[i] = [xQueeni, yQueeni]
#represents the position of the ith black queen on the chessboard. You are
#also given an integer array king of length 2 where king = [xKing, yKing]
#represents the position of the white king.
#
#Return the coordinates of the black queens that can directly attack the king.
#You may return the answer in any order.
#
#Example 1:
#Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
#Output: [[0,1],[1,0],[3,3]]
#Explanation: The diagram above shows the three queens that can directly attack
#the king and the three queens that cannot.
#
#Example 2:
#Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
#Output: [[2,2],[3,4],[4,4]]
#
#Constraints:
#    1 <= queens.length < 64
#    queens[i].length == king.length == 2
#    0 <= xQueeni, yQueeni, xKing, yKing < 8
#    All the given positions are unique.

from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        """
        Search from king in all 8 directions.
        Stop when we find a queen or go out of bounds.
        """
        queen_set = set(map(tuple, queens))
        kx, ky = king

        # 8 directions: horizontal, vertical, diagonal
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        result = []

        for dx, dy in directions:
            x, y = kx + dx, ky + dy

            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in queen_set:
                    result.append([x, y])
                    break
                x += dx
                y += dy

        return result


class SolutionQueenPerspective:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        """
        From each queen, check if it can see the king.
        Track closest queen in each direction.
        """
        kx, ky = king

        # For each direction, track closest queen
        # Direction encoded as (sign(dx), sign(dy))
        closest = {}

        for qx, qy in queens:
            dx, dy = qx - kx, qy - ky

            # Check if queen is in line with king
            if dx == 0 or dy == 0 or abs(dx) == abs(dy):
                # Get direction
                dir_x = 0 if dx == 0 else dx // abs(dx)
                dir_y = 0 if dy == 0 else dy // abs(dy)
                direction = (dir_x, dir_y)

                distance = max(abs(dx), abs(dy))

                if direction not in closest or distance < closest[direction][0]:
                    closest[direction] = (distance, [qx, qy])

        return [pos for _, pos in closest.values()]
