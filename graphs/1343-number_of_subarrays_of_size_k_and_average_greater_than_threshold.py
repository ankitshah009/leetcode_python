#1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#Medium
#
#Given an array of integers arr and two integers k and threshold, return the
#number of sub-arrays of size k and average greater than or equal to threshold.
#
#Example 1:
#Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
#Output: 3
#Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively.
#All other sub-arrays of size 3 have averages less than 4 (the threshold).
#
#Example 2:
#Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
#Output: 6
#Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
#
#Constraints:
#    1 <= arr.length <= 10^5
#    1 <= arr[i] <= 10^4
#    1 <= k <= arr.length
#    0 <= threshold <= 10^4

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        Sliding window. Average >= threshold means sum >= k * threshold.
        """
        n = len(arr)
        target_sum = k * threshold

        # Initial window sum
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= target_sum else 0

        # Slide window
        for i in range(k, n):
            window_sum += arr[i] - arr[i - k]
            if window_sum >= target_sum:
                count += 1

        return count


class SolutionPrefixSum:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """Using prefix sums"""
        n = len(arr)
        target_sum = k * threshold

        # Build prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        count = 0
        for i in range(k, n + 1):
            if prefix[i] - prefix[i - k] >= target_sum:
                count += 1

        return count
