#16. 3Sum Closest
#Medium
#
#Given an integer array nums of length n and an integer target, find three
#integers in nums such that the sum is closest to target.
#
#Return the sum of the three integers.
#
#You may assume that each input would have exactly one solution.
#
#Example 1:
#Input: nums = [-1,2,1,-4], target = 1
#Output: 2
#Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#Example 2:
#Input: nums = [0,0,0], target = 1
#Output: 0
#Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
#
#Constraints:
#    3 <= nums.length <= 500
#    -1000 <= nums[i] <= 1000
#    -10^4 <= target <= 10^4

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Sort + Two Pointers - O(n^2) time.
        """
        nums.sort()
        n = len(nums)
        closest = float('inf')

        for i in range(n - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return target

                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest


class SolutionOptimized:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Optimized with early termination checks.
        """
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Check minimum possible sum with this i
            min_sum = nums[i] + nums[i + 1] + nums[i + 2]
            if min_sum > target:
                if abs(min_sum - target) < abs(closest - target):
                    closest = min_sum
                break

            # Check maximum possible sum with this i
            max_sum = nums[i] + nums[n - 2] + nums[n - 1]
            if max_sum < target:
                if abs(max_sum - target) < abs(closest - target):
                    closest = max_sum
                continue

            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return target

                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest


class SolutionBinarySearch:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Using binary search for the third element.
        """
        import bisect

        nums.sort()
        n = len(nums)
        closest = float('inf')

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                remaining = target - nums[i] - nums[j]
                k = bisect.bisect_left(nums, remaining, j + 1)

                # Check element at k and k-1
                for idx in [k - 1, k]:
                    if j < idx < n:
                        current_sum = nums[i] + nums[j] + nums[idx]
                        if abs(current_sum - target) < abs(closest - target):
                            closest = current_sum

        return closest
