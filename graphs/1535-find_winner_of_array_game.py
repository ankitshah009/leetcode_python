#1535. Find the Winner of an Array Game
#Medium
#
#Given an integer array arr of distinct integers and an integer k.
#
#A game will be played between the first two elements of the array (i.e. arr[0]
#and arr[1]). In each round of the game, we compare arr[0] with arr[1], the
#larger integer wins and remains at position 0, and the smaller integer moves to
#the end of the array. The game ends when an integer wins k consecutive rounds.
#
#Return the integer which will win the game.
#
#It is guaranteed that there will be a winner of the game.
#
#Example 1:
#Input: arr = [2,1,3,5,4,6,7], k = 2
#Output: 5
#Explanation: Let's see the rounds of the game:
#Round |       arr       | winner | win_count
#  1   | [2,1,3,5,4,6,7] | 2      | 1
#  2   | [2,3,5,4,6,7,1] | 3      | 1
#  3   | [3,5,4,6,7,1,2] | 5      | 1
#  4   | [5,4,6,7,1,2,3] | 5      | 2
#So we can see that 5 wins 2 consecutive rounds.
#
#Example 2:
#Input: arr = [3,2,1], k = 10
#Output: 3
#Explanation: 3 will win the first 10 rounds consecutively.
#
#Constraints:
#    2 <= arr.length <= 10^5
#    1 <= arr[i] <= 10^6
#    arr contains distinct integers.
#    1 <= k <= 10^9

from typing import List
from collections import deque

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        """
        Key insight: If k >= n-1, the max element will always win.
        Otherwise, simulate until someone wins k consecutive rounds.

        Optimization: No need to actually rotate - just track current winner.
        """
        n = len(arr)

        # If k is large enough, max element will eventually reach front and win
        if k >= n - 1:
            return max(arr)

        current_winner = arr[0]
        consecutive_wins = 0

        for i in range(1, n):
            if arr[i] > current_winner:
                current_winner = arr[i]
                consecutive_wins = 1
            else:
                consecutive_wins += 1

            if consecutive_wins == k:
                return current_winner

        # If we've gone through all elements, current_winner is the max
        return current_winner


class SolutionDeque:
    def getWinner(self, arr: List[int], k: int) -> int:
        """
        Simulation using deque for rotation.
        Note: This is slower but follows the problem description exactly.
        """
        n = len(arr)

        if k >= n - 1:
            return max(arr)

        q = deque(arr)
        wins = 0
        prev_winner = None

        while wins < k:
            a, b = q.popleft(), q.popleft()

            if a > b:
                winner, loser = a, b
            else:
                winner, loser = b, a

            q.appendleft(winner)
            q.append(loser)

            if winner == prev_winner:
                wins += 1
            else:
                wins = 1
                prev_winner = winner

        return prev_winner


class SolutionMaxTracking:
    def getWinner(self, arr: List[int], k: int) -> int:
        """
        Track maximum seen so far.
        Once we see the overall max, it will win forever.
        """
        max_val = max(arr)
        current = arr[0]
        wins = 0

        for i in range(1, len(arr)):
            if current == max_val:
                return current

            if current > arr[i]:
                wins += 1
            else:
                current = arr[i]
                wins = 1

            if wins == k:
                return current

        return current  # Must be max_val


class SolutionSimple:
    def getWinner(self, arr: List[int], k: int) -> int:
        """
        Simplified logic.
        """
        winner = arr[0]
        count = 0

        for i in range(1, len(arr)):
            if arr[i] > winner:
                winner = arr[i]
                count = 1
            else:
                count += 1

            if count >= k:
                return winner

        return winner
