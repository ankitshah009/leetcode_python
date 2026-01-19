#352. Data Stream as Disjoint Intervals
#Hard
#
#Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers
#seen so far as a list of disjoint intervals.
#
#Implement the SummaryRanges class:
#    SummaryRanges() Initializes the object with an empty stream.
#    void addNum(int value) Adds the integer value to the stream.
#    int[][] getIntervals() Returns a summary of the integers in the stream currently as a
#        list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
#
#Example 1:
#Input: ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
#        "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
#       [[], [1], [], [3], [], [7], [], [2], [], [6], []]
#Output: [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]],
#         null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
#
#Constraints:
#    0 <= value <= 10^4
#    At most 3 * 10^4 calls will be made to addNum and getIntervals.

from sortedcontainers import SortedList

class SummaryRanges:
    def __init__(self):
        self.intervals = SortedList()

    def addNum(self, value: int) -> None:
        # Find position to insert
        left, right = value, value

        # Find intervals that can be merged
        to_remove = []
        for interval in self.intervals:
            if interval[0] <= value <= interval[1]:
                return  # Already covered
            if interval[1] + 1 == value:
                left = interval[0]
                to_remove.append(interval)
            elif interval[0] - 1 == value:
                right = interval[1]
                to_remove.append(interval)

        for interval in to_remove:
            self.intervals.remove(interval)

        self.intervals.add((left, right))

    def getIntervals(self) -> List[List[int]]:
        return [list(interval) for interval in self.intervals]
