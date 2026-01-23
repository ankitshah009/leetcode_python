#1099. Two Sum Less Than K
#Easy
#
#Given an array nums of integers and integer k, return the maximum sum such
#that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no
#i, j exist satisfying this equation, return -1.
#
#Example 1:
#Input: nums = [34,23,1,24,75,33,54,8], k = 60
#Output: 58
#Explanation: We can use 34 and 24 to sum 58 which is less than 60.
#
#Example 2:
#Input: nums = [10,20,30], k = 15
#Output: -1
#Explanation: In this case it is not possible to get a pair sum less that 15.
#
#Constraints:
#    1 <= nums.length <= 100
#    1 <= nums[i] <= 1000
#    1 <= k <= 2000

from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """
        Sort and use two pointers.
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        result = -1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < k:
                result = max(result, current_sum)
                left += 1
            else:
                right -= 1

        return result


class SolutionBruteForce:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """O(n^2) brute force"""
        result = -1
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                s = nums[i] + nums[j]
                if s < k:
                    result = max(result, s)

        return result


class SolutionCounting:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """Counting sort approach for bounded values"""
        count = [0] * 1001

        for num in nums:
            count[num] += 1

        result = -1
        left, right = 1, 1000

        while left <= right:
            if left + right >= k or count[right] == 0:
                right -= 1
            elif count[left] == 0:
                left += 1
            elif left < right:
                result = max(result, left + right)
                left += 1
            else:  # left == right
                if count[left] > 1:
                    result = max(result, left * 2)
                left += 1

        return result
