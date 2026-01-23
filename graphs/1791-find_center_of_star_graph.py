#1791. Find Center of Star Graph
#Easy
#
#There is an undirected star graph consisting of n nodes labeled from 1 to n. A
#star graph is a graph where there is one center node and exactly n - 1 edges
#that connect the center node with every other node.
#
#You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
#that there is an edge between the nodes ui and vi. Return the center of the
#given star graph.
#
#Example 1:
#Input: edges = [[1,2],[2,3],[4,2]]
#Output: 2
#
#Example 2:
#Input: edges = [[1,2],[5,1],[1,3],[1,4]]
#Output: 1
#
#Constraints:
#    3 <= n <= 10^5
#    edges.length == n - 1
#    edges[i].length == 2
#    1 <= ui, vi <= n
#    ui != vi
#    The given edges represent a valid star graph.

from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        Center appears in all edges - just check first two edges.
        """
        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]


class SolutionSet:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        Find common node in first two edges.
        """
        set1 = set(edges[0])
        set2 = set(edges[1])
        return (set1 & set2).pop()


class SolutionDegree:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        Center has degree n-1 (appears in all edges).
        """
        from collections import Counter

        degree = Counter()
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1

        return degree.most_common(1)[0][0]


class SolutionOneEdge:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        Just need to find node that appears in both first two edges.
        """
        a, b = edges[0]
        c, d = edges[1]

        if a == c or a == d:
            return a
        return b
