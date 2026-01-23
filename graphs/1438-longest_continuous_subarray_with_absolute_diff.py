#1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#Medium
#
#Given an array of integers nums and an integer limit, return the size of the
#longest non-empty subarray such that the absolute difference between any two
#elements of this subarray is less than or equal to limit.
#
#Example 1:
#Input: nums = [8,2,4,7], limit = 4
#Output: 2
#Explanation: All subarrays are:
#[8] with maximum absolute diff |8-8| = 0 <= 4.
#[8,2] with maximum absolute diff |8-2| = 6 > 4.
#[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
#[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
#[2] with maximum absolute diff |2-2| = 0 <= 4.
#[2,4] with maximum absolute diff |2-4| = 2 <= 4.
#[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
#[4] with maximum absolute diff |4-4| = 0 <= 4.
#[4,7] with maximum absolute diff |4-7| = 3 <= 4.
#[7] with maximum absolute diff |7-7| = 0 <= 4.
#Therefore, the size of the longest subarray is 2.
#
#Example 2:
#Input: nums = [10,1,2,4,7,2], limit = 5
#Output: 4
#Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute
#diff is |2-7| = 5 <= 5.
#
#Example 3:
#Input: nums = [4,2,2,2,4,4,2,2], limit = 0
#Output: 3
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^9
#    0 <= limit <= 10^9

from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        Sliding window with two monotonic deques:
        - max_deque: decreasing, front is max
        - min_deque: increasing, front is min

        Expand right, shrink left when max - min > limit.
        """
        max_dq = deque()  # Decreasing
        min_dq = deque()  # Increasing

        left = 0
        result = 0

        for right in range(len(nums)):
            # Add nums[right] to both deques
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)

            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)

            # Shrink window if constraint violated
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                left += 1
                # Remove elements outside window
                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()

            result = max(result, right - left + 1)

        return result


class SolutionSortedList:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """Using sorted container for O(n log n) solution"""
        from sortedcontainers import SortedList

        sl = SortedList()
        left = 0
        result = 0

        for right in range(len(nums)):
            sl.add(nums[right])

            while sl[-1] - sl[0] > limit:
                sl.remove(nums[left])
                left += 1

            result = max(result, right - left + 1)

        return result


class SolutionHeap:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """Using two heaps (less efficient due to lazy deletion)"""
        import heapq

        max_heap = []  # (-value, index)
        min_heap = []  # (value, index)

        left = 0
        result = 0

        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))

            while -max_heap[0][0] - min_heap[0][0] > limit:
                left += 1
                # Lazy removal
                while max_heap and max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                while min_heap and min_heap[0][1] < left:
                    heapq.heappop(min_heap)

            result = max(result, right - left + 1)

        return result
