#802. Find Eventual Safe States
#Medium
#
#There is a directed graph of n nodes with each node labeled from 0 to n - 1.
#The graph is represented by a 0-indexed 2D integer array graph where graph[i]
#is an integer array of nodes adjacent to node i.
#
#A node is a terminal node if there are no outgoing edges. A node is a safe node
#if every possible path starting from that node leads to a terminal node.
#
#Return an array containing all the safe nodes of the graph. The answer should
#be sorted in ascending order.
#
#Example 1:
#Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
#Output: [2,4,5,6]
#
#Example 2:
#Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
#Output: [4]
#
#Constraints:
#    n == graph.length
#    1 <= n <= 10^4
#    0 <= graph[i].length <= n
#    0 <= graph[i][j] <= n - 1
#    graph[i] is sorted in strictly increasing order.
#    The graph may contain self-loops.
#    The number of edges in the graph will be at most 4 * 10^4.

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        """
        DFS with coloring: 0=unvisited, 1=visiting, 2=safe
        A node is unsafe if it's part of a cycle.
        """
        n = len(graph)
        color = [0] * n  # 0: unvisited, 1: visiting, 2: safe

        def is_safe(node):
            if color[node] > 0:
                return color[node] == 2

            color[node] = 1  # Mark as visiting

            for neighbor in graph[node]:
                if not is_safe(neighbor):
                    return False

            color[node] = 2  # Mark as safe
            return True

        return [i for i in range(n) if is_safe(i)]


class SolutionTopological:
    """Reverse graph + topological sort (Kahn's)"""

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        from collections import deque

        n = len(graph)
        # Build reverse graph
        reverse_graph = [[] for _ in range(n)]
        out_degree = [0] * n

        for u in range(n):
            out_degree[u] = len(graph[u])
            for v in graph[u]:
                reverse_graph[v].append(u)

        # Start with terminal nodes (out_degree = 0)
        queue = deque([i for i in range(n) if out_degree[i] == 0])
        safe = set()

        while queue:
            node = queue.popleft()
            safe.add(node)

            for neighbor in reverse_graph[node]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(safe)


class SolutionIterative:
    """Iterative DFS"""

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        state = [0] * n  # 0: unvisited, 1: visiting, 2: safe, 3: unsafe

        def dfs(start):
            stack = [(start, iter(graph[start]))]
            state[start] = 1

            while stack:
                node, it = stack[-1]
                try:
                    neighbor = next(it)
                    if state[neighbor] == 1 or state[neighbor] == 3:
                        # Cycle or leads to cycle
                        while stack:
                            n, _ = stack.pop()
                            state[n] = 3
                        return
                    elif state[neighbor] == 0:
                        state[neighbor] = 1
                        stack.append((neighbor, iter(graph[neighbor])))
                except StopIteration:
                    state[node] = 2
                    stack.pop()

        for i in range(n):
            if state[i] == 0:
                dfs(i)

        return [i for i in range(n) if state[i] == 2]
