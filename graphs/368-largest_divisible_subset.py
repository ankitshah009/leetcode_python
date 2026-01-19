#368. Largest Divisible Subset
#Medium
#
#Given a set of distinct positive integers nums, return the largest subset
#answer such that every pair (answer[i], answer[j]) of elements in this subset
#satisfies:
#- answer[i] % answer[j] == 0, or
#- answer[j] % answer[i] == 0
#
#If there are multiple solutions, return any of them.
#
#Example 1:
#Input: nums = [1,2,3]
#Output: [1,2]
#Explanation: [1,3] is also accepted.
#
#Example 2:
#Input: nums = [1,2,4,8]
#Output: [1,2,4,8]
#
#Constraints:
#    1 <= nums.length <= 1000
#    1 <= nums[i] <= 2 * 10^9
#    All the integers in nums are unique.

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        DP approach similar to LIS.
        Sort first, then for each number find the longest chain ending at it.
        """
        if not nums:
            return []

        nums.sort()
        n = len(nums)

        # dp[i] = length of longest divisible subset ending at nums[i]
        dp = [1] * n
        # parent[i] = index of previous element in the chain
        parent = [-1] * n

        max_len = 1
        max_idx = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        # Reconstruct the subset
        result = []
        idx = max_idx
        while idx >= 0:
            result.append(nums[idx])
            idx = parent[idx]

        return result[::-1]


class SolutionDict:
    """Using dictionary for cleaner reconstruction"""

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()

        # dp[num] = (length, previous_num) of longest chain ending at num
        dp = {num: (1, -1) for num in nums}

        max_len = 1
        last_num = nums[0]

        for i, num in enumerate(nums):
            for j in range(i):
                if num % nums[j] == 0:
                    if dp[nums[j]][0] + 1 > dp[num][0]:
                        dp[num] = (dp[nums[j]][0] + 1, nums[j])

            if dp[num][0] > max_len:
                max_len = dp[num][0]
                last_num = num

        # Reconstruct
        result = []
        while last_num != -1:
            result.append(last_num)
            last_num = dp[last_num][1]

        return result[::-1]


class SolutionRecursive:
    """Recursive with memoization"""

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        from functools import lru_cache

        nums.sort()
        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(i):
            """Returns (length, next_index) for longest chain starting at i"""
            max_len = 1
            next_idx = -1

            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    length = 1 + dp(j)[0]
                    if length > max_len:
                        max_len = length
                        next_idx = j

            return (max_len, next_idx)

        # Find best starting point
        best_start = 0
        best_len = 1
        for i in range(n):
            length, _ = dp(i)
            if length > best_len:
                best_len = length
                best_start = i

        # Reconstruct
        result = []
        idx = best_start
        while idx != -1:
            result.append(nums[idx])
            _, idx = dp(idx)

        return result
