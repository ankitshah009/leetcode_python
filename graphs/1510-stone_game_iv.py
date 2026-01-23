#1510. Stone Game IV
#Hard
#
#Alice and Bob take turns playing a game, with Alice starting first.
#
#Initially, there are n stones in a pile. On each player's turn, that player
#makes a move consisting of removing any non-zero square number of stones in
#the pile.
#
#Also, if a player cannot make a move, he/she loses the game.
#
#Given a positive integer n, return true if and only if Alice wins the game
#otherwise return false, assuming both players play optimally.
#
#Example 1:
#Input: n = 1
#Output: true
#Explanation: Alice can remove 1 stone winning the game because Bob doesn't
#have any moves.
#
#Example 2:
#Input: n = 2
#Output: false
#Explanation: Alice can only remove 1 stone, after that Bob removes the last
#one winning the game (2 -> 1 -> 0).
#
#Example 3:
#Input: n = 4
#Output: true
#Explanation: n is already a perfect square, Alice can win with one move,
#removing 4 stones (4 -> 0).
#
#Constraints:
#    1 <= n <= 10^5

from functools import lru_cache

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
        Game theory DP.
        dp[i] = True if current player wins with i stones.
        Current player wins if they can move to any losing state for opponent.
        """
        @lru_cache(maxsize=None)
        def can_win(stones: int) -> bool:
            if stones == 0:
                return False  # No moves = lose

            # Try all square number moves
            k = 1
            while k * k <= stones:
                # If opponent loses after this move, current player wins
                if not can_win(stones - k * k):
                    return True
                k += 1

            return False

        return can_win(n)


class SolutionIterative:
    def winnerSquareGame(self, n: int) -> bool:
        """
        Bottom-up DP.
        """
        import math

        dp = [False] * (n + 1)
        # dp[0] = False (no stones = lose)

        for i in range(1, n + 1):
            # Check all possible square moves
            k = 1
            while k * k <= i:
                if not dp[i - k * k]:  # Can move to losing state
                    dp[i] = True
                    break
                k += 1

        return dp[n]


class SolutionOptimized:
    def winnerSquareGame(self, n: int) -> bool:
        """
        Optimized with precomputed squares.
        """
        import math

        # Precompute all squares <= n
        squares = []
        k = 1
        while k * k <= n:
            squares.append(k * k)
            k += 1

        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                if not dp[i - sq]:
                    dp[i] = True
                    break

        return dp[n]


class SolutionMath:
    def winnerSquareGame(self, n: int) -> bool:
        """
        Mathematical observation:
        Pattern repeats with some structure.

        Actually, no simple closed form - use DP.
        """
        # Check if n is a perfect square
        import math
        sqrt_n = int(math.sqrt(n))

        # Use iterative DP
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            for k in range(1, sqrt_n + 2):
                if k * k > i:
                    break
                if not dp[i - k * k]:
                    dp[i] = True
                    break

        return dp[n]
