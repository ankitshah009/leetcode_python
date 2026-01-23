#886. Possible Bipartition
#Medium
#
#We want to split a group of n people (labeled from 1 to n) into two groups of
#any size. Each person may dislike some other people, and they should not go
#into the same group.
#
#Given the integer n and the array dislikes where dislikes[i] = [ai, bi]
#indicates that the person labeled ai does not like the person labeled bi,
#return true if it is possible to split everyone into two groups in this way.
#
#Example 1:
#Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
#Output: true
#Explanation: group1 = [1,4], group2 = [2,3]
#
#Example 2:
#Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
#Output: false
#
#Example 3:
#Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
#Output: false
#
#Constraints:
#    1 <= n <= 2000
#    0 <= dislikes.length <= 10^4
#    dislikes[i].length == 2
#    1 <= ai < bi <= n
#    All the pairs of dislikes are unique.

from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        """
        Graph coloring: check if graph is bipartite using BFS.
        """
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = {}  # -1 or 1

        for start in range(1, n + 1):
            if start in color:
                continue

            # BFS
            queue = deque([start])
            color[start] = 0

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor in color:
                        if color[neighbor] == color[node]:
                            return False
                    else:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)

        return True


class SolutionDFS:
    """DFS coloring"""

    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = {}

        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if neighbor in color:
                    if color[neighbor] == c:
                        return False
                elif not dfs(neighbor, 1 - c):
                    return False
            return True

        for i in range(1, n + 1):
            if i not in color and not dfs(i, 0):
                return False

        return True


class SolutionUnionFind:
    """Union-Find: for each person, all disliked should be in same group"""

    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        for person in range(1, n + 1):
            enemies = graph[person]
            if not enemies:
                continue

            # All enemies should be in the same group
            for i in range(1, len(enemies)):
                union(enemies[0], enemies[i])

            # Person should not be in same group as enemies
            if find(person) == find(enemies[0]):
                return False

        return True
