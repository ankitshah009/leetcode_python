#416. Partition Equal Subset Sum
#Medium
#
#Given an integer array nums, return true if you can partition the array into two subsets
#such that the sum of the elements in both subsets is equal or false otherwise.
#
#Example 1:
#Input: nums = [1,5,11,5]
#Output: true
#Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#Example 2:
#Input: nums = [1,2,3,5]
#Output: false
#Explanation: The array cannot be partitioned into equal sum subsets.
#
#Constraints:
#    1 <= nums.length <= 200
#    1 <= nums[i] <= 100

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # If total is odd, cannot partition equally
        if total % 2 != 0:
            return False

        target = total // 2

        # dp[i] = True if sum i is achievable
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # Iterate backwards to avoid using same number twice
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]
