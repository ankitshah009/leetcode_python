#910. Smallest Range II
#Medium
#
#You are given an integer array nums and an integer k.
#
#For each index i, you must apply one of the following operations:
#- Add k to nums[i], or
#- Subtract k from nums[i]
#
#The score of nums is the difference between the maximum and minimum elements.
#
#Return the minimum score of nums after applying the above operation exactly
#once for each index in it.
#
#Example 1:
#Input: nums = [1], k = 0
#Output: 0
#
#Example 2:
#Input: nums = [0,10], k = 2
#Output: 6
#
#Example 3:
#Input: nums = [1,3,6], k = 3
#Output: 3
#
#Constraints:
#    1 <= nums.length <= 10^4
#    0 <= nums[i] <= 10^4
#    0 <= k <= 10^4

class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        """
        Sort array. For optimal solution, some prefix gets +k, suffix gets -k.
        Try all split points.
        """
        nums.sort()
        n = len(nums)

        # Initial answer: all +k or all -k (same range)
        result = nums[-1] - nums[0]

        # Try split point: nums[0:i+1] + k, nums[i+1:] - k
        for i in range(n - 1):
            # After operation:
            # min can be nums[0]+k or nums[i+1]-k
            # max can be nums[i]+k or nums[-1]-k
            high = max(nums[i] + k, nums[-1] - k)
            low = min(nums[0] + k, nums[i + 1] - k)
            result = min(result, high - low)

        return result


class SolutionExplained:
    """With detailed explanation"""

    def smallestRangeII(self, nums: list[int], k: int) -> int:
        """
        Key insight: After sorting, optimal solution has form:
        [+k, +k, ..., +k, -k, -k, ..., -k]

        The +k elements should be the smaller ones, -k should be larger ones.
        """
        nums.sort()
        n = len(nums)
        result = nums[-1] - nums[0]  # All same operation

        left_max = nums[0] + k  # Starts as first element + k
        right_min = nums[-1] - k  # Ends as last element - k

        for i in range(n - 1):
            # Elements [0, i] get +k, elements [i+1, n-1] get -k
            curr_max = max(nums[i] + k, nums[-1] - k)
            curr_min = min(nums[0] + k, nums[i + 1] - k)
            result = min(result, curr_max - curr_min)

        return result
