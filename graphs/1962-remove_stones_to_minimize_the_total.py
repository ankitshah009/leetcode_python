#1962. Remove Stones to Minimize the Total
#Medium
#
#You are given a 0-indexed integer array piles, where piles[i] represents the
#number of stones in the ith pile, and an integer k. You should apply the
#following operation exactly k times:
#
#Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
#
#Notice that you can apply the operation on the same pile more than once.
#
#Return the minimum possible total number of stones remaining after applying
#the k operations.
#
#Example 1:
#Input: piles = [5,4,9], k = 2
#Output: 12
#Explanation: Apply operation on pile 2 (9 -> 5), then pile 0 (5 -> 3).
#Total = 3 + 4 + 5 = 12.
#
#Example 2:
#Input: piles = [4,3,6,7], k = 3
#Output: 12
#
#Constraints:
#    1 <= piles.length <= 10^5
#    1 <= piles[i] <= 10^4
#    1 <= k <= 10^5

from typing import List
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
        Use max heap to always reduce the largest pile.
        """
        # Create max heap (negate values)
        heap = [-p for p in piles]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            removed = largest // 2
            heapq.heappush(heap, -(largest - removed))

        return -sum(heap)


class SolutionOptimized:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
        Optimized with total tracking.
        """
        heap = [-p for p in piles]
        heapq.heapify(heap)
        total = sum(piles)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            removed = largest // 2
            total -= removed
            heapq.heappush(heap, -(largest - removed))

        return total


class SolutionCountingSort:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
        Bucket/counting approach for limited range.
        """
        max_pile = max(piles)
        buckets = [0] * (max_pile + 1)

        for p in piles:
            buckets[p] += 1

        total = sum(piles)
        current_max = max_pile

        for _ in range(k):
            # Find largest non-empty bucket
            while buckets[current_max] == 0:
                current_max -= 1

            if current_max == 0:
                break

            # Remove floor(current_max / 2) stones
            removed = current_max // 2
            total -= removed

            buckets[current_max] -= 1
            new_size = current_max - removed
            buckets[new_size] += 1

        return total
