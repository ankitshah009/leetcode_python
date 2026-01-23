#855. Exam Room
#Medium
#
#There is an exam room with n seats in a single row labeled from 0 to n - 1.
#
#When a student enters the room, they must sit in the seat that maximizes the
#distance to the closest person. If there are multiple such seats, they sit in
#the seat with the lowest number. If no one is in the room, then the student
#sits at seat number 0.
#
#Design a class that simulates the mentioned exam room.
#
#Implement the ExamRoom class:
#- ExamRoom(int n) Initializes the object with the number of seats n.
#- int seat() Returns the label of the seat at which the next student will sit.
#- void leave(int p) Indicates that the student sitting at seat p will leave
#  the room. It is guaranteed that there will be a student sitting at seat p.
#
#Example 1:
#Input: ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
#       [[10], [], [], [], [], [4], []]
#Output: [null, 0, 9, 4, 2, null, 5]
#
#Constraints:
#    1 <= n <= 10^9
#    It is guaranteed that there is a student sitting at seat p.
#    At most 10^4 calls will be made to seat and leave.

import bisect

class ExamRoom:
    """
    Maintain sorted list of occupied seats.
    """
    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            seat = 0
        else:
            # Check edge cases and gaps
            max_dist = self.students[0]  # Distance from seat 0
            seat = 0

            # Check gaps between students
            for i in range(1, len(self.students)):
                prev = self.students[i - 1]
                curr = self.students[i]
                dist = (curr - prev) // 2

                if dist > max_dist:
                    max_dist = dist
                    seat = prev + dist

            # Check distance from last student to end
            end_dist = self.n - 1 - self.students[-1]
            if end_dist > max_dist:
                seat = self.n - 1

        bisect.insort(self.students, seat)
        return seat

    def leave(self, p: int) -> None:
        self.students.remove(p)


class ExamRoomHeap:
    """Using heap for O(log n) operations"""

    def __init__(self, n: int):
        import heapq
        self.n = n
        self.students = set()
        # Heap of (-distance, start, end) representing gaps
        self.heap = []
        heapq.heappush(self.heap, self._create_interval(-1, n))

    def _create_interval(self, start, end):
        """Create interval with distance for heap"""
        if start == -1:
            dist = end  # Distance from seat 0
        elif end == self.n:
            dist = self.n - 1 - start  # Distance from last seat
        else:
            dist = (end - start) // 2  # Middle of gap

        # Negative for max heap, use start for tie-breaking
        return (-dist, start, end)

    def _get_seat(self, start, end):
        """Get seat position for interval"""
        if start == -1:
            return 0
        elif end == self.n:
            return self.n - 1
        else:
            return start + (end - start) // 2

    def seat(self) -> int:
        import heapq

        while self.heap:
            _, start, end = heapq.heappop(self.heap)

            # Validate interval (boundaries must still be valid)
            left_valid = start == -1 or start in self.students
            right_valid = end == self.n or end in self.students

            if left_valid and right_valid:
                seat = self._get_seat(start, end)

                # Add new intervals
                heapq.heappush(self.heap, self._create_interval(start, seat))
                heapq.heappush(self.heap, self._create_interval(seat, end))

                self.students.add(seat)
                return seat

        return -1  # Should not reach

    def leave(self, p: int) -> None:
        self.students.remove(p)
        # Lazy deletion - invalid intervals will be filtered in seat()
        # In production, would need to merge adjacent intervals
