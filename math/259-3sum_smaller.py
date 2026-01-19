#259. 3Sum Smaller
#Medium
#
#Given an array of n integers nums and an integer target, find the number of
#index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition
#nums[i] + nums[j] + nums[k] < target.
#
#Example 1:
#Input: nums = [-2,0,1,3], target = 2
#Output: 2
#Explanation: Because there are two triplets which sums are less than 2:
#[-2,0,1] and [-2,0,3]
#
#Example 2:
#Input: nums = [], target = 0
#Output: 0
#
#Example 3:
#Input: nums = [0], target = 0
#Output: 0
#
#Constraints:
#    n == nums.length
#    0 <= n <= 3500
#    -100 <= nums[i] <= 100
#    -100 <= target <= 100

from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        Two-pointer approach after sorting.
        O(n^2) time, O(1) space (excluding sort).
        """
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < target:
                    # All pairs (left, left+1), (left, left+2), ..., (left, right)
                    # also satisfy the condition
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count


class SolutionBinarySearch:
    """Binary search for the third element"""

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        import bisect

        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                needed = target - nums[i] - nums[j]
                # Find count of elements < needed
                k = bisect.bisect_left(nums, needed, j + 1)
                count += k - j - 1

        return count


class SolutionBruteForce:
    """O(n^3) brute force"""

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] < target:
                        count += 1

        return count
