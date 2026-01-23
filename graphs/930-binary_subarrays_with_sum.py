#930. Binary Subarrays With Sum
#Medium
#
#Given a binary array nums and an integer goal, return the number of non-empty
#subarrays with a sum goal.
#
#A subarray is a contiguous part of the array.
#
#Example 1:
#Input: nums = [1,0,1,0,1], goal = 2
#Output: 4
#Explanation: Subarrays are [1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1].
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
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        Prefix sum with hash map.
        """
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        result = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            result += prefix_count[prefix_sum - goal]
            prefix_count[prefix_sum] += 1

        return result


class SolutionSlidingWindow:
    """Sliding window: atMost(goal) - atMost(goal-1)"""

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atMost(k):
            if k < 0:
                return 0

            result = 0
            left = 0
            window_sum = 0

            for right in range(len(nums)):
                window_sum += nums[right]

                while window_sum > k:
                    window_sum -= nums[left]
                    left += 1

                result += right - left + 1

            return result

        return atMost(goal) - atMost(goal - 1)


class SolutionTwoPointers:
    """Two pointers tracking range of valid lefts"""

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        result = 0
        prefix_sum = 0
        count = defaultdict(int)
        count[0] = 1

        for num in nums:
            prefix_sum += num
            result += count.get(prefix_sum - goal, 0)
            count[prefix_sum] += 1

        return result
