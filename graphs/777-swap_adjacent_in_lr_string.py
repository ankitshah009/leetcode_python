#777. Swap Adjacent in LR String
#Medium
#
#In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move
#consists of either replacing one occurrence of "XL" with "LX", or replacing
#one occurrence of "RX" with "XR". Given the starting string start and the
#ending string end, return True if and only if there exists a sequence of moves
#to transform start to end.
#
#Example 1:
#Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
#Output: true
#Explanation: We can transform start to end following these steps:
#RXXLRXRXL ->
#XRXLRXRXL ->
#XRLXRXRXL ->
#XRLXXRRXL ->
#XRLXXRRLX
#
#Example 2:
#Input: start = "X", end = "L"
#Output: false
#
#Constraints:
#    1 <= start.length <= 10^4
#    start.length == end.length
#    Both start and end will only consist of characters in 'L', 'R', and 'X'.

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        L can only move left, R can only move right.
        Check relative order and positions.
        """
        # Remove X and check if L/R sequence is same
        if start.replace('X', '') != end.replace('X', ''):
            return False

        # Get positions of L and R in both strings
        n = len(start)
        j = 0

        for i in range(n):
            if start[i] == 'X':
                continue

            # Find corresponding position in end
            while j < n and end[j] == 'X':
                j += 1

            # Check position constraints
            if start[i] == 'L' and i < j:
                return False  # L cannot move right
            if start[i] == 'R' and i > j:
                return False  # R cannot move left

            j += 1

        return True


class SolutionTwoPointers:
    """Explicit two-pointer approach"""

    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        i, j = 0, 0

        while i < n or j < n:
            # Skip X in both
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1

            # If one finished but not the other
            if (i < n) != (j < n):
                return False

            # Both finished
            if i >= n and j >= n:
                break

            # Characters must match
            if start[i] != end[j]:
                return False

            # Check position constraints
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True


class SolutionWithPositions:
    """Store positions explicitly"""

    def canTransform(self, start: str, end: str) -> bool:
        # Get (char, position) for non-X characters
        start_chars = [(c, i) for i, c in enumerate(start) if c != 'X']
        end_chars = [(c, i) for i, c in enumerate(end) if c != 'X']

        if len(start_chars) != len(end_chars):
            return False

        for (c1, i1), (c2, i2) in zip(start_chars, end_chars):
            if c1 != c2:
                return False
            if c1 == 'L' and i1 < i2:
                return False
            if c1 == 'R' and i1 > i2:
                return False

        return True
