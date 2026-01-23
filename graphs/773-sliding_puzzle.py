#773. Sliding Puzzle
#Hard
#
#On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty
#square represented by 0. A move consists of choosing 0 and a 4-directionally
#adjacent number and swapping it.
#
#The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
#
#Given the puzzle board board, return the least number of moves required so
#that the state of the board is solved. If it is impossible for the state of
#the board to be solved, return -1.
#
#Example 1:
#Input: board = [[1,2,3],[4,0,5]]
#Output: 1
#Explanation: Swap the 0 and the 5 in one move.
#
#Example 2:
#Input: board = [[1,2,3],[5,4,0]]
#Output: -1
#
#Example 3:
#Input: board = [[4,1,2],[5,0,3]]
#Output: 5
#
#Constraints:
#    board.length == 2
#    board[i].length == 3
#    0 <= board[i][j] <= 5
#    Each value board[i][j] is unique.

from collections import deque

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        """
        BFS on state space. State is tuple of flattened board.
        """
        # Neighbors for each position in flattened 2x3 board
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        start = tuple(board[0] + board[1])
        target = (1, 2, 3, 4, 5, 0)

        if start == target:
            return 0

        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            state, moves = queue.popleft()

            # Find position of 0
            zero_pos = state.index(0)

            # Try all possible swaps
            for neighbor in neighbors[zero_pos]:
                # Create new state by swapping
                new_state = list(state)
                new_state[zero_pos], new_state[neighbor] = new_state[neighbor], new_state[zero_pos]
                new_state = tuple(new_state)

                if new_state == target:
                    return moves + 1

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + 1))

        return -1


class SolutionAStar:
    """A* search with Manhattan distance heuristic"""

    def slidingPuzzle(self, board: list[list[int]]) -> int:
        import heapq

        neighbors = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}

        def manhattan(state):
            dist = 0
            for i, val in enumerate(state):
                if val != 0:
                    target_row, target_col = (val - 1) // 3, (val - 1) % 3
                    curr_row, curr_col = i // 3, i % 3
                    dist += abs(target_row - curr_row) + abs(target_col - curr_col)
            return dist

        start = tuple(board[0] + board[1])
        target = (1, 2, 3, 4, 5, 0)

        if start == target:
            return 0

        heap = [(manhattan(start), 0, start)]
        visited = {start: 0}

        while heap:
            _, moves, state = heapq.heappop(heap)

            if state == target:
                return moves

            zero_pos = state.index(0)

            for neighbor in neighbors[zero_pos]:
                new_state = list(state)
                new_state[zero_pos], new_state[neighbor] = new_state[neighbor], new_state[zero_pos]
                new_state = tuple(new_state)
                new_moves = moves + 1

                if new_state not in visited or visited[new_state] > new_moves:
                    visited[new_state] = new_moves
                    heapq.heappush(heap, (new_moves + manhattan(new_state), new_moves, new_state))

        return -1
