#1685. Sum of Absolute Differences in a Sorted Array
#Medium
#
#You are given an integer array nums sorted in non-decreasing order.
#
#Build and return an integer array result with the same length as nums such that
#result[i] is equal to the summation of absolute differences between nums[i] and
#all the other elements in the array.
#
#In other words, result[i] = sum(|nums[i] - nums[j]|) for all 0 <= j < n, j != i.
#
#Example 1:
#Input: nums = [2,3,5]
#Output: [4,3,5]
#Explanation: For i=0: |2-3| + |2-5| = 4
#             For i=1: |3-2| + |3-5| = 3
#             For i=2: |5-2| + |5-3| = 5
#
#Example 2:
#Input: nums = [1,4,6,8,10]
#Output: [24,15,13,15,21]
#
#Constraints:
#    2 <= nums.length <= 10^5
#    1 <= nums[i] <= nums[i + 1] <= 10^4

from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        Use prefix sums to calculate efficiently.
        For sorted array:
        - Left elements contribute: i * nums[i] - prefix_sum[i]
        - Right elements contribute: (suffix_sum[i+1]) - (n-i-1) * nums[i]
        """
        n = len(nums)
        total = sum(nums)
        result = []
        prefix_sum = 0

        for i in range(n):
            # Elements to the left: all smaller or equal, so nums[i] - nums[j]
            left_count = i
            left_contribution = left_count * nums[i] - prefix_sum

            # Elements to the right: all larger or equal, so nums[j] - nums[i]
            right_sum = total - prefix_sum - nums[i]
            right_count = n - i - 1
            right_contribution = right_sum - right_count * nums[i]

            result.append(left_contribution + right_contribution)
            prefix_sum += nums[i]

        return result


class SolutionPrefixArray:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        Using explicit prefix sum array.
        """
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        result = []

        for i in range(n):
            # Sum of elements left of i
            left_sum = prefix[i]
            # Sum of elements right of i
            right_sum = prefix[n] - prefix[i + 1]

            # Contribution from left (all smaller)
            left_diff = i * nums[i] - left_sum

            # Contribution from right (all larger)
            right_diff = right_sum - (n - i - 1) * nums[i]

            result.append(left_diff + right_diff)

        return result


class SolutionMath:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        Mathematical derivation approach.

        sum(|nums[i] - nums[j]|) for j < i = i * nums[i] - sum(nums[0:i])
        sum(|nums[i] - nums[j]|) for j > i = sum(nums[i+1:n]) - (n-i-1) * nums[i]
        """
        n = len(nums)
        total = sum(nums)
        result = []

        running_sum = 0
        for i, num in enumerate(nums):
            left = i * num - running_sum
            right = (total - running_sum - num) - (n - i - 1) * num
            result.append(left + right)
            running_sum += num

        return result


class SolutionCompact:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        Compact implementation.
        """
        n, total, prefix = len(nums), sum(nums), 0
        return [
            (prefix := prefix + nums[i]) and
            i * nums[i] - (prefix - nums[i]) +
            (total - prefix) - (n - i - 1) * nums[i]
            for i in range(n)
        ] if False else [
            i * nums[i] - sum(nums[:i]) +
            sum(nums[i+1:]) - (n - i - 1) * nums[i]
            for i in range(n)
        ] if n < 100 else self.getSumAbsoluteDifferencesFast(nums)

    def getSumAbsoluteDifferencesFast(self, nums: List[int]) -> List[int]:
        n, total = len(nums), sum(nums)
        result, prefix = [], 0
        for i, num in enumerate(nums):
            left = i * num - prefix
            right = (total - prefix - num) - (n - i - 1) * num
            result.append(left + right)
            prefix += num
        return result
