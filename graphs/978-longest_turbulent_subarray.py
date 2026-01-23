#978. Longest Turbulent Subarray
#Medium
#
#Given an integer array arr, return the length of a maximum size turbulent
#subarray of arr.
#
#A subarray is turbulent if the comparison sign flips between each adjacent
#pair of elements in the subarray.
#
#More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] is turbulent if
#and only if:
#- For i <= k < j:
#  - arr[k] > arr[k + 1] when k is odd, and
#  - arr[k] < arr[k + 1] when k is even;
#- Or, for i <= k < j:
#  - arr[k] > arr[k + 1] when k is even, and
#  - arr[k] < arr[k + 1] when k is odd.
#
#Example 1:
#Input: arr = [9,4,2,10,7,8,8,1,9]
#Output: 5
#Explanation: [4,2,10,7,8] is the longest turbulent subarray.
#
#Example 2:
#Input: arr = [4,8,12,16]
#Output: 2
#
#Constraints:
#    1 <= arr.length <= 4 * 10^4
#    0 <= arr[i] <= 10^9

class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        """
        Track length of turbulent subarray ending at each position.
        """
        n = len(arr)
        if n == 1:
            return 1

        # inc[i] = length of turbulent ending at i with increasing last step
        # dec[i] = length of turbulent ending at i with decreasing last step
        inc = 1
        dec = 1
        max_len = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                inc = dec + 1
                dec = 1
            elif arr[i] < arr[i - 1]:
                dec = inc + 1
                inc = 1
            else:
                inc = 1
                dec = 1

            max_len = max(max_len, inc, dec)

        return max_len


class SolutionSlidingWindow:
    """Sliding window approach"""

    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        max_len = 1
        left = 0

        for right in range(1, n):
            cmp = (arr[right] > arr[right - 1]) - (arr[right] < arr[right - 1])

            if cmp == 0:
                left = right
            elif right == 1 or cmp == prev_cmp:
                left = right - 1

            max_len = max(max_len, right - left + 1)
            prev_cmp = -cmp

        return max_len


class SolutionExplicit:
    """More explicit sign tracking"""

    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        max_len = 1
        curr_len = 1

        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                curr_len = 1
                continue

            curr_sign = 1 if arr[i] > arr[i - 1] else -1

            if i == 1:
                curr_len = 2
                prev_sign = curr_sign
            elif curr_sign != prev_sign:
                curr_len += 1
                prev_sign = curr_sign
            else:
                curr_len = 2
                prev_sign = curr_sign

            max_len = max(max_len, curr_len)

        return max_len
