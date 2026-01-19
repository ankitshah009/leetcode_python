#930. Binary Subarrays With Sum
#Medium
#
#Given a binary array nums and an integer goal, return the number of non-empty subarrays
#with a sum goal.
#
#A subarray is a contiguous part of the array.
#
#Example 1:
#Input: nums = [1,0,1,0,1], goal = 2
#Output: 4
#Explanation: The 4 subarrays are bolded and underlined below:
#[1,0,1,0,1]
#[1,0,1,0,1]
#[1,0,1,0,1]
#[1,0,1,0,1]
#
#Example 2:
#Input: nums = [0,0,0,0,0], goal = 0
#Output: 15
#
#Constraints:
#    1 <= nums.length <= 3 * 10^4
#    nums[i] is either 0 or 1.
#    0 <= goal <= nums.length

from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Using prefix sum + hash map
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            # Number of subarrays ending here with sum = goal
            count += prefix_count[prefix_sum - goal]
            prefix_count[prefix_sum] += 1

        return count

    # Alternative: Sliding window (exactly k = at most k - at most k-1)
    def numSubarraysWithSumSlidingWindow(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            if k < 0:
                return 0
            left = 0
            window_sum = 0
            count = 0
            for right in range(len(nums)):
                window_sum += nums[right]
                while window_sum > k:
                    window_sum -= nums[left]
                    left += 1
                count += right - left + 1
            return count

        return atMost(goal) - atMost(goal - 1)
