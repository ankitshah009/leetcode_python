#1642. Furthest Building You Can Reach
#Medium
#
#You are given an integer array heights representing the heights of buildings,
#some bricks, and some ladders.
#
#You start your journey from building 0 and move to the next building by possibly
#using bricks or ladders.
#
#While moving from building i to building i+1 (0-indexed),
#- If the current building's height is greater than or equal to the next
#  building's height, you do not need a ladder or bricks.
#- If the current building's height is less than the next building's height,
#  you can either use one ladder or (h[i+1] - h[i]) bricks.
#
#Return the furthest building index (0-indexed) you can reach if you use the
#given ladders and bricks optimally.
#
#Example 1:
#Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
#Output: 4
#Explanation: Starting at building 0, you can follow these steps:
#- Go to building 1 without using ladders nor bricks since 4 >= 2.
#- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
#- Go to building 3 without using ladders nor bricks since 7 >= 6.
#- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
#It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
#
#Example 2:
#Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
#Output: 7
#
#Example 3:
#Input: heights = [14,3,19,3], bricks = 17, ladders = 0
#Output: 3
#
#Constraints:
#    1 <= heights.length <= 10^5
#    1 <= heights[i] <= 10^6
#    0 <= bricks <= 10^9
#    0 <= ladders <= heights.length

from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Greedy with min-heap: Use ladders for largest climbs.

        Use a min-heap to track the climbs where we used ladders.
        If we need more ladders than available, convert smallest climb to bricks.
        """
        heap = []  # Min-heap of climb heights where ladders are used

        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]

            if climb <= 0:
                continue  # No climb needed

            heapq.heappush(heap, climb)

            if len(heap) > ladders:
                # Too many ladder uses, convert smallest to bricks
                smallest_climb = heapq.heappop(heap)
                bricks -= smallest_climb

                if bricks < 0:
                    return i

        return len(heights) - 1


class SolutionBinarySearch:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Binary search: Can we reach building mid?
        """
        def can_reach(target: int) -> bool:
            # Collect all climbs needed to reach target
            climbs = []
            for i in range(target):
                climb = heights[i + 1] - heights[i]
                if climb > 0:
                    climbs.append(climb)

            if len(climbs) <= ladders:
                return True

            # Use ladders for largest climbs, bricks for rest
            climbs.sort(reverse=True)
            brick_climbs = climbs[ladders:]
            return sum(brick_climbs) <= bricks

        left, right = 0, len(heights) - 1

        while left < right:
            mid = (left + right + 1) // 2
            if can_reach(mid):
                left = mid
            else:
                right = mid - 1

        return left


class SolutionMaxHeap:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Alternative: Use bricks first, replace with ladders when needed.
        """
        heap = []  # Max-heap (negative values) of brick climbs

        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]

            if climb <= 0:
                continue

            bricks -= climb
            heapq.heappush(heap, -climb)  # Max-heap

            if bricks < 0:
                if ladders > 0:
                    # Replace largest brick climb with ladder
                    bricks -= heapq.heappop(heap)  # Add back (it's negative)
                    ladders -= 1
                else:
                    return i

        return len(heights) - 1
