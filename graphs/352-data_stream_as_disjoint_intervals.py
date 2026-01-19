#352. Data Stream as Disjoint Intervals
#Hard
#
#Given a data stream input of non-negative integers a1, a2, ..., an, summarize
#the numbers seen so far as a list of disjoint intervals.
#
#Implement the SummaryRanges class:
#- SummaryRanges() Initializes the object with an empty stream.
#- void addNum(int value) Adds the integer value to the stream.
#- int[][] getIntervals() Returns a summary of the integers in the stream
#  currently as a list of disjoint intervals [starti, endi]. The answer should
#  be sorted by starti.
#
#Example 1:
#Input: ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
#        "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
#        "getIntervals"]
#       [[], [1], [], [3], [], [7], [], [2], [], [6], []]
#Output: [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null,
#         [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null,
#         [[1, 3], [6, 7]]]
#
#Constraints:
#    0 <= value <= 10^4
#    At most 3 * 10^4 calls will be made to addNum and getIntervals.
#    At most 10^2 calls will be made to getIntervals.

from typing import List
from sortedcontainers import SortedList

class SummaryRanges:
    """Using SortedList for efficient interval management"""

    def __init__(self):
        self.intervals = SortedList(key=lambda x: x[0])

    def addNum(self, value: int) -> None:
        # Find intervals that could merge with value
        left = right = None

        # Find interval that ends at value-1 (to extend right)
        # Find interval that starts at value+1 (to extend left)

        idx = self.intervals.bisect_left([value, value])

        # Check if value is already covered
        if idx > 0:
            prev = self.intervals[idx - 1]
            if prev[0] <= value <= prev[1]:
                return  # Already covered

        # Check previous interval
        if idx > 0 and self.intervals[idx - 1][1] >= value - 1:
            left = self.intervals[idx - 1]

        # Check next interval
        if idx < len(self.intervals) and self.intervals[idx][0] <= value + 1:
            right = self.intervals[idx]

        if left and right:
            # Merge both
            new_interval = [left[0], max(right[1], value)]
            self.intervals.remove(left)
            self.intervals.remove(right)
            self.intervals.add(new_interval)
        elif left:
            # Extend left
            self.intervals.remove(left)
            self.intervals.add([left[0], max(left[1], value)])
        elif right:
            # Extend right
            self.intervals.remove(right)
            self.intervals.add([min(right[0], value), right[1]])
        else:
            # New interval
            self.intervals.add([value, value])

    def getIntervals(self) -> List[List[int]]:
        return list(self.intervals)


class SummaryRangesSet:
    """Using set for seen numbers, build intervals on demand"""

    def __init__(self):
        self.seen = set()

    def addNum(self, value: int) -> None:
        self.seen.add(value)

    def getIntervals(self) -> List[List[int]]:
        if not self.seen:
            return []

        nums = sorted(self.seen)
        intervals = []
        start = end = nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                intervals.append([start, end])
                start = end = num

        intervals.append([start, end])
        return intervals


class SummaryRangesUnionFind:
    """Using Union-Find for interval merging"""

    def __init__(self):
        self.parent = {}
        self.start = {}  # start[root] = start of interval
        self.end = {}    # end[root] = end of interval

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def addNum(self, value: int) -> None:
        if value in self.parent:
            return

        self.parent[value] = value
        self.start[value] = value
        self.end[value] = value

        # Try to merge with left neighbor
        if value - 1 in self.parent:
            root_left = self.find(value - 1)
            root_curr = self.find(value)
            self.parent[root_curr] = root_left
            self.end[root_left] = self.end[root_curr]

        # Try to merge with right neighbor
        if value + 1 in self.parent:
            root_curr = self.find(value)
            root_right = self.find(value + 1)
            if root_curr != root_right:
                self.parent[root_right] = root_curr
                self.end[root_curr] = self.end[root_right]

    def getIntervals(self) -> List[List[int]]:
        roots = set()
        for val in self.parent:
            roots.add(self.find(val))

        intervals = []
        for root in roots:
            intervals.append([self.start[root], self.end[root]])

        intervals.sort()
        return intervals
