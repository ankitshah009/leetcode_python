#862. Shortest Subarray with Sum at Least K
#Hard
#
#Given an integer array nums and an integer k, return the length of the shortest
#non-empty subarray of nums with a sum of at least k. If there is no such
#subarray, return -1.
#
#A subarray is a contiguous part of an array.
#
#Example 1:
#Input: nums = [1], k = 1
#Output: 1
#
#Example 2:
#Input: nums = [1,2], k = 4
#Output: -1
#
#Example 3:
#Input: nums = [2,-1,2], k = 3
#Output: 3
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^5 <= nums[i] <= 10^5
#    1 <= k <= 10^9

from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        """
        Monotonic deque with prefix sums.
        For each i, find smallest j where prefix[i] - prefix[j] >= k.
        """
        n = len(nums)

        # Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Monotonic deque of indices (increasing prefix values)
        dq = deque()
        result = float('inf')

        for i in range(n + 1):
            # Pop from front while sum >= k
            while dq and prefix[i] - prefix[dq[0]] >= k:
                result = min(result, i - dq.popleft())

            # Pop from back while current prefix <= previous
            # (they can never give shorter subarray)
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return result if result != float('inf') else -1


class SolutionExplained:
    """With detailed explanation"""

    def shortestSubarray(self, nums: list[int], k: int) -> int:
        """
        Key insights:
        1. Use prefix sums: sum[i:j] = prefix[j] - prefix[i]
        2. For each j, find smallest i where prefix[j] - prefix[i] >= k
        3. Maintain increasing deque of prefix values
           - Remove from front when valid (found answer for those indices)
           - Remove from back when prefix decreases (current is better candidate)
        """
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        dq = deque()  # Stores indices with increasing prefix values
        min_len = float('inf')

        for j in range(len(prefix)):
            # Check if current forms valid subarray with front elements
            while dq and prefix[j] - prefix[dq[0]] >= k:
                min_len = min(min_len, j - dq.popleft())

            # Maintain increasing order
            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(j)

        return min_len if min_len != float('inf') else -1
