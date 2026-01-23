#1144. Decrease Elements To Make Array Zigzag
#Medium
#
#Given an array nums of integers, a move consists of choosing any element
#and decreasing it by 1.
#
#An array A is a zigzag array if either:
#    Every even-indexed element is greater than adjacent elements, ie.
#    A[0] > A[1] < A[2] > A[3] < A[4] > ...
#    OR, every odd-indexed element is greater than adjacent elements, ie.
#    A[0] < A[1] > A[2] < A[3] > A[4] < ...
#
#Return the minimum number of moves to transform the given array nums into
#a zigzag array.
#
#Example 1:
#Input: nums = [1,2,3]
#Output: 2
#Explanation: We can decrease 2 to 0 or 3 to 1.
#
#Example 2:
#Input: nums = [9,6,1,6,2]
#Output: 4
#
#Constraints:
#    1 <= nums.length <= 1000
#    1 <= nums[i] <= 1000

from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        """
        Try both patterns and return minimum.
        For each pattern, decrease elements at odd/even positions.
        """
        def cost(parity):
            """Cost to make nums[parity::2] valleys (smaller than neighbors)"""
            total = 0
            n = len(nums)

            for i in range(parity, n, 2):
                left = nums[i - 1] if i > 0 else float('inf')
                right = nums[i + 1] if i < n - 1 else float('inf')
                target = min(left, right) - 1
                if nums[i] > target:
                    total += nums[i] - target

            return total

        # Pattern 1: even indices are peaks (odd indices are valleys)
        # Pattern 2: odd indices are peaks (even indices are valleys)
        return min(cost(0), cost(1))


class SolutionExplicit:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        """More explicit implementation"""
        n = len(nums)

        def solve(peaks_at_even):
            """
            If peaks_at_even: A[0] > A[1] < A[2] > ...
            Make valleys by decreasing.
            """
            total = 0
            arr = nums.copy()

            valley_start = 1 if peaks_at_even else 0

            for i in range(valley_start, n, 2):
                neighbors = []
                if i > 0:
                    neighbors.append(arr[i - 1])
                if i < n - 1:
                    neighbors.append(arr[i + 1])

                min_neighbor = min(neighbors)
                if arr[i] >= min_neighbor:
                    total += arr[i] - min_neighbor + 1

            return total

        return min(solve(True), solve(False))
