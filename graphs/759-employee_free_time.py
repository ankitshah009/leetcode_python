#759. Employee Free Time
#Hard
#
#We are given a list schedule of employees, which represents the working time
#for each employee.
#
#Each employee has a list of non-overlapping Intervals, and these intervals are
#in sorted order.
#
#Return the list of finite intervals representing common, positive-length free
#time for all employees, also in sorted order.
#
#Example 1:
#Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
#Output: [[3,4]]
#Explanation: There are a total of three employees, and all common free time
#intervals would be [-inf, 1], [3, 4], [10, inf]. We discard any intervals that
#contain inf as they aren't finite.
#
#Example 2:
#Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
#Output: [[5,6],[7,9]]
#
#Constraints:
#    1 <= schedule.length, schedule[i].length <= 50
#    0 <= schedule[i][j].start < schedule[i][j].end <= 10^8

# Definition for an Interval.
# class Interval:
#     def __init__(self, start: int = None, end: int = None):
#         self.start = start
#         self.end = end

class Solution:
    def employeeFreeTime(self, schedule):
        """
        Merge all intervals, find gaps between merged intervals.
        """
        # Collect all intervals
        all_intervals = []
        for employee in schedule:
            for interval in employee:
                all_intervals.append((interval.start, interval.end))

        # Sort by start time
        all_intervals.sort()

        # Merge intervals
        merged = [all_intervals[0]]
        for start, end in all_intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))

        # Find gaps
        result = []
        for i in range(1, len(merged)):
            if merged[i][0] > merged[i - 1][1]:
                result.append(Interval(merged[i - 1][1], merged[i][0]))

        return result


class SolutionHeap:
    """Using min-heap for merging"""

    def employeeFreeTime(self, schedule):
        import heapq

        # Min-heap: (interval_start, interval_end)
        heap = []
        for employee in schedule:
            for interval in employee:
                heapq.heappush(heap, (interval.start, interval.end))

        result = []
        prev_end = heapq.heappop(heap)[1]

        while heap:
            start, end = heapq.heappop(heap)

            if start > prev_end:
                result.append(Interval(prev_end, start))
                prev_end = end
            else:
                prev_end = max(prev_end, end)

        return result


class SolutionSweepLine:
    """Sweep line algorithm"""

    def employeeFreeTime(self, schedule):
        events = []

        for employee in schedule:
            for interval in employee:
                events.append((interval.start, 0))  # Start event
                events.append((interval.end, 1))    # End event

        events.sort()

        result = []
        active = 0
        prev_end = None

        for time, event_type in events:
            if active == 0 and prev_end is not None and time > prev_end:
                result.append(Interval(prev_end, time))

            if event_type == 0:
                active += 1
            else:
                active -= 1
                prev_end = time

        return result
