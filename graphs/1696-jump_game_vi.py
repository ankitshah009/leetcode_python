#1696. Jump Game VI
#Medium
#
#You are given a 0-indexed integer array nums and an integer k.
#
#You are initially standing at index 0. In one move, you can jump at most k
#steps forward without going outside the boundaries of the array. That is, you
#can jump from index i to any index in the range [i + 1, min(n - 1, i + k)]
#inclusive.
#
#You want to reach the last index of the array (index n - 1). Your score is the
#sum of all nums[j] for each index j you visited in the array.
#
#Return the maximum score you can get.
#
#Example 1:
#Input: nums = [1,-1,-2,4,-7,3], k = 2
#Output: 7
#Explanation: Jump 1->3->5 to collect 1+4+3 = 8. Total score = 7.
#
#Example 2:
#Input: nums = [10,-5,-2,4,0,3], k = 3
#Output: 17
#Explanation: Jump 0->3->5. Score = 10+4+3 = 17.
#
#Example 3:
#Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
#Output: 0
#
#Constraints:
#    1 <= nums.length, k <= 10^5
#    -10^4 <= nums[i] <= 10^4

from typing import List
from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """
        DP with monotonic deque for O(n) time.
        dp[i] = max score to reach index i
        dp[i] = nums[i] + max(dp[i-k], ..., dp[i-1])
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        # Monotonic deque storing indices, decreasing by dp value
        dq = deque([0])

        for i in range(1, n):
            # Remove indices out of window
            while dq and dq[0] < i - k:
                dq.popleft()

            # dp[i] = nums[i] + max in window
            dp[i] = nums[i] + dp[dq[0]]

            # Maintain monotonic property
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            dq.append(i)

        return dp[n - 1]


class SolutionHeap:
    def maxResult(self, nums: List[int], k: int) -> int:
        """
        Using max-heap for range maximum queries.
        O(n log n) time complexity.
        """
        import heapq

        n = len(nums)
        # Max-heap of (-dp_value, index)
        heap = [(-nums[0], 0)]
        dp = nums[0]

        for i in range(1, n):
            # Remove elements outside window
            while heap[0][1] < i - k:
                heapq.heappop(heap)

            dp = nums[i] - heap[0][0]
            heapq.heappush(heap, (-dp, i))

        return dp


class SolutionDP:
    def maxResult(self, nums: List[int], k: int) -> int:
        """
        Basic DP (O(n*k) - may TLE for large inputs).
        """
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = nums[0]

        for i in range(1, n):
            for j in range(max(0, i - k), i):
                dp[i] = max(dp[i], dp[j] + nums[i])

        return dp[n - 1]


class SolutionSegmentTree:
    def maxResult(self, nums: List[int], k: int) -> int:
        """
        Using segment tree for range maximum query.
        """
        n = len(nums)

        # Build segment tree
        size = 1
        while size < n:
            size *= 2

        tree = [float('-inf')] * (2 * size)

        def update(idx: int, val: int):
            idx += size
            tree[idx] = val
            while idx > 1:
                idx //= 2
                tree[idx] = max(tree[2 * idx], tree[2 * idx + 1])

        def query(left: int, right: int) -> int:
            left += size
            right += size + 1
            result = float('-inf')
            while left < right:
                if left & 1:
                    result = max(result, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    result = max(result, tree[right])
                left //= 2
                right //= 2
            return result

        dp = nums[0]
        update(0, dp)

        for i in range(1, n):
            max_prev = query(max(0, i - k), i - 1)
            dp = nums[i] + max_prev
            update(i, dp)

        return dp


class SolutionCompact:
    def maxResult(self, nums: List[int], k: int) -> int:
        """
        Compact monotonic deque solution.
        """
        from collections import deque

        n = len(nums)
        dq = deque([(nums[0], 0)])  # (score, index)

        for i in range(1, n):
            while dq[0][1] < i - k:
                dq.popleft()

            score = nums[i] + dq[0][0]

            while dq and dq[-1][0] <= score:
                dq.pop()

            dq.append((score, i))

        return dq[-1][0]
