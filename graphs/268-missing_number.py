#268. Missing Number
#Easy
#
#Given an array nums containing n distinct numbers in the range [0, n], return
#the only number in the range that is missing from the array.
#
#Example 1:
#Input: nums = [3,0,1]
#Output: 2
#Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
#[0,3]. 2 is the missing number in the range since it does not appear in nums.
#
#Example 2:
#Input: nums = [0,1]
#Output: 2
#Explanation: n = 2 since there are 2 numbers, so all numbers are in the range
#[0,2]. 2 is the missing number in the range since it does not appear in nums.
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
#
#Follow up: Could you implement a solution using only O(1) extra space
#complexity and O(n) runtime complexity?

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Gauss formula: sum of 0 to n minus sum of array"""
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


class SolutionXOR:
    """XOR approach - O(1) space, avoids overflow"""

    def missingNumber(self, nums: List[int]) -> int:
        # XOR all indices and all values
        # Same numbers cancel out, leaving the missing number
        result = len(nums)

        for i, num in enumerate(nums):
            result ^= i ^ num

        return result


class SolutionSet:
    """Set approach - O(n) space"""

    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)

        for i in range(len(nums) + 1):
            if i not in num_set:
                return i

        return -1


class SolutionSort:
    """Sort and find first mismatch"""

    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i, num in enumerate(nums):
            if i != num:
                return i

        return len(nums)


class SolutionCyclicSort:
    """Cyclic sort - O(n) time, O(1) space"""

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            correct_pos = nums[i]
            # Swap if not at correct position and within bounds
            if nums[i] < n and nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1

        # Find the missing number
        for i in range(n):
            if nums[i] != i:
                return i

        return n
