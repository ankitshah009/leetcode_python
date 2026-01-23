#1574. Shortest Subarray to be Removed to Make Array Sorted
#Medium
#
#Given an integer array arr, remove a subarray (can be empty) from arr such that
#the remaining elements in arr are non-decreasing.
#
#Return the length of the shortest subarray to remove.
#
#A subarray is a contiguous subsequence of the array.
#
#Example 1:
#Input: arr = [1,2,3,10,4,2,3,5]
#Output: 3
#Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The
#remaining elements after that will be [1,2,3,3,5] which are sorted.
#
#Example 2:
#Input: arr = [5,4,3,2,1]
#Output: 4
#Explanation: Since the array is strictly decreasing, we can only keep a single
#element. Any element is fine, so we can remove [5,4,3,2] or [4,3,2,1].
#
#Example 3:
#Input: arr = [1,2,3]
#Output: 0
#Explanation: The array is already non-decreasing. We do not need to remove any elements.
#
#Constraints:
#    1 <= arr.length <= 10^5
#    0 <= arr[i] <= 10^9

from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        Find longest non-decreasing prefix and suffix.
        Then try to merge them with two pointers.
        """
        n = len(arr)

        # Find longest non-decreasing prefix
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        # Already sorted
        if left == n - 1:
            return 0

        # Find longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # Option 1: Remove everything after prefix
        # Option 2: Remove everything before suffix
        result = min(n - left - 1, right)

        # Option 3: Merge prefix and suffix
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                # Can merge at this point
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1

        return result


class SolutionBinarySearch:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        Binary search for merging prefix with suffix.
        """
        import bisect

        n = len(arr)

        # Find prefix
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        # Find suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # Remove all middle, or keep only prefix, or only suffix
        result = min(n - left - 1, right)

        # Try to keep prefix[0:i+1] and suffix[j:]
        for i in range(left + 1):
            # Find smallest j where arr[j] >= arr[i]
            j = bisect.bisect_left(arr, arr[i], right, n)
            result = min(result, j - i - 1)

        return result


class SolutionExplained:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        Detailed explanation.

        We want to keep a prefix and suffix that together form a sorted array.
        The subarray to remove is everything in between.

        1. Find longest sorted prefix ending at index 'left'
        2. Find longest sorted suffix starting at index 'right'
        3. Try different ways to merge them

        Base cases:
        - Remove everything after prefix: length = n - left - 1
        - Remove everything before suffix: length = right

        Optimization:
        - Two pointers to find best merge point
        """
        n = len(arr)

        # Step 1: Find sorted prefix
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:
            return 0  # Already sorted

        # Step 2: Find sorted suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # Step 3: Initial answer (keep only prefix or only suffix)
        ans = min(n - left - 1, right)

        # Step 4: Try merging prefix and suffix
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                # Valid merge: remove arr[i+1:j]
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1

        return ans
