#908. Smallest Range I
#Easy
#
#You are given an integer array nums and an integer k.
#
#In one operation, you can choose any index i and change nums[i] to any value
#in the range [nums[i] - k, nums[i] + k].
#
#The score of nums is the difference between the maximum and minimum elements.
#
#Return the minimum score of nums after applying the mentioned operation at most
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
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 10^4
#    0 <= nums[i] <= 10^4
#    0 <= k <= 10^4

class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        """
        Move min up by k, move max down by k.
        """
        min_val = min(nums)
        max_val = max(nums)

        return max(0, max_val - min_val - 2 * k)


class SolutionExplicit:
    """More explicit calculation"""

    def smallestRangeI(self, nums: list[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)

        # After operations:
        # min can become min + k
        # max can become max - k
        new_diff = (max_val - k) - (min_val + k)

        return max(0, new_diff)
