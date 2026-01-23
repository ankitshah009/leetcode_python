#1743. Restore the Array From Adjacent Pairs
#Medium
#
#There is an integer array nums that consists of n unique elements, but you have
#forgotten it. However, you do remember every pair of adjacent elements in nums.
#
#You are given a 2D integer array adjacentPairs of size n - 1 where each
#adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent
#in nums.
#
#It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1]
#will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]].
#The pairs can appear in any order.
#
#Return the original array nums. If there are multiple solutions, return any of
#them.
#
#Example 1:
#Input: adjacentPairs = [[2,1],[3,4],[3,2]]
#Output: [1,2,3,4]
#
#Example 2:
#Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
#Output: [-2,4,1,-3]
#
#Example 3:
#Input: adjacentPairs = [[100000,-100000]]
#Output: [100000,-100000]
#
#Constraints:
#    nums.length == n
#    adjacentPairs.length == n - 1
#    adjacentPairs[i].length == 2
#    2 <= n <= 10^5
#    -10^5 <= nums[i], ui, vi <= 10^5

from typing import List
from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        """
        Build graph, find endpoint (degree 1), traverse.
        """
        graph = defaultdict(list)

        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        # Find an endpoint (node with only one neighbor)
        start = None
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                start = node
                break

        # Traverse from start
        n = len(adjacentPairs) + 1
        result = [start]
        seen = {start}

        while len(result) < n:
            current = result[-1]
            for neighbor in graph[current]:
                if neighbor not in seen:
                    result.append(neighbor)
                    seen.add(neighbor)
                    break

        return result


class SolutionDFS:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        """
        DFS traversal.
        """
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        # Find endpoint
        start = next(node for node, neighbors in graph.items()
                    if len(neighbors) == 1)

        result = []
        visited = set()

        def dfs(node):
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)
        return result


class SolutionIterative:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        """
        Iterative with simpler tracking.
        """
        graph = defaultdict(set)
        for u, v in adjacentPairs:
            graph[u].add(v)
            graph[v].add(u)

        # Find endpoint
        start = next(node for node in graph if len(graph[node]) == 1)

        result = [start]
        prev = None

        while len(result) < len(adjacentPairs) + 1:
            current = result[-1]
            # Find next node (not previous)
            for neighbor in graph[current]:
                if neighbor != prev:
                    result.append(neighbor)
                    prev = current
                    break

        return result
