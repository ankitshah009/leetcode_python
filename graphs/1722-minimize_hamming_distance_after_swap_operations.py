#1722. Minimize Hamming Distance After Swap Operations
#Medium
#
#You are given two integer arrays, source and target, both of length n. You are
#also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates
#that you are allowed to swap the elements at index ai and index bi (0-indexed)
#of array source. Note that you can swap elements at a specific pair of indices
#multiple times and in any order.
#
#The Hamming distance of two arrays of the same length, source and target, is
#the number of positions where the elements are different. Formally, it is the
#number of indices i for 0 <= i <= n - 1 where source[i] != target[i].
#
#Return the minimum Hamming distance of source and target after performing any
#amount of swap operations on array source.
#
#Example 1:
#Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
#Output: 1
#
#Example 2:
#Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
#Output: 2
#
#Example 3:
#Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
#Output: 0
#
#Constraints:
#    n == source.length == target.length
#    1 <= n <= 10^5
#    1 <= source[i], target[i] <= 10^5
#    0 <= allowedSwaps.length <= 10^5
#    allowedSwaps[i].length == 2
#    0 <= ai, bi <= n - 1

from typing import List
from collections import Counter, defaultdict

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        """
        Union-Find: indices in same component can be freely rearranged.
        For each component, count mismatches that can't be resolved.
        """
        n = len(source)
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        # Build components
        for a, b in allowedSwaps:
            union(a, b)

        # Group indices by component
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)

        # For each component, count minimum unmatched elements
        hamming = 0
        for indices in components.values():
            source_count = Counter(source[i] for i in indices)
            target_count = Counter(target[i] for i in indices)

            # Count matches
            matches = sum((source_count & target_count).values())

            # Unmatched = component size - matches
            hamming += len(indices) - matches

        return hamming


class SolutionDFS:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        """
        DFS to find connected components.
        """
        n = len(source)
        graph = defaultdict(list)

        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        hamming = 0

        def dfs(node: int, component: list):
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)

        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)

                # Count mismatches in this component
                source_count = Counter(source[j] for j in component)
                target_count = Counter(target[j] for j in component)

                matches = sum((source_count & target_count).values())
                hamming += len(component) - matches

        return hamming
