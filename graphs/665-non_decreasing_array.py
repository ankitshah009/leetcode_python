#665. Non-decreasing Array
#Medium
#
#Given an array nums with n integers, your task is to check if it could become
#non-decreasing by modifying at most one element.
#
#We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every
#i (0-based) such that (0 <= i <= n - 2).
#
#Example 1:
#Input: nums = [4,2,3]
#Output: true
#Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
#
#Example 2:
#Input: nums = [4,2,1]
#Output: false
#Explanation: You cannot get a non-decreasing array by modifying at most one element.
#
#Constraints:
#    n == nums.length
#    1 <= n <= 10^4
#    -10^5 <= nums[i] <= 10^5

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        Find violation and try to fix by modifying either element.
        """
        n = len(nums)
        count = 0

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:
                    return False

                # Try to fix: either lower nums[i] or raise nums[i+1]
                # Prefer lowering nums[i] if possible
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]  # Lower nums[i]
                else:
                    nums[i + 1] = nums[i]  # Raise nums[i+1]

        return True


class SolutionNoModify:
    """Without modifying the array"""

    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        violation = -1

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if violation != -1:
                    return False
                violation = i

        if violation == -1:
            return True

        # Can we fix by modifying nums[violation]?
        if violation == 0 or nums[violation - 1] <= nums[violation + 1]:
            return True

        # Can we fix by modifying nums[violation + 1]?
        if violation == n - 2 or nums[violation] <= nums[violation + 2]:
            return True

        return False


class SolutionConcise:
    """Concise one-pass solution"""

    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if modified:
                    return False
                modified = True

                # Check if we can fix
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]

        return True
