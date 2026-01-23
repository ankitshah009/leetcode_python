#1557. Minimum Number of Vertices to Reach All Nodes
#Medium
#
#Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an
#array edges where edges[i] = [fromi, toi] represents a directed edge from node
#fromi to node toi.
#
#Find the smallest set of vertices from which all nodes in the graph are
#reachable. It's guaranteed that a unique solution exists.
#
#Notice that you can return the vertices in any order.
#
#Example 1:
#Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
#Output: [0,3]
#Explanation: From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5].
#Vertices 0 and 3 are the only vertices that cannot be reached from other vertices.
#
#Example 2:
#Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
#Output: [0,2,3]
#Explanation: Vertices 0, 2 and 3 are not reachable from any other vertex,
#so we must include them. Also, any of these vertices can reach vertices 1 and 4.
#
#Constraints:
#    2 <= n <= 10^5
#    1 <= edges.length <= min(10^5, n * (n - 1) / 2)
#    edges[i].length == 2
#    0 <= fromi, toi < n
#    All pairs (fromi, toi) are distinct.

from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Key insight: We need all nodes with no incoming edges (in-degree 0).

        Why? If a node has an incoming edge, we can reach it from somewhere else.
        If a node has no incoming edges, it can only be a starting point.
        """
        # Find all nodes that have incoming edges
        has_incoming = set()
        for _, to_node in edges:
            has_incoming.add(to_node)

        # Return all nodes without incoming edges
        return [i for i in range(n) if i not in has_incoming]


class SolutionInDegree:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Using in-degree array.
        """
        in_degree = [0] * n

        for _, to_node in edges:
            in_degree[to_node] += 1

        return [i for i in range(n) if in_degree[i] == 0]


class SolutionSet:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Set difference approach.
        """
        all_nodes = set(range(n))
        reachable = {to_node for _, to_node in edges}

        return list(all_nodes - reachable)


class SolutionExplained:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Detailed explanation.

        In a DAG, a node with in-degree 0 cannot be reached from any other node.
        Therefore, we MUST include it in our starting set.

        Conversely, any node with in-degree > 0 CAN be reached from some other
        node, so we don't need to start from it.

        The minimum set is exactly the set of nodes with in-degree 0.

        This is also the set of source nodes in the DAG.
        """
        # Collect all destination nodes
        destinations = set()
        for src, dst in edges:
            destinations.add(dst)

        # Nodes not in destinations have in-degree 0
        result = []
        for node in range(n):
            if node not in destinations:
                result.append(node)

        return result


class SolutionComprehension:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        One-liner using set comprehension.
        """
        return list(set(range(n)) - {to for _, to in edges})
