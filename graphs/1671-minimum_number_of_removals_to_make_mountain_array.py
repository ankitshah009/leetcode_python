#1671. Minimum Number of Removals to Make Mountain Array
#Hard
#
#You may recall that an array arr is a mountain array if and only if:
#- arr.length >= 3
#- There exists some index i with 0 < i < arr.length - 1 such that:
#  - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#  - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
#Given an integer array nums, return the minimum number of elements to remove
#to make nums a mountain array.
#
#Example 1:
#Input: nums = [1,3,1]
#Output: 0
#Explanation: The array itself is a mountain array.
#
#Example 2:
#Input: nums = [2,1,1,5,6,2,3,1]
#Output: 3
#Explanation: Remove elements at indices 0, 1, and 5 to get [1,5,6,3,1].
#
#Example 3:
#Input: nums = [4,3,2,1,1,2,3,1]
#Output: 4
#
#Constraints:
#    3 <= nums.length <= 1000
#    1 <= nums[i] <= 10^9
#    It is guaranteed that you can make a mountain array out of nums.

from typing import List
import bisect

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """
        For each index i as peak:
        - Find LIS ending at i (from left)
        - Find LIS starting at i (from right, which is LDS from left)
        Mountain length = LIS_left[i] + LIS_right[i] - 1
        """
        n = len(nums)

        # LIS ending at each index (from left)
        lis_left = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis_left[i] = max(lis_left[i], lis_left[j] + 1)

        # LIS starting at each index (from right) = LDS from right
        lis_right = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    lis_right[i] = max(lis_right[i], lis_right[j] + 1)

        # Find maximum mountain length
        max_mountain = 0
        for i in range(1, n - 1):
            # Valid peak needs at least 2 on each side
            if lis_left[i] > 1 and lis_right[i] > 1:
                mountain_len = lis_left[i] + lis_right[i] - 1
                max_mountain = max(max_mountain, mountain_len)

        return n - max_mountain


class SolutionBinarySearch:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """
        O(n log n) solution using binary search for LIS.
        """
        n = len(nums)

        def get_lis_lengths(arr):
            """Get LIS length ending at each index."""
            result = [1] * len(arr)
            tails = []

            for i, num in enumerate(arr):
                pos = bisect.bisect_left(tails, num)
                result[i] = pos + 1

                if pos == len(tails):
                    tails.append(num)
                else:
                    tails[pos] = num

            return result

        # LIS from left
        lis_left = get_lis_lengths(nums)

        # LIS from right (reverse array)
        lis_right = get_lis_lengths(nums[::-1])[::-1]

        # Find max mountain
        max_len = 0
        for i in range(1, n - 1):
            if lis_left[i] > 1 and lis_right[i] > 1:
                max_len = max(max_len, lis_left[i] + lis_right[i] - 1)

        return n - max_len


class SolutionDP:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """
        DP solution with explicit state.
        """
        n = len(nums)

        # dp_inc[i] = length of longest increasing subsequence ending at i
        dp_inc = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)

        # dp_dec[i] = length of longest decreasing subsequence starting at i
        dp_dec = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)

        # Maximum mountain with peak at i
        ans = 0
        for i in range(1, n - 1):
            if dp_inc[i] >= 2 and dp_dec[i] >= 2:
                ans = max(ans, dp_inc[i] + dp_dec[i] - 1)

        return n - ans


class SolutionOptimized:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """
        Optimized with binary search LIS in both directions.
        """
        n = len(nums)

        def lis_ending_at(arr):
            dp = [0] * len(arr)
            seq = []
            for i, x in enumerate(arr):
                pos = bisect.bisect_left(seq, x)
                dp[i] = pos + 1
                if pos == len(seq):
                    seq.append(x)
                else:
                    seq[pos] = x
            return dp

        left = lis_ending_at(nums)
        right = lis_ending_at(nums[::-1])[::-1]

        max_mountain = 0
        for i in range(1, n - 1):
            if left[i] > 1 and right[i] > 1:
                max_mountain = max(max_mountain, left[i] + right[i] - 1)

        return n - max_mountain
