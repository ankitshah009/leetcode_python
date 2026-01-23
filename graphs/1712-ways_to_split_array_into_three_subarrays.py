#1712. Ways to Split Array Into Three Subarrays
#Medium
#
#A split of an integer array is good if:
#- The array is split into three non-empty contiguous subarrays - named left,
#  mid, right respectively from left to right.
#- The sum of the elements in left is less than or equal to the sum of the
#  elements in mid, and the sum of the elements in mid is less than or equal
#  to the sum of the elements in right.
#
#Given nums, an array of non-negative integers, return the number of good ways
#to split nums. As the number may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: nums = [1,1,1]
#Output: 1
#
#Example 2:
#Input: nums = [1,2,2,2,5,0]
#Output: 3
#
#Example 3:
#Input: nums = [3,2,1]
#Output: 0
#
#Constraints:
#    3 <= nums.length <= 10^5
#    0 <= nums[i] <= 10^4

from typing import List
import bisect

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        """
        Prefix sum with binary search.
        For each left boundary, find valid range for mid boundary.
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Compute prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        total = prefix[n]
        result = 0

        # i is the last index of left subarray
        for i in range(n - 2):
            left_sum = prefix[i + 1]

            # Left sum must be at most 1/3 of total
            if left_sum * 3 > total:
                break

            # Find minimum j: mid_sum >= left_sum
            # mid_sum = prefix[j+1] - prefix[i+1] >= left_sum
            # prefix[j+1] >= 2 * left_sum
            min_j = bisect.bisect_left(prefix, 2 * left_sum, i + 2, n)

            # Find maximum j: mid_sum <= right_sum
            # mid_sum = prefix[j+1] - left_sum
            # right_sum = total - prefix[j+1]
            # prefix[j+1] - left_sum <= total - prefix[j+1]
            # 2 * prefix[j+1] <= total + left_sum
            # prefix[j+1] <= (total + left_sum) / 2
            max_j = bisect.bisect_right(prefix, (total + left_sum) // 2, min_j, n) - 1

            if max_j >= min_j:
                result = (result + max_j - min_j + 1) % MOD

        return result


class SolutionTwoPointers:
    def waysToSplit(self, nums: List[int]) -> int:
        """
        Two pointers approach - more efficient in practice.
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        total = prefix[n]
        result = 0
        j = k = 0

        for i in range(n - 2):
            left_sum = prefix[i + 1]

            # Move j to find min valid mid boundary
            j = max(j, i + 1)
            while j < n - 1 and prefix[j + 1] - left_sum < left_sum:
                j += 1

            # Move k to find max valid mid boundary
            k = max(k, j)
            while k < n - 1 and prefix[k + 1] - left_sum <= total - prefix[k + 1]:
                k += 1

            if j < n - 1 and k >= j:
                result = (result + k - j) % MOD

        return result
