#347. Top K Frequent Elements
#Medium
#
#Given an integer array nums and an integer k, return the k most frequent
#elements. You may return the answer in any order.
#
#Example 1:
#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]
#
#Example 2:
#Input: nums = [1], k = 1
#Output: [1]
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^4 <= nums[i] <= 10^4
#    k is in the range [1, the number of unique elements in the array].
#    It is guaranteed that the answer is unique.
#
#Follow up: Your algorithm's time complexity must be better than O(n log n),
#where n is the array's size.

from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Bucket sort approach - O(n) time"""
        count = Counter(nums)
        n = len(nums)

        # Bucket where index = frequency
        buckets = [[] for _ in range(n + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result


class SolutionHeap:
    """Min heap approach - O(n log k)"""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # Use min heap of size k
        return heapq.nlargest(k, count.keys(), key=count.get)


class SolutionQuickSelect:
    """Quick select approach - O(n) average"""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import random

        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_idx):
            pivot_freq = count[unique[pivot_idx]]
            # Move pivot to end
            unique[pivot_idx], unique[right] = unique[right], unique[pivot_idx]

            store_idx = left
            for i in range(left, right):
                if count[unique[i]] < pivot_freq:
                    unique[store_idx], unique[i] = unique[i], unique[store_idx]
                    store_idx += 1

            # Move pivot to its final place
            unique[right], unique[store_idx] = unique[store_idx], unique[right]
            return store_idx

        def quickselect(left, right, k_smallest):
            if left == right:
                return

            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)

            if k_smallest == pivot_idx:
                return
            elif k_smallest < pivot_idx:
                quickselect(left, pivot_idx - 1, k_smallest)
            else:
                quickselect(pivot_idx + 1, right, k_smallest)

        n = len(unique)
        quickselect(0, n - 1, n - k)

        return unique[n - k:]


class SolutionSorted:
    """Simple sorting - O(n log n)"""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [num for num, _ in count.most_common(k)]
