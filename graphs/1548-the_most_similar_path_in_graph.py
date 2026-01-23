#1548. The Most Similar Path in a Graph
#Hard
#
#We have n cities and m bi-directional roads where roads[i] = [ai, bi] connects
#city ai with city bi. Each city has a name consisting of exactly three upper-case
#English letters given in the string array names. Starting at any city x, you
#can reach any city y where y != x (i.e., the cities and the roads are forming
#an undirected connected graph).
#
#You will be given a string array targetPath. You should find a path in the
#graph of the same length and with the minimum edit distance to targetPath.
#
#You need to return the order of the nodes in the path with the minimum edit
#distance. The path should be of the same length of targetPath and should be
#valid (i.e., there should be a direct road between ans[i] and ans[i + 1]). If
#there are multiple answers return any one of them.
#
#The edit distance is defined as follows:
#
#Edit distance = sum of (target[i] != path[i]) for all i in [0, len(target))
#
#Example 1:
#Input: n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"], targetPath = ["ATL","DXB","HND","LAX"]
#Output: [0,2,4,2]
#Explanation: [0,2,4,2], [0,3,0,2] and [0,3,1,2] are accepted answers.
#[0,2,4,2] is equivalent to ["ATL","LAX","HND","LAX"] which has edit distance = 1 with targetPath.
#[0,3,0,2] is equivalent to ["ATL","DXB","ATL","LAX"] which has edit distance = 1 with targetPath.
#[0,3,1,2] is equivalent to ["ATL","DXB","PEK","LAX"] which has edit distance = 1 with targetPath.
#
#Example 2:
#Input: n = 4, roads = [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], names = ["ATL","PEK","LAX","DXB"], targetPath = ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]
#Output: [0,1,0,1,0,1,0,1]
#Explanation: Any path in this graph has edit distance = 8 with targetPath.
#
#Example 3:
#Input: n = 6, roads = [[0,1],[1,2],[2,3],[3,4],[4,5]], names = ["ATL","PEK","LAX","ATL","DXB","HND"], targetPath = ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
#Output: [3,4,5,4,3,2,1]
#Explanation: [3,4,5,4,3,2,1] is the only path with edit distance = 0 with targetPath.
#
#Constraints:
#    2 <= n <= 100
#    m == roads.length
#    n - 1 <= m <= (n * (n - 1) / 2)
#    0 <= ai, bi <= n - 1
#    ai != bi
#    The graph is guaranteed to be connected and each pair of nodes may have at
#    most one direct road.
#    names.length == n
#    names[i].length == 3
#    names[i] consists of upper-case English letters.
#    1 <= targetPath.length <= 100
#    targetPath[i].length == 3
#    targetPath[i] consists of upper-case English letters.

from typing import List
from collections import defaultdict

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        """
        DP approach: dp[i][j] = min edit distance to reach city j at step i.
        Track parent to reconstruct path.
        """
        # Build adjacency list
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        m = len(targetPath)
        INF = float('inf')

        # dp[i][j] = min edit distance ending at city j after i steps
        dp = [[INF] * n for _ in range(m)]

        # parent[i][j] = which city we came from to reach city j at step i
        parent = [[-1] * n for _ in range(m)]

        # Initialize first step
        for j in range(n):
            dp[0][j] = 0 if names[j] == targetPath[0] else 1

        # Fill DP
        for i in range(1, m):
            for j in range(n):
                cost = 0 if names[j] == targetPath[i] else 1

                for prev in graph[j]:
                    if dp[i - 1][prev] + cost < dp[i][j]:
                        dp[i][j] = dp[i - 1][prev] + cost
                        parent[i][j] = prev

        # Find best ending city
        min_dist = INF
        end_city = 0
        for j in range(n):
            if dp[m - 1][j] < min_dist:
                min_dist = dp[m - 1][j]
                end_city = j

        # Reconstruct path
        path = [0] * m
        path[m - 1] = end_city
        for i in range(m - 2, -1, -1):
            path[i] = parent[i + 1][path[i + 1]]

        return path


class SolutionOptimized:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        """
        Space-optimized DP using only two rows.
        """
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        m = len(targetPath)
        INF = float('inf')

        # Only keep current and previous row
        prev_dp = [INF] * n
        prev_parent = [[-1] * n for _ in range(m)]

        # Initialize
        for j in range(n):
            prev_dp[j] = 0 if names[j] == targetPath[0] else 1

        # DP
        for i in range(1, m):
            curr_dp = [INF] * n

            for j in range(n):
                cost = 0 if names[j] == targetPath[i] else 1

                for p in graph[j]:
                    if prev_dp[p] + cost < curr_dp[j]:
                        curr_dp[j] = prev_dp[p] + cost
                        prev_parent[i][j] = p

            prev_dp = curr_dp

        # Find minimum
        end = min(range(n), key=lambda x: prev_dp[x])

        # Reconstruct
        path = [end]
        for i in range(m - 1, 0, -1):
            path.append(prev_parent[i][path[-1]])

        return path[::-1]


class SolutionBFS:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        """
        BFS-like approach processing level by level.
        """
        from collections import defaultdict

        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        m = len(targetPath)

        # State: (edit_distance, path_so_far)
        # dp[city] = (min_dist, path)
        current = {}
        for city in range(n):
            dist = 0 if names[city] == targetPath[0] else 1
            current[city] = (dist, [city])

        for i in range(1, m):
            next_level = {}

            for city in range(n):
                cost = 0 if names[city] == targetPath[i] else 1

                for prev in graph[city]:
                    if prev in current:
                        prev_dist, prev_path = current[prev]
                        new_dist = prev_dist + cost

                        if city not in next_level or new_dist < next_level[city][0]:
                            next_level[city] = (new_dist, prev_path + [city])

            current = next_level

        # Find minimum
        best = min(current.values(), key=lambda x: x[0])
        return best[1]
