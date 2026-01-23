#1732. Find the Highest Altitude
#Easy
#
#There is a biker going on a road trip. The road trip consists of n + 1 points
#at different altitudes. The biker starts at point 0 with altitude 0.
#
#You are given an integer array gain of length n where gain[i] is the net gain
#in altitude between points i and i + 1 for all (0 <= i < n). Return the highest
#altitude of a point.
#
#Example 1:
#Input: gain = [-5,1,5,0,-7]
#Output: 1
#
#Example 2:
#Input: gain = [-4,-3,-2,-1,4,3,2]
#Output: 0
#
#Constraints:
#    n == gain.length
#    1 <= n <= 100
#    -100 <= gain[i] <= 100

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Track current altitude and max altitude.
        """
        max_alt = 0
        current = 0

        for g in gain:
            current += g
            max_alt = max(max_alt, current)

        return max_alt


class SolutionPrefixSum:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Using accumulate.
        """
        from itertools import accumulate

        altitudes = list(accumulate(gain, initial=0))
        return max(altitudes)


class SolutionOneLiner:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        One-liner using accumulate.
        """
        from itertools import accumulate
        return max(accumulate(gain, initial=0))
