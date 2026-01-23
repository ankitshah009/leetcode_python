#1900. The Earliest and Latest Rounds Where Players Compete
#Hard
#
#There is a tournament where n players are participating. The players are
#standing in a single row and are numbered from 1 to n based on their initial
#standing position (player 1 is the first player in the row, player 2 is the
#second player in the row, etc.).
#
#The tournament consists of multiple rounds. In each round, the ith player from
#the front of the row competes against the ith player from the end of the row,
#and the winner advances to the next round. When the number of players is odd,
#the player in the middle automatically advances to the next round.
#
#After each round, the winners are lined up in the row based on the original
#ordering assigned to them initially.
#
#The players numbered firstPlayer and secondPlayer are the best players in the
#tournament. They can win against any other player before they compete against
#each other. If any other two players compete against each other, either of
#them might win.
#
#Given the integers n, firstPlayer, and secondPlayer, return an integer array
#containing two values:
#- The earliest round number where these two players meet.
#- The latest round number where these two players meet.
#
#Example 1:
#Input: n = 11, firstPlayer = 2, secondPlayer = 4
#Output: [3,4]
#
#Example 2:
#Input: n = 5, firstPlayer = 1, secondPlayer = 5
#Output: [1,1]
#
#Constraints:
#    2 <= n <= 28
#    1 <= firstPlayer < secondPlayer <= n

from typing import List
from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        """
        DFS/BFS to explore all possible tournament outcomes.
        State: positions of first and second player.
        """
        # Ensure firstPlayer < secondPlayer (by position)
        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer

        @lru_cache(maxsize=None)
        def dfs(n: int, p1: int, p2: int) -> tuple:
            """Return (earliest, latest) round for p1, p2 to meet."""
            # p1 and p2 are 1-indexed positions

            # Check if they meet this round
            if p1 + p2 == n + 1:
                return (1, 1)

            # If they're in the same half, they can't meet yet
            # Determine new positions after this round

            earliest = float('inf')
            latest = 0

            # Number of players advancing: (n + 1) // 2
            new_n = (n + 1) // 2

            # p1 and p2 will fight different opponents
            # p1 fights player at position (n + 1 - p1)
            # p2 fights player at position (n + 1 - p2)

            # They don't meet if p1 + p2 != n + 1
            # After winning, their new positions depend on who else wins

            # Players in positions [1, p1-1]: some win, some lose
            # Players in positions [p1+1, p2-1]: some win, some lose
            # Players in positions [p2+1, n]: some win, some lose

            # Key insight: p1's new position = 1 + (number of winners before p1)
            # Winners before p1 come from positions 1 to p1-1

            # Positions 1 to p1-1: pair with positions n to n-p1+2
            # If position i < p1 < (n+1)/2, then i pairs with n+1-i > p1
            # Winner can be either, contributing to count before p1 or not

            # Simplify: enumerate possible new positions

            # Number of pairs before p1 (both players have position < p1)
            # Number of pairs where p1 or p2 is involved

            # Let's think differently:
            # left = p1 - 1 (players to the left of p1)
            # mid = p2 - p1 - 1 (players between p1 and p2)
            # right = n - p2 (players to the right of p2)

            left = p1 - 1
            mid = p2 - p1 - 1
            right = n - p2

            # From left pairs: some might both be in left half, some cross
            # Actually, player i pairs with player n+1-i

            # Enumerate possible scenarios for p1 and p2's new positions
            for new_p1 in range(1, new_n + 1):
                for new_p2 in range(new_p1 + 1, new_n + 1):
                    # Check if this combination is achievable
                    # new_p1 = 1 + winners from positions < p1
                    # new_p2 = new_p1 + 1 + winners from positions in (p1, p2)

                    # Winners before p1: can be 0 to left
                    # But constrained by pairing

                    # This is getting complex. Use simpler state-based recursion.
                    pass

            # Simplified approach: enumerate all possible (new_p1, new_p2) pairs
            # and check validity

            for wins_left in range(left + 1):
                for wins_mid in range(mid + 1):
                    # p1's new position = 1 + wins_left
                    # p2's new position = 1 + wins_left + 1 + wins_mid
                    new_p1 = 1 + wins_left
                    new_p2 = new_p1 + 1 + wins_mid

                    if new_p2 <= new_n:
                        e, l = dfs(new_n, new_p1, new_p2)
                        earliest = min(earliest, e + 1)
                        latest = max(latest, l + 1)

            return (earliest, latest)

        result = dfs(n, firstPlayer, secondPlayer)
        return [result[0], result[1]]


class SolutionBFS:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        """
        BFS exploring all states.
        """
        from collections import deque

        # State: (n, p1, p2) where p1 < p2
        p1, p2 = min(firstPlayer, secondPlayer), max(firstPlayer, secondPlayer)

        earliest = float('inf')
        latest = 0

        queue = deque([(n, p1, p2, 1)])  # (players, pos1, pos2, round)
        visited = {(n, p1, p2)}

        while queue:
            players, pos1, pos2, round_num = queue.popleft()

            # Check if they meet
            if pos1 + pos2 == players + 1:
                earliest = min(earliest, round_num)
                latest = max(latest, round_num)
                continue

            # Generate next states
            new_players = (players + 1) // 2
            left = pos1 - 1
            mid = pos2 - pos1 - 1

            for w_left in range(left + 1):
                for w_mid in range(mid + 1):
                    new_p1 = 1 + w_left
                    new_p2 = new_p1 + 1 + w_mid

                    if new_p2 <= new_players:
                        state = (new_players, new_p1, new_p2)
                        if state not in visited:
                            visited.add(state)
                            queue.append((new_players, new_p1, new_p2, round_num + 1))

        return [earliest, latest]
