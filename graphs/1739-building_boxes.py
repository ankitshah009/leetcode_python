#1739. Building Boxes
#Hard
#
#You have a cubic storeroom where the width, length, and height of the room are
#all equal to n units. You are asked to place n boxes in this room where each
#box is a unit cube. There are however some rules to placing the boxes:
#
#- You can place the boxes anywhere on the floor.
#- If box x is placed on top of box y, then each side of the four vertical sides
#  of box y must either be adjacent to another box or to a wall.
#
#Given an integer n, return the minimum possible number of boxes touching the
#floor.
#
#Example 1:
#Input: n = 3
#Output: 3
#
#Example 2:
#Input: n = 4
#Output: 3
#
#Example 3:
#Input: n = 10
#Output: 6
#
#Constraints:
#    1 <= n <= 10^9

class Solution:
    def minimumBoxes(self, n: int) -> int:
        """
        Optimal stacking: build staircase structure from corner.

        Complete pyramid of height h has:
        - Floor boxes = 1 + 2 + ... + h = h(h+1)/2
        - Total boxes = 1 + (1+2) + (1+2+3) + ... = h(h+1)(h+2)/6

        After full pyramid, add extra floor boxes one at a time.
        Each new floor box at position i can hold i additional boxes on top.
        """
        # Find largest complete pyramid height
        h = 0
        total = 0
        while total + (h + 1) * (h + 2) // 2 <= n:
            h += 1
            total += h * (h + 1) // 2

        floor = h * (h + 1) // 2  # Floor boxes for complete pyramid

        # Add remaining boxes
        remaining = n - total
        extra = 0
        capacity = 0

        while capacity < remaining:
            extra += 1
            capacity += extra

        return floor + extra


class SolutionBinarySearch:
    def minimumBoxes(self, n: int) -> int:
        """
        Binary search for answer.
        """
        def total_boxes(floor: int) -> int:
            """Calculate max boxes that can be stacked with 'floor' floor boxes."""
            # Find largest h where h(h+1)/2 <= floor
            # Then compute total for full pyramid + extra

            # For triangular number h(h+1)/2 <= floor
            h = int((2 * floor) ** 0.5)
            while h * (h + 1) // 2 > floor:
                h -= 1
            while (h + 1) * (h + 2) // 2 <= floor:
                h += 1

            # Full pyramid with height h
            full_pyramid = h * (h + 1) * (h + 2) // 6
            floor_used = h * (h + 1) // 2
            extra_floor = floor - floor_used

            # Extra floor boxes: can stack 1, 2, 3, ... boxes
            extra_total = extra_floor * (extra_floor + 1) // 2

            return full_pyramid + extra_total

        # Binary search for minimum floor
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if total_boxes(mid) >= n:
                right = mid
            else:
                left = mid + 1

        return left


class SolutionMath:
    def minimumBoxes(self, n: int) -> int:
        """
        Direct mathematical approach.
        """
        # Find h such that h(h+1)(h+2)/6 <= n
        h = int((6 * n) ** (1/3))
        while h * (h + 1) * (h + 2) // 6 > n:
            h -= 1
        while (h + 1) * (h + 2) * (h + 3) // 6 <= n:
            h += 1

        # Full pyramid totals
        total = h * (h + 1) * (h + 2) // 6
        floor = h * (h + 1) // 2

        # Add extra to reach n
        remaining = n - total
        extra = int((2 * remaining) ** 0.5)
        while extra * (extra + 1) // 2 < remaining:
            extra += 1

        return floor + extra
