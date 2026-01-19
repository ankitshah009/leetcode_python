#209. Minimum Size Subarray Sum
#Medium
#
#Given an array of positive integers nums and a positive integer target, return
#the minimal length of a subarray whose sum is greater than or equal to target.
#If there is no such subarray, return 0 instead.
#
#Example 1:
#Input: target = 7, nums = [2,3,1,2,4,3]
#Output: 2
#Explanation: The subarray [4,3] has the minimal length under the problem constraint.
#
#Example 2:
#Input: target = 4, nums = [1,4,4]
#Output: 1
#
#Example 3:
#Input: target = 11, nums = [1,1,1,1,1,1,1,1]
#Output: 0
#
#Constraints:
#    1 <= target <= 10^9
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^4
#
#Follow up: If you have figured out the O(n) solution, try coding another
#solution of which the time complexity is O(n log(n)).

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Sliding window - O(n)"""
        n = len(nums)
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(n):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0


class SolutionBinarySearch:
    """Binary search with prefix sums - O(n log n)"""

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        import bisect

        n = len(nums)
        prefix_sums = [0] * (n + 1)

        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]

        min_length = float('inf')

        for i in range(n + 1):
            # Find smallest j such that prefix_sums[j] >= prefix_sums[i] + target
            needed = prefix_sums[i] + target
            j = bisect.bisect_left(prefix_sums, needed)

            if j <= n:
                min_length = min(min_length, j - i)

        return min_length if min_length != float('inf') else 0


class SolutionTwoPointer:
    """Alternative two-pointer implementation"""

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        window_sum = 0
        min_len = len(nums) + 1

        while right < len(nums):
            window_sum += nums[right]
            right += 1

            while window_sum >= target:
                min_len = min(min_len, right - left)
                window_sum -= nums[left]
                left += 1

        return min_len if min_len <= len(nums) else 0
