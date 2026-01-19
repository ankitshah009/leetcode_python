#239. Sliding Window Maximum
#Hard
#
#You are given an array of integers nums, there is a sliding window of size k
#which is moving from the very left of the array to the very right. You can
#only see the k numbers in the window. Each time the sliding window moves right
#by one position.
#
#Return the max sliding window.
#
#Example 1:
#Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
#Output: [3,3,5,5,6,7]
#Explanation:
#Window position                Max
#---------------               -----
#[1  3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7
#
#Example 2:
#Input: nums = [1], k = 1
#Output: [1]
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^4 <= nums[i] <= 10^4
#    1 <= k <= nums.length

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Monotonic decreasing deque - O(n) time.
        Deque stores indices of potential maximum elements.
        Front of deque is always the maximum for current window.
        """
        result = []
        dq = deque()  # Stores indices

        for i, num in enumerate(nums):
            # Remove indices outside current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements (they'll never be max)
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(i)

            # Add to result once we have full window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


class SolutionBruteForce:
    """O(n*k) brute force"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]


class SolutionHeap:
    """Using max heap - O(n log n)"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq

        # Max heap: store (-value, index)
        heap = []
        result = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            if i >= k - 1:
                # Remove elements outside window
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)

                result.append(-heap[0][0])

        return result


class SolutionDP:
    """DP approach splitting array into blocks"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []

        # left[i] = max from start of block to i
        # right[i] = max from i to end of block
        left = [0] * n
        right = [0] * n

        for i in range(n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])

            j = n - 1 - i
            if (j + 1) % k == 0 or j == n - 1:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])

        result = []
        for i in range(n - k + 1):
            result.append(max(right[i], left[i + k - 1]))

        return result
