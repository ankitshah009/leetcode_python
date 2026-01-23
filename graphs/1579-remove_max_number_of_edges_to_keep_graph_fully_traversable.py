#1579. Remove Max Number of Edges to Keep Graph Fully Traversable
#Hard
#
#Alice and Bob have an undirected graph of n nodes and three types of edges:
#- Type 1: Can be traversed by Alice only.
#- Type 2: Can be traversed by Bob only.
#- Type 3: Can be traversed by both Alice and Bob.
#
#Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional
#edge of type typei between nodes ui and vi, find the maximum number of edges
#you can remove so that after removing the edges, the graph can still be fully
#traversed by both Alice and Bob. The graph is fully traversed by Alice (resp.
#Bob) if starting from any node, she (resp. he) can reach all other nodes.
#
#If it is impossible for the graph to be fully traversed by both Alice and Bob,
#return -1.
#
#Example 1:
#Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
#Output: 2
#Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still
#be fully traversable by Alice and Bob. Removing any additional edge will not
#make it so. So the maximum number of edges we can remove is 2.
#
#Example 2:
#Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
#Output: 0
#Explanation: Notice that removing any edge will not make the graph fully
#traversable by Alice and Bob.
#
#Example 3:
#Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
#Output: -1
#Explanation: In the current graph, Alice cannot reach node 4 from the other
#nodes. Likewise, Bob cannot reach 1.
#
#Constraints:
#    1 <= n <= 10^5
#    1 <= edges.length <= min(10^5, 3 * n * (n - 1) / 2)
#    edges[i].length == 3
#    1 <= typei <= 3
#    1 <= ui < vi <= n
#    All tuples (typei, ui, vi) are distinct.

from typing import List

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """
        Union-Find with priority to type 3 edges (shared by both).

        Strategy:
        1. Process type 3 edges first (they help both)
        2. Process type 1 edges for Alice's graph
        3. Process type 2 edges for Bob's graph
        4. Count redundant edges
        """
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n + 1))
                self.rank = [0] * (n + 1)
                self.components = n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return False  # Already connected

                if self.rank[px] < self.rank[py]:
                    px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
                self.components -= 1
                return True

            def is_connected(self):
                return self.components == 1

        alice = UnionFind(n)
        bob = UnionFind(n)
        removed = 0

        # Process type 3 edges first
        for t, u, v in edges:
            if t == 3:
                alice_added = alice.union(u, v)
                bob.union(u, v)  # Same decision for both
                if not alice_added:
                    removed += 1

        # Process type 1 edges (Alice only)
        for t, u, v in edges:
            if t == 1:
                if not alice.union(u, v):
                    removed += 1

        # Process type 2 edges (Bob only)
        for t, u, v in edges:
            if t == 2:
                if not bob.union(u, v):
                    removed += 1

        # Check if both graphs are fully connected
        if alice.is_connected() and bob.is_connected():
            return removed
        return -1


class SolutionDetailed:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """
        Detailed explanation with step-by-step processing.
        """
        # Union-Find class
        class UF:
            def __init__(self, n):
                self.p = list(range(n + 1))
                self.count = n

            def find(self, x):
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

            def union(self, x, y):
                rx, ry = self.find(x), self.find(y)
                if rx == ry:
                    return 0  # Redundant edge
                self.p[rx] = ry
                self.count -= 1
                return 1  # Used edge

        # Separate edges by type
        type3 = [(u, v) for t, u, v in edges if t == 3]
        type1 = [(u, v) for t, u, v in edges if t == 1]
        type2 = [(u, v) for t, u, v in edges if t == 2]

        # Initialize Union-Find for Alice and Bob
        alice = UF(n)
        bob = UF(n)

        used = 0

        # Type 3 edges first (greedy: they help both)
        for u, v in type3:
            a_used = alice.union(u, v)
            bob.union(u, v)
            used += a_used

        # Type 1 edges for Alice
        for u, v in type1:
            used += alice.union(u, v)

        # Type 2 edges for Bob
        for u, v in type2:
            used += bob.union(u, v)

        # Check connectivity
        if alice.count != 1 or bob.count != 1:
            return -1

        return len(edges) - used
