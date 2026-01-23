#1494. Parallel Courses II
#Hard
#
#You are given an integer n, which indicates that there are n courses labeled
#from 1 to n. You are also given an array relations where relations[i] = [prevCoursei,
#nextCoursei], representing a prerequisite relationship between course prevCoursei
#and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.
#Also, you are given the integer k.
#
#In one semester, you can take at most k courses as long as you have taken all
#the prerequisites in the previous semesters for the courses you are taking.
#
#Return the minimum number of semesters needed to take all courses. The testcases
#will be generated such that it is possible to take every course.
#
#Example 1:
#Input: n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
#Output: 3
#Explanation: The figure above represents the given graph.
#In the first semester, you can take courses 2 and 3.
#In the second semester, you can take course 1.
#In the third semester, you can take course 4.
#
#Example 2:
#Input: n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
#Output: 4
#Explanation: The figure above represents the given graph.
#In the first semester, you can take courses 2 and 3 only since you cannot take
#more than two per semester.
#In the second semester, you can take course 4.
#In the third semester, you can take course 1.
#In the fourth semester, you can take course 5.
#
#Constraints:
#    1 <= n <= 15
#    1 <= k <= n
#    0 <= relations.length <= n * (n-1) / 2
#    relations[i].length == 2
#    1 <= prevCoursei, nextCoursei <= n
#    prevCoursei != nextCoursei
#    All the pairs [prevCoursei, nextCoursei] are unique.
#    The given graph is a directed acyclic graph.

from typing import List
from functools import lru_cache

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        """
        Bitmask DP: state = which courses have been taken.
        For each state, find available courses and try all subsets of size <= k.
        """
        # prereq[i] = bitmask of prerequisites for course i
        prereq = [0] * n

        for prev, next_course in relations:
            # Convert to 0-indexed
            prereq[next_course - 1] |= (1 << (prev - 1))

        @lru_cache(maxsize=None)
        def dp(taken: int) -> int:
            """Minimum semesters to complete all courses given 'taken' courses done"""
            if taken == (1 << n) - 1:
                return 0

            # Find available courses (prerequisites satisfied and not taken)
            available = 0
            for i in range(n):
                if not (taken & (1 << i)):  # Not taken yet
                    if (taken & prereq[i]) == prereq[i]:  # All prereqs satisfied
                        available |= (1 << i)

            # Try all subsets of available courses with size <= k
            min_semesters = float('inf')

            # Enumerate all subsets of 'available'
            subset = available
            while subset > 0:
                if bin(subset).count('1') <= k:
                    min_semesters = min(min_semesters, 1 + dp(taken | subset))
                # Get next subset
                subset = (subset - 1) & available

            return min_semesters

        return dp(0)


class SolutionBFS:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        """
        BFS approach with bitmask states.
        """
        from collections import deque

        # Build prerequisites
        prereq = [0] * n
        for prev, next_course in relations:
            prereq[next_course - 1] |= (1 << (prev - 1))

        all_done = (1 << n) - 1

        # BFS
        queue = deque([0])  # Start with no courses taken
        visited = {0}
        semesters = 0

        while queue:
            semesters += 1
            for _ in range(len(queue)):
                taken = queue.popleft()

                # Find available courses
                available = 0
                for i in range(n):
                    if not (taken & (1 << i)) and (taken & prereq[i]) == prereq[i]:
                        available |= (1 << i)

                # Try all valid subsets
                subset = available
                while subset > 0:
                    if bin(subset).count('1') <= k:
                        new_state = taken | subset
                        if new_state == all_done:
                            return semesters
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append(new_state)
                    subset = (subset - 1) & available

        return semesters


class SolutionOptimized:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        """
        Optimized: enumerate subsets more efficiently.
        """
        prereq = [0] * n
        for prev, next_course in relations:
            prereq[next_course - 1] |= (1 << (prev - 1))

        # Precompute available courses for each state
        all_states = 1 << n
        available = [0] * all_states

        for mask in range(all_states):
            for i in range(n):
                if not (mask & (1 << i)) and (mask & prereq[i]) == prereq[i]:
                    available[mask] |= (1 << i)

        # DP
        INF = float('inf')
        dp = [INF] * all_states
        dp[0] = 0

        for mask in range(all_states):
            if dp[mask] == INF:
                continue

            avail = available[mask]

            # Enumerate subsets of size <= k
            subset = avail
            while subset > 0:
                if bin(subset).count('1') <= k:
                    dp[mask | subset] = min(dp[mask | subset], dp[mask] + 1)
                subset = (subset - 1) & avail

        return dp[all_states - 1]
