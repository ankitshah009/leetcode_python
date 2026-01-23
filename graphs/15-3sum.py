#15. 3Sum
#Medium
#
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
#such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
#Notice that the solution set must not contain duplicate triplets.
#
#Example 1:
#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
#Explanation:
#nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#The distinct triplets are [-1,0,1] and [-1,-1,2].
#
#Example 2:
#Input: nums = [0,1,1]
#Output: []
#
#Example 3:
#Input: nums = [0,0,0]
#Output: [[0,0,0]]
#
#Constraints:
#    3 <= nums.length <= 3000
#    -10^5 <= nums[i] <= 10^5

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort + Two Pointers - O(n^2) time.
        """
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Early termination
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result


class SolutionHashSet:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Using hash set for two sum lookup.
        """
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()
            j = i + 1

            while j < n:
                complement = -nums[i] - nums[j]

                if complement in seen:
                    result.append([nums[i], complement, nums[j]])
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1

                seen.add(nums[j])
                j += 1

        return result


class SolutionNoSort:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Without sorting using hash sets.
        """
        result = set()
        duplicates = set()
        seen = {}

        for i, val1 in enumerate(nums):
            if val1 not in duplicates:
                duplicates.add(val1)

                for j, val2 in enumerate(nums[i + 1:]):
                    complement = -val1 - val2

                    if complement in seen and seen[complement] == i:
                        result.add(tuple(sorted([val1, val2, complement])))

                    seen[val2] = i

        return [list(x) for x in result]
