#560. Subarray Sum Equals K
#Medium
#
#Given an array of integers nums and an integer k, return the total number of
#subarrays whose sum equals to k.
#
#A subarray is a contiguous non-empty sequence of elements within an array.
#
#Example 1:
#Input: nums = [1,1,1], k = 2
#Output: 2
#
#Example 2:
#Input: nums = [1,2,3], k = 3
#Output: 2
#
#Constraints:
#    1 <= nums.length <= 2 * 10^4
#    -1000 <= nums[i] <= 1000
#    -10^7 <= k <= 10^7

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Prefix sum with hash map.
        If prefix[j] - prefix[i] = k, then subarray (i+1, j] sums to k.
        """
        count = 0
        prefix_sum = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1  # Empty prefix

        for num in nums:
            prefix_sum += num
            # Check if (prefix_sum - k) exists
            count += sum_count[prefix_sum - k]
            sum_count[prefix_sum] += 1

        return count


class SolutionBruteForce:
    """O(n^2) brute force"""

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total == k:
                    count += 1

        return count


class SolutionPrefixArray:
    """Using prefix sum array"""

    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        count = 0
        sum_count = defaultdict(int)

        for p in prefix:
            count += sum_count[p - k]
            sum_count[p] += 1

        return count
