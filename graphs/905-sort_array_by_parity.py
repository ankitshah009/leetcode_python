#905. Sort Array By Parity
#Easy
#
#Given an integer array nums, move all the even integers at the beginning of the
#array followed by all the odd integers. Return any array that satisfies this.
#
#Example 1:
#Input: nums = [3,1,2,4]
#Output: [2,4,3,1]
#Explanation: [4,2,3,1], [2,4,1,3], [4,2,1,3] are also accepted.
#
#Example 2:
#Input: nums = [0]
#Output: [0]
#
#Constraints:
#    1 <= nums.length <= 5000
#    0 <= nums[i] <= 5000

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """
        Two-pointer swap in place.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums


class SolutionSort:
    """Using sort with key"""

    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        return sorted(nums, key=lambda x: x % 2)


class SolutionTwoPass:
    """Two pass: evens first, then odds"""

    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]


class SolutionInPlaceSingle:
    """Single pointer in-place"""

    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even_idx = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[even_idx], nums[i] = nums[i], nums[even_idx]
                even_idx += 1

        return nums
