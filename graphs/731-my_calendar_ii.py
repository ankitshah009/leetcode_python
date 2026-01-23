#731. My Calendar II
#Medium
#
#You are implementing a program to use as your calendar. We can add a new event
#if adding the event will not cause a triple booking.
#
#A triple booking happens when three events have some non-empty intersection.
#
#Implement the MyCalendarTwo class:
#- MyCalendarTwo() Initializes the calendar object.
#- boolean book(int start, int end) Returns true if the event can be added
#  successfully without causing a triple booking. Otherwise, return false and
#  do not add the event.
#
#Example 1:
#Input: ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
#       [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
#Output: [null, true, true, true, false, true, true]
#
#Constraints:
#    0 <= start < end <= 10^9
#    At most 1000 calls will be made to book.

class MyCalendarTwo:
    """
    Track single bookings and double bookings separately.
    """

    def __init__(self):
        self.single = []  # Single bookings
        self.double = []  # Double bookings (overlaps)

    def book(self, start: int, end: int) -> bool:
        # Check if this would create a triple booking
        for s, e in self.double:
            if start < e and end > s:
                return False

        # Add overlaps with existing single bookings to double
        for s, e in self.single:
            if start < e and end > s:
                self.double.append((max(start, s), min(end, e)))

        self.single.append((start, end))
        return True


class MyCalendarTwoSweepLine:
    """Sweep line approach with event points"""

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        self.events.append((start, 1))   # Event start
        self.events.append((end, -1))    # Event end

        self.events.sort()

        count = 0
        for _, delta in self.events:
            count += delta
            if count >= 3:
                # Remove the event we just added
                self.events.remove((start, 1))
                self.events.remove((end, -1))
                return False

        return True


class MyCalendarTwoOptimized:
    """Optimized with sorted dictionary"""

    def __init__(self):
        from sortedcontainers import SortedDict
        self.delta = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.delta[start] = self.delta.get(start, 0) + 1
        self.delta[end] = self.delta.get(end, 0) - 1

        count = 0
        for time in self.delta:
            count += self.delta[time]
            if count >= 3:
                # Rollback
                self.delta[start] -= 1
                self.delta[end] += 1
                if self.delta[start] == 0:
                    del self.delta[start]
                if self.delta[end] == 0:
                    del self.delta[end]
                return False

        return True
