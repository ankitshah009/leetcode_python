#729. My Calendar I
#Medium
#
#You are implementing a program to use as your calendar. We can add a new event
#if adding the event will not cause a double booking.
#
#A double booking happens when two events have some non-empty intersection
#(i.e., some moment is common to both events).
#
#The event can be represented as a pair of integers start and end that represents
#a booking on the half-open interval [start, end), the range of real numbers x
#such that start <= x < end.
#
#Implement the MyCalendar class:
#- MyCalendar() Initializes the calendar object.
#- boolean book(int start, int end) Returns true if the event can be added to
#  the calendar successfully without causing a double booking. Otherwise, return
#  false and do not add the event to the calendar.
#
#Example 1:
#Input: ["MyCalendar", "book", "book", "book"]
#       [[], [10, 20], [15, 25], [20, 30]]
#Output: [null, true, false, true]
#Explanation:
#MyCalendar myCalendar = new MyCalendar();
#myCalendar.book(10, 20); // return True
#myCalendar.book(15, 25); // return False, overlaps with [10, 20)
#myCalendar.book(20, 30); // return True, [10, 20) and [20, 30) do not overlap
#
#Constraints:
#    0 <= start < end <= 10^9
#    At most 1000 calls will be made to book.

from sortedcontainers import SortedList

class MyCalendar:
    """
    Use sorted list to maintain events and binary search for overlaps.
    """

    def __init__(self):
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        # Find where this event would be inserted
        idx = self.events.bisect_left((start, end))

        # Check overlap with previous event
        if idx > 0:
            prev_start, prev_end = self.events[idx - 1]
            if prev_end > start:
                return False

        # Check overlap with next event
        if idx < len(self.events):
            next_start, next_end = self.events[idx]
            if end > next_start:
                return False

        self.events.add((start, end))
        return True


class MyCalendarSimple:
    """Simple list-based approach"""

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if start < e and end > s:  # Overlap condition
                return False

        self.bookings.append((start, end))
        return True


class MyCalendarBST:
    """BST-based approach"""

    class TreeNode:
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = self.TreeNode(start, end)
            return True

        return self._insert(self.root, start, end)

    def _insert(self, node, start, end):
        if end <= node.start:
            if node.left:
                return self._insert(node.left, start, end)
            else:
                node.left = self.TreeNode(start, end)
                return True
        elif start >= node.end:
            if node.right:
                return self._insert(node.right, start, end)
            else:
                node.right = self.TreeNode(start, end)
                return True
        else:
            return False  # Overlap
