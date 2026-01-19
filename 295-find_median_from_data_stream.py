#295. Find Median from Data Stream
#Hard
#
#The median is the middle value in an ordered integer list. If the size of the list is even,
#there is no middle value, and the median is the mean of the two middle values.
#
#Implement the MedianFinder class:
#    MedianFinder() initializes the MedianFinder object.
#    void addNum(int num) adds the integer num from the data stream to the data structure.
#    double findMedian() returns the median of all elements so far.
#
#Example 1:
#Input
#["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
#[[], [1], [2], [], [3], []]
#Output
#[null, null, null, 1.5, null, 2.0]
#
#Constraints:
#    -10^5 <= num <= 10^5
#    There will be at least one element in the data structure before calling findMedian.
#    At most 5 * 10^4 calls will be made to addNum and findMedian.

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negated)
        self.large = []  # Min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
