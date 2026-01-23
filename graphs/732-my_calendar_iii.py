#732. My Calendar III
#Hard
#
#A k-booking happens when k events have some non-empty intersection.
#
#You are given some events [start, end), after each given event, return an
#integer k representing the maximum k-booking between all the previous events.
#
#Implement the MyCalendarThree class:
#- MyCalendarThree() Initializes the object.
#- int book(int start, int end) Returns an integer k representing the largest
#  integer such that there exists a k-booking in the calendar.
#
#Example 1:
#Input: ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
#       [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
#Output: [null, 1, 1, 2, 3, 3, 3]
#
#Constraints:
#    0 <= start < end <= 10^9
#    At most 400 calls will be made to book.

from sortedcontainers import SortedDict

class MyCalendarThree:
    """
    Sweep line: track +1 at start, -1 at end.
    """

    def __init__(self):
        self.delta = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.delta[start] = self.delta.get(start, 0) + 1
        self.delta[end] = self.delta.get(end, 0) - 1

        max_k = 0
        current = 0

        for time in self.delta:
            current += self.delta[time]
            max_k = max(max_k, current)

        return max_k


class MyCalendarThreeDict:
    """Using regular dictionary with sorting"""

    def __init__(self):
        self.events = {}

    def book(self, start: int, end: int) -> int:
        self.events[start] = self.events.get(start, 0) + 1
        self.events[end] = self.events.get(end, 0) - 1

        max_booking = 0
        current = 0

        for time in sorted(self.events.keys()):
            current += self.events[time]
            max_booking = max(max_booking, current)

        return max_booking


class MyCalendarThreeSegmentTree:
    """Segment tree with lazy propagation"""

    def __init__(self):
        self.tree = {}
        self.lazy = {}

    def update(self, node, start, end, l, r):
        if r < start or end < l:
            return

        if l <= start and end <= r:
            self.tree[node] = self.tree.get(node, 0) + 1
            self.lazy[node] = self.lazy.get(node, 0) + 1
            return

        mid = (start + end) // 2
        self.update(2 * node, start, mid, l, r)
        self.update(2 * node + 1, mid + 1, end, l, r)

        self.tree[node] = self.lazy.get(node, 0) + max(
            self.tree.get(2 * node, 0),
            self.tree.get(2 * node + 1, 0)
        )

    def book(self, start: int, end: int) -> int:
        self.update(1, 0, 10**9, start, end - 1)
        return self.tree.get(1, 0)
