#47. Permutations II
#Medium
#
#Given a collection of numbers, nums, that might contain duplicates, return all
#possible unique permutations in any order.
#
#Example 1:
#Input: nums = [1,1,2]
#Output: [[1,1,2],[1,2,1],[2,1,1]]
#
#Example 2:
#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#Constraints:
#    1 <= nums.length <= 8
#    -10 <= nums[i] <= 10

from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking with Counter to handle duplicates.
        """
        result = []
        counter = Counter(nums)

        def backtrack(path: List[int]):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    path.append(num)
                    backtrack(path)
                    path.pop()
                    counter[num] += 1

        backtrack([])
        return result


class SolutionSort:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Sort + backtracking with used array.
        """
        result = []
        nums.sort()
        used = [False] * len(nums)

        def backtrack(path: List[int]):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Skip duplicates at the same level
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return result


class SolutionSwap:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Swap approach with set to track used elements at each level.
        """
        result = []

        def backtrack(start: int):
            if start == len(nums):
                result.append(nums[:])
                return

            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])

                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result


class SolutionItertools:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Using itertools with set for uniqueness.
        """
        from itertools import permutations
        return list(set(permutations(nums)))
