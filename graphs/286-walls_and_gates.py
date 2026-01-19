#286. Walls and Gates
#Medium
#
#You are given an m x n grid rooms initialized with these three possible values.
#    -1 A wall or an obstacle.
#    0 A gate.
#    INF Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent
#        INF as you may assume that the distance to a gate is less than 2147483647.
#
#Fill each empty room with the distance to its nearest gate. If it is impossible to reach
#a gate, it should be filled with INF.
#
#Example 1:
#Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],
#                [2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
#Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
#
#Example 2:
#Input: rooms = [[-1]]
#Output: [[-1]]
#
#Constraints:
#    m == rooms.length
#    n == rooms[i].length
#    1 <= m, n <= 250
#    rooms[i][j] is -1, 0, or 2^31 - 1.

from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        INF = 2147483647
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Multi-source BFS from all gates
        queue = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))

        while queue:
            row, col, dist = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < m and 0 <= new_col < n and rooms[new_row][new_col] == INF:
                    rooms[new_row][new_col] = dist + 1
                    queue.append((new_row, new_col, dist + 1))
