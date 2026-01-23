#1936. Add Minimum Number of Rungs
#Medium
#
#You are given a strictly increasing integer array rungs that represents the
#height of rungs on a ladder. You are currently on the floor at height 0, and
#you want to reach the last rung.
#
#You are also given an integer dist. You can only climb to the next highest
#rung if the distance between where you are currently at (the floor or on a
#rung) and the next rung is at most dist. You are able to insert rungs at any
#positive integer height if a rung is not already there.
#
#Return the minimum number of rungs that must be added to the ladder in order
#for you to climb to the last rung.
#
#Example 1:
#Input: rungs = [1,3,5,10], dist = 2
#Output: 2
#
#Example 2:
#Input: rungs = [3,6,8,10], dist = 3
#Output: 0
#
#Example 3:
#Input: rungs = [3,4,6,7], dist = 2
#Output: 1
#
#Constraints:
#    1 <= rungs.length <= 10^5
#    1 <= rungs[i] <= 10^9
#    1 <= dist <= 10^9
#    rungs is strictly increasing.

from typing import List

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        """
        For each gap > dist, calculate rungs needed.
        """
        count = 0
        prev = 0

        for rung in rungs:
            gap = rung - prev
            if gap > dist:
                # Number of rungs needed: (gap - 1) // dist
                count += (gap - 1) // dist
            prev = rung

        return count


class SolutionExplained:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        """
        Detailed explanation:

        If gap between two rungs is g and max step is d:
        - If g <= d: no rungs needed
        - If g > d: need ceil(g/d) - 1 = (g-1)//d rungs

        Why (g-1)//d?
        Example: g=10, d=3
        - Original: 0 ... 10
        - Need rungs at: 3, 6, 9
        - That's 3 rungs = (10-1)//3 = 3
        """
        added = 0
        current_height = 0

        for rung in rungs:
            gap = rung - current_height
            if gap > dist:
                added += (gap - 1) // dist
            current_height = rung

        return added


class SolutionMath:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        """
        Using math.ceil.
        """
        import math

        count = 0
        prev = 0

        for rung in rungs:
            gap = rung - prev
            if gap > dist:
                # ceil(gap/dist) - 1 rungs needed
                count += math.ceil(gap / dist) - 1
            prev = rung

        return count
