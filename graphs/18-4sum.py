#18. 4Sum
#Medium
#
#Given an array nums of n integers, return an array of all the unique quadruplets
#[nums[a], nums[b], nums[c], nums[d]] such that:
#    0 <= a, b, c, d < n
#    a, b, c, d are distinct.
#    nums[a] + nums[b] + nums[c] + nums[d] == target
#
#You may return the answer in any order.
#
#Example 1:
#Input: nums = [1,0,-1,0,-2,2], target = 0
#Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#Example 2:
#Input: nums = [2,2,2,2,2], target = 8
#Output: [[2,2,2,2]]
#
#Constraints:
#    1 <= nums.length <= 200
#    -10^9 <= nums[i] <= 10^9
#    -10^9 <= target <= 10^9

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Generalized k-sum approach using recursion.
        """
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            result = []

            if not nums:
                return result

            # Pruning
            average = target // k
            if nums[0] > average or nums[-1] < average:
                return result

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                    result.append([nums[i]] + subset)

            return result

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            left, right = 0, len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

            return result

        nums.sort()
        return kSum(nums, target, 4)


class SolutionIterative:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Iterative approach with two nested loops and two pointers.
        """
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Pruning
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Pruning
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                left, right = j + 1, n - 1
                remaining = target - nums[i] - nums[j]

                while left < right:
                    current_sum = nums[left] + nums[right]

                    if current_sum == remaining:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif current_sum < remaining:
                        left += 1
                    else:
                        right -= 1

        return result


class SolutionHashSet:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Using hash set for pair lookup.
        """
        nums.sort()
        n = len(nums)
        result = set()

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                seen = set()
                k = j + 1
                while k < n:
                    complement = target - nums[i] - nums[j] - nums[k]
                    if complement in seen:
                        result.add((nums[i], nums[j], complement, nums[k]))
                    seen.add(nums[k])
                    k += 1

        return [list(x) for x in result]
