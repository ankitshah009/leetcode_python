#362. Design Hit Counter
#Medium
#
#Design a hit counter which counts the number of hits received in the past 5
#minutes (i.e., the past 300 seconds).
#
#Your system should accept a timestamp parameter (in seconds granularity), and
#you may assume that calls are being made to the system in chronological order
#(i.e., timestamp is monotonically increasing). Several hits may arrive roughly
#at the same time.
#
#Implement the HitCounter class:
#- HitCounter() Initializes the object of the hit counter system.
#- void hit(int timestamp) Records a hit that happened at timestamp (in
#  seconds). Several hits may happen at the same timestamp.
#- int getHits(int timestamp) Returns the number of hits in the past 5 minutes
#  from timestamp (i.e., the past 300 seconds).
#
#Example 1:
#Input: ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits",
#        "getHits"]
#       [[], [1], [2], [3], [4], [300], [300], [301]]
#Output: [null, null, null, null, 3, null, 4, 3]
#
#Constraints:
#    1 <= timestamp <= 2 * 10^9
#    All the calls are being made to the system in chronological order (i.e.,
#    timestamp is monotonically increasing).
#    At most 300 calls will be made to hit and getHits.

from collections import deque

class HitCounter:
    """Using deque to store timestamps"""

    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # Remove old hits
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)


class HitCounterBuckets:
    """O(1) space using fixed-size buckets"""

    def __init__(self):
        self.times = [0] * 300
        self.counts = [0] * 300

    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300
        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.counts[idx] = 1
        else:
            self.counts[idx] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.counts[i]
        return total


class HitCounterScalable:
    """Scalable solution with deque storing (timestamp, count) pairs"""

    def __init__(self):
        self.hits = deque()
        self.total = 0

    def hit(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            self.hits.append([timestamp, 1])
        self.total += 1

        # Clean old entries
        self._cleanup(timestamp)

    def getHits(self, timestamp: int) -> int:
        self._cleanup(timestamp)
        return self.total

    def _cleanup(self, timestamp: int):
        while self.hits and self.hits[0][0] <= timestamp - 300:
            self.total -= self.hits[0][1]
            self.hits.popleft()


class HitCounterBinarySearch:
    """Using binary search for large number of hits"""

    def __init__(self):
        import bisect
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        import bisect
        # Find hits in range (timestamp - 300, timestamp]
        left = bisect.bisect_right(self.hits, timestamp - 300)
        return len(self.hits) - left
