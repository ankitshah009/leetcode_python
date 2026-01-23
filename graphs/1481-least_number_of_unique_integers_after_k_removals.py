#1481. Least Number of Unique Integers after K Removals
#Medium
#
#Given an array of integers arr and an integer k. Find the least number of
#unique integers after removing exactly k elements.
#
#Example 1:
#Input: arr = [5,5,4], k = 1
#Output: 1
#Explanation: Remove the single 4, only 5 is left.
#
#Example 2:
#Input: arr = [4,3,1,1,3,3,2], k = 3
#Output: 2
#Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3
#will be left.
#
#Constraints:
#    1 <= arr.length <= 10^5
#    1 <= arr[i] <= 10^9
#    0 <= k <= arr.length

from typing import List
from collections import Counter
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        Greedy: remove elements with smallest frequencies first.
        """
        freq = Counter(arr)

        # Sort frequencies
        frequencies = sorted(freq.values())

        unique_count = len(frequencies)

        for count in frequencies:
            if k >= count:
                k -= count
                unique_count -= 1
            else:
                break

        return unique_count


class SolutionHeap:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """Using min-heap"""
        freq = Counter(arr)

        # Min-heap of frequencies
        heap = list(freq.values())
        heapq.heapify(heap)

        while k > 0 and heap:
            min_freq = heapq.heappop(heap)
            if k >= min_freq:
                k -= min_freq
            else:
                heapq.heappush(heap, min_freq)
                break

        return len(heap)


class SolutionBucketSort:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        Bucket sort approach for O(n) time.
        """
        freq = Counter(arr)
        n = len(arr)

        # Count how many elements have each frequency
        # bucket[i] = count of unique elements with frequency i
        bucket = [0] * (n + 1)
        for count in freq.values():
            bucket[count] += 1

        unique_count = len(freq)

        # Remove elements starting from lowest frequency
        for frequency in range(1, n + 1):
            if bucket[frequency] == 0:
                continue

            # How many elements of this frequency can we remove?
            removable = min(bucket[frequency], k // frequency)
            k -= removable * frequency
            unique_count -= removable

            if k < frequency:
                break

        return unique_count


class SolutionCounter:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """Alternative using Counter.most_common()"""
        freq = Counter(arr)

        # Sort by frequency (ascending)
        sorted_items = sorted(freq.items(), key=lambda x: x[1])

        removed = 0
        for _, count in sorted_items:
            if k >= count:
                k -= count
                removed += 1
            else:
                break

        return len(freq) - removed
