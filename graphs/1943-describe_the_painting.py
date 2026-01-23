#1943. Describe the Painting
#Medium
#
#There is a long and thin painting that can be represented by a number line.
#The painting was painted with multiple overlapping segments where each segment
#was painted with a unique color. You are given a 2D integer array segments,
#where segments[i] = [start_i, end_i, color_i] represents the half-closed
#segment [start_i, end_i) with color_i.
#
#The colors in the overlapping segments of the painting were mixed. When two or
#more colors mix, they form a new color that can be represented as a set of
#mixed colors.
#
#Return a 2D array painting describing the finished painting. Each element
#painting[j] = [left_j, right_j, mix_j] describes a maximal segment of mixed
#colors where:
#- Every point in [left_j, right_j) is painted.
#- Every point in [left_j, right_j) has the same mix_j color.
#- mix_j is a sum of all unique colors painted on the segment.
#
#Sort painting by left_j in ascending order.
#
#Example 1:
#Input: segments = [[1,4,5],[4,7,7],[1,7,9]]
#Output: [[1,4,14],[4,7,16]]
#
#Example 2:
#Input: segments = [[1,7,9],[6,8,15],[8,10,7]]
#Output: [[1,6,9],[6,7,24],[7,8,15],[8,10,7]]
#
#Constraints:
#    1 <= segments.length <= 2 * 10^4
#    segments[i].length == 3
#    1 <= start_i < end_i <= 10^5
#    1 <= color_i <= 10^9
#    Each color_i is distinct.

from typing import List
from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        """
        Line sweep: track color sum changes at each point.
        """
        # Events: position -> change in color sum
        events = defaultdict(int)

        for start, end, color in segments:
            events[start] += color
            events[end] -= color

        # Sort positions
        positions = sorted(events.keys())

        result = []
        current_sum = 0

        for i in range(len(positions) - 1):
            current_sum += events[positions[i]]

            if current_sum > 0:
                result.append([positions[i], positions[i + 1], current_sum])

        return result


class SolutionExplained:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        """
        Same approach with clearer structure.

        Key insight: use sum of colors as mix representation.
        At each boundary point, color sum changes.
        """
        diff = defaultdict(int)

        for start, end, color in segments:
            diff[start] += color  # Add color at start
            diff[end] -= color    # Remove color at end

        sorted_points = sorted(diff.keys())
        result = []
        running_sum = 0

        for i in range(len(sorted_points) - 1):
            running_sum += diff[sorted_points[i]]

            # Only include painted segments
            if running_sum > 0:
                result.append([sorted_points[i], sorted_points[i + 1], running_sum])

        return result
