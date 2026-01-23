#1627. Graph Connectivity With Threshold
#Hard
#
#We have n cities labeled from 1 to n. Two different cities a and b are directly
#connected by a bidirectional road if there exists an integer c where c > threshold
#and both a and b are divisible by c.
#
#You are given two integers, n and threshold, and an array of queries, where
#queries[i] = [ai, bi]. For each query, you need to determine if cities ai and bi
#are connected directly or indirectly.
#
#Return an array answer, where answer.length == queries.length and answer[i] is
#true if for the ith query, there is a path between ai and bi, or answer[i] is
#false if there is no path.
#
#Example 1:
#Input: n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]
#Output: [false,false,true]
#Explanation: For c = 3, 3 and 6 are divisible by 3.
#
#Example 2:
#Input: n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]
#Output: [true,true,true,true,true]
#Explanation: With threshold 0, all divisors > 0 create edges.
#
#Example 3:
#Input: n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]
#Output: [false,false,false,false,false]
#Explanation: Only threshold > 1 divisors count. No common divisor > 1 exists.
#
#Constraints:
#    2 <= n <= 10^4
#    0 <= threshold <= n
#    1 <= queries.length <= 10^5
#    queries[i].length == 2
#    1 <= ai, bi <= n
#    ai != bi

from typing import List

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        """
        Use Union-Find. Connect all multiples of each c > threshold.

        For each c from threshold+1 to n:
        - Connect c with 2c, 3c, ..., up to n
        - All multiples of c form a connected component
        """
        # Union-Find
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

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

        # Build graph: connect all multiples
        for c in range(threshold + 1, n + 1):
            for multiple in range(2 * c, n + 1, c):
                union(c, multiple)

        # Answer queries
        return [find(a) == find(b) for a, b in queries]


class SolutionOptimized:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        """
        Same approach with slight optimizations.
        """
        # Quick path: if threshold >= n, no edges exist
        if threshold >= n:
            return [False] * len(queries)

        # Union-Find with path compression
        parent = list(range(n + 1))

        def find(x):
            root = x
            while parent[root] != root:
                root = parent[root]
            # Path compression
            while parent[x] != root:
                parent[x], x = root, parent[x]
            return root

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # Connect multiples
        for divisor in range(threshold + 1, n + 1):
            # Connect all multiples of this divisor
            multiple = 2 * divisor
            while multiple <= n:
                union(divisor, multiple)
                multiple += divisor

        return [find(a) == find(b) for a, b in queries]


class SolutionDetailed:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        """
        Detailed solution with Union-Find class.
        """
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [0] * size

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return False
                if self.rank[px] < self.rank[py]:
                    px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
                return True

            def connected(self, x, y):
                return self.find(x) == self.find(y)

        uf = UnionFind(n + 1)

        # For each possible common divisor > threshold
        for c in range(threshold + 1, n + 1):
            # Connect all multiples of c
            for mult in range(c, n + 1, c):
                if mult != c:
                    uf.union(c, mult)

        return [uf.connected(a, b) for a, b in queries]
