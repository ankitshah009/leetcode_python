#41. First Missing Positive
#Hard
#
#Given an unsorted integer array nums, return the smallest missing positive
#integer.
#
#You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary
#space.
#
#Example 1:
#Input: nums = [1,2,0]
#Output: 3
#Explanation: The numbers in the range [1,2] are all in the array.
#
#Example 2:
#Input: nums = [3,4,-1,1]
#Output: 2
#Explanation: 1 is in the array but 2 is missing.
#
#Example 3:
#Input: nums = [7,8,9,11,12]
#Output: 1
#Explanation: The smallest positive integer 1 is missing.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -2^31 <= nums[i] <= 2^31 - 1

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Cyclic sort - place each number at index num-1.
        O(n) time, O(1) space.
        """
        n = len(nums)

        # Place each number in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] to its correct position
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # Find first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


class SolutionMarking:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Mark presence using sign - O(n) time, O(1) space.
        """
        n = len(nums)

        # Mark invalid numbers
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Use sign to mark presence
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # Find first positive (unmarked) position
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


class SolutionSet:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Using set - O(n) time, O(n) space.
        Not meeting space constraint, for comparison.
        """
        num_set = set(nums)

        for i in range(1, len(nums) + 2):
            if i not in num_set:
                return i

        return 1


class SolutionSort:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Sorting approach - O(n log n) time.
        Not meeting time constraint, for comparison.
        """
        nums.sort()
        missing = 1

        for num in nums:
            if num == missing:
                missing += 1
            elif num > missing:
                break

        return missing
