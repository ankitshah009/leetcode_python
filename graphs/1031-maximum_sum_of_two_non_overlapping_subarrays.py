#1031. Maximum Sum of Two Non-Overlapping Subarrays
#Medium
#
#Given an integer array nums and two integers firstLen and secondLen, return
#the maximum sum of elements in two non-overlapping subarrays with lengths
#firstLen and secondLen.
#
#The array with length firstLen could occur before or after the array with
#length secondLen, but they have to be non-overlapping.
#
#A subarray is a contiguous part of an array.
#
#Example 1:
#Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
#Output: 20
#Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
#
#Example 2:
#Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
#Output: 29
#Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
#
#Example 3:
#Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
#Output: 31
#Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
#
#Constraints:
#    1 <= firstLen, secondLen <= 1000
#    2 <= firstLen + secondLen <= 1000
#    firstLen + secondLen <= nums.length <= 1000
#    0 <= nums[i] <= 1000

from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        """
        Sliding window with prefix sums.
        Track max sum of firstLen subarray to the left of current position,
        then compute sum of secondLen subarray at current position.
        """
        n = len(nums)
        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def subarray_sum(i, length):
            return prefix[i + length] - prefix[i]

        def solve(L, M):
            # L-length subarray before M-length subarray
            max_L = 0
            result = 0

            for i in range(L + M, n + 1):
                # Max L-sum ending before position i-M
                max_L = max(max_L, subarray_sum(i - L - M, L))
                # Current M-sum
                result = max(result, max_L + subarray_sum(i - M, M))

            return result

        return max(solve(firstLen, secondLen), solve(secondLen, firstLen))


class SolutionDP:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        """
        DP approach: Track best L-subarray sum ending at or before each index.
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def get_sum(i, length):
            return prefix[i + length] - prefix[i]

        # max_left[i] = max sum of L-length subarray ending at or before i
        def compute(L, M):
            max_left = [0] * n
            max_left[L - 1] = get_sum(0, L)

            for i in range(L, n):
                max_left[i] = max(max_left[i - 1], get_sum(i - L + 1, L))

            result = 0
            for i in range(L + M - 1, n):
                m_sum = get_sum(i - M + 1, M)
                result = max(result, max_left[i - M] + m_sum)

            return result

        return max(compute(firstLen, secondLen), compute(secondLen, firstLen))
