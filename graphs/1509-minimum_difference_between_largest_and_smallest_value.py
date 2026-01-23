#1509. Minimum Difference Between Largest and Smallest Value in Three Moves
#Medium
#
#You are given an integer array nums. In one move, you can choose one element
#of nums and change it by any value.
#
#Return the minimum difference between the largest and smallest value of nums
#after performing at most three moves.
#
#Example 1:
#Input: nums = [5,3,2,4]
#Output: 0
#Explanation: Change the array [5,3,2,4] to [2,2,2,2].
#The difference between the maximum and minimum is 2-2 = 0.
#
#Example 2:
#Input: nums = [1,5,0,10,14]
#Output: 1
#Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1].
#The difference between the maximum and minimum is 1-0 = 1.
#
#Example 3:
#Input: nums = [3,100,20]
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^9 <= nums[i] <= 10^9

from typing import List
import heapq

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        With 3 moves, we can remove any 3 elements (set them to any value).
        To minimize range, remove some from smallest and/or largest.

        Options:
        - Remove 3 smallest
        - Remove 2 smallest, 1 largest
        - Remove 1 smallest, 2 largest
        - Remove 3 largest

        Only need 4 smallest and 4 largest values.
        """
        n = len(nums)

        # If array has 4 or fewer elements, can make all same
        if n <= 4:
            return 0

        # Sort and check all 4 options
        nums.sort()

        # Options: remove i smallest and (3-i) largest
        min_diff = float('inf')
        for i in range(4):
            # After removing i smallest and (3-i) largest
            # Remaining range is nums[n-1-(3-i)] - nums[i]
            # = nums[n-4+i] - nums[i]
            diff = nums[n - 4 + i] - nums[i]
            min_diff = min(min_diff, diff)

        return min_diff


class SolutionHeap:
    def minDifference(self, nums: List[int]) -> int:
        """
        O(n) average using partial sort (nlargest/nsmallest).
        """
        n = len(nums)

        if n <= 4:
            return 0

        # Get 4 smallest and 4 largest
        smallest = heapq.nsmallest(4, nums)
        largest = heapq.nlargest(4, nums)

        min_diff = float('inf')
        for i in range(4):
            # Remove i smallest and (3-i) largest
            diff = largest[3 - i] - smallest[i]
            min_diff = min(min_diff, diff)

        return min_diff


class SolutionPartition:
    def minDifference(self, nums: List[int]) -> int:
        """
        Using quickselect-style partitioning.
        """
        n = len(nums)

        if n <= 4:
            return 0

        # We only need indices 0,1,2,3 and n-4,n-3,n-2,n-1
        # Partial sort to get these

        nums.sort()  # Full sort for simplicity

        return min(
            nums[n - 1] - nums[3],    # Remove 3 smallest
            nums[n - 2] - nums[2],    # Remove 2 smallest, 1 largest
            nums[n - 3] - nums[1],    # Remove 1 smallest, 2 largest
            nums[n - 4] - nums[0]     # Remove 3 largest
        )


class SolutionExplicit:
    def minDifference(self, nums: List[int]) -> int:
        """
        Explicit enumeration of all options.
        """
        n = len(nums)

        if n <= 4:
            return 0

        nums.sort()

        # After removing k elements, we have n-k elements
        # We remove 3 elements total
        # Options for which 3 to remove (from extremes):

        options = [
            # (smallest_removed, largest_removed)
            (3, 0),  # Remove 3 smallest
            (2, 1),  # Remove 2 smallest, 1 largest
            (1, 2),  # Remove 1 smallest, 2 largest
            (0, 3),  # Remove 3 largest
        ]

        min_diff = float('inf')
        for s_removed, l_removed in options:
            # After removal, smallest is nums[s_removed]
            # largest is nums[n - 1 - l_removed]
            diff = nums[n - 1 - l_removed] - nums[s_removed]
            min_diff = min(min_diff, diff)

        return min_diff
