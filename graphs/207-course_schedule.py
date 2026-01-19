#207. Course Schedule
#Medium
#
#There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
#You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
#must take course bi first if you want to take course ai.
#
#Return true if you can finish all courses. Otherwise, return false.
#
#Example 1:
#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true
#Explanation: There are a total of 2 courses to take. To take course 1 you should have
#finished course 0. So it is possible.
#
#Example 2:
#Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
#Output: false
#Explanation: There are a total of 2 courses to take. To take course 1 you should have
#finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
#Constraints:
#    1 <= numCourses <= 2000
#    0 <= prerequisites.length <= 5000
#    prerequisites[i].length == 2
#    0 <= ai, bi < numCourses
#    All the pairs prerequisites[i] are unique.

from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Kahn's algorithm (BFS topological sort)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses
