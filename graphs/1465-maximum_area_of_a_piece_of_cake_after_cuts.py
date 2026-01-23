#1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#Medium
#
#You are given a rectangular cake of size h x w and two arrays of integers
#horizontalCuts and verticalCuts where:
#    horizontalCuts[i] is the distance from the top of the rectangular cake to
#    the ith horizontal cut and similarly, and
#    verticalCuts[j] is the distance from the left of the rectangular cake to
#    the jth vertical cut.
#
#Return the maximum area of a piece of cake after you cut at each horizontal
#and vertical position provided in the arrays horizontalCuts and verticalCuts.
#Since the answer can be a huge number, return this modulo 10^9 + 7.
#
#Example 1:
#Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
#Output: 4
#Explanation: The figure above represents the given rectangular cake. Red lines
#are the horizontal and vertical cuts. After you cut the cake, the green piece
#of cake has the maximum area.
#
#Example 2:
#Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
#Output: 6
#Explanation: The figure above represents the given rectangular cake. Red lines
#are the horizontal and vertical cuts. After you cut the cake, the green and
#yellow pieces of cake have the maximum area.
#
#Example 3:
#Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
#Output: 9
#
#Constraints:
#    2 <= h, w <= 10^9
#    1 <= horizontalCuts.length <= min(h - 1, 10^5)
#    1 <= verticalCuts.length <= min(w - 1, 10^5)
#    1 <= horizontalCuts[i] < h
#    1 <= verticalCuts[i] < w
#    All the elements in horizontalCuts are distinct.
#    All the elements in verticalCuts are distinct.

from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """
        Max area = max horizontal gap * max vertical gap.
        Sort cuts and find maximum gap between consecutive cuts.
        """
        MOD = 10**9 + 7

        # Sort cuts
        horizontalCuts.sort()
        verticalCuts.sort()

        # Find max horizontal gap (include edges)
        max_h = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i - 1])

        # Find max vertical gap (include edges)
        max_w = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i - 1])

        return (max_h * max_w) % MOD


class SolutionAlternative:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """
        Alternative: add boundaries to cuts list.
        """
        MOD = 10**9 + 7

        # Add boundaries
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]

        # Max gaps
        max_h = max(horizontalCuts[i] - horizontalCuts[i - 1]
                    for i in range(1, len(horizontalCuts)))
        max_w = max(verticalCuts[i] - verticalCuts[i - 1]
                    for i in range(1, len(verticalCuts)))

        return (max_h * max_w) % MOD


class SolutionZip:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """Using zip for cleaner gap calculation"""
        MOD = 10**9 + 7

        def max_gap(cuts: List[int], limit: int) -> int:
            cuts = sorted(cuts)
            # Include first gap (0 to first cut) and last gap (last cut to limit)
            gaps = [cuts[0]] + [cuts[i] - cuts[i-1] for i in range(1, len(cuts))] + [limit - cuts[-1]]
            return max(gaps)

        max_h = max_gap(horizontalCuts, h)
        max_w = max_gap(verticalCuts, w)

        return (max_h * max_w) % MOD
