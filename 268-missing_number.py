#268. Missing Number
#Easy
#
#Given an array nums containing n distinct numbers in the range [0, n], return the only number
#in the range that is missing from the array.
#
#Example 1:
#Input: nums = [3,0,1]
#Output: 2
#Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
#2 is the missing number in the range since it does not appear in nums.
#
#Example 2:
#Input: nums = [0,1]
#Output: 2
#
#Example 3:
#Input: nums = [9,6,4,2,3,5,7,0,1]
#Output: 8
#
#Constraints:
#    n == nums.length
#    1 <= n <= 10^4
#    0 <= nums[i] <= n
#    All the numbers of nums are unique.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
