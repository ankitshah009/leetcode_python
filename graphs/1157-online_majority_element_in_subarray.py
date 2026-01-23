#1157. Online Majority Element In Subarray
#Hard
#
#Design a data structure that efficiently finds the majority element of a
#given subarray.
#
#The majority element of a subarray is an element that occurs threshold times
#or more in the subarray.
#
#Implementing the MajorityChecker class:
#    MajorityChecker(int[] arr) Initializes the instance with the given array arr.
#    int query(int left, int right, int threshold) returns the element in the
#    subarray arr[left...right] that occurs at least threshold times, or -1 if
#    no such element exists.
#
#Example 1:
#Input
#["MajorityChecker", "query", "query", "query"]
#[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
#Output
#[null, 1, -1, 2]
#
#Constraints:
#    1 <= arr.length <= 2 * 10^4
#    1 <= arr[i] <= 2 * 10^4
#    0 <= left <= right < arr.length
#    threshold <= right - left + 1
#    2 * threshold > right - left + 1
#    At most 10^4 calls will be made to query.

from typing import List
from collections import defaultdict
import bisect
import random

class MajorityChecker:
    """
    Use random sampling + binary search.
    Since majority must appear > half the time, random sampling
    has high probability of hitting it.
    """
    def __init__(self, arr: List[int]):
        self.arr = arr
        # Store positions of each element
        self.positions = defaultdict(list)
        for i, num in enumerate(arr):
            self.positions[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        # Try random samples
        for _ in range(20):  # 20 tries gives very high success probability
            idx = random.randint(left, right)
            candidate = self.arr[idx]

            # Count occurrences using binary search
            pos = self.positions[candidate]
            left_idx = bisect.bisect_left(pos, left)
            right_idx = bisect.bisect_right(pos, right)
            count = right_idx - left_idx

            if count >= threshold:
                return candidate

        return -1


class MajorityCheckerSegmentTree:
    """
    Segment tree with Boyer-Moore voting.
    Each node stores potential majority candidate.
    """
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)
        self.positions = defaultdict(list)
        for i, num in enumerate(arr):
            self.positions[num].append(i)

        # Build segment tree storing (candidate, count)
        self.tree = [(0, 0)] * (4 * self.n)
        self._build(1, 0, self.n - 1)

    def _build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = (self.arr[start], 1)
            return

        mid = (start + end) // 2
        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid + 1, end)
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])

    def _merge(self, left, right):
        if left[0] == right[0]:
            return (left[0], left[1] + right[1])
        elif left[1] > right[1]:
            return (left[0], left[1] - right[1])
        else:
            return (right[0], right[1] - left[1])

    def _query_tree(self, node: int, start: int, end: int, left: int, right: int):
        if right < start or end < left:
            return (0, 0)
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_res = self._query_tree(2 * node, start, mid, left, right)
        right_res = self._query_tree(2 * node + 1, mid + 1, end, left, right)
        return self._merge(left_res, right_res)

    def query(self, left: int, right: int, threshold: int) -> int:
        candidate, _ = self._query_tree(1, 0, self.n - 1, left, right)

        if candidate == 0:
            return -1

        # Verify count
        pos = self.positions[candidate]
        left_idx = bisect.bisect_left(pos, left)
        right_idx = bisect.bisect_right(pos, right)

        if right_idx - left_idx >= threshold:
            return candidate
        return -1
