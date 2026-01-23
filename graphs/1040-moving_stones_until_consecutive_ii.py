#1040. Moving Stones Until Consecutive II
#Medium
#
#There are some stones in different positions on the X-axis. You are given
#an integer array stones, the positions of the stones.
#
#Call a stone an endpoint stone if it has the smallest or largest position.
#In one move, you pick up an endpoint stone and move it to an unoccupied
#position so that it is no longer an endpoint stone.
#
#The game ends when you cannot make any more moves (ie. the stones are in
#three or more consecutive positions).
#
#Return an integer array answer of length 2 where:
#    answer[0] is the minimum number of moves, and
#    answer[1] is the maximum number of moves.
#
#Example 1:
#Input: stones = [7,4,9]
#Output: [1,2]
#
#Example 2:
#Input: stones = [6,5,4,3,10]
#Output: [2,3]
#
#Example 3:
#Input: stones = [100,101,104,102,103]
#Output: [0,0]
#
#Constraints:
#    3 <= stones.length <= 10^4
#    1 <= stones[i] <= 10^9
#    All the values of stones are unique.

from typing import List

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        """
        After sorting:
        - Max moves: Total spaces we can fill, minus the space we skip
          by moving endpoint.
        - Min moves: Sliding window of size n to find window with most
          stones already inside.

        Max: We can move left endpoint right or right endpoint left.
             If move left: skip (stones[1] - stones[0] - 1) spaces
             If move right: skip (stones[-1] - stones[-2] - 1) spaces
             Total spaces = stones[-1] - stones[0] - (n-1)
             Max moves = total - min(skip_left, skip_right)

        Min: Use sliding window. Find window of size n with most stones.
             Moves needed = n - stones_in_window.
             Special case: if window has n-1 stones and gap is at endpoint.
        """
        stones.sort()
        n = len(stones)

        # Maximum moves
        # Total positions = stones[-1] - stones[0] + 1
        # Empty positions = total - n = stones[-1] - stones[0] + 1 - n
        # We skip some positions on first move
        skip_left = stones[1] - stones[0] - 1
        skip_right = stones[-1] - stones[-2] - 1
        total_empty = stones[-1] - stones[0] + 1 - n
        max_moves = total_empty - min(skip_left, skip_right)

        # Minimum moves using sliding window
        min_moves = n
        j = 0

        for i in range(n):
            # Expand window to include positions up to stones[i] + n - 1
            while j < n and stones[j] <= stones[i] + n - 1:
                j += 1

            stones_in_window = j - i

            # Special case: n-1 stones consecutive, one stone far away
            # e.g., [1,2,3,4,10] - can't move 10 to 5, must move 1 first
            if stones_in_window == n - 1 and stones[j - 1] - stones[i] == n - 2:
                # Window covers n-1 positions with n-1 stones (all consecutive)
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - stones_in_window)

        return [min_moves, max_moves]


class SolutionDetailed:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        """More explicit implementation with comments"""
        stones.sort()
        n = len(stones)

        # Check if already consecutive
        if stones[-1] - stones[0] == n - 1:
            return [0, 0]

        # Maximum moves calculation
        # Total gap = stones[-1] - stones[0] - (n-1) empty spots
        # After first move, we "close off" one side
        gap_left = stones[1] - stones[0] - 1  # Gap to left of second stone
        gap_right = stones[-1] - stones[-2] - 1  # Gap to right of second-to-last

        # Max is achieved by always moving the endpoint with smaller gap
        max_moves = stones[-1] - stones[0] - n + 1 - min(gap_left, gap_right)

        # Minimum moves: sliding window
        min_moves = float('inf')
        left = 0

        for right in range(n):
            # Window: [stones[left], stones[left] + n - 1]
            # Find how many stones fit in a window of size n starting at stones[left]
            while stones[right] - stones[left] >= n:
                left += 1

            count = right - left + 1  # Stones in window

            # Special case handling
            if count == n - 1 and stones[right] - stones[left] == n - 2:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - count)

        return [min_moves, max_moves]
