#1319. Number of Operations to Make Network Connected
#Medium
#
#There are n computers numbered from 0 to n - 1 connected by ethernet cables
#connections forming a network where connections[i] = [ai, bi] represents a
#connection between computers ai and bi. Any computer can reach any other
#computer directly or indirectly through the network.
#
#You are given an initial computer network connections. You can extract certain
#cables between two directly connected computers, and place them between any
#pair of disconnected computers to make them directly connected.
#
#Return the minimum number of times you need to do this in order to make all
#the computers connected. If it is not possible, return -1.
#
#Example 1:
#Input: n = 4, connections = [[0,1],[0,2],[1,2]]
#Output: 1
#Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
#
#Example 2:
#Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
#Output: 2
#
#Example 3:
#Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
#Output: -1
#Explanation: There are not enough cables.
#
#Constraints:
#    1 <= n <= 10^5
#    1 <= connections.length <= min(n * (n - 1) / 2, 10^5)
#    connections[i].length == 2
#    0 <= ai, bi < n
#    ai != bi
#    There are no repeated connections.
#    No two computers are connected by more than one cable.

from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        Need at least n-1 cables to connect n computers.
        Count connected components. Need (components - 1) moves.
        """
        # Check if we have enough cables
        if len(connections) < n - 1:
            return -1

        # Build adjacency list and find connected components
        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)

        # Count connected components using DFS
        visited = [False] * n
        components = 0

        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1

        # Need (components - 1) operations to connect all components
        return components - 1


class SolutionUnionFind:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """Union-Find approach"""
        if len(connections) < n - 1:
            return -1

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        for a, b in connections:
            union(a, b)

        # Count unique roots
        components = len(set(find(i) for i in range(n)))

        return components - 1


class SolutionBFS:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """BFS for counting components"""
        from collections import deque

        if len(connections) < n - 1:
            return -1

        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n
        components = 0

        for start in range(n):
            if visited[start]:
                continue

            queue = deque([start])
            visited[start] = True

            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

            components += 1

        return components - 1
