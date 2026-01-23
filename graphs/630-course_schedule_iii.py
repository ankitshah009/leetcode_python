#630. Course Schedule III
#Hard
#
#There are n different online courses numbered from 1 to n. You are given an array
#courses where courses[i] = [durationi, lastDayi] indicate that the ith course
#should be taken continuously for durationi days and must be finished before or
#on lastDayi.
#
#You will start on the 1st day and you cannot take two or more courses simultaneously.
#
#Return the maximum number of courses that you can take.
#
#Example 1:
#Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
#Output: 3
#Explanation: There are totally 4 courses, but you can take 3 courses at most:
#- First, take the 1st course, it costs 100 days so you will finish it on day 100.
#- Next, take the 3rd course, it costs 1000 days so you will finish it on day 1100.
#- Finally, take the 2nd course, it costs 200 days so you will finish it on day 1300.
#
#Example 2:
#Input: courses = [[1,2]]
#Output: 1
#
#Example 3:
#Input: courses = [[3,2],[4,3]]
#Output: 0
#
#Constraints:
#    1 <= courses.length <= 10^4
#    1 <= durationi, lastDayi <= 10^4

from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        Greedy with max heap.
        Sort by deadline, greedily take courses.
        If can't take a course, swap with longest course taken.
        """
        # Sort by deadline
        courses.sort(key=lambda x: x[1])

        max_heap = []  # Max heap of durations (negative for max)
        current_time = 0

        for duration, deadline in courses:
            if current_time + duration <= deadline:
                # Can take this course
                current_time += duration
                heapq.heappush(max_heap, -duration)
            elif max_heap and -max_heap[0] > duration:
                # Swap with longest course
                longest = -heapq.heappop(max_heap)
                current_time -= longest - duration
                heapq.heappush(max_heap, -duration)

        return len(max_heap)


class SolutionDP:
    """DP approach - less efficient but educational"""

    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(idx, time):
            if idx == len(courses):
                return 0

            duration, deadline = courses[idx]

            # Skip this course
            result = dp(idx + 1, time)

            # Take this course if possible
            if time + duration <= deadline:
                result = max(result, 1 + dp(idx + 1, time + duration))

            return result

        return dp(0, 0)
