#703. Kth Largest Element in a Stream
#Easy
#
#You are part of a university admissions office and need to keep track of the kth
#highest test score from applicants in real-time. This helps to determine cut-off
#marks for interviews and admissions dynamically as new applicants submit their scores.
#
#You are tasked to implement a class which, for a given integer k, maintains a
#stream of test scores and continuously returns the kth highest test score after
#a new score has been submitted. More specifically, we are looking for the kth
#highest score in the sorted list of all scores.
#
#Implement the KthLargest class:
#- KthLargest(int k, int[] nums) Initializes the object with the integer k and
#  the stream of test scores nums.
#- int add(int val) Adds a new test score val to the stream and returns the element
#  representing the kth largest element in the pool of test scores so far.
#
#Example 1:
#Input: ["KthLargest", "add", "add", "add", "add", "add"]
#       [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
#Output: [null, 4, 5, 5, 8, 8]
#
#Constraints:
#    0 <= nums.length <= 10^4
#    1 <= k <= nums.length + 1
#    -10^4 <= nums[i] <= 10^4
#    -10^4 <= val <= 10^4
#    At most 10^4 calls will be made to add.

from typing import List
import heapq

class KthLargest:
    """Min heap of size k - top is kth largest"""

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]


class KthLargestHeapify:
    """Using heapify for initialization"""

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


class KthLargestSortedList:
    """Using sorted container"""

    def __init__(self, k: int, nums: List[int]):
        from sortedcontainers import SortedList
        self.k = k
        self.sl = SortedList(nums)

    def add(self, val: int) -> int:
        self.sl.add(val)
        return self.sl[-self.k]
