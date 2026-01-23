#1300. Sum of Mutated Array Closest to Target
#Medium
#
#Given an integer array arr and a target value target, return the integer value
#such that when we change all the integers larger than value in the given array
#to be equal to value, the sum of the array gets as close as possible (in
#absolute difference) to target.
#
#In case of a tie, return the minimum such integer.
#
#Example 1:
#Input: arr = [4,9,3], target = 10
#Output: 3
#Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
#
#Example 2:
#Input: arr = [2,3,5], target = 10
#Output: 5
#
#Example 3:
#Input: arr = [60864,25176,27249,21296,20204], target = 56803
#Output: 11361
#
#Constraints:
#    1 <= arr.length <= 10^4
#    1 <= arr[i], target <= 10^5

from typing import List
import bisect

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        """
        Binary search on the answer value.
        """
        arr.sort()
        n = len(arr)

        # Prefix sums for faster calculation
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        def get_sum(value):
            # Find how many elements are >= value
            idx = bisect.bisect_left(arr, value)
            return prefix[idx] + value * (n - idx)

        # Binary search between 0 and max(arr)
        left, right = 0, max(arr)

        while left < right:
            mid = (left + right) // 2
            if get_sum(mid) < target:
                left = mid + 1
            else:
                right = mid

        # Check both left-1 and left for closest
        if left == 0:
            return 0

        sum_prev = get_sum(left - 1)
        sum_curr = get_sum(left)

        if abs(sum_prev - target) <= abs(sum_curr - target):
            return left - 1
        return left


class SolutionLinear:
    def findBestValue(self, arr: List[int], target: int) -> int:
        """Linear approach after sorting"""
        arr.sort()
        n = len(arr)
        total = sum(arr)

        # If sum <= target, no need to mutate
        if total <= target:
            return arr[-1]

        # Try setting value to each arr[i] and check
        prefix_sum = 0
        for i, num in enumerate(arr):
            # If we set value = num, remaining elements stay same
            remaining = n - i
            # Check if target can be achieved with value around num
            needed = target - prefix_sum
            value = needed // remaining

            if value <= num:
                # Check value and value+1
                if abs(prefix_sum + value * remaining - target) <= \
                   abs(prefix_sum + (value + 1) * remaining - target):
                    return value
                return value + 1

            prefix_sum += num

        return arr[-1]
