#360. Sort Transformed Array
#Medium
#
#Given a sorted integer array nums and three integers a, b and c, apply a
#quadratic function of the form f(x) = ax² + bx + c to each element nums[i] in
#the array, and return the array in a sorted order.
#
#Example 1:
#Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
#Output: [3,9,15,33]
#
#Example 2:
#Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
#Output: [-23,-5,1,7]
#
#Constraints:
#    1 <= nums.length <= 200
#    -100 <= nums[i], a, b, c <= 100
#    nums is sorted in ascending order.
#
#Follow up: Could you solve it in O(n) time?

from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        """
        Two pointers approach - O(n).

        Key insight:
        - If a > 0: parabola opens upward, max values at ends
        - If a < 0: parabola opens downward, min values at ends
        - If a = 0: linear function
        """
        def f(x):
            return a * x * x + b * x + c

        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1

        if a >= 0:
            # Fill from the end (largest values at array ends)
            idx = n - 1
            while left <= right:
                left_val = f(nums[left])
                right_val = f(nums[right])
                if left_val >= right_val:
                    result[idx] = left_val
                    left += 1
                else:
                    result[idx] = right_val
                    right -= 1
                idx -= 1
        else:
            # Fill from the start (smallest values at array ends)
            idx = 0
            while left <= right:
                left_val = f(nums[left])
                right_val = f(nums[right])
                if left_val <= right_val:
                    result[idx] = left_val
                    left += 1
                else:
                    result[idx] = right_val
                    right -= 1
                idx += 1

        return result


class SolutionSimple:
    """Simple O(n log n) approach"""

    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def f(x):
            return a * x * x + b * x + c

        return sorted(f(x) for x in nums)


class SolutionDeque:
    """Using deque for cleaner code"""

    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        from collections import deque

        def f(x):
            return a * x * x + b * x + c

        values = deque([f(x) for x in nums])
        result = []

        while values:
            if a >= 0:
                # Want largest first, then reverse
                if values[0] >= values[-1]:
                    result.append(values.popleft())
                else:
                    result.append(values.pop())
            else:
                # Want smallest first
                if values[0] <= values[-1]:
                    result.append(values.popleft())
                else:
                    result.append(values.pop())

        if a >= 0:
            result.reverse()

        return result
