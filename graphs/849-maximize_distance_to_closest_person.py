#849. Maximize Distance to Closest Person
#Medium
#
#You are given an array representing a row of seats where seats[i] = 1 represents
#a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat
#is empty.
#
#There is at least one empty seat, and at least one person sitting.
#
#Alex wants to sit in the seat such that the distance between him and the closest
#person to him is maximized.
#
#Return that maximum distance to the closest person.
#
#Example 1:
#Input: seats = [1,0,0,0,1,0,1]
#Output: 2
#Explanation: Sit at seat 3. Closest person is at seat 0 or 4, distance = 2.
#
#Example 2:
#Input: seats = [1,0,0,0]
#Output: 3
#Explanation: Sit at seat 3. Closest person is at seat 0, distance = 3.
#
#Example 3:
#Input: seats = [0,1]
#Output: 1
#
#Constraints:
#    2 <= seats.length <= 2 * 10^4
#    seats[i] is 0 or 1.
#    At least one seat is empty.
#    At least one seat is occupied.

class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        """
        Track gaps between seated people.
        Middle gaps: best seat is in the middle, distance = gap // 2
        Edge gaps: distance = gap length
        """
        n = len(seats)

        # Find first and last occupied seats
        first = next(i for i in range(n) if seats[i] == 1)
        last = next(i for i in range(n - 1, -1, -1) if seats[i] == 1)

        max_dist = max(first, n - 1 - last)  # Edge gaps

        # Check middle gaps
        prev = first
        for i in range(first + 1, last + 1):
            if seats[i] == 1:
                gap = i - prev
                max_dist = max(max_dist, gap // 2)
                prev = i

        return max_dist


class SolutionTwoPass:
    """Two pass: left distance and right distance"""

    def maxDistToClosest(self, seats: list[int]) -> int:
        n = len(seats)

        # left[i] = distance to nearest person on left
        left = [float('inf')] * n
        # right[i] = distance to nearest person on right
        right = [float('inf')] * n

        # Left pass
        for i in range(n):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1

        # Right pass
        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < n - 1:
                right[i] = right[i + 1] + 1

        # Find seat with maximum min distance
        return max(min(left[i], right[i]) for i in range(n) if seats[i] == 0)


class SolutionGroupBy:
    """Using groupby to find gaps"""

    def maxDistToClosest(self, seats: list[int]) -> int:
        from itertools import groupby

        max_dist = 0

        for i, (val, group) in enumerate(groupby(seats)):
            length = len(list(group))

            if val == 0:
                if i == 0 or i == sum(1 for _ in groupby(seats)) - 1:
                    # Edge gap
                    max_dist = max(max_dist, length)
                else:
                    # Middle gap
                    max_dist = max(max_dist, (length + 1) // 2)

        # Recalculate to handle edge cases properly
        n = len(seats)
        first = seats.index(1)
        last = n - 1 - seats[::-1].index(1)

        max_dist = max(first, n - 1 - last)
        prev = first

        for i in range(first + 1, last + 1):
            if seats[i] == 1:
                max_dist = max(max_dist, (i - prev) // 2)
                prev = i

        return max_dist
