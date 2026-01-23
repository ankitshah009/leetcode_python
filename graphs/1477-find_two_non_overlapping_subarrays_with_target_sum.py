#1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
#Medium
#
#You are given an array of integers arr and an integer target.
#
#You have to find two non-overlapping sub-arrays of arr each with a sum equal
#to target. There can be multiple answers so you have to find an answer where
#the sum of the lengths of the two sub-arrays is minimum.
#
#Return the minimum sum of the lengths of the two required sub-arrays, or
#return -1 if you cannot find such two sub-arrays.
#
#Example 1:
#Input: arr = [3,2,2,4,3], target = 3
#Output: 2
#Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their
#lengths is 2.
#
#Example 2:
#Input: arr = [7,3,4,7], target = 7
#Output: 2
#Explanation: Although we have three non-overlapping sub-arrays of sum = 7
#([7], [3,4] and [7]), we will choose the first and third sub-arrays as the
#sum of their lengths is minimum.
#
#Example 3:
#Input: arr = [4,3,2,6,2,3,4], target = 6
#Output: -1
#Explanation: We have only one sub-array of sum = 6.
#
#Constraints:
#    1 <= arr.length <= 10^5
#    1 <= arr[i] <= 1000
#    1 <= target <= 10^8

from typing import List
from collections import defaultdict

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """
        Use prefix sum with hash map.
        Track minimum subarray length ending at or before each position.
        """
        n = len(arr)
        INF = float('inf')

        # prefix_sum -> index
        prefix_map = {0: -1}
        prefix_sum = 0

        # min_len[i] = minimum length of subarray with sum=target ending at or before i
        min_len = [INF] * n

        result = INF

        for i, num in enumerate(arr):
            prefix_sum += num

            # Check if there's a subarray ending at i with sum = target
            if prefix_sum - target in prefix_map:
                start = prefix_map[prefix_sum - target]
                curr_len = i - start

                # If there's a valid subarray before start, update result
                if start >= 0 and min_len[start] != INF:
                    result = min(result, min_len[start] + curr_len)
                elif start == -1 and i > 0 and min_len[i - 1] != INF:
                    # Edge case: start is -1, check if there's another subarray before
                    pass

                # Update min_len for current position
                min_len[i] = curr_len

            # min_len[i] is minimum of current or previous
            if i > 0:
                min_len[i] = min(min_len[i], min_len[i - 1])

            # Check result again with proper previous minimum
            if prefix_sum - target in prefix_map:
                start = prefix_map[prefix_sum - target]
                curr_len = i - start
                if start >= 0 and min_len[start] != INF:
                    result = min(result, min_len[start] + curr_len)

            prefix_map[prefix_sum] = i

        return result if result != INF else -1


class SolutionCleaner:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """
        Cleaner implementation with prefix sum.
        """
        n = len(arr)
        INF = float('inf')

        # best[i] = minimum length subarray with sum=target ending at or before i
        best = [INF] * n

        prefix_sum = 0
        prefix_map = {0: -1}
        result = INF

        for i in range(n):
            prefix_sum += arr[i]

            if prefix_sum - target in prefix_map:
                j = prefix_map[prefix_sum - target]
                length = i - j

                # Check if we can pair with a subarray before index j+1
                if j >= 0 and best[j] != INF:
                    result = min(result, best[j] + length)

                # Update best for current position
                best[i] = length

            # Propagate best from previous position
            if i > 0:
                best[i] = min(best[i], best[i - 1])

            prefix_map[prefix_sum] = i

        return result if result != INF else -1


class SolutionSlidingWindow:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """
        Sliding window for positive numbers.
        Track minimum length subarray on the left.
        """
        n = len(arr)
        INF = float('inf')

        # min_left[i] = min length of subarray with sum=target ending at or before i
        min_left = [INF] * n

        # Sliding window to find all subarrays with sum = target
        left = 0
        window_sum = 0
        result = INF

        for right in range(n):
            window_sum += arr[right]

            while window_sum > target and left <= right:
                window_sum -= arr[left]
                left += 1

            if window_sum == target:
                length = right - left + 1

                # Check if we can combine with a subarray on the left
                if left > 0 and min_left[left - 1] != INF:
                    result = min(result, min_left[left - 1] + length)

                min_left[right] = length

            # Propagate minimum from left
            if right > 0:
                min_left[right] = min(min_left[right], min_left[right - 1])

        return result if result != INF else -1
