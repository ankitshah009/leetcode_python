#215. Kth Largest Element in an Array
#Medium
#
#Given an integer array nums and an integer k, return the kth largest element
#in the array.
#
#Note that it is the kth largest element in the sorted order, not the kth
#distinct element.
#
#Can you solve it without sorting?
#
#Example 1:
#Input: nums = [3,2,1,5,6,4], k = 2
#Output: 5
#
#Example 2:
#Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
#Output: 4
#
#Constraints:
#    1 <= k <= nums.length <= 10^5
#    -10^4 <= nums[i] <= 10^4

import heapq
import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Min heap of size k - O(n log k)"""
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


class SolutionQuickSelect:
    """Quickselect - average O(n), worst O(n^2)"""

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert to kth smallest from end
        target = len(nums) - k

        def quickselect(left, right):
            # Randomly choose pivot to avoid worst case
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            pivot = nums[right]
            store_idx = left

            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1

            nums[store_idx], nums[right] = nums[right], nums[store_idx]

            if store_idx == target:
                return nums[store_idx]
            elif store_idx < target:
                return quickselect(store_idx + 1, right)
            else:
                return quickselect(left, store_idx - 1)

        return quickselect(0, len(nums) - 1)


class SolutionMaxHeap:
    """Max heap - pop k-1 times, then peek"""

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Python has min heap, so negate values for max heap
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        for _ in range(k - 1):
            heapq.heappop(max_heap)

        return -max_heap[0]


class SolutionNLargest:
    """Using heapq.nlargest - O(n + k log n)"""

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
