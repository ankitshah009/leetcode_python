#56. Merge Intervals
#Medium
#
#Given an array of intervals where intervals[i] = [starti, endi], merge all
#overlapping intervals, and return an array of the non-overlapping intervals that
#cover all the intervals in the input.
#
#Example 1:
#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
#Example 2:
#Input: intervals = [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#Constraints:
#    1 <= intervals.length <= 10^4
#    intervals[i].length == 2
#    0 <= starti <= endi <= 10^4

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort by start time and merge overlapping intervals.
        """
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                # Overlapping - extend the end
                merged[-1][1] = max(merged[-1][1], end)
            else:
                # Non-overlapping - add new interval
                merged.append([start, end])

        return merged


class SolutionStack:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Using stack-like approach.
        """
        intervals.sort()
        stack = []

        for interval in intervals:
            if stack and stack[-1][1] >= interval[0]:
                stack[-1][1] = max(stack[-1][1], interval[1])
            else:
                stack.append(interval)

        return stack


class SolutionLineSweep:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Line sweep algorithm.
        """
        events = []

        for start, end in intervals:
            events.append((start, 0))  # 0 = start
            events.append((end, 1))    # 1 = end

        events.sort()

        result = []
        count = 0
        interval_start = 0

        for time, event_type in events:
            if event_type == 0:  # Start
                if count == 0:
                    interval_start = time
                count += 1
            else:  # End
                count -= 1
                if count == 0:
                    result.append([interval_start, time])

        return result


class SolutionGraph:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Graph-based approach - Union-Find.
        """
        from collections import defaultdict

        def overlaps(a, b):
            return a[0] <= b[1] and b[0] <= a[1]

        # Build graph
        graph = defaultdict(list)
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if overlaps(intervals[i], intervals[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        # Find connected components
        visited = [False] * len(intervals)
        result = []

        for i in range(len(intervals)):
            if not visited[i]:
                visited[i] = True
                component = [i]
                queue = [i]

                while queue:
                    node = queue.pop(0)
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            component.append(neighbor)
                            queue.append(neighbor)

                # Merge all intervals in component
                merged_start = min(intervals[j][0] for j in component)
                merged_end = max(intervals[j][1] for j in component)
                result.append([merged_start, merged_end])

        return result
