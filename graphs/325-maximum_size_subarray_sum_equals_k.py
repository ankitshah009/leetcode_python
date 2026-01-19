#325. Maximum Size Subarray Sum Equals k
#Medium
#
#Given an integer array nums and an integer k, return the maximum length of a
#subarray that sums to k. If there is not one, return 0 instead.
#
#Example 1:
#Input: nums = [1,-1,5,-2,3], k = 3
#Output: 4
#Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
#
#Example 2:
#Input: nums = [-2,-1,2,1], k = 1
#Output: 2
#Explanation: The subarray [-1, 2] sums to 1 and is the longest.
#
#Constraints:
#    1 <= nums.length <= 2 * 10^5
#    -10^4 <= nums[i] <= 10^4
#    -10^9 <= k <= 10^9

from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """Prefix sum with hash map"""
        prefix_sum = 0
        # Map prefix sum to its earliest index
        sum_index = {0: -1}
        max_len = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            # Check if we can form sum k ending at index i
            if prefix_sum - k in sum_index:
                max_len = max(max_len, i - sum_index[prefix_sum - k])

            # Only store first occurrence (for maximum length)
            if prefix_sum not in sum_index:
                sum_index[prefix_sum] = i

        return max_len


class SolutionBruteForce:
    """Brute force O(n^2) - for reference"""

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                if current_sum == k:
                    max_len = max(max_len, j - i + 1)

        return max_len


class SolutionPrefixArray:
    """Using prefix sum array"""

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        sum_index = {}
        max_len = 0

        for i in range(n + 1):
            # Looking for prefix[j] where prefix[i] - prefix[j] = k
            target = prefix[i] - k
            if target in sum_index:
                max_len = max(max_len, i - sum_index[target])

            if prefix[i] not in sum_index:
                sum_index[prefix[i]] = i

        return max_len
