#78. Subsets
#Medium
#
#Given an integer array nums of unique elements, return all possible subsets (the
#power set).
#
#The solution set must not contain duplicate subsets. Return the solution in any
#order.
#
#Example 1:
#Input: nums = [1,2,3]
#Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#Example 2:
#Input: nums = [0]
#Output: [[],[0]]
#
#Constraints:
#    1 <= nums.length <= 10
#    -10 <= nums[i] <= 10
#    All the numbers of nums are unique.

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking approach.
        """
        result = []

        def backtrack(start: int, path: List[int]):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result


class SolutionIterative:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Iterative - add each number to existing subsets.
        """
        result = [[]]

        for num in nums:
            result += [subset + [num] for subset in result]

        return result


class SolutionBitmask:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Bitmask approach - each number maps to bit position.
        """
        n = len(nums)
        result = []

        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            result.append(subset)

        return result


class SolutionRecursive:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Recursive - include or exclude each element.
        """
        if not nums:
            return [[]]

        rest = self.subsets(nums[1:])
        return rest + [[nums[0]] + s for s in rest]


class SolutionItertools:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Using itertools.combinations.
        """
        from itertools import combinations

        result = []
        for r in range(len(nums) + 1):
            result.extend(list(c) for c in combinations(nums, r))

        return result
