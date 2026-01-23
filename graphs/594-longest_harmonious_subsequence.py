#594. Longest Harmonious Subsequence
#Easy
#
#We define a harmonious array as an array where the difference between its maximum
#value and its minimum value is exactly 1.
#
#Given an integer array nums, return the length of its longest harmonious
#subsequence among all its possible subsequences.
#
#A subsequence of array is a sequence that can be derived from the array by
#deleting some or no elements without changing the order of the remaining elements.
#
#Example 1:
#Input: nums = [1,3,2,2,5,2,3,7]
#Output: 5
#Explanation: The longest harmonious subsequence is [3,2,2,2,3].
#
#Example 2:
#Input: nums = [1,2,3,4]
#Output: 2
#
#Example 3:
#Input: nums = [1,1,1,1]
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 2 * 10^4
#    -10^9 <= nums[i] <= 10^9

from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """Count frequencies and check adjacent values"""
        count = Counter(nums)
        max_len = 0

        for num in count:
            if num + 1 in count:
                max_len = max(max_len, count[num] + count[num + 1])

        return max_len


class SolutionSorting:
    """Using sorting"""

    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        max_len = 0
        prev_count = 0
        curr_count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                curr_count += 1
            else:
                if nums[i] - nums[i - 1] == 1:
                    max_len = max(max_len, prev_count + curr_count)
                prev_count = curr_count
                curr_count = 1

        # Don't need to check last group since there's no next value

        return max_len


class SolutionOnePass:
    """Single pass with hash map"""

    def findLHS(self, nums: List[int]) -> int:
        count = {}
        max_len = 0

        for num in nums:
            count[num] = count.get(num, 0) + 1

            if num - 1 in count:
                max_len = max(max_len, count[num] + count[num - 1])
            if num + 1 in count:
                max_len = max(max_len, count[num] + count[num + 1])

        return max_len
