#1728. Cat and Mouse II
#Hard
#
#A game is played by a cat and a mouse named Cat and Mouse.
#
#The environment is represented by a grid of size rows x cols, where each
#element is a wall, floor, player (Cat, Mouse), or food.
#
#- Players are represented by 'C' (Cat), 'M' (Mouse).
#- Floors are '.' and can be walked on.
#- Walls are '#' and cannot be walked on.
#- Food is 'F' and can be walked on.
#- There is only one of each 'C', 'M', 'F' in grid.
#
#Mouse and Cat play according to the following rules:
#- Mouse moves first, then they take turns.
#- In each turn, Cat and Mouse can jump at most catJump or mouseJump cells.
#- They cannot jump over walls.
#- They can stay in place.
#
#The game can end in 4 ways:
#- Cat wins if Cat occupies same position as Mouse.
#- Cat wins if Cat reaches Food first.
#- Mouse wins if Mouse reaches Food first.
#- Mouse wins if Mouse is not caught for 1000 turns.
#
#Return true if Mouse can win assuming both play optimally.
#
#Constraints:
#    rows == grid.length
#    cols == grid[i].length
#    1 <= rows, cols <= 8
#    grid[i][j] consists only of 'C', 'M', 'F', '.', '#'
#    There is only one of each 'C', 'M', 'F' in grid.
#    1 <= catJump, mouseJump <= 8

from typing import List
from functools import lru_cache

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        """
        Game theory with memoization.
        State: (mouse_pos, cat_pos, turn, moves)
        """
        rows, cols = len(grid), len(grid[0])

        # Find positions
        mouse_start = cat_start = food = None
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'M':
                    mouse_start = (i, j)
                elif grid[i][j] == 'C':
                    cat_start = (i, j)
                elif grid[i][j] == 'F':
                    food = (i, j)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def get_moves(pos, max_jump):
            """Get all possible moves from position."""
            r, c = pos
            moves = [(r, c)]  # Can stay in place

            for dr, dc in directions:
                for jump in range(1, max_jump + 1):
                    nr, nc = r + dr * jump, c + dc * jump
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                        moves.append((nr, nc))
                    else:
                        break  # Can't jump over walls

            return moves

        @lru_cache(maxsize=None)
        def can_mouse_win(mouse, cat, is_mouse_turn, turns):
            # Too many turns - mouse wins by default
            if turns >= 70:  # rows * cols is enough
                return False

            # Mouse on food - mouse wins
            if mouse == food:
                return True

            # Cat on food or catches mouse - cat wins
            if cat == food or cat == mouse:
                return False

            if is_mouse_turn:
                # Mouse's turn - mouse wins if ANY move leads to win
                for next_mouse in get_moves(mouse, mouseJump):
                    if can_mouse_win(next_mouse, cat, False, turns + 1):
                        return True
                return False
            else:
                # Cat's turn - mouse wins if ALL cat moves still lead to mouse win
                for next_cat in get_moves(cat, catJump):
                    if not can_mouse_win(mouse, next_cat, True, turns + 1):
                        return False
                return True

        return can_mouse_win(mouse_start, cat_start, True, 0)


class SolutionBFS:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        """
        BFS approach with state encoding.
        """
        from collections import deque

        rows, cols = len(grid), len(grid[0])

        # Find positions
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'M':
                    mouse_start = i * cols + j
                elif grid[i][j] == 'C':
                    cat_start = i * cols + j
                elif grid[i][j] == 'F':
                    food = i * cols + j

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def get_moves(pos, max_jump):
            r, c = pos // cols, pos % cols
            moves = [pos]
            for dr, dc in directions:
                for jump in range(1, max_jump + 1):
                    nr, nc = r + dr * jump, c + dc * jump
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                        moves.append(nr * cols + nc)
                    else:
                        break
            return moves

        MAX_TURNS = rows * cols * 2

        # Memo: (mouse, cat, turn) -> True/False/None
        memo = {}

        def solve(mouse, cat, is_mouse_turn, turns):
            if turns > MAX_TURNS:
                return False
            if mouse == food:
                return True
            if cat == food or cat == mouse:
                return False

            state = (mouse, cat, is_mouse_turn)
            if state in memo:
                return memo[state]

            if is_mouse_turn:
                result = any(solve(nm, cat, False, turns + 1)
                            for nm in get_moves(mouse, mouseJump))
            else:
                result = all(solve(mouse, nc, True, turns + 1)
                            for nc in get_moves(cat, catJump))

            memo[state] = result
            return result

        return solve(mouse_start, cat_start, True, 0)
