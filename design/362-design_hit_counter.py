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
#    HitCounter() Initializes the object of the hit counter system.
#    void hit(int timestamp) Records a hit that happened at timestamp (in seconds).
#    int getHits(int timestamp) Returns the number of hits in the past 5 minutes
#    from timestamp (i.e., the past 300 seconds).
#
#Example 1:
#Input
#["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
#[[], [1], [2], [3], [4], [300], [300], [301]]
#Output
#[null, null, null, null, 3, null, 4, 3]
#
#Explanation
#HitCounter hitCounter = new HitCounter();
#hitCounter.hit(1);       // hit at timestamp 1.
#hitCounter.hit(2);       // hit at timestamp 2.
#hitCounter.hit(3);       // hit at timestamp 3.
#hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
#hitCounter.hit(300);     // hit at timestamp 300.
#hitCounter.getHits(300); // get hits at timestamp 300, return 4.
#hitCounter.getHits(301); // get hits at timestamp 301, return 3.
#
#Constraints:
#    1 <= timestamp <= 2 * 10^9
#    All the calls are being made to the system in chronological order.
#    At most 300 calls will be made to hit and getHits.
#
#Follow up: What if the number of hits per second could be huge? Does your
#design scale?

from collections import deque

class HitCounter:
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # Remove hits older than 300 seconds
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        return len(self.hits)


class HitCounterScalable:
    """O(1) space using circular buffer - handles many hits per second"""

    def __init__(self):
        self.times = [0] * 300   # Timestamp for each bucket
        self.hits = [0] * 300   # Hit count for each bucket

    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300
        if self.times[idx] != timestamp:
            # New timestamp for this bucket
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            # Same timestamp, increment
            self.hits[idx] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        return total


class HitCounterBinarySearch:
    """Using binary search for getHits"""

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        import bisect
        # Find first hit >= timestamp - 299
        start = bisect.bisect_left(self.hits, timestamp - 299)
        return len(self.hits) - start
