#1462. Course Schedule IV
#Medium
#
#There are a total of numCourses courses you have to take, labeled from 0 to
#numCourses - 1. You are given an array prerequisites where prerequisites[i] =
#[ai, bi] indicates that you must take course ai first if you want to take
#course bi.
#
#For example, the pair [0, 1] indicates that you have to take course 0 before
#you can take course 1.
#
#Prerequisites can also be indirect. If course a is a prerequisite of course b,
#and course b is a prerequisite of course c, then course a is a prerequisite of
#course c.
#
#You are also given an array queries where queries[j] = [uj, vj]. For the jth
#query, you should answer whether course uj is a prerequisite of course vj or not.
#
#Return a boolean array answer, where answer[j] is the answer to the jth query.
#
#Example 1:
#Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
#Output: [false,true]
#Explanation: The pair [1, 0] indicates that you have to take course 1 before
#you can take course 0. Course 0 is not a prerequisite of course 1, but the
#opposite is true.
#
#Example 2:
#Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
#Output: [false,false]
#Explanation: There are no prerequisites, and each course is independent.
#
#Example 3:
#Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
#Output: [true,true]
#
#Constraints:
#    2 <= numCourses <= 100
#    0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
#    prerequisites[i].length == 2
#    0 <= ai, bi <= n - 1
#    ai != bi
#    All the pairs [ai, bi] are unique.
#    The prerequisites graph has no cycles.
#    1 <= queries.length <= 10^4
#    0 <= uj, vj <= n - 1
#    uj != vj

from typing import List
from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        Floyd-Warshall approach: compute transitive closure.
        reachable[i][j] = True if there's a path from i to j.
        """
        # Initialize reachability matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]

        # Direct prerequisites
        for pre, course in prerequisites:
            reachable[pre][course] = True

        # Floyd-Warshall for transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])

        return [reachable[u][v] for u, v in queries]


class SolutionBFS:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        BFS from each node to find all reachable nodes.
        """
        graph = defaultdict(list)
        for pre, course in prerequisites:
            graph[pre].append(course)

        # For each node, find all nodes reachable from it
        reachable = [set() for _ in range(numCourses)]

        for start in range(numCourses):
            visited = set()
            queue = deque([start])

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        reachable[start].add(neighbor)
                        queue.append(neighbor)

        return [v in reachable[u] for u, v in queries]


class SolutionDFS:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        DFS with memoization to find all prerequisites.
        """
        graph = defaultdict(list)
        for pre, course in prerequisites:
            graph[pre].append(course)

        # prereqs[i] = set of all prerequisites of course i
        prereqs = [set() for _ in range(numCourses)]

        def dfs(node: int, visited: set) -> set:
            if prereqs[node]:
                return prereqs[node]

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    prereqs[node].add(neighbor)
                    prereqs[node] |= dfs(neighbor, visited)

            return prereqs[node]

        for i in range(numCourses):
            dfs(i, set())

        return [v in prereqs[u] for u, v in queries]


class SolutionTopological:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        Topological sort approach.
        Process nodes in topological order and propagate reachability.
        """
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for pre, course in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # prereqs[i] = set of all prerequisites (nodes that can reach i)
        prereqs = [set() for _ in range(numCourses)]

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                # node is a prerequisite of neighbor
                prereqs[neighbor].add(node)
                # All prerequisites of node are also prerequisites of neighbor
                prereqs[neighbor] |= prereqs[node]

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return [u in prereqs[v] for u, v in queries]
