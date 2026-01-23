#1673. Find the Most Competitive Subsequence
#Medium
#
#Given an integer array nums and a positive integer k, return the most
#competitive subsequence of nums of size k.
#
#An array's subsequence is a resulting sequence obtained by erasing some
#(possibly zero) elements from the array.
#
#We define that a subsequence a is more competitive than a subsequence b
#(of the same length) if in the first position where a and b differ, a has
#a number less than the corresponding number in b.
#
#Example 1:
#Input: nums = [3,5,2,6], k = 2
#Output: [2,6]
#Explanation: [2,6] is the most competitive. Other subsequences of length 2
#are [3,5], [3,2], [3,6], [5,2], [5,6], [2,6]. All are lexicographically
#larger than [2,6].
#
#Example 2:
#Input: nums = [2,4,3,3,5,4,9,6], k = 4
#Output: [2,3,3,4]
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= nums[i] <= 10^9
#    1 <= k <= nums.length

from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        Monotonic stack approach.
        Pop elements while we can still get k elements and current is smaller.
        """
        n = len(nums)
        stack = []

        for i, num in enumerate(nums):
            # Pop while:
            # 1. Stack is not empty
            # 2. Current element is smaller than stack top
            # 3. We have enough remaining elements to fill k positions
            remaining = n - i
            while stack and num < stack[-1] and len(stack) + remaining > k:
                stack.pop()

            if len(stack) < k:
                stack.append(num)

        return stack


class SolutionDetailed:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        Detailed implementation with clear logic.
        """
        n = len(nums)
        result = []
        to_remove = n - k  # Number of elements we can remove

        for num in nums:
            # Remove larger elements from result if we can
            while result and to_remove > 0 and result[-1] > num:
                result.pop()
                to_remove -= 1

            result.append(num)

        # Keep only first k elements
        return result[:k]


class SolutionGreedy:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        Greedy selection with look-ahead.
        """
        n = len(nums)
        result = []

        for i in range(n):
            # While we can remove and current is better
            while result and result[-1] > nums[i] and len(result) - 1 + n - i >= k:
                result.pop()

            if len(result) < k:
                result.append(nums[i])

        return result


class SolutionWithDeque:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        Using deque for stack operations.
        """
        from collections import deque

        n = len(nums)
        stack = deque()
        removals = n - k

        for num in nums:
            while stack and removals > 0 and stack[-1] > num:
                stack.pop()
                removals -= 1

            stack.append(num)

        return list(stack)[:k]


class SolutionCompact:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        Compact one-pass solution.
        """
        stack = []
        n = len(nums)

        for i, x in enumerate(nums):
            while stack and stack[-1] > x and len(stack) + n - i > k:
                stack.pop()
            if len(stack) < k:
                stack.append(x)

        return stack
