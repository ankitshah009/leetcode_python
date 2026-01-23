#1036. Escape a Large Maze
#Hard
#
#There is a 1 million by 1 million grid on an XY-plane, and the coordinates
#of each grid square are (x, y).
#
#We start at the source = [sx, sy] square and want to reach the target =
#[tx, ty] square. There is also an array of blocked squares, where each
#blocked[i] = [xi, yi] represents a blocked square with coordinates (xi, yi).
#
#Each move, we can walk from one square to an adjacent square in one of the
#4 cardinal directions (north, east, west, south) unless the blocked square
#or grid boundary would prevent that.
#
#Return true if and only if it is possible to reach the target square from
#the source square through a sequence of valid moves.
#
#Example 1:
#Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
#Output: false
#Explanation: The target square is inaccessible.
#
#Example 2:
#Input: blocked = [], source = [0,0], target = [999999,999999]
#Output: true
#
#Constraints:
#    0 <= blocked.length <= 200
#    blocked[i].length == 2
#    0 <= xi, yi < 10^6
#    source.length == target.length == 2
#    0 <= sx, sy, tx, ty < 10^6
#    source != target
#    It is guaranteed that source and target are not blocked.

from typing import List
from collections import deque

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """
        Key insight: With at most 200 blocked cells, max enclosed area
        is when they form a corner (200*199/2 < 20000 cells).

        BFS from both source and target. If either can escape the
        potential enclosure (visit more than max_area cells), or if
        they meet, return True.
        """
        if not blocked:
            return True

        blocked_set = set(map(tuple, blocked))
        N = 10**6

        # Maximum area that can be enclosed by n blocks
        n = len(blocked)
        max_area = n * (n - 1) // 2

        def bfs(start, end):
            """Returns True if start is not enclosed or can reach end"""
            queue = deque([tuple(start)])
            visited = {tuple(start)}
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while queue:
                if len(visited) > max_area:
                    return True  # Escaped enclosure

                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in blocked_set and (nx, ny) not in visited:
                        if [nx, ny] == end:
                            return True
                        visited.add((nx, ny))
                        queue.append((nx, ny))

            return False

        # Both source and target must be able to escape their potential enclosures
        return bfs(source, target) and bfs(target, source)


class SolutionDFS:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """DFS approach with same logic"""
        if not blocked:
            return True

        blocked_set = set(map(tuple, blocked))
        N = 10**6
        max_area = len(blocked) * (len(blocked) - 1) // 2

        def dfs(start, end):
            stack = [tuple(start)]
            visited = {tuple(start)}
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while stack:
                if len(visited) > max_area:
                    return True

                x, y = stack.pop()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in blocked_set and (nx, ny) not in visited:
                        if [nx, ny] == end:
                            return True
                        visited.add((nx, ny))
                        stack.append((nx, ny))

            return False

        return dfs(source, target) and dfs(target, source)
