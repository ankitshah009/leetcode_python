#365. Water and Jug Problem
#Medium
#
#You are given two jugs with capacities jug1Capacity and jug2Capacity liters.
#There is an infinite amount of water supply available. Determine whether it is
#possible to measure exactly targetCapacity liters using these two jugs.
#
#If targetCapacity liters of water are measurable, you must have targetCapacity
#liters of water contained within one or both buckets by the end.
#
#Operations allowed:
#- Fill any of the jugs with water.
#- Empty any of the jugs.
#- Pour water from one jug into another till the other jug is completely full,
#  or the first jug itself is empty.
#
#Example 1:
#Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
#Output: true
#Explanation: The famous Die Hard example
#
#Example 2:
#Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
#Output: false
#
#Example 3:
#Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
#Output: true
#
#Constraints:
#    1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6

import math

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        """
        Mathematical solution using Bezout's identity.

        We can measure target liters if and only if target is a multiple of
        gcd(jug1, jug2) and target <= jug1 + jug2.
        """
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False

        if targetCapacity == 0:
            return True

        return targetCapacity % math.gcd(jug1Capacity, jug2Capacity) == 0


class SolutionBFS:
    """BFS approach - explore all states"""

    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        from collections import deque

        if targetCapacity > jug1Capacity + jug2Capacity:
            return False

        visited = set()
        queue = deque([(0, 0)])

        while queue:
            j1, j2 = queue.popleft()

            if j1 + j2 == targetCapacity:
                return True

            if (j1, j2) in visited:
                continue
            visited.add((j1, j2))

            # All possible operations
            next_states = [
                (jug1Capacity, j2),  # Fill jug1
                (j1, jug2Capacity),  # Fill jug2
                (0, j2),             # Empty jug1
                (j1, 0),             # Empty jug2
            ]

            # Pour jug1 into jug2
            pour = min(j1, jug2Capacity - j2)
            next_states.append((j1 - pour, j2 + pour))

            # Pour jug2 into jug1
            pour = min(j2, jug1Capacity - j1)
            next_states.append((j1 + pour, j2 - pour))

            for state in next_states:
                if state not in visited:
                    queue.append(state)

        return False


class SolutionDFS:
    """DFS with memoization"""

    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False

        visited = set()

        def dfs(j1, j2):
            if j1 + j2 == targetCapacity:
                return True

            if (j1, j2) in visited:
                return False

            visited.add((j1, j2))

            # Try all operations
            operations = [
                (jug1Capacity, j2),
                (j1, jug2Capacity),
                (0, j2),
                (j1, 0),
                (j1 - min(j1, jug2Capacity - j2), j2 + min(j1, jug2Capacity - j2)),
                (j1 + min(j2, jug1Capacity - j1), j2 - min(j2, jug1Capacity - j1))
            ]

            return any(dfs(nj1, nj2) for nj1, nj2 in operations)

        return dfs(0, 0)
