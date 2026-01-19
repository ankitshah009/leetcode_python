#210. Course Schedule II
#Medium
#
#There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
#You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
#must take course bi first if you want to take course ai.
#
#Return the ordering of courses you should take to finish all courses. If there are many
#valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
#
#Example 1:
#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: [0,1]
#
#Example 2:
#Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
#Output: [0,2,1,3]
#
#Example 3:
#Input: numCourses = 1, prerequisites = []
#Output: [0]
#
#Constraints:
#    1 <= numCourses <= 2000
#    0 <= prerequisites.length <= numCourses * (numCourses - 1)
#    prerequisites[i].length == 2
#    0 <= ai, bi < numCourses
#    ai != bi
#    All the pairs [ai, bi] are distinct.

from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return order if len(order) == numCourses else []
