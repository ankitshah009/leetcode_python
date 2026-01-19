#215. Kth Largest Element in an Array
#Medium
#
#Given an integer array nums and an integer k, return the kth largest element in the array.
#
#Note that it is the kth largest element in the sorted order, not the kth distinct element.
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

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use min-heap of size k
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

        return heap[0]
