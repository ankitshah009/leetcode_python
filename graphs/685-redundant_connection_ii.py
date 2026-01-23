#685. Redundant Connection II
#Hard
#
#In this problem, a rooted tree is a directed graph such that, there is exactly
#one node (the root) for which all other nodes are descendants of this node,
#plus every node has exactly one parent, except for the root node which has no
#parents.
#
#The given input is a directed graph that started as a rooted tree with n nodes
#(with distinct values from 1 to n), with one additional directed edge added.
#The added edge has two different vertices chosen from 1 to n, and was not an
#edge that already existed.
#
#The resulting graph is given as a 2D-array of edges. Each element of edges is
#a pair [ui, vi] that represents a directed edge connecting nodes ui and vi,
#where ui is a parent of child vi.
#
#Return an edge that can be removed so that the resulting graph is a rooted tree
#of n nodes. If there are multiple answers, return the answer that occurs last
#in the input.
#
#Example 1:
#Input: edges = [[1,2],[1,3],[2,3]]
#Output: [2,3]
#
#Example 2:
#Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
#Output: [4,1]
#
#Constraints:
#    n == edges.length
#    3 <= n <= 1000
#    edges[i].length == 2
#    1 <= ui, vi <= n
#    ui != vi

class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        """
        Three cases:
        1. No node has two parents, just find cycle (like undirected case)
        2. One node has two parents, no cycle -> remove second edge to that node
        3. One node has two parents, has cycle -> remove edge in cycle
        """
        n = len(edges)
        parent = [0] * (n + 1)

        # Find if any node has two parents
        candidate1 = candidate2 = None
        for u, v in edges:
            if parent[v] != 0:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
            else:
                parent[v] = u

        # Union-Find
        root = list(range(n + 1))

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        for u, v in edges:
            if [u, v] == candidate2:
                continue  # Skip candidate2 temporarily

            pu, pv = find(u), find(v)
            if pu == pv:
                # Found cycle
                if candidate1 is None:
                    return [u, v]  # Case 1: no two parents
                return candidate1  # Case 3: cycle involves candidate1
            root[pv] = pu

        return candidate2  # Case 2: no cycle when removing candidate2


class SolutionDetailed:
    """More explicit handling of all cases"""

    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)

        # Find node with two parents
        parents = {}
        edge_to_node_with_two_parents = []

        for i, (u, v) in enumerate(edges):
            if v in parents:
                edge_to_node_with_two_parents = [parents[v], i]
            else:
                parents[v] = i

        # Union-Find
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[py] = px
            return True

        if not edge_to_node_with_two_parents:
            # Case 1: No node with two parents, find cycle edge
            for u, v in edges:
                if not union(u, v):
                    return [u, v]
        else:
            # Case 2 or 3: Node has two parents
            first_idx, second_idx = edge_to_node_with_two_parents

            # Try removing second edge
            for i, (u, v) in enumerate(edges):
                if i == second_idx:
                    continue
                if not union(u, v):
                    # Cycle found, first edge is the problem
                    return edges[first_idx]

            # No cycle when removing second edge
            return edges[second_idx]

        return []
