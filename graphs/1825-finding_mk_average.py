#1825. Finding MK Average
#Hard
#
#You are given two integers, m and k, and a stream of integers. You are tasked
#to implement a data structure that calculates the MKAverage for the stream.
#
#The MKAverage can be calculated using these steps:
#1. If the number of the elements in the stream is less than m you should
#   consider the MKAverage to be -1. Otherwise, copy the last m elements of the
#   stream to a separate container.
#2. Remove the smallest k elements and the largest k elements from the
#   container.
#3. Calculate the average value of the rest of the elements rounded down to the
#   nearest integer.
#
#Implement the MKAverage class:
#- MKAverage(int m, int k) Initializes the MKAverage object with an empty
#  stream and the two integers m and k.
#- void addElement(int num) Inserts a new element num into the stream.
#- int calculateMKAverage() Calculates and returns the MKAverage for the
#  current stream rounded down to the nearest integer.
#
#Example 1:
#Input: ["MKAverage", "addElement", "addElement", "calculateMKAverage",
#        "addElement", "calculateMKAverage", "addElement", "addElement",
#        "addElement", "calculateMKAverage"]
#       [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
#Output: [null, null, null, -1, null, 3, null, null, null, 5]
#
#Constraints:
#    3 <= m <= 10^5
#    1 <= k*2 < m
#    1 <= num <= 10^5
#    At most 10^5 calls will be made to addElement and calculateMKAverage.

from collections import deque
from sortedcontainers import SortedList

class MKAverage:
    """
    Using SortedList for O(log n) operations.
    """

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.queue = deque()
        self.sorted_list = SortedList()
        self.total_sum = 0

    def addElement(self, num: int) -> None:
        self.queue.append(num)
        self.sorted_list.add(num)
        self.total_sum += num

        if len(self.queue) > self.m:
            removed = self.queue.popleft()
            self.sorted_list.remove(removed)
            self.total_sum -= removed

    def calculateMKAverage(self) -> int:
        if len(self.queue) < self.m:
            return -1

        # Sum of smallest k
        smallest_sum = sum(self.sorted_list[:self.k])
        # Sum of largest k
        largest_sum = sum(self.sorted_list[-self.k:])

        middle_sum = self.total_sum - smallest_sum - largest_sum
        middle_count = self.m - 2 * self.k

        return middle_sum // middle_count


class MKAverageThreeLists:
    """
    Alternative using three sorted lists for bottom, middle, top.
    """

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.queue = deque()
        self.bottom = SortedList()  # smallest k
        self.middle = SortedList()  # middle m-2k
        self.top = SortedList()     # largest k
        self.middle_sum = 0

    def _balance(self):
        """Rebalance the three lists."""
        # Move from bottom to middle
        while len(self.bottom) > self.k:
            val = self.bottom.pop()
            self.middle.add(val)
            self.middle_sum += val

        # Move from middle to bottom
        while len(self.bottom) < self.k and self.middle:
            val = self.middle.pop(0)
            self.bottom.add(val)
            self.middle_sum -= val

        # Move from top to middle
        while len(self.top) > self.k:
            val = self.top.pop(0)
            self.middle.add(val)
            self.middle_sum += val

        # Move from middle to top
        while len(self.top) < self.k and self.middle:
            val = self.middle.pop()
            self.top.add(val)
            self.middle_sum -= val

    def addElement(self, num: int) -> None:
        self.queue.append(num)

        # Insert into appropriate list
        if self.bottom and num <= self.bottom[-1]:
            self.bottom.add(num)
        elif self.top and num >= self.top[0]:
            self.top.add(num)
        else:
            self.middle.add(num)
            self.middle_sum += num

        # Remove oldest if over capacity
        if len(self.queue) > self.m:
            removed = self.queue.popleft()
            if removed in self.bottom:
                self.bottom.remove(removed)
            elif removed in self.top:
                self.top.remove(removed)
            else:
                self.middle.remove(removed)
                self.middle_sum -= removed

        self._balance()

    def calculateMKAverage(self) -> int:
        if len(self.queue) < self.m:
            return -1
        return self.middle_sum // len(self.middle)
