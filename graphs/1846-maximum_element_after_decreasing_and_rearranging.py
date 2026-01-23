#1846. Maximum Element After Decreasing and Rearranging
#Medium
#
#You are given an array of positive integers arr. Perform some operations
#(possibly none) on arr so that it satisfies these conditions:
#- The value of the first element in arr must be 1.
#- The absolute difference between any 2 adjacent elements must be less than or
#  equal to 1.
#
#There are 2 types of operations that you can perform any number of times:
#- Decrease the value of any element of arr to a smaller positive integer.
#- Rearrange the elements of arr to be in any order.
#
#Return the maximum possible value of an element in arr after performing the
#operations to satisfy the conditions.
#
#Example 1:
#Input: arr = [2,2,1,2,1]
#Output: 2
#
#Example 2:
#Input: arr = [100,1,1000]
#Output: 3
#
#Example 3:
#Input: arr = [1,2,3,4,5]
#Output: 5
#
#Constraints:
#    1 <= arr.length <= 10^5
#    1 <= arr[i] <= 10^9

from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        """
        Sort and greedily build increasing sequence.
        """
        arr.sort()
        arr[0] = 1  # First must be 1

        for i in range(1, len(arr)):
            # Each element can be at most prev + 1
            arr[i] = min(arr[i], arr[i - 1] + 1)

        return arr[-1]


class SolutionSimple:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        """
        Track current max without modifying array.
        """
        arr.sort()
        current_max = 0

        for num in arr:
            # New element can be at most current_max + 1
            current_max = min(num, current_max + 1)

        return current_max


class SolutionCounting:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        """
        Counting sort approach - O(n) time.
        """
        n = len(arr)
        # Max possible answer is n
        count = [0] * (n + 1)

        for num in arr:
            count[min(num, n)] += 1

        current_max = 0

        for val in range(1, n + 1):
            # Use up to count[val] elements of this value
            # Each can increase max by at most 1
            current_max = min(current_max + count[val], val)

        return current_max
