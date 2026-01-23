#1950. Maximum of Minimum Values in All Subarrays
#Medium
#
#You are given an integer array nums of size n. You are asked to solve n queries
#for each integer i in the range [1, n].
#
#To get the answer for the ith query, find the minimum value of each subarray of
#size i, then find the maximum of all such minimum values.
#
#Return a 0-indexed integer array ans of size n where ans[i - 1] is the answer
#to the ith query.
#
#Example 1:
#Input: nums = [0,1,2,4]
#Output: [4,2,1,0]
#
#Example 2:
#Input: nums = [10,20,50,10]
#Output: [50,20,10,10]
#
#Constraints:
#    n == nums.length
#    1 <= n <= 10^5
#    0 <= nums[i] <= 10^9

from typing import List

class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        """
        Monotonic stack to find range where each element is minimum.
        """
        n = len(nums)

        # Find previous smaller element index
        prev_smaller = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        # Find next smaller element index
        next_smaller = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)

        # For each element, it's minimum in window of size (next - prev - 1)
        result = [0] * n

        for i in range(n):
            window_size = next_smaller[i] - prev_smaller[i] - 1
            result[window_size - 1] = max(result[window_size - 1], nums[i])

        # Fill gaps: answer for smaller window >= answer for larger window
        for i in range(n - 2, -1, -1):
            result[i] = max(result[i], result[i + 1])

        return result


class SolutionBruteForce:
    def findMaximums(self, nums: List[int]) -> List[int]:
        """
        O(n^2) approach using sliding window minimum.
        """
        from collections import deque

        n = len(nums)
        result = []

        for k in range(1, n + 1):
            max_min = float('-inf')
            dq = deque()

            for i in range(n):
                # Remove elements outside window
                while dq and dq[0] < i - k + 1:
                    dq.popleft()

                # Remove larger elements
                while dq and nums[dq[-1]] >= nums[i]:
                    dq.pop()

                dq.append(i)

                if i >= k - 1:
                    max_min = max(max_min, nums[dq[0]])

            result.append(max_min)

        return result
