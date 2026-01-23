#1202. Smallest String With Swaps
#Medium
#
#You are given a string s, and an array of pairs of indices in the string pairs
#where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
#
#You can swap the characters at any pair of indices in the given pairs any
#number of times.
#
#Return the lexicographically smallest string that s can be changed to after
#using the swaps.
#
#Example 1:
#Input: s = "dcab", pairs = [[0,3],[1,2]]
#Output: "bacd"
#Explanation:
#Swap s[0] and s[3], s = "bcad"
#Swap s[1] and s[2], s = "bacd"
#
#Example 2:
#Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
#Output: "abcd"
#Explanation:
#Swap s[0] and s[3], s = "bcad"
#Swap s[0] and s[2], s = "acbd"
#Swap s[1] and s[2], s = "abcd"
#
#Example 3:
#Input: s = "cba", pairs = [[0,1],[1,2]]
#Output: "abc"
#Explanation:
#Swap s[0] and s[1], s = "bca"
#Swap s[1] and s[2], s = "bac"
#Swap s[0] and s[1], s = "abc"
#
#Constraints:
#    1 <= s.length <= 10^5
#    0 <= pairs.length <= 10^5
#    0 <= pairs[i][0], pairs[i][1] < s.length
#    s only contains lower case English letters.

from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        Connected indices can be arbitrarily rearranged.
        Use Union-Find to group connected indices.
        Sort characters within each group.
        """
        n = len(s)
        uf = UnionFind(n)

        # Union all pairs
        for a, b in pairs:
            uf.union(a, b)

        # Group indices by their root
        groups = defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(i)

        # Build result
        result = list(s)

        for indices in groups.values():
            # Get characters at these indices, sort them
            chars = sorted(s[i] for i in indices)
            # Place sorted characters back at sorted indices
            for idx, char in zip(sorted(indices), chars):
                result[idx] = char

        return ''.join(result)


class SolutionDFS:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """DFS-based connected components"""
        n = len(s)

        # Build adjacency list
        graph = defaultdict(list)
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        result = list(s)

        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)

        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)

                # Sort characters in this component
                chars = sorted(s[idx] for idx in component)
                for idx, char in zip(sorted(component), chars):
                    result[idx] = char

        return ''.join(result)
