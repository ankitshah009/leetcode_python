#1425. Constrained Subsequence Sum
#Hard
#
#Given an integer array nums and an integer k, return the maximum sum of a
#non-empty subsequence of that array such that for every two consecutive
#integers in the subsequence, nums[i] and nums[j], where i < j, the condition
#j - i <= k is satisfied.
#
#A subsequence of an array is obtained by deleting some number of elements
#(can be zero) from the array, leaving the remaining elements in their original
#order.
#
#Example 1:
#Input: nums = [10,2,-10,5,20], k = 2
#Output: 37
#Explanation: The subsequence is [10, 2, 5, 20].
#
#Example 2:
#Input: nums = [-1,-2,-3], k = 1
#Output: -1
#Explanation: The subsequence must be non-empty, so we choose the largest number.
#
#Example 3:
#Input: nums = [10,-2,-10,-5,20], k = 2
#Output: 23
#Explanation: The subsequence is [10, -2, -5, 20].
#
#Constraints:
#    1 <= k <= nums.length <= 10^5
#    -10^4 <= nums[i] <= 10^4

from typing import List
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
        dp[i] = max sum subsequence ending at i.
        dp[i] = nums[i] + max(0, max(dp[i-k], ..., dp[i-1]))

        Use monotonic deque to maintain max in sliding window.
        """
        n = len(nums)
        dp = [0] * n

        # Deque stores indices, dp values are monotonically decreasing
        dq = deque()
        max_sum = float('-inf')

        for i in range(n):
            # Remove indices outside window
            while dq and dq[0] < i - k:
                dq.popleft()

            # dp[i] = nums[i] + max(0, max of dp in window)
            dp[i] = nums[i]
            if dq:
                dp[i] = max(dp[i], nums[i] + dp[dq[0]])

            # Maintain decreasing monotonic deque
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)

            max_sum = max(max_sum, dp[i])

        return max_sum


class SolutionHeap:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """Using max heap"""
        import heapq

        n = len(nums)
        dp = [0] * n

        # Max heap: (-dp[i], i)
        heap = []
        max_sum = float('-inf')

        for i in range(n):
            # Remove elements outside window
            while heap and heap[0][1] < i - k:
                heapq.heappop(heap)

            dp[i] = nums[i]
            if heap:
                dp[i] = max(dp[i], nums[i] - heap[0][0])

            heapq.heappush(heap, (-dp[i], i))
            max_sum = max(max_sum, dp[i])

        return max_sum


class SolutionDP:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """Simple DP O(n*k) - for understanding"""
        n = len(nums)
        dp = nums.copy()

        for i in range(1, n):
            for j in range(max(0, i - k), i):
                if dp[j] > 0:
                    dp[i] = max(dp[i], nums[i] + dp[j])

        return max(dp)
