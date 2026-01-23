#1710. Maximum Units on a Truck
#Easy
#
#You are assigned to put some amount of boxes onto one truck. You are given a 2D
#array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
#
#- numberOfBoxesi is the number of boxes of type i.
#- numberOfUnitsPerBoxi is the number of units in each box of the type i.
#
#You are also given an integer truckSize, which is the maximum number of boxes
#that can be put on the truck. You can choose any boxes to put on the truck as
#long as the number of boxes does not exceed truckSize.
#
#Return the maximum total number of units that can be put on the truck.
#
#Example 1:
#Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
#Output: 8
#
#Example 2:
#Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
#Output: 91
#
#Constraints:
#    1 <= boxTypes.length <= 1000
#    1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
#    1 <= truckSize <= 10^6

from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        Greedy - sort by units per box (descending), take boxes greedily.
        """
        # Sort by units per box in descending order
        boxTypes.sort(key=lambda x: -x[1])

        total_units = 0
        remaining = truckSize

        for count, units in boxTypes:
            if remaining <= 0:
                break

            take = min(count, remaining)
            total_units += take * units
            remaining -= take

        return total_units


class SolutionCountingSort:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        Counting sort approach - units <= 1000.
        """
        # Count boxes for each unit value
        unit_count = [0] * 1001

        for count, units in boxTypes:
            unit_count[units] += count

        total_units = 0
        remaining = truckSize

        # Process from highest units
        for units in range(1000, 0, -1):
            if remaining <= 0:
                break

            if unit_count[units] > 0:
                take = min(unit_count[units], remaining)
                total_units += take * units
                remaining -= take

        return total_units


class SolutionHeap:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        Max heap approach.
        """
        import heapq

        # Max heap (negative for max behavior)
        heap = [(-units, count) for count, units in boxTypes]
        heapq.heapify(heap)

        total_units = 0
        remaining = truckSize

        while heap and remaining > 0:
            neg_units, count = heapq.heappop(heap)
            units = -neg_units

            take = min(count, remaining)
            total_units += take * units
            remaining -= take

        return total_units
