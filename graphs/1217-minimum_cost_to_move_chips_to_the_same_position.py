#1217. Minimum Cost to Move Chips to The Same Position
#Easy
#
#We have n chips, where the position of the ith chip is position[i].
#
#We need to move all the chips to the same position. In one step, we can
#change the position of the ith chip from position[i] to:
#    position[i] + 2 or position[i] - 2 with cost = 0.
#    position[i] + 1 or position[i] - 1 with cost = 1.
#
#Return the minimum cost needed to move all the chips to the same position.
#
#Example 1:
#Input: position = [1,2,3]
#Output: 1
#Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
#Second step: Move the chip at position 2 to position 1 with cost = 1.
#Total cost is 1.
#
#Example 2:
#Input: position = [2,2,2,3,3]
#Output: 2
#Explanation: We can move the two chips at position 3 to position 2. Each move has cost = 1. The total cost = 2.
#
#Example 3:
#Input: position = [1,1000000000]
#Output: 1
#
#Constraints:
#    1 <= position.length <= 100
#    1 <= position[i] <= 10^9

from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """
        Key insight: Moving by 2 is free, so we can move all chips to
        either position 0 (even) or position 1 (odd) for free.

        Then we just need to move chips between odd and even positions.
        Cost = min(count of odd, count of even).
        """
        odd_count = sum(1 for p in position if p % 2 == 1)
        even_count = len(position) - odd_count

        return min(odd_count, even_count)


class SolutionExplicit:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """More explicit counting"""
        odd = 0
        even = 0

        for p in position:
            if p % 2 == 0:
                even += 1
            else:
                odd += 1

        # Move all to even position: cost = odd (each odd chip costs 1)
        # Move all to odd position: cost = even
        return min(odd, even)
