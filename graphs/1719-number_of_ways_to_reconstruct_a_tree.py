#1719. Number Of Ways To Reconstruct A Tree
#Hard
#
#You are given an array pairs, where pairs[i] = [xi, yi], and:
#- There are no duplicates.
#- xi < yi
#
#Let ways be the number of rooted trees that satisfy the following conditions:
#- The tree consists of nodes whose values appeared in pairs.
#- A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi
#  is an ancestor of xi.
#- Note: the tree does not have to be a binary tree.
#
#Two ways are considered to be different if there is at least one node that has
#different parents in both ways.
#
#Return:
#- 0 if ways == 0
#- 1 if ways == 1
#- 2 if ways > 1
#
#Example 1:
#Input: pairs = [[1,2],[2,3]]
#Output: 1
#
#Example 2:
#Input: pairs = [[1,2],[2,3],[1,3]]
#Output: 2
#
#Example 3:
#Input: pairs = [[1,2],[2,3],[2,4],[1,5]]
#Output: 0
#
#Constraints:
#    1 <= pairs.length <= 10^5
#    1 <= xi < yi <= 500

from typing import List
from collections import defaultdict

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        """
        Key insight: In a tree, if x is ancestor of y, then all ancestors of y
        are also ancestors of x. So degree[x] >= degree[y].
        The root has degree = n - 1 (connected to all nodes).
        """
        # Build adjacency set
        adj = defaultdict(set)
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)

        # Get all nodes
        nodes = list(adj.keys())
        n = len(nodes)

        # Find potential root (node connected to all others)
        root = None
        for node in nodes:
            if len(adj[node]) == n - 1:
                root = node
                break

        if root is None:
            return 0

        # Sort nodes by degree (descending)
        nodes.sort(key=lambda x: -len(adj[x]))

        result = 1
        parent = {}

        for node in nodes:
            # Find parent: smallest degree node in adj[node] with larger degree
            par = None
            min_degree = float('inf')

            for neighbor in adj[node]:
                if len(adj[neighbor]) >= len(adj[node]) and len(adj[neighbor]) < min_degree:
                    min_degree = len(adj[neighbor])
                    par = neighbor

            if par is None:
                # This node should be root
                if len(adj[node]) != n - 1:
                    return 0
            else:
                parent[node] = par

                # All neighbors of node (except parent path) must be in parent's neighbors
                for neighbor in adj[node]:
                    if neighbor != par and neighbor not in adj[par]:
                        return 0

                # If parent has same degree as node, they can swap
                if len(adj[par]) == len(adj[node]):
                    result = 2

        return result


class SolutionAlternate:
    def checkWays(self, pairs: List[List[int]]) -> int:
        """
        Alternative implementation with clearer structure.
        """
        graph = defaultdict(set)
        for a, b in pairs:
            graph[a].add(b)
            graph[b].add(a)

        nodes = list(graph.keys())
        n = len(nodes)

        # Check if root exists (degree n-1)
        max_degree = max(len(graph[node]) for node in nodes)
        if max_degree != n - 1:
            return 0

        # Sort by degree descending
        nodes.sort(key=lambda x: len(graph[x]), reverse=True)

        has_multiple = False
        visited = set()

        for i, node in enumerate(nodes):
            visited.add(node)

            # Find parent (first node with larger degree in neighbors)
            parent = None
            for j in range(i):
                if nodes[j] in graph[node]:
                    parent = nodes[j]
                    break

            if parent is None:
                continue

            # Validate: node's neighbors (except parent) subset of parent's neighbors
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in graph[parent]:
                    return 0

            # Check for swappable (equal degree)
            if len(graph[node]) == len(graph[parent]):
                has_multiple = True

        return 2 if has_multiple else 1
