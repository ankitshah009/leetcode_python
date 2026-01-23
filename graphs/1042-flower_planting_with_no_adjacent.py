#1042. Flower Planting With No Adjacent
#Medium
#
#You have n gardens, labeled from 1 to n, and an array paths where
#paths[i] = [xi, yi] describes a bidirectional path between garden xi and
#garden yi. In each garden, you want to plant one of 4 types of flowers.
#
#All gardens have at most 3 paths coming into or leaving it.
#
#Your task is to choose a flower type for each garden such that, for any
#two gardens connected by a path, they have different types of flowers.
#
#Return any such a choice as an array answer, where answer[i] is the type
#of flower planted in the (i+1)th garden. The flower types are denoted 1, 2,
#3, or 4. It is guaranteed an answer exists.
#
#Example 1:
#Input: n = 3, paths = [[1,2],[2,3],[3,1]]
#Output: [1,2,3]
#
#Example 2:
#Input: n = 4, paths = [[1,2],[3,4]]
#Output: [1,2,1,2]
#
#Example 3:
#Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
#Output: [1,2,3,4]
#
#Constraints:
#    1 <= n <= 10^4
#    0 <= paths.length <= 2 * 10^4
#    paths[i].length == 2
#    1 <= xi, yi <= n
#    xi != yi
#    Every garden has at most 3 paths coming into or leaving it.

from typing import List
from collections import defaultdict

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        """
        Greedy graph coloring. Since max degree is 3 and we have 4 colors,
        we can always find a valid color for each node.
        """
        # Build adjacency list
        graph = defaultdict(list)
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)

        result = [0] * n

        for garden in range(1, n + 1):
            # Find colors used by neighbors
            used_colors = set()
            for neighbor in graph[garden]:
                if result[neighbor - 1] != 0:
                    used_colors.add(result[neighbor - 1])

            # Pick first available color
            for color in range(1, 5):
                if color not in used_colors:
                    result[garden - 1] = color
                    break

        return result


class SolutionSet:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        """Using set difference for available colors"""
        graph = defaultdict(set)
        for x, y in paths:
            graph[x].add(y)
            graph[y].add(x)

        result = [0] * n
        all_colors = {1, 2, 3, 4}

        for garden in range(1, n + 1):
            neighbor_colors = {result[nei - 1] for nei in graph[garden]}
            available = all_colors - neighbor_colors
            result[garden - 1] = available.pop()

        return result
