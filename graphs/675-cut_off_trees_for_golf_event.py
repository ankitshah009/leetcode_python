#675. Cut Off Trees for Golf Event
#Hard
#
#You are asked to cut off all the trees in a forest for a golf event. The forest
#is represented as an m x n matrix. In this matrix:
#
#- 0 means the cell cannot be walked through.
#- 1 means the cell can be walked through and is empty.
#- A number greater than 1 represents a tree in the cell that can be walked through
#  and the number is the tree's height.
#
#In one step, you can walk in any of the four directions: north, east, south, west.
#You can only cut off a tree when you are standing at the same cell as the tree.
#After cutting off a tree, the cell becomes 1 (an empty cell).
#
#You must cut off the trees in order from shortest to tallest. When you cut off
#a tree, the height of that tree becomes 1.
#
#Return the minimum steps you need to walk to cut off all the trees. If you cannot
#cut off all the trees, return -1.
#
#Example 1:
#Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
#Output: 6
#
#Example 2:
#Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
#Output: -1
#
#Example 3:
#Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
#Output: 6
#
#Constraints:
#    m == forest.length
#    n == forest[i].length
#    1 <= m, n <= 50
#    0 <= forest[i][j] <= 10^9

from typing import List
from collections import deque
import heapq

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        """
        BFS between consecutive trees (sorted by height).
        """
        if not forest or not forest[0]:
            return -1

        m, n = len(forest), len(forest[0])

        # Collect all trees and sort by height
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))

        trees.sort()

        def bfs(sr, sc, tr, tc):
            """BFS to find shortest path from (sr, sc) to (tr, tc)"""
            if sr == tr and sc == tc:
                return 0

            visited = [[False] * n for _ in range(m)]
            visited[sr][sc] = True
            queue = deque([(sr, sc, 0)])

            while queue:
                r, c, dist = queue.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and forest[nr][nc] != 0:
                        if nr == tr and nc == tc:
                            return dist + 1

                        visited[nr][nc] = True
                        queue.append((nr, nc, dist + 1))

            return -1

        total_steps = 0
        curr_r, curr_c = 0, 0

        for _, tree_r, tree_c in trees:
            steps = bfs(curr_r, curr_c, tree_r, tree_c)
            if steps == -1:
                return -1
            total_steps += steps
            curr_r, curr_c = tree_r, tree_c

        return total_steps


class SolutionAStar:
    """A* search for potentially better performance"""

    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1

        m, n = len(forest), len(forest[0])

        trees = sorted((forest[i][j], i, j)
                      for i in range(m)
                      for j in range(n)
                      if forest[i][j] > 1)

        def astar(sr, sc, tr, tc):
            if sr == tr and sc == tc:
                return 0

            # Priority queue: (f_score, g_score, r, c)
            # f_score = g_score + heuristic
            heap = [(abs(sr - tr) + abs(sc - tc), 0, sr, sc)]
            visited = set()

            while heap:
                _, dist, r, c = heapq.heappop(heap)

                if (r, c) in visited:
                    continue
                visited.add((r, c))

                if r == tr and c == tc:
                    return dist

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and forest[nr][nc] != 0:
                        h = abs(nr - tr) + abs(nc - tc)
                        heapq.heappush(heap, (dist + 1 + h, dist + 1, nr, nc))

            return -1

        total = 0
        cr, cc = 0, 0

        for _, tr, tc in trees:
            steps = astar(cr, cc, tr, tc)
            if steps == -1:
                return -1
            total += steps
            cr, cc = tr, tc

        return total
