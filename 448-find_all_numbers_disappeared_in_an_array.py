#448. Find All Numbers Disappeared in an Array
#Easy
#
#Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all
#the integers in the range [1, n] that do not appear in nums.
#
#Example 1:
#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [5,6]
#
#Example 2:
#Input: nums = [1,1]
#Output: [2]
#
#Constraints:
#    n == nums.length
#    1 <= n <= 10^5
#    1 <= nums[i] <= n

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark indices as negative to indicate presence
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Find indices that are still positive
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result
