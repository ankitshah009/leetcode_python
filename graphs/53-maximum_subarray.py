#53. Maximum Subarray
#Medium
#
#Given an integer array nums, find the subarray with the largest sum, and return
#its sum.
#
#Example 1:
#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
#Example 2:
#Input: nums = [1]
#Output: 1
#Explanation: The subarray [1] has the largest sum 1.
#
#Example 3:
#Input: nums = [5,4,-1,7,8]
#Output: 23
#Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^4 <= nums[i] <= 10^4
#
#Follow up: If you have figured out the O(n) solution, try coding another solution
#using the divide and conquer approach, which is more subtle.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm - O(n) time, O(1) space.
        """
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            # Either extend current subarray or start new one
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum


class SolutionDP:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        DP approach - more explicit state tracking.
        dp[i] = max sum of subarray ending at i.
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)


class SolutionDivideConquer:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Divide and Conquer - O(n log n).
        """
        def helper(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            # Max sum in left half
            left_max = helper(left, mid)

            # Max sum in right half
            right_max = helper(mid + 1, right)

            # Max sum crossing the middle
            left_sum = float('-inf')
            current = 0
            for i in range(mid, left - 1, -1):
                current += nums[i]
                left_sum = max(left_sum, current)

            right_sum = float('-inf')
            current = 0
            for i in range(mid + 1, right + 1):
                current += nums[i]
                right_sum = max(right_sum, current)

            cross_max = left_sum + right_sum

            return max(left_max, right_max, cross_max)

        return helper(0, len(nums) - 1)


class SolutionPrefix:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Prefix sum approach.
        max_sum = max(prefix[j] - prefix[i]) for all j > i.
        """
        max_sum = nums[0]
        prefix_sum = 0
        min_prefix = 0

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_prefix)
            min_prefix = min(min_prefix, prefix_sum)

        return max_sum
