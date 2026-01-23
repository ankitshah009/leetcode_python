#1063. Number of Valid Subarrays
#Hard
#
#Given an integer array nums, return the number of non-empty subarrays with
#the leftmost element of the subarray not larger than other elements in the
#subarray.
#
#A subarray is a contiguous part of an array.
#
#Example 1:
#Input: nums = [1,4,2,5,3]
#Output: 11
#Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],
#[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
#
#Example 2:
#Input: nums = [3,2,1]
#Output: 3
#Explanation: The 3 valid subarrays are: [3],[2],[1].
#
#Example 3:
#Input: nums = [2,2,2]
#Output: 6
#Explanation: The 6 valid subarrays are: [2],[2],[2],[2,2],[2,2],[2,2,2].
#
#Constraints:
#    1 <= nums.length <= 5 * 10^4
#    0 <= nums[i] <= 10^5

from typing import List

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        """
        Monotonic stack: For each element, find next smaller element.
        Number of valid subarrays starting at i = index of next smaller - i.
        """
        n = len(nums)
        result = 0
        stack = []  # Indices of elements in increasing order

        for i in range(n):
            # Pop elements larger than current
            while stack and nums[stack[-1]] > nums[i]:
                j = stack.pop()
                result += i - j

            stack.append(i)

        # Remaining elements have no smaller element to the right
        while stack:
            j = stack.pop()
            result += n - j

        return result


class SolutionAlternative:
    def validSubarrays(self, nums: List[int]) -> int:
        """
        For each position, count subarrays starting there.
        """
        n = len(nums)
        # next_smaller[i] = index of next smaller element
        next_smaller = [n] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                next_smaller[stack.pop()] = i
            stack.append(i)

        return sum(next_smaller[i] - i for i in range(n))


class SolutionBruteForce:
    def validSubarrays(self, nums: List[int]) -> int:
        """O(n^2) brute force for verification"""
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i, n):
                if all(nums[k] >= nums[i] for k in range(i, j + 1)):
                    count += 1
                else:
                    break

        return count
