#300. Longest Increasing Subsequence
#Medium
#
#Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
#Example 1:
#Input: nums = [10,9,2,5,3,7,101,18]
#Output: 4
#Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#
#Example 2:
#Input: nums = [0,1,0,3,2,3]
#Output: 4
#
#Example 3:
#Input: nums = [7,7,7,7,7,7,7]
#Output: 1
#
#Constraints:
#    1 <= nums.length <= 2500
#    -10^4 <= nums[i] <= 10^4

import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Binary search approach - O(n log n)
        tails = []

        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num

        return len(tails)

    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        # DP approach - O(n^2)
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
