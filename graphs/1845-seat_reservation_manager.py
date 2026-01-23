#1845. Seat Reservation Manager
#Medium
#
#Design a system that manages the reservation state of n seats that are
#numbered from 1 to n.
#
#Implement the SeatManager class:
#- SeatManager(int n) Initializes a SeatManager object that will manage n seats
#  numbered from 1 to n. All seats are initially available.
#- int reserve() Fetches the smallest-numbered unreserved seat, reserves it,
#  and returns its number.
#- void unreserve(int seatNumber) Unreserves the seat with the given
#  seatNumber.
#
#Example 1:
#Input: ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve",
#        "reserve", "reserve", "unreserve"]
#       [[5], [], [], [2], [], [], [], [], [5]]
#Output: [null, 1, 2, null, 2, 3, 4, 5, null]
#
#Constraints:
#    1 <= n <= 10^5
#    1 <= seatNumber <= n
#    For each call to reserve, it is guaranteed that there will be at least one
#    unreserved seat.
#    For each call to unreserve, it is guaranteed that seatNumber will be
#    reserved.
#    At most 10^5 calls in total will be made to reserve and unreserve.

import heapq

class SeatManager:
    """
    Min-heap based implementation.
    """

    def __init__(self, n: int):
        self.available = list(range(1, n + 1))
        heapq.heapify(self.available)

    def reserve(self) -> int:
        return heapq.heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)


class SeatManagerLazy:
    """
    Lazy initialization - only add seats to heap when unreserved.
    """

    def __init__(self, n: int):
        self.n = n
        self.next_seat = 1  # Next seat to reserve if heap empty
        self.available = []  # Min-heap of unreserved seats

    def reserve(self) -> int:
        if self.available:
            return heapq.heappop(self.available)
        seat = self.next_seat
        self.next_seat += 1
        return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)


class SeatManagerSortedSet:
    """
    Using sorted set for O(log n) operations.
    """
    from sortedcontainers import SortedSet

    def __init__(self, n: int):
        self.available = self.SortedSet(range(1, n + 1))

    def reserve(self) -> int:
        seat = self.available[0]
        self.available.remove(seat)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        self.available.add(seatNumber)
