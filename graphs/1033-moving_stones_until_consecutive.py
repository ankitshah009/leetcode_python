#1033. Moving Stones Until Consecutive
#Medium
#
#Three stones are on a number line at positions a, b, and c.
#
#Each turn, you pick up a stone at an endpoint (i.e., either the lowest or
#highest position stone), and move it to an unoccupied position between
#those endpoints. Formally, let's say the stones are currently at positions
#x, y, z with x < y < z. You pick up the stone at either position x or
#position z, and move that stone to an integer position k, with x < k < z
#and k != y.
#
#The game ends when you cannot make any more moves (i.e., the stones are in
#consecutive positions).
#
#Return an integer array answer of length 2 where:
#    answer[0] is the minimum number of moves you can make, and
#    answer[1] is the maximum number of moves you can make.
#
#Example 1:
#Input: a = 1, b = 2, c = 5
#Output: [1,2]
#Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.
#
#Example 2:
#Input: a = 4, b = 3, c = 2
#Output: [0,0]
#Explanation: We cannot make any moves.
#
#Example 3:
#Input: a = 3, b = 5, c = 1
#Output: [1,2]
#
#Constraints:
#    1 <= a, b, c <= 100
#    a, b, and c have different values.

from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        """
        Sort positions, then analyze gaps.

        Max moves: sum of gaps - 2 (move one step at a time)
        Min moves:
            - 0 if already consecutive
            - 1 if any gap is 1 or 2 (can fill in one move)
            - 2 otherwise
        """
        x, y, z = sorted([a, b, c])

        # Maximum: move one step at a time
        max_moves = (z - y - 1) + (y - x - 1)

        # Minimum
        if x + 1 == y and y + 1 == z:
            min_moves = 0  # Already consecutive
        elif y - x <= 2 or z - y <= 2:
            min_moves = 1  # Gap of 1 or 2
        else:
            min_moves = 2  # Need to move both endpoints

        return [min_moves, max_moves]


class SolutionDetailed:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        """More explicit case analysis"""
        stones = sorted([a, b, c])
        x, y, z = stones

        gap1 = y - x - 1  # Gap between x and y
        gap2 = z - y - 1  # Gap between y and z

        # Maximum moves
        max_moves = gap1 + gap2

        # Minimum moves
        if gap1 == 0 and gap2 == 0:
            min_moves = 0
        elif gap1 == 0 or gap2 == 0:
            # One side already consecutive
            min_moves = 1
        elif gap1 == 1 or gap2 == 1:
            # Gap of exactly 1 - can put stone there in one move
            min_moves = 1
        else:
            min_moves = 2

        return [min_moves, max_moves]
