#1054. Distant Barcodes
#Medium
#
#In a warehouse, there is a row of barcodes, where the ith barcode is
#barcodes[i].
#
#Rearrange the barcodes so that no two adjacent barcodes are equal. You may
#return any answer, and it is guaranteed an answer exists.
#
#Example 1:
#Input: barcodes = [1,1,1,2,2,2]
#Output: [2,1,2,1,2,1]
#
#Example 2:
#Input: barcodes = [1,1,1,1,2,2,3,3]
#Output: [1,3,1,3,1,2,1,2]
#
#Constraints:
#    1 <= barcodes.length <= 10000
#    1 <= barcodes[i] <= 10000

from typing import List
from collections import Counter
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        Greedy with max heap.
        Always place the most frequent element that isn't the previous.
        """
        count = Counter(barcodes)
        # Max heap (negate for max behavior)
        heap = [(-cnt, val) for val, cnt in count.items()]
        heapq.heapify(heap)

        result = []
        prev = None

        while heap:
            cnt, val = heapq.heappop(heap)

            if val == prev:
                # Can't use this one, get next
                if not heap:
                    break
                cnt2, val2 = heapq.heappop(heap)
                result.append(val2)
                prev = val2
                if cnt2 + 1 < 0:
                    heapq.heappush(heap, (cnt2 + 1, val2))
                heapq.heappush(heap, (cnt, val))
            else:
                result.append(val)
                prev = val
                if cnt + 1 < 0:
                    heapq.heappush(heap, (cnt + 1, val))

        return result


class SolutionFillPositions:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        Fill even indices first with most frequent, then odd indices.
        """
        n = len(barcodes)
        count = Counter(barcodes)
        result = [0] * n

        # Sort by frequency
        sorted_items = sorted(count.items(), key=lambda x: -x[1])

        idx = 0
        for val, cnt in sorted_items:
            for _ in range(cnt):
                result[idx] = val
                idx += 2
                if idx >= n:
                    idx = 1  # Switch to odd positions

        return result


class SolutionCounting:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """Interleave approach"""
        count = Counter(barcodes)
        n = len(barcodes)
        result = [0] * n

        # Find most frequent
        most_freq = max(count.keys(), key=lambda x: count[x])

        # Fill even positions with most frequent first
        idx = 0
        while count[most_freq] > 0:
            result[idx] = most_freq
            count[most_freq] -= 1
            idx += 2
            if idx >= n:
                idx = 1

        # Fill rest
        for val, cnt in count.items():
            while cnt > 0:
                if idx >= n:
                    idx = 1
                result[idx] = val
                cnt -= 1
                idx += 2

        return result
