#46. Permutations
#Medium
#
#Given an array nums of distinct integers, return all the possible permutations.
#You can return the answer in any order.
#
#Example 1:
#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#Example 2:
#Input: nums = [0,1]
#Output: [[0,1],[1,0]]
#
#Example 3:
#Input: nums = [1]
#Output: [[1]]
#
#Constraints:
#    1 <= nums.length <= 6
#    -10 <= nums[i] <= 10
#    All the integers of nums are unique.

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking with used set.
        """
        result = []

        def backtrack(path: List[int], used: set):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in nums:
                if num not in used:
                    path.append(num)
                    used.add(num)
                    backtrack(path, used)
                    path.pop()
                    used.remove(num)

        backtrack([], set())
        return result


class SolutionSwap:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking with in-place swapping.
        """
        result = []

        def backtrack(start: int):
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result


class SolutionItertools:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Using itertools.permutations.
        """
        from itertools import permutations
        return [list(p) for p in permutations(nums)]


class SolutionIterative:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Iterative approach - insert each number at all positions.
        """
        result = [[]]

        for num in nums:
            new_result = []
            for perm in result:
                for i in range(len(perm) + 1):
                    new_result.append(perm[:i] + [num] + perm[i:])
            result = new_result

        return result


class SolutionQueue:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        BFS-like approach using queue.
        """
        from collections import deque

        result = []
        queue = deque([[]])

        while queue:
            current = queue.popleft()

            if len(current) == len(nums):
                result.append(current)
            else:
                for num in nums:
                    if num not in current:
                        queue.append(current + [num])

        return result
