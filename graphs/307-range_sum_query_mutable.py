#307. Range Sum Query - Mutable
#Medium
#
#Given an integer array nums, handle multiple queries of the following types:
#1. Update the value of an element in nums.
#2. Calculate the sum of the elements of nums between indices left and right
#   inclusive where left <= right.
#
#Implement the NumArray class:
#    NumArray(int[] nums) Initializes the object with the integer array nums.
#    void update(int index, int val) Updates the value of nums[index] to be val.
#    int sumRange(int left, int right) Returns the sum of the elements of nums
#    between indices left and right.
#
#Example 1:
#Input
#["NumArray", "sumRange", "update", "sumRange"]
#[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
#Output
#[null, 9, null, 8]
#
#Constraints:
#    1 <= nums.length <= 3 * 10^4
#    -100 <= nums[i] <= 100
#    0 <= index < nums.length
#    -100 <= val <= 100
#    0 <= left <= right < nums.length
#    At most 3 * 10^4 calls will be made to update and sumRange.

from typing import List

class NumArray:
    """Binary Indexed Tree (Fenwick Tree) - O(log n) update and query"""

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)

        # Build tree
        for i, num in enumerate(nums):
            self._add(i + 1, num)

    def _add(self, i, delta):
        """Add delta to index i (1-indexed)"""
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # Move to parent

    def _prefix_sum(self, i):
        """Get sum of elements [0, i-1] (i is 1-indexed)"""
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)  # Move to previous
        return total

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum(right + 1) - self._prefix_sum(left)


class NumArraySegmentTree:
    """Segment Tree implementation"""

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)

        # Build tree (leaves start at index n)
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]

        # Build internal nodes
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        index += self.n  # Move to leaf
        self.tree[index] = val

        # Update parents
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        total = 0

        while left <= right:
            if left % 2 == 1:  # Left is right child
                total += self.tree[left]
                left += 1
            if right % 2 == 0:  # Right is left child
                total += self.tree[right]
                right -= 1
            left //= 2
            right //= 2

        return total
