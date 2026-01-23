#1782. Count Pairs Of Nodes
#Hard
#
#You are given an undirected graph defined by an integer n, the number of nodes,
#and a 2D integer array edges, the edges in the graph, where edges[i] = [ui, vi]
#indicates that there is an undirected edge between ui and vi. You are also given
#an integer array queries.
#
#Let incident(a, b) be defined as the number of edges that are connected to
#either node a or node b.
#
#Note that there can be multiple edges between two nodes.
#
#The answer to the jth query is the number of pairs of nodes (a, b) that satisfy
#both of the following conditions:
#- a < b
#- incident(a, b) > queries[j]
#
#Return an array answers such that answers[j] is the answer of the jth query.
#
#Example 1:
#Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
#Output: [6,5]
#
#Constraints:
#    2 <= n <= 2 * 10^4
#    1 <= edges.length <= 10^5
#    1 <= ui, vi <= n
#    ui != vi
#    1 <= queries.length <= 20
#    0 <= queries[j] < edges.length

from typing import List
from collections import Counter, defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        """
        For pair (a, b): incident(a,b) = degree[a] + degree[b] - edge_count(a,b)

        1. Sort degrees and use two pointers to count pairs where deg[a] + deg[b] > q
        2. Subtract overcounted pairs where deg[a] + deg[b] - edge_count > q is false
        """
        # Count degrees
        degree = [0] * (n + 1)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1

        # Count edges between pairs
        edge_count = Counter()
        for u, v in edges:
            edge_count[(min(u, v), max(u, v))] += 1

        # Sorted degrees for two pointer
        sorted_deg = sorted(degree[1:])

        result = []

        for q in queries:
            count = 0

            # Two pointers on sorted degrees
            left, right = 0, n - 1
            while left < right:
                if sorted_deg[left] + sorted_deg[right] > q:
                    count += right - left
                    right -= 1
                else:
                    left += 1

            # Subtract overcounted pairs
            for (u, v), ec in edge_count.items():
                if degree[u] + degree[v] > q and degree[u] + degree[v] - ec <= q:
                    count -= 1

            result.append(count)

        return result


class SolutionBinarySearch:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        """
        Binary search approach.
        """
        import bisect

        degree = [0] * (n + 1)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1

        edge_count = Counter((min(u, v), max(u, v)) for u, v in edges)
        sorted_deg = sorted(degree[1:])

        result = []
        for q in queries:
            count = 0

            # For each node, find how many others can pair with it
            for i in range(n):
                # Need sorted_deg[j] > q - sorted_deg[i]
                threshold = q - sorted_deg[i]
                j = bisect.bisect_right(sorted_deg, threshold, i + 1)
                count += n - j

            # Subtract overcounted
            for (u, v), ec in edge_count.items():
                if degree[u] + degree[v] > q and degree[u] + degree[v] - ec <= q:
                    count -= 1

            result.append(count)

        return result
