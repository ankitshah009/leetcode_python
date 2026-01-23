#1840. Maximum Building Height
#Hard
#
#You want to build n new buildings in a city. The new buildings will be built
#in a line and are labeled from 1 to n.
#
#However, there are city restrictions on the heights of the new buildings:
#- The height of each building must be a non-negative integer.
#- The height of the first building must be 0.
#- The height difference between any two adjacent buildings cannot exceed 1.
#
#Additionally, there are city restrictions on the maximum height of specific
#buildings. These restrictions are given as a 2D integer array restrictions
#where restrictions[i] = [id_i, maxHeight_i] indicates that building id_i must
#have a height less than or equal to maxHeight_i.
#
#It is guaranteed that each building will appear at most once in restrictions,
#and building 1 will not be in restrictions.
#
#Return the maximum possible height of the tallest building.
#
#Example 1:
#Input: n = 5, restrictions = [[2,1],[4,1]]
#Output: 2
#
#Example 2:
#Input: n = 6, restrictions = []
#Output: 5
#
#Example 3:
#Input: n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
#Output: 5
#
#Constraints:
#    2 <= n <= 10^9
#    0 <= restrictions.length <= min(n - 1, 10^5)
#    2 <= id_i <= n
#    id_i is unique.
#    0 <= maxHeight_i <= 10^9

from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        """
        Two passes to propagate restrictions, then find max height between
        consecutive restrictions.
        """
        if not restrictions:
            return n - 1

        # Add building 1 with height 0 and building n with height n-1
        restrictions.append([1, 0])
        restrictions.sort()

        # If building n not restricted, add it
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        # Forward pass: propagate restrictions left to right
        for i in range(1, len(restrictions)):
            prev_id, prev_max = restrictions[i - 1]
            curr_id, curr_max = restrictions[i]
            dist = curr_id - prev_id
            # Max height at curr_id given prev constraint
            restrictions[i][1] = min(curr_max, prev_max + dist)

        # Backward pass: propagate restrictions right to left
        for i in range(len(restrictions) - 2, -1, -1):
            next_id, next_max = restrictions[i + 1]
            curr_id, curr_max = restrictions[i]
            dist = next_id - curr_id
            restrictions[i][1] = min(curr_max, next_max + dist)

        # Find maximum height between consecutive restrictions
        max_height = 0
        for i in range(1, len(restrictions)):
            prev_id, prev_max = restrictions[i - 1]
            curr_id, curr_max = restrictions[i]
            dist = curr_id - prev_id

            # Max height in between: meet in the middle
            # h = prev_max + x = curr_max + (dist - x)
            # 2x = curr_max - prev_max + dist
            # x = (curr_max - prev_max + dist) / 2
            # h = prev_max + (curr_max - prev_max + dist) / 2
            #   = (prev_max + curr_max + dist) / 2
            between_max = (prev_max + curr_max + dist) // 2
            max_height = max(max_height, between_max)

        return max_height


class SolutionExplained:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        """
        Same algorithm with detailed comments.
        """
        # Handle no restrictions case
        if not restrictions:
            return n - 1

        # Add boundary conditions
        restrictions.append([1, 0])
        restrictions.sort()

        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        m = len(restrictions)

        # Forward pass: can't exceed previous + distance
        for i in range(1, m):
            diff = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1],
                                      restrictions[i-1][1] + diff)

        # Backward pass: can't exceed next + distance
        for i in range(m - 2, -1, -1):
            diff = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1],
                                      restrictions[i+1][1] + diff)

        # Find peak between each pair
        result = 0
        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            dist = id2 - id1

            # Peak height between two buildings
            peak = (h1 + h2 + dist) // 2
            result = max(result, peak)

        return result
