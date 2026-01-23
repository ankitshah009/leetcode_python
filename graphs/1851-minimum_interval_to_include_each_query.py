#1851. Minimum Interval to Include Each Query
#Hard
#
#You are given a 2D integer array intervals, where intervals[i] = [left_i,
#right_i] describes the ith interval starting at left_i and ending at right_i
#(inclusive). The size of an interval is defined as the number of integers it
#contains, or more formally right_i - left_i + 1.
#
#You are also given an integer array queries. The answer to the jth query is
#the size of the smallest interval i such that left_i <= queries[j] <= right_i.
#If no such interval exists, the answer is -1.
#
#Return an array containing the answers to the queries.
#
#Example 1:
#Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
#Output: [3,3,1,4]
#
#Example 2:
#Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
#Output: [2,-1,4,6]
#
#Constraints:
#    1 <= intervals.length <= 10^5
#    1 <= queries.length <= 10^5
#    intervals[i].length == 2
#    1 <= left_i <= right_i <= 10^7
#    1 <= queries[j] <= 10^7

from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        Offline processing with sorted queries and min-heap.
        """
        # Sort intervals by start
        intervals.sort()

        # Sort queries with original indices
        indexed_queries = sorted(enumerate(queries), key=lambda x: x[1])

        result = [-1] * len(queries)
        heap = []  # (size, end)
        i = 0

        for query_idx, q in indexed_queries:
            # Add all intervals that start <= q
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                size = right - left + 1
                heapq.heappush(heap, (size, right))
                i += 1

            # Remove intervals that end < q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                result[query_idx] = heap[0][0]

        return result


class SolutionDict:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        Using dictionary to map queries to results.
        """
        intervals.sort(key=lambda x: x[1] - x[0])  # Sort by size
        sorted_queries = sorted(set(queries))

        # Union-Find style: for each query, find smallest interval containing it
        result_map = {}
        # For each query, store result as we process smallest to largest intervals

        for left, right in intervals:
            for q in sorted_queries:
                if q in result_map:
                    continue
                if left <= q <= right:
                    result_map[q] = right - left + 1

        return [result_map.get(q, -1) for q in queries]


class SolutionSweepLine:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        Sweep line with sorted container.
        """
        from sortedcontainers import SortedList

        # Create events
        events = []
        for i, (left, right) in enumerate(intervals):
            size = right - left + 1
            events.append((left, 0, size, right))   # Start: add interval
            events.append((right + 1, 1, size, right))  # End: remove interval

        for i, q in enumerate(queries):
            events.append((q, 2, i))  # Query

        events.sort()

        result = [-1] * len(queries)
        active = SortedList()  # (size, end)

        for event in events:
            if event[1] == 0:  # Start
                _, _, size, end = event
                active.add((size, end))
            elif event[1] == 1:  # End
                _, _, size, end = event
                active.discard((size, end))
            else:  # Query
                _, _, query_idx = event
                if active:
                    result[query_idx] = active[0][0]

        return result
