#448. Find All Numbers Disappeared in an Array
#Easy
#
#Given an array nums of n integers where nums[i] is in the range [1, n], return
#an array of all the integers in the range [1, n] that do not appear in nums.
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
#
#Follow up: Could you do it without extra space and in O(n) runtime? You may
#assume the returned list does not count as extra space.

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        O(n) time, O(1) space using array itself as hash.
        Mark presence by negating value at corresponding index.
        """
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result


class SolutionSet:
    """Using set - O(n) space"""

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in num_set]


class SolutionCycleSort:
    """Cyclic sort approach"""

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Place each number at its correct index
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        return [i + 1 for i in range(n) if nums[i] != i + 1]


class SolutionAdd:
    """Using addition instead of negation"""

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for num in nums:
            idx = (num - 1) % n
            nums[idx] += n

        return [i + 1 for i in range(n) if nums[i] <= n]
