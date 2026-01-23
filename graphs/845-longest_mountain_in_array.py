#845. Longest Mountain in Array
#Medium
#
#You may recall that an array arr is a mountain array if and only if:
#- arr.length >= 3
#- There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
#  - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#  - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
#Given an integer array arr, return the length of the longest subarray, which
#is a mountain. Return 0 if there is no mountain subarray.
#
#Example 1:
#Input: arr = [2,1,4,7,3,2,5]
#Output: 5
#Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
#
#Example 2:
#Input: arr = [2,2,2]
#Output: 0
#Explanation: There is no mountain.
#
#Constraints:
#    1 <= arr.length <= 10^4
#    0 <= arr[i] <= 10^4
#
#Follow up: Can you solve it using only one pass?

class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        """
        Single pass: track increasing and decreasing lengths.
        """
        n = len(arr)
        if n < 3:
            return 0

        max_len = 0
        i = 1

        while i < n:
            # Skip flat regions
            while i < n and arr[i] == arr[i - 1]:
                i += 1

            # Count increasing
            up = 0
            while i < n and arr[i] > arr[i - 1]:
                up += 1
                i += 1

            # Count decreasing
            down = 0
            while i < n and arr[i] < arr[i - 1]:
                down += 1
                i += 1

            # Valid mountain needs both up and down
            if up > 0 and down > 0:
                max_len = max(max_len, up + down + 1)

        return max_len


class SolutionTwoArrays:
    """Track increasing/decreasing lengths at each position"""

    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        # up[i] = length of increasing sequence ending at i
        # down[i] = length of decreasing sequence starting at i
        up = [0] * n
        down = [0] * n

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up[i] = up[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                down[i] = down[i + 1] + 1

        max_len = 0
        for i in range(1, n - 1):
            if up[i] > 0 and down[i] > 0:
                max_len = max(max_len, up[i] + down[i] + 1)

        return max_len


class SolutionEnumerate:
    """Enumerate all mountains"""

    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        max_len = 0

        for peak in range(1, n - 1):
            if arr[peak - 1] < arr[peak] > arr[peak + 1]:
                # Found potential peak
                left = peak
                right = peak

                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                max_len = max(max_len, right - left + 1)

        return max_len
