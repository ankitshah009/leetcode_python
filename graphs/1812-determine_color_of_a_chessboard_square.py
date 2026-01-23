#1812. Determine Color of a Chessboard Square
#Easy
#
#You are given coordinates, a string that represents the coordinates of a
#square of the chessboard. Below is a chessboard for your reference.
#
#Return true if the square is white, and false if the square is black.
#
#The coordinate will always represent a valid chessboard square. The coordinate
#will always have the letter first, and the number second.
#
#Example 1:
#Input: coordinates = "a1"
#Output: false
#
#Example 2:
#Input: coordinates = "h3"
#Output: true
#
#Example 3:
#Input: coordinates = "c7"
#Output: false
#
#Constraints:
#    coordinates.length == 2
#    'a' <= coordinates[0] <= 'h'
#    '1' <= coordinates[1] <= '8'

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        """
        White if sum of coordinates is odd.
        a=1, b=2, ..., h=8
        """
        col = ord(coordinates[0]) - ord('a') + 1
        row = int(coordinates[1])
        return (col + row) % 2 == 1


class SolutionAlt:
    def squareIsWhite(self, coordinates: str) -> bool:
        """
        Using XOR of parities.
        """
        return (ord(coordinates[0]) + ord(coordinates[1])) % 2 == 1


class SolutionExplicit:
    def squareIsWhite(self, coordinates: str) -> bool:
        """
        Explicit pattern matching.
        """
        col = coordinates[0]
        row = int(coordinates[1])

        # Odd columns (a, c, e, g) have white on even rows
        # Even columns (b, d, f, h) have white on odd rows
        if col in 'aceg':
            return row % 2 == 0
        else:
            return row % 2 == 1
