#1766. Tree of Coprimes
#Hard
#
#There is a tree (i.e., a connected, undirected graph with no cycles) consisting
#of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. Each node has a
#value associated with it, and the root of the tree is node 0.
#
#To represent this tree, you are given an integer array nums and a 2D array
#edges. Each nums[i] represents the ith node's value, and each edges[j] =
#[uj, vj] represents an edge between nodes uj and vj in the tree.
#
#Two values x and y are coprime if gcd(x, y) == 1 where gcd(x, y) is the greatest
#common divisor of x and y.
#
#An ancestor of a node i is any other node on the shortest path from node i to
#the root. A node is not considered an ancestor of itself.
#
#Return an array ans of size n, where ans[i] is the closest ancestor of node i
#such that nums[i] and nums[ans[i]] are coprime, or -1 if there is no such
#ancestor.
#
#Example 1:
#Input: nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
#Output: [-1,0,0,1]
#
#Constraints:
#    nums.length == n
#    1 <= nums[i] <= 50
#    1 <= n <= 10^5
#    edges.length == n - 1
#    edges[j].length == 2
#    0 <= uj, vj < n
#    uj != vj

from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        """
        DFS with tracking ancestors by value.
        Precompute coprime pairs (values 1-50).
        """
        n = len(nums)

        # Precompute coprime pairs
        coprimes = defaultdict(list)
        for i in range(1, 51):
            for j in range(1, 51):
                if gcd(i, j) == 1:
                    coprimes[i].append(j)

        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        result = [-1] * n
        # ancestors[val] = stack of (node_id, depth) with value val
        ancestors = defaultdict(list)

        def dfs(node: int, parent: int, depth: int):
            # Find closest coprime ancestor
            best_depth = -1
            best_node = -1

            for coprime_val in coprimes[nums[node]]:
                if ancestors[coprime_val]:
                    ancestor_node, ancestor_depth = ancestors[coprime_val][-1]
                    if ancestor_depth > best_depth:
                        best_depth = ancestor_depth
                        best_node = ancestor_node

            result[node] = best_node

            # Add current node to ancestors
            val = nums[node]
            ancestors[val].append((node, depth))

            # DFS children
            for child in adj[node]:
                if child != parent:
                    dfs(child, node, depth + 1)

            # Remove current node from ancestors (backtrack)
            ancestors[val].pop()

        dfs(0, -1, 0)
        return result


class SolutionIterative:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        """
        Iterative DFS with explicit stack.
        """
        from math import gcd

        n = len(nums)

        # Precompute coprimes
        coprimes = defaultdict(list)
        for i in range(1, 51):
            for j in range(1, 51):
                if gcd(i, j) == 1:
                    coprimes[i].append(j)

        # Build tree
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        result = [-1] * n
        ancestors = defaultdict(list)
        visited = [False] * n

        # Stack: (node, parent, depth, is_entering)
        stack = [(0, -1, 0, True)]

        while stack:
            node, parent, depth, entering = stack.pop()

            if entering:
                # Find best coprime ancestor
                best_depth, best_node = -1, -1
                for cp in coprimes[nums[node]]:
                    if ancestors[cp]:
                        anc_node, anc_depth = ancestors[cp][-1]
                        if anc_depth > best_depth:
                            best_depth = anc_depth
                            best_node = anc_node
                result[node] = best_node

                # Add exit marker
                stack.append((node, parent, depth, False))

                # Add to ancestors
                ancestors[nums[node]].append((node, depth))
                visited[node] = True

                # Add children
                for child in adj[node]:
                    if not visited[child]:
                        stack.append((child, node, depth + 1, True))
            else:
                # Exiting - remove from ancestors
                ancestors[nums[node]].pop()

        return result
