#933. Number of Recent Calls
#Easy
#
#You have a RecentCounter class which counts the number of recent requests
#within a certain time frame.
#
#Implement the RecentCounter class:
#- RecentCounter() Initializes the counter with zero recent requests.
#- int ping(int t) Adds a new request at time t (ms), and returns the number
#  of requests in the past 3000 milliseconds (including the new request).
#
#It is guaranteed that every call to ping uses a strictly larger value of t.
#
#Example 1:
#Input: ["RecentCounter","ping","ping","ping","ping"]
#       [[],[1],[100],[3001],[3002]]
#Output: [null,1,2,3,3]
#
#Constraints:
#    1 <= t <= 10^9
#    Each test case will call ping with strictly increasing values of t.
#    At most 10^4 calls will be made to ping.

from collections import deque

class RecentCounter:
    """
    Queue to maintain requests within time window.
    """

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)

        # Remove requests older than 3000ms
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)


class RecentCounterList:
    """Using list with binary search"""

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        import bisect

        self.requests.append(t)
        # Find first request >= t - 3000
        idx = bisect.bisect_left(self.requests, t - 3000)
        return len(self.requests) - idx


class RecentCounterArray:
    """Using list with pruning"""

    def __init__(self):
        self.requests = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)

        while self.requests[self.start] < t - 3000:
            self.start += 1

        return len(self.requests) - self.start
