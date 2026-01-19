#368. Largest Divisible Subset
#Medium
#
#Given a set of distinct positive integers nums, return the largest subset answer such that
#every pair (answer[i], answer[j]) of elements in this subset satisfies:
#    answer[i] % answer[j] == 0, or
#    answer[j] % answer[i] == 0
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

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)

        # dp[i] = length of largest divisible subset ending at index i
        dp = [1] * n
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
        while idx != -1:
            result.append(nums[idx])
            idx = parent[idx]

        return result
