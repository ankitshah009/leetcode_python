#909. Snakes and Ladders
#Medium
#
#You are given an n x n integer matrix board where the cells are labeled from 1
#to n^2 in a Boustrophedon style starting from the bottom left.
#
#You start on square 1 of the board. In each move, starting from square curr,
#do the following:
#- Choose a destination square next with a label in the range [curr+1, min(curr+6, n^2)]
#- If next has a snake or ladder, you must move to the destination of that snake/ladder
#
#Return the minimum number of moves to reach square n^2, or -1 if impossible.
#
#Example 1:
#Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],
#                [-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
#Output: 4
#
#Constraints:
#    n == board.length == board[i].length
#    2 <= n <= 20
#    board[i][j] is either -1 or in the range [1, n^2].
#    Square 1 and n^2 have no snake or ladder.

from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        """
        BFS from square 1 to n^2.
        """
        n = len(board)
        target = n * n

        def get_position(num: int) -> tuple[int, int]:
            """Convert square number to board coordinates."""
            num -= 1
            row = n - 1 - num // n
            col = num % n if (n - 1 - row) % 2 == 0 else n - 1 - num % n
            return row, col

        queue = deque([1])
        visited = {1}
        moves = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr == target:
                    return moves

                for dice in range(1, 7):
                    next_sq = curr + dice
                    if next_sq > target:
                        break

                    r, c = get_position(next_sq)
                    if board[r][c] != -1:
                        next_sq = board[r][c]

                    if next_sq not in visited:
                        visited.add(next_sq)
                        queue.append(next_sq)

            moves += 1

        return -1


class SolutionFlatten:
    """Flatten board first"""

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        # Flatten board
        cells = [0]  # 1-indexed
        for i in range(n - 1, -1, -1):
            row = board[i] if (n - 1 - i) % 2 == 0 else board[i][::-1]
            cells.extend(row)

        target = n * n
        queue = deque([1])
        dist = {1: 0}

        while queue:
            curr = queue.popleft()

            for dice in range(1, 7):
                next_sq = curr + dice
                if next_sq > target:
                    break

                if cells[next_sq] != -1:
                    next_sq = cells[next_sq]

                if next_sq == target:
                    return dist[curr] + 1

                if next_sq not in dist:
                    dist[next_sq] = dist[curr] + 1
                    queue.append(next_sq)

        return -1
