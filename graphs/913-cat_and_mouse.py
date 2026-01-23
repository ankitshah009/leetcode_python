#913. Cat and Mouse
#Hard
#
#A game is played by a cat and a mouse named Cat and Mouse.
#
#The environment is represented by a graph, where nodes are numbered from 0 to
#graph.length - 1. Node 0 is the "Hole". The cat starts at node 2, and the mouse
#starts at node 1. They take turns moving (mouse moves first).
#
#In each turn, the Cat or Mouse must move to an adjacent node of the graph.
#Additionally, the Cat cannot move into the Hole (node 0).
#
#The game can end in three ways:
#- If the Cat occupies the same node as the Mouse, the Cat wins.
#- If the Mouse reaches the Hole, the Mouse wins.
#- If a position is repeated, the game is a draw.
#
#Return: 1 if Mouse wins, 2 if Cat wins, 0 if draw.
#
#Constraints:
#    3 <= graph.length <= 50
#    1 <= graph[i].length < graph.length
#    0 <= graph[i][j] < graph.length
#    graph[i][j] != i
#    graph[i] is unique.
#    The mouse and the cat can always move.

class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        """
        Minimax with memoization.
        State: (mouse_pos, cat_pos, turn)
        """
        from functools import lru_cache

        MOUSE_WIN, CAT_WIN, DRAW = 1, 2, 0
        n = len(graph)

        @lru_cache(maxsize=None)
        def dp(mouse: int, cat: int, turn: int) -> int:
            # Check if game over
            if mouse == 0:
                return MOUSE_WIN
            if mouse == cat:
                return CAT_WIN
            if turn >= 2 * n:
                return DRAW  # Position must have repeated

            if turn % 2 == 0:  # Mouse's turn
                can_draw = False
                for next_mouse in graph[mouse]:
                    result = dp(next_mouse, cat, turn + 1)
                    if result == MOUSE_WIN:
                        return MOUSE_WIN
                    if result == DRAW:
                        can_draw = True
                return DRAW if can_draw else CAT_WIN
            else:  # Cat's turn
                can_draw = False
                for next_cat in graph[cat]:
                    if next_cat == 0:  # Cat can't go to hole
                        continue
                    result = dp(mouse, next_cat, turn + 1)
                    if result == CAT_WIN:
                        return CAT_WIN
                    if result == DRAW:
                        can_draw = True
                return DRAW if can_draw else MOUSE_WIN

        return dp(1, 2, 0)


class SolutionBFS:
    """BFS from terminal states"""

    def catMouseGame(self, graph: list[list[int]]) -> int:
        from collections import deque

        n = len(graph)
        MOUSE_WIN, CAT_WIN, DRAW = 1, 2, 0

        # State: (mouse, cat, turn) where turn 0 = mouse, 1 = cat
        # color[mouse][cat][turn] = outcome
        color = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        # Initialize degrees
        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = len(graph[c]) - (1 if 0 in graph[c] else 0)

        queue = deque()

        # Terminal states
        for c in range(n):
            for t in range(2):
                # Mouse at hole - mouse wins
                color[0][c][t] = MOUSE_WIN
                queue.append((0, c, t, MOUSE_WIN))
                # Mouse and cat same position (cat wins)
                if c > 0:
                    color[c][c][t] = CAT_WIN
                    queue.append((c, c, t, CAT_WIN))

        while queue:
            m, c, t, outcome = queue.popleft()
            prev_turn = 1 - t

            if prev_turn == 0:  # Previous was mouse's turn
                for prev_m in graph[m]:
                    if color[prev_m][c][prev_turn] == DRAW:
                        if outcome == MOUSE_WIN:
                            color[prev_m][c][prev_turn] = MOUSE_WIN
                            queue.append((prev_m, c, prev_turn, MOUSE_WIN))
                        else:
                            degree[prev_m][c][prev_turn] -= 1
                            if degree[prev_m][c][prev_turn] == 0:
                                color[prev_m][c][prev_turn] = CAT_WIN
                                queue.append((prev_m, c, prev_turn, CAT_WIN))
            else:  # Previous was cat's turn
                for prev_c in graph[c]:
                    if prev_c == 0:
                        continue
                    if color[m][prev_c][prev_turn] == DRAW:
                        if outcome == CAT_WIN:
                            color[m][prev_c][prev_turn] = CAT_WIN
                            queue.append((m, prev_c, prev_turn, CAT_WIN))
                        else:
                            degree[m][prev_c][prev_turn] -= 1
                            if degree[m][prev_c][prev_turn] == 0:
                                color[m][prev_c][prev_turn] = MOUSE_WIN
                                queue.append((m, prev_c, prev_turn, MOUSE_WIN))

        return color[1][2][0]
