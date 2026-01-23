#1861. Rotating the Box
#Medium
#
#You are given an m x n matrix of characters box representing a side-view of a
#box. Each cell of the box is one of the following:
#- A stone '#'
#- A stationary obstacle '*'
#- Empty '.'
#
#The box is rotated 90 degrees clockwise, causing some of the stones to fall
#due to gravity. Each stone falls down until it lands on an obstacle, another
#stone, or the bottom of the box. Gravity does not affect the obstacles'
#positions, and the inertia from the box's rotation does not affect the stones'
#horizontal positions.
#
#It is guaranteed that each stone in box rests on an obstacle, another stone,
#or the bottom of the box.
#
#Return an n x m matrix representing the box after the rotation described
#above.
#
#Example 1:
#Input: box = [["#",".","#"]]
#Output: [["."],["#"],["#"]]
#
#Example 2:
#Input: box = [["#",".","*","."],
#              ["#","#","*","."]]
#Output: [["#","."],
#         ["#","#"],
#         ["*","*"],
#         [".","."]]
#
#Constraints:
#    m == box.length
#    n == box[i].length
#    1 <= m, n <= 500
#    box[i][j] is either '#', '*', or '.'.

from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
        1. Apply gravity (stones fall right)
        2. Rotate 90 degrees clockwise
        """
        m, n = len(box), len(box[0])

        # Apply gravity to each row (stones fall to the right)
        for row in box:
            empty = n - 1  # Rightmost empty position

            for col in range(n - 1, -1, -1):
                if row[col] == '*':
                    empty = col - 1
                elif row[col] == '#':
                    row[col] = '.'
                    row[empty] = '#'
                    empty -= 1

        # Rotate 90 degrees clockwise
        # new[j][m-1-i] = old[i][j]
        # Or: new[col][m-1-row] for each (row, col)
        result = [['' for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = box[i][j]

        return result


class SolutionCombined:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
        Rotate first, then apply gravity (stones fall down).
        """
        m, n = len(box), len(box[0])

        # Rotate 90 degrees clockwise
        rotated = [[box[m - 1 - j][i] for j in range(m)] for i in range(n)]

        new_m, new_n = n, m

        # Apply gravity (stones fall down in each column)
        for col in range(new_n):
            empty = new_m - 1

            for row in range(new_m - 1, -1, -1):
                if rotated[row][col] == '*':
                    empty = row - 1
                elif rotated[row][col] == '#':
                    rotated[row][col] = '.'
                    rotated[empty][col] = '#'
                    empty -= 1

        return rotated
