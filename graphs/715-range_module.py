#715. Range Module
#Hard
#
#A Range Module is a module that tracks ranges of numbers. Design a data
#structure to track the ranges represented as half-open intervals and query
#about them.
#
#A half-open interval [left, right) denotes all the real numbers x where
#left <= x < right.
#
#Implement the RangeModule class:
#- RangeModule() Initializes the object of the data structure.
#- void addRange(int left, int right) Adds the half-open interval [left, right),
#  tracking every real number in that interval.
#- boolean queryRange(int left, int right) Returns true if every real number
#  in the interval [left, right) is currently being tracked, and false otherwise.
#- void removeRange(int left, int right) Stops tracking every real number
#  currently being tracked in the half-open interval [left, right).
#
#Example 1:
#Input: ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange",
#        "queryRange"]
#       [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
#Output: [null, null, null, true, false, true]
#
#Constraints:
#    1 <= left < right <= 10^9
#    At most 10^4 calls will be made to addRange, queryRange, and removeRange.

from sortedcontainers import SortedDict

class RangeModule:
    """
    Use sorted dictionary to store disjoint intervals.
    Key = interval start, Value = interval end
    """

    def __init__(self):
        self.intervals = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        # Find overlapping intervals and merge
        starts = list(self.intervals.keys())

        # Find intervals that might overlap
        i = self.intervals.bisect_right(left)
        if i > 0:
            i -= 1

        # Merge overlapping intervals
        while i < len(starts):
            start = starts[i]
            end = self.intervals[start]

            if start > right:
                break

            if end >= left:
                left = min(left, start)
                right = max(right, end)
                del self.intervals[start]
                starts = list(self.intervals.keys())
            else:
                i += 1

        self.intervals[left] = right

    def queryRange(self, left: int, right: int) -> bool:
        # Find the interval that could contain [left, right)
        idx = self.intervals.bisect_right(left)
        if idx == 0:
            return False

        start = self.intervals.keys()[idx - 1]
        end = self.intervals[start]

        return start <= left and right <= end

    def removeRange(self, left: int, right: int) -> None:
        starts = list(self.intervals.keys())
        new_intervals = []

        for start in starts:
            end = self.intervals[start]

            if end <= left or start >= right:
                # No overlap
                new_intervals.append((start, end))
            else:
                # Has overlap - split if needed
                if start < left:
                    new_intervals.append((start, left))
                if end > right:
                    new_intervals.append((right, end))

                del self.intervals[start]

        for s, e in new_intervals:
            if s not in self.intervals:
                self.intervals[s] = e


class RangeModuleSimple:
    """Simpler list-based implementation"""

    def __init__(self):
        self.ranges = []  # List of [start, end] pairs

    def addRange(self, left: int, right: int) -> None:
        new_ranges = []
        placed = False

        for start, end in self.ranges:
            if end < left:
                new_ranges.append([start, end])
            elif start > right:
                if not placed:
                    new_ranges.append([left, right])
                    placed = True
                new_ranges.append([start, end])
            else:
                left = min(left, start)
                right = max(right, end)

        if not placed:
            new_ranges.append([left, right])

        self.ranges = new_ranges

    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.ranges:
            if start <= left and right <= end:
                return True
            if start > left:
                break
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_ranges = []

        for start, end in self.ranges:
            if end <= left or start >= right:
                new_ranges.append([start, end])
            else:
                if start < left:
                    new_ranges.append([start, left])
                if end > right:
                    new_ranges.append([right, end])

        self.ranges = new_ranges
