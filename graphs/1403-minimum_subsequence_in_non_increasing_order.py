#1403. Minimum Subsequence in Non-Increasing Order
#Easy
#
#Given the array nums, obtain a subsequence of the array whose sum of elements
#is strictly greater than the sum of the non included elements in such
#subsequence.
#
#If there are multiple solutions, return the subsequence with minimum size and
#if there still exist multiple solutions, return the subsequence with the
#maximum total sum of all its elements. A subsequence of an array can be obtained
#by erasing some (possibly zero) elements from the array.
#
#Note that the solution with the given constraints is guaranteed to be unique.
#Also return the answer sorted in non-increasing order.
#
#Example 1:
#Input: nums = [4,3,10,9,8]
#Output: [10,9]
#Explanation: The subsequences [10,9] and [10,8] are minimal such that the sum
#of their elements is strictly greater than the sum of elements not included.
#However, the subsequence [10,9] has the maximum total sum of its elements.
#
#Example 2:
#Input: nums = [4,4,7,6,7]
#Output: [7,7,6]
#Explanation: The subsequence [7,7] has the sum of its elements equal to 14
#which is not strictly greater than the sum of elements not included (14 = 4 + 4 + 6).
#Therefore, the subsequence [7,6,7] is the minimal satisfying the conditions.
#Note the subsequence has to be returned in non-increasing order.
#
#Example 3:
#Input: nums = [6]
#Output: [6]
#
#Constraints:
#    1 <= nums.length <= 500
#    1 <= nums[i] <= 100

from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        """
        Greedy: Sort descending, take elements until sum > remaining sum.
        This minimizes count and maximizes sum.
        """
        nums.sort(reverse=True)
        total = sum(nums)

        result = []
        current_sum = 0

        for num in nums:
            result.append(num)
            current_sum += num
            if current_sum > total - current_sum:
                break

        return result


class SolutionExplicit:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        """More explicit version"""
        nums.sort(reverse=True)
        total_sum = sum(nums)

        result = []
        subsequence_sum = 0
        remaining_sum = total_sum

        for num in nums:
            result.append(num)
            subsequence_sum += num
            remaining_sum -= num

            if subsequence_sum > remaining_sum:
                return result

        return result


class SolutionTwoPointer:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        """Alternative with tracking both sums"""
        nums.sort(reverse=True)

        total = sum(nums)
        target = total // 2  # Need sum > target

        result = []
        current_sum = 0

        for num in nums:
            if current_sum > target:
                break
            result.append(num)
            current_sum += num

        return result
