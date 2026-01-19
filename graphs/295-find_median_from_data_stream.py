#295. Find Median from Data Stream
#Hard
#
#The median is the middle value in an ordered integer list. If the size of the
#list is even, there is no middle value, and the median is the mean of the two
#middle values.
#
#For example, for arr = [2,3,4], the median is 3.
#For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
#
#Implement the MedianFinder class:
#    MedianFinder() initializes the MedianFinder object.
#    void addNum(int num) adds the integer num from the data stream to the
#    data structure.
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
#    There will be at least one element in the data structure before calling
#    findMedian.
#    At most 5 * 10^4 calls will be made to addNum and findMedian.
#
#Follow up: How would you design if all integers are in [0, 100]?
#How would you design if 99% of integers are in [0, 100]?

import heapq

class MedianFinder:
    """
    Two heaps: max heap for lower half, min heap for upper half.
    Median is at the top of one or both heaps.
    """

    def __init__(self):
        self.small = []  # Max heap (negated values)
        self.large = []  # Min heap

    def addNum(self, num: int) -> None:
        # Add to max heap (lower half)
        heapq.heappush(self.small, -num)

        # Balance: ensure all elements in small <= all elements in large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Maintain size: small can have at most 1 more element than large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2


class MedianFinderSortedList:
    """Using SortedList for O(log n) insertion"""

    def __init__(self):
        from sortedcontainers import SortedList
        self.nums = SortedList()

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2


class MedianFinderCounting:
    """For follow-up: integers in [0, 100] - use counting"""

    def __init__(self):
        self.counts = [0] * 101
        self.total = 0

    def addNum(self, num: int) -> None:
        self.counts[num] += 1
        self.total += 1

    def findMedian(self) -> float:
        target = (self.total + 1) // 2
        count = 0

        for i in range(101):
            count += self.counts[i]

            if count >= target:
                if self.total % 2 == 1:
                    return i
                else:
                    # Find the next element
                    if count > target:
                        return i
                    for j in range(i + 1, 101):
                        if self.counts[j] > 0:
                            return (i + j) / 2

        return 0
