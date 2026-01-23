#1476. Subrectangle Queries
#Medium
#
#Implement the class SubrectangleQueries which receives a rows x cols rectangle
#as a matrix of integers in the constructor and supports two methods:
#
#1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
#   Updates all values with newValue in the subrectangle whose upper left
#   coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
#
#2. getValue(int row, int col)
#   Returns the current value of the coordinate (row,col) from the rectangle.
#
#Example 1:
#Input
#["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
#[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
#Output
#[null,1,null,5,5,null,10,5]
#
#Example 2:
#Input
#["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
#[[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
#Output
#[null,1,null,100,100,null,20]
#
#Constraints:
#    There will be at most 500 operations considering both methods.
#    1 <= rows, cols <= 100
#    rows == rectangle.length
#    cols == rectangle[i].length
#    0 <= row1 <= row2 < rows
#    0 <= col1 <= col2 < cols
#    1 <= newValue, rectangle[i][j] <= 10^9
#    0 <= row < rows
#    0 <= col < cols

from typing import List

class SubrectangleQueries:
    """
    Store updates and apply lazily during getValue.
    Good when updates >> getValue calls.
    """

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.updates = []  # List of (r1, c1, r2, c2, val)

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updates.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        # Check updates in reverse order (latest first)
        for r1, c1, r2, c2, val in reversed(self.updates):
            if r1 <= row <= r2 and c1 <= col <= c2:
                return val
        return self.rectangle[row][col]


class SubrectangleQueriesEager:
    """
    Apply updates immediately.
    Good when getValue >> updates.
    """

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.rectangle[r][c] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


class SubrectangleQueriesHybrid:
    """
    Hybrid: apply updates periodically.
    """

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.updates = []
        self.threshold = 10  # Apply updates when this many accumulated

    def _apply_updates(self):
        """Apply all pending updates to rectangle"""
        for r1, c1, r2, c2, val in self.updates:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    self.rectangle[r][c] = val
        self.updates = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updates.append((row1, col1, row2, col2, newValue))
        if len(self.updates) >= self.threshold:
            self._apply_updates()

    def getValue(self, row: int, col: int) -> int:
        # Check updates in reverse order
        for r1, c1, r2, c2, val in reversed(self.updates):
            if r1 <= row <= r2 and c1 <= col <= c2:
                return val
        return self.rectangle[row][col]


class SubrectangleQueriesSlice:
    """
    Use row slice assignment for faster updates.
    """

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2 + 1):
            self.rectangle[r][col1:col2 + 1] = [newValue] * (col2 - col1 + 1)

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
