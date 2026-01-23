#1793. Maximum Score of a Good Subarray
#Hard
#
#You are given an array of integers nums (0-indexed) and an integer k.
#
#The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ...,
#nums[j]) * (j - i + 1).
#
#A good subarray is a subarray where i <= k <= j.
#
#Return the maximum possible score of a good subarray.
#
#Example 1:
#Input: nums = [1,4,3,7,4,5], k = 3
#Output: 15
#
#Example 2:
#Input: nums = [5,5,4,5,4,1,1,1], k = 0
#Output: 20
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 2 * 10^4
#    0 <= k < nums.length

from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        """
        Two pointers expanding from k.
        Greedy: always expand towards the larger element.
        """
        n = len(nums)
        left = right = k
        min_val = nums[k]
        max_score = nums[k]

        while left > 0 or right < n - 1:
            # Expand towards larger element (or only valid direction)
            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] >= nums[right + 1]:
                left -= 1
            else:
                right += 1

            min_val = min(min_val, nums[left], nums[right])
            score = min_val * (right - left + 1)
            max_score = max(max_score, score)

        return max_score


class SolutionStack:
    def maximumScore(self, nums: List[int], k: int) -> int:
        """
        Monotonic stack approach.
        For each element as minimum, find valid range.
        """
        n = len(nums)

        # Find left boundary (first smaller to left)
        left_bound = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left_bound[i] = stack[-1] if stack else -1
            stack.append(i)

        # Find right boundary (first smaller to right)
        right_bound = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right_bound[i] = stack[-1] if stack else n
            stack.append(i)

        # Find max score for subarrays containing k
        max_score = 0
        for i in range(n):
            left = left_bound[i] + 1
            right = right_bound[i] - 1

            # Check if this range contains k
            if left <= k <= right:
                score = nums[i] * (right - left + 1)
                max_score = max(max_score, score)

        return max_score


class SolutionBinarySearch:
    def maximumScore(self, nums: List[int], k: int) -> int:
        """
        Binary search on minimum value.
        """
        def can_achieve(min_val: int) -> int:
            """Return max width of subarray containing k with all elements >= min_val."""
            left = right = k

            while left > 0 and nums[left - 1] >= min_val:
                left -= 1
            while right < len(nums) - 1 and nums[right + 1] >= min_val:
                right += 1

            return right - left + 1

        max_score = 0

        for val in set(nums):
            width = can_achieve(val)
            max_score = max(max_score, val * width)

        return max_score
