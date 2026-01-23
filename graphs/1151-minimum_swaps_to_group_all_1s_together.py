#1151. Minimum Swaps to Group All 1s Together
#Medium
#
#Given a binary array data, return the minimum number of swaps required to
#group all 1's present in the array together in any place in the array.
#
#Example 1:
#Input: data = [1,0,1,0,1]
#Output: 1
#Explanation: There are 3 ways to group all 1's together:
#[1,1,1,0,0] using 1 swap.
#[0,1,1,1,0] using 2 swaps.
#[0,0,1,1,1] using 1 swap.
#The minimum is 1.
#
#Example 2:
#Input: data = [0,0,0,1,0]
#Output: 0
#Explanation: Since there is only one 1 in the array, no swaps are needed.
#
#Example 3:
#Input: data = [1,0,1,0,1,0,0,1,1,0,1]
#Output: 3
#Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
#
#Constraints:
#    1 <= data.length <= 10^5
#    data[i] is either 0 or 1.

from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        """
        Sliding window: Window size = count of 1s.
        Find window with maximum 1s (minimum 0s to swap).
        """
        ones = sum(data)
        if ones <= 1:
            return 0

        # Count 1s in first window
        window_ones = sum(data[:ones])
        max_ones = window_ones

        # Slide window
        for i in range(ones, len(data)):
            window_ones += data[i] - data[i - ones]
            max_ones = max(max_ones, window_ones)

        return ones - max_ones


class SolutionPrefixSum:
    def minSwaps(self, data: List[int]) -> int:
        """Using prefix sum for window queries"""
        n = len(data)
        ones = sum(data)

        if ones <= 1:
            return 0

        # Build prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + data[i]

        # Find window with max 1s
        max_ones = 0
        for i in range(ones, n + 1):
            window_ones = prefix[i] - prefix[i - ones]
            max_ones = max(max_ones, window_ones)

        return ones - max_ones
