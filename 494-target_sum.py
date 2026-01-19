#494. Target Sum
#Medium
#
#You are given an integer array nums and an integer target.
#
#You want to build an expression out of nums by adding one of the symbols '+' and '-' before
#each integer in nums and then concatenate all the integers.
#
#For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate
#them to build the expression "+2-1".
#
#Return the number of different expressions that you can build, which evaluates to target.
#
#Example 1:
#Input: nums = [1,1,1,1,1], target = 3
#Output: 5
#Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
#-1 + 1 + 1 + 1 + 1 = 3
#+1 - 1 + 1 + 1 + 1 = 3
#+1 + 1 - 1 + 1 + 1 = 3
#+1 + 1 + 1 - 1 + 1 = 3
#+1 + 1 + 1 + 1 - 1 = 3
#
#Example 2:
#Input: nums = [1], target = 1
#Output: 1
#
#Constraints:
#    1 <= nums.length <= 20
#    0 <= nums[i] <= 1000
#    0 <= sum(nums[i]) <= 1000
#    -1000 <= target <= 1000

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Convert to subset sum problem
        # P - N = target, P + N = sum
        # P = (target + sum) / 2
        total = sum(nums)

        if (target + total) % 2 != 0 or abs(target) > total:
            return 0

        subset_sum = (target + total) // 2

        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            new_dp = defaultdict(int)
            for s, count in dp.items():
                new_dp[s + num] += count
                new_dp[s] += count
            dp = new_dp

        return dp[subset_sum]
