#1386. Cinema Seat Allocation
#Medium
#
#A cinema has n rows of seats, numbered from 1 to n and there are ten seats in
#each row, labelled from 1 to 10.
#
#Given the array reservedSeats containing the numbers of seats already reserved,
#for example, reservedSeats[i] = [3,8] means the seat located in row 3 and
#labelled with 8 is already reserved.
#
#Return the maximum number of four-person groups you can assign on the cinema
#seats. A four-person group occupies four adjacent seats in one single row.
#Seats across an aisle (such as [3,3] and [3,4]) are not considered to be
#adjacent, but there is an exceptional case on which an aisle split a
#four-person group, in that case, the aisle split a four-person group in the
#middle, which means to have two people on each side.
#
#Example 1:
#Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
#Output: 4
#Explanation: The figure above shows the optimal allocation for four groups,
#where seats mark with blue are already reserved and contiguous seats mark
#with orange are for one group.
#
#Example 2:
#Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
#Output: 2
#
#Example 3:
#Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
#Output: 4
#
#Constraints:
#    1 <= n <= 10^9
#    1 <= reservedSeats.length <= min(10*n, 10^4)
#    reservedSeats[i].length == 2
#    1 <= reservedSeats[i][0] <= n
#    1 <= reservedSeats[i][1] <= 10
#    All reservedSeats[i] are distinct.

from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """
        Valid groups of 4 can sit at:
        - Seats 2,3,4,5 (left)
        - Seats 4,5,6,7 (middle)
        - Seats 6,7,8,9 (right)

        For each row, check which combinations work.
        Rows with no reservations can fit 2 groups.
        """
        # Group reserved seats by row
        reserved_by_row = defaultdict(set)
        for row, seat in reservedSeats:
            reserved_by_row[row].add(seat)

        # Rows with no reservations: 2 groups each
        rows_with_reservations = len(reserved_by_row)
        result = (n - rows_with_reservations) * 2

        # Check rows with reservations
        for row, reserved in reserved_by_row.items():
            # Check left (2-5), middle (4-7), right (6-9)
            left = not any(s in reserved for s in [2, 3, 4, 5])
            middle = not any(s in reserved for s in [4, 5, 6, 7])
            right = not any(s in reserved for s in [6, 7, 8, 9])

            if left and right:
                result += 2
            elif left or middle or right:
                result += 1

        return result


class SolutionBitmask:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """Using bitmask for seat representation"""
        reserved_by_row = defaultdict(int)

        for row, seat in reservedSeats:
            # Seat numbers 1-10, use bits 0-9
            reserved_by_row[row] |= (1 << (seat - 1))

        rows_with_reservations = len(reserved_by_row)
        result = (n - rows_with_reservations) * 2

        # Masks for valid group positions (seats 2-5, 4-7, 6-9)
        left_mask = 0b0000011110   # seats 2,3,4,5
        middle_mask = 0b0001111000  # seats 4,5,6,7
        right_mask = 0b0111100000   # seats 6,7,8,9

        for reserved in reserved_by_row.values():
            left_ok = (reserved & left_mask) == 0
            middle_ok = (reserved & middle_mask) == 0
            right_ok = (reserved & right_mask) == 0

            if left_ok and right_ok:
                result += 2
            elif left_ok or middle_ok or right_ok:
                result += 1

        return result


class SolutionExplicit:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """More explicit version"""
        reserved_by_row = defaultdict(set)
        for row, seat in reservedSeats:
            reserved_by_row[row].add(seat)

        result = 0
        checked_rows = set()

        for row, reserved in reserved_by_row.items():
            checked_rows.add(row)
            groups = 0

            # Try left group (seats 2-5)
            if all(s not in reserved for s in range(2, 6)):
                groups += 1
                # Try right group (seats 6-9)
                if all(s not in reserved for s in range(6, 10)):
                    groups += 1
            # Try right group (seats 6-9)
            elif all(s not in reserved for s in range(6, 10)):
                groups += 1
            # Try middle group (seats 4-7)
            elif all(s not in reserved for s in range(4, 8)):
                groups += 1

            result += groups

        # Unreserved rows: 2 groups each
        result += (n - len(checked_rows)) * 2

        return result
