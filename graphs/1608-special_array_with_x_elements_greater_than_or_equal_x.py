#1608. Special Array With X Elements Greater Than or Equal X
#Easy
#
#You are given an array nums of non-negative integers. nums is considered
#special if there exists a number x such that there are exactly x numbers in
#nums that are greater than or equal to x.
#
#Notice that x does not have to be an element in nums.
#
#If there is no such number x, return -1. Otherwise, return x.
#
#Example 1:
#Input: nums = [3,5]
#Output: 2
#Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
#
#Example 2:
#Input: nums = [0,0]
#Output: -1
#Explanation: No numbers fit the criteria for x.
#
#Example 3:
#Input: nums = [0,4,3,0,4]
#Output: 3
#Explanation: There are 3 values that are greater than or equal to 3.
#
#Constraints:
#    1 <= nums.length <= 100
#    0 <= nums[i] <= 1000

from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        Sort and try each possible x from 1 to n.
        """
        nums.sort(reverse=True)
        n = len(nums)

        for x in range(1, n + 1):
            # Count numbers >= x
            if nums[x - 1] >= x and (x == n or nums[x] < x):
                return x

        return -1


class SolutionBinarySearch:
    def specialArray(self, nums: List[int]) -> int:
        """
        Binary search for each candidate x.
        """
        from bisect import bisect_left

        nums.sort()
        n = len(nums)

        for x in range(1, n + 1):
            # Count numbers >= x using binary search
            count = n - bisect_left(nums, x)
            if count == x:
                return x

        return -1


class SolutionCounting:
    def specialArray(self, nums: List[int]) -> int:
        """
        Counting sort approach - O(n).
        """
        n = len(nums)

        # count[i] = number of elements >= i (capped at n)
        count = [0] * (n + 2)

        for num in nums:
            count[min(num, n + 1)] += 1

        # Compute suffix sums
        total = 0
        for x in range(n, 0, -1):
            total += count[x]
            if total == x:
                return x

        return -1


class SolutionBruteForce:
    def specialArray(self, nums: List[int]) -> int:
        """
        Brute force: try each x from 1 to n.
        """
        n = len(nums)

        for x in range(1, n + 1):
            count = sum(1 for num in nums if num >= x)
            if count == x:
                return x

        return -1


class SolutionSortOptimized:
    def specialArray(self, nums: List[int]) -> int:
        """
        After sorting, nums[i] indicates how many elements are >= nums[i].
        """
        nums.sort()
        n = len(nums)

        for i in range(n):
            # Number of elements from index i to end is (n - i)
            x = n - i

            # Check if x satisfies the condition
            if nums[i] >= x and (i == 0 or nums[i - 1] < x):
                return x

        return -1
