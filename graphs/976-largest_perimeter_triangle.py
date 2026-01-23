#976. Largest Perimeter Triangle
#Easy
#
#Given an integer array nums, return the largest perimeter of a triangle with
#a non-zero area, formed from three of these lengths. If it is impossible to
#form any triangle of a non-zero area, return 0.
#
#Example 1:
#Input: nums = [2,1,2]
#Output: 5
#Explanation: Use all three sides.
#
#Example 2:
#Input: nums = [1,2,1,10]
#Output: 0
#Explanation: Can't form any valid triangle.
#
#Constraints:
#    3 <= nums.length <= 10^4
#    1 <= nums[i] <= 10^6

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        """
        Sort and check consecutive triplets.
        """
        nums.sort(reverse=True)

        for i in range(len(nums) - 2):
            # Triangle inequality: sum of two smaller > largest
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]

        return 0


class SolutionSortAsc:
    """Sort ascending and check from end"""

    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < nums[i - 1] + nums[i - 2]:
                return nums[i] + nums[i - 1] + nums[i - 2]

        return 0


class SolutionExplicit:
    """More explicit check"""

    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)

        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]

            # Valid triangle if largest side < sum of other two
            # Since sorted: a >= b >= c, so check a < b + c
            if a < b + c:
                return a + b + c

        return 0
