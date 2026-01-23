#1330. Reverse Subarray To Maximize Array Value
#Hard
#
#You are given an integer array nums. The value of this array is defined as the
#sum of |nums[i] - nums[i + 1]| for all 0 <= i < nums.length - 1.
#
#You are allowed to select any subarray of the given array and reverse it. You
#can perform this operation only once.
#
#Find maximum possible value of the final array.
#
#Example 1:
#Input: nums = [2,3,1,5,4]
#Output: 10
#Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4]
#whose value is 10.
#
#Example 2:
#Input: nums = [2,4,9,24,2,1,10]
#Output: 68
#
#Constraints:
#    1 <= nums.length <= 3 * 10^4
#    -10^5 <= nums[i] <= 10^5

from typing import List

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        """
        Key insight: Reversing [i+1, j] changes value at positions i and j only.
        Original: |nums[i] - nums[i+1]| + |nums[j] - nums[j+1]|
        After: |nums[i] - nums[j]| + |nums[i+1] - nums[j+1]|

        For interior reversals, the gain is maximized when we can increase
        the difference at boundaries.
        """
        n = len(nums)
        if n <= 2:
            return sum(abs(nums[i] - nums[i + 1]) for i in range(n - 1))

        # Original value
        original = sum(abs(nums[i] - nums[i + 1]) for i in range(n - 1))

        # Case 1: Reverse starting from index 0
        # Changes |nums[0] - nums[1]| to |nums[0] - nums[j]| + adds |nums[1] - nums[j+1]|
        max_gain = 0
        for j in range(1, n - 1):
            # Reverse [0, j]
            gain = abs(nums[j + 1] - nums[0]) - abs(nums[j + 1] - nums[j])
            max_gain = max(max_gain, gain)

        # Case 2: Reverse ending at index n-1
        for i in range(n - 2):
            # Reverse [i+1, n-1]
            gain = abs(nums[i] - nums[n - 1]) - abs(nums[i] - nums[i + 1])
            max_gain = max(max_gain, gain)

        # Case 3: Interior reversal [i+1, j] where 0 < i+1 < j < n-1
        # Gain = |a-d| + |b-c| - |a-b| - |c-d| where a=nums[i], b=nums[i+1], c=nums[j], d=nums[j+1]
        # Maximum gain occurs when we can pair small with large values

        # Track min(max(a,b)) and max(min(a,b)) across all adjacent pairs
        min_of_max = float('inf')
        max_of_min = float('-inf')

        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            min_of_max = min(min_of_max, max(a, b))
            max_of_min = max(max_of_min, min(a, b))

        # The maximum gain from interior reversals
        interior_gain = 2 * max(0, max_of_min - min_of_max)
        max_gain = max(max_gain, interior_gain)

        return original + max_gain


class SolutionBruteForce:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        """O(n^2) brute force - check all subarrays"""
        n = len(nums)

        def array_value(arr):
            return sum(abs(arr[i] - arr[i + 1]) for i in range(len(arr) - 1))

        original = array_value(nums)
        max_value = original

        for i in range(n):
            for j in range(i + 1, n + 1):
                # Reverse nums[i:j]
                new_arr = nums[:i] + nums[i:j][::-1] + nums[j:]
                max_value = max(max_value, array_value(new_arr))

        return max_value
