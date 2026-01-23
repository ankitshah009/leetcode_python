#747. Largest Number At Least Twice of Others
#Easy
#
#You are given an integer array nums where the largest integer is unique.
#
#Determine whether the largest element in the array is at least twice as much
#as every other number in the array. If it is, return the index of the largest
#element, or return -1 otherwise.
#
#Example 1:
#Input: nums = [3,6,1,0]
#Output: 1
#Explanation: 6 is the largest integer.
#For every other number in the array x, 6 is at least twice as big as x.
#The index of value 6 is 1, so we return 1.
#
#Example 2:
#Input: nums = [1,2,3,4]
#Output: -1
#Explanation: 4 is less than twice the value of 3, so we return -1.
#
#Constraints:
#    2 <= nums.length <= 50
#    0 <= nums[i] <= 100
#    The largest element in nums is unique.

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        """
        Find max and second max, compare.
        """
        max_idx = 0
        max_val = nums[0]
        second_max = float('-inf')

        for i in range(1, len(nums)):
            if nums[i] > max_val:
                second_max = max_val
                max_val = nums[i]
                max_idx = i
            elif nums[i] > second_max:
                second_max = nums[i]

        return max_idx if max_val >= 2 * second_max else -1


class SolutionSort:
    """Using sorting"""

    def dominantIndex(self, nums: list[int]) -> int:
        max_idx = nums.index(max(nums))
        sorted_nums = sorted(nums, reverse=True)

        if sorted_nums[0] >= 2 * sorted_nums[1]:
            return max_idx
        return -1


class SolutionSimple:
    """Simple approach with max"""

    def dominantIndex(self, nums: list[int]) -> int:
        max_val = max(nums)
        max_idx = nums.index(max_val)

        for num in nums:
            if num != max_val and max_val < 2 * num:
                return -1

        return max_idx


class SolutionOnePass:
    """Single pass tracking max and second max"""

    def dominantIndex(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        first = second = float('-inf')
        max_idx = 0

        for i, num in enumerate(nums):
            if num > first:
                second = first
                first = num
                max_idx = i
            elif num > second:
                second = num

        return max_idx if first >= 2 * second else -1
