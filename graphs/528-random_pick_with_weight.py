#528. Random Pick with Weight
#Medium
#
#You are given a 0-indexed array of positive integers w where w[i] describes the
#weight of the ith index.
#
#You need to implement the function pickIndex(), which randomly picks an index in
#the range [0, w.length - 1] (inclusive) and returns it. The probability of picking
#an index i is w[i] / sum(w).
#
#Example 1:
#Input
#["Solution", "pickIndex"]
#[[[1]], []]
#Output
#[null, 0]
#
#Example 2:
#Input
#["Solution", "pickIndex", "pickIndex", "pickIndex", "pickIndex", "pickIndex"]
#[[[1, 3]], [], [], [], [], []]
#Output
#[null, 1, 1, 1, 1, 0]
#Explanation: The probability of picking index 1 is 3/4. Index 0 has probability 1/4.
#
#Constraints:
#    1 <= w.length <= 10^4
#    1 <= w[i] <= 10^5
#    pickIndex will be called at most 10^4 times.

from typing import List
import random
import bisect

class Solution:
    """Prefix sum with binary search"""

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)


class SolutionManualBinarySearch:
    """Manual binary search implementation"""

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.random() * self.total

        left, right = 0, len(self.prefix) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left


class SolutionLinear:
    """Linear search (for small arrays)"""

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)

        for i, p in enumerate(self.prefix):
            if p >= target:
                return i

        return len(self.prefix) - 1
