#90. Subsets II
#Medium
#
#Given an integer array nums that may contain duplicates, return all possible
#subsets (the power set).
#
#The solution set must not contain duplicate subsets. Return the solution in any
#order.
#
#Example 1:
#Input: nums = [1,2,2]
#Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#Example 2:
#Input: nums = [0]
#Output: [[],[0]]
#
#Constraints:
#    1 <= nums.length <= 10
#    -10 <= nums[i] <= 10

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking with sorting to handle duplicates.
        """
        result = []
        nums.sort()

        def backtrack(start: int, current: List[int]):
            result.append(current[:])

            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result


class SolutionIterative:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Iterative approach - track subset start for duplicates.
        """
        nums.sort()
        result = [[]]
        start = 0

        for i in range(len(nums)):
            # If current is duplicate, only extend subsets added in last iteration
            if i > 0 and nums[i] == nums[i - 1]:
                new_subsets = [subset + [nums[i]] for subset in result[start:]]
            else:
                new_subsets = [subset + [nums[i]] for subset in result]

            start = len(result)
            result.extend(new_subsets)

        return result


class SolutionSet:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Using set to remove duplicates (less efficient).
        """
        nums.sort()
        result = set()

        def backtrack(start: int, current: tuple):
            result.add(current)

            for i in range(start, len(nums)):
                backtrack(i + 1, current + (nums[i],))

        backtrack(0, ())
        return [list(subset) for subset in result]


class SolutionBitMask:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Bit manipulation with duplicate detection.
        """
        nums.sort()
        n = len(nums)
        result = []
        seen = set()

        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])

            key = tuple(subset)
            if key not in seen:
                seen.add(key)
                result.append(subset)

        return result
