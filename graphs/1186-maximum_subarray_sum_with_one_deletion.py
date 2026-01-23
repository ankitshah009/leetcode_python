#1186. Maximum Subarray Sum with One Deletion
#Medium
#
#Given an array of integers, return the maximum sum for a non-empty subarray
#(contiguous elements) with at most one element deletion. In other words, you
#want to choose a subarray and optionally delete one element from it so that
#there is still at least one element left and the sum of the remaining
#elements is maximum possible.
#
#Note that the subarray needs to be non-empty after deleting one element.
#
#Example 1:
#Input: arr = [1,-2,0,3]
#Output: 4
#Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the
#subarray [1, 0, 3] becomes the maximum value.
#
#Example 2:
#Input: arr = [1,-2,-2,3]
#Output: 3
#Explanation: We just choose [3] and it's the maximum sum.
#
#Example 3:
#Input: arr = [-1,-1,-1,-1]
#Output: -1
#Explanation: The final subarray needs to be non-empty. You can't choose [-1]
#and delete -1 from it, then get an empty subarray to make the sum equals to 0.
#
#Constraints:
#    1 <= arr.length <= 10^5
#    -10^4 <= arr[i] <= 10^4

from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        """
        DP with two states:
        - no_del[i]: max sum ending at i with no deletion
        - one_del[i]: max sum ending at i with one deletion

        Transitions:
        - no_del[i] = max(arr[i], no_del[i-1] + arr[i])
        - one_del[i] = max(no_del[i-1], one_del[i-1] + arr[i])
        """
        n = len(arr)

        # Initialize
        no_del = arr[0]  # Max sum ending here with no deletion
        one_del = float('-inf')  # Max sum ending here with one deletion
        result = arr[0]

        for i in range(1, n):
            # Update in reverse order to use previous values
            new_one_del = max(no_del, one_del + arr[i])  # Delete arr[i] or keep previous deletion
            new_no_del = max(arr[i], no_del + arr[i])  # Start fresh or extend

            no_del = new_no_del
            one_del = new_one_del

            result = max(result, no_del, one_del)

        return result


class SolutionPrefixSuffix:
    def maximumSum(self, arr: List[int]) -> int:
        """
        Precompute max subarray ending at each index (prefix) and
        starting at each index (suffix).
        For each deleted index i, answer is prefix[i-1] + suffix[i+1].
        """
        n = len(arr)

        # max_ending[i] = max subarray sum ending at index i
        max_ending = [0] * n
        max_ending[0] = arr[0]
        for i in range(1, n):
            max_ending[i] = max(arr[i], max_ending[i - 1] + arr[i])

        # max_starting[i] = max subarray sum starting at index i
        max_starting = [0] * n
        max_starting[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            max_starting[i] = max(arr[i], max_starting[i + 1] + arr[i])

        # Result without deletion
        result = max(max_ending)

        # Try deleting each element (except first and last which would leave no subarray)
        for i in range(1, n - 1):
            # Delete arr[i], combine prefix ending at i-1 with suffix starting at i+1
            result = max(result, max_ending[i - 1] + max_starting[i + 1])

        return result
